from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


# ============================================================
# CONFIGURATION
# ============================================================

BUILD_NAME = Path(__file__).resolve().parents[1].name.removeprefix("build")

CALCULATOR_URL = "https://testsheepnz.github.io/BasicCalculator.html"

REPORT_DIR = Path(__file__).resolve().parent.parent / "test_runs"
CASE_DIR = Path(__file__).resolve().parents[3] / "test_cases" / "substract"
CASE_FILE_PATTERN = "TC-SUBSTRACT-*.md"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def escape_markdown_table(value):
    """Escape characters that can break a Markdown table."""
    return str(value).replace("|", r"\|").replace("\n", " ")


def get_table_field(markdown, field_name):
    """Return a value from a Field/Details Markdown table."""
    pattern = (
        rf"^\|\s+\*\*{re.escape(field_name)}\*\*\s+\|\s*(.*?)\s*\|\s*$"
    )
    match = re.search(pattern, markdown, re.MULTILINE)
    if not match:
        raise ValueError(f"Missing '{field_name}' field")
    return match.group(1).strip()


def load_test_cases():
    """Load subtraction test inputs and expectations from their Markdown files."""
    test_cases = []
    case_files = sorted(CASE_DIR.glob(CASE_FILE_PATTERN))

    for case_path in case_files:
        markdown = case_path.read_text(encoding="utf-8")
        test_steps = get_table_field(markdown, "Test Steps")
        test_id_match = re.search(
            r"TC-SUBTRACT-\d+",
            get_table_field(markdown, "Test ID"),
            re.IGNORECASE,
        )
        if not test_id_match:
            raise ValueError(f"Invalid Test ID in {case_path.name}")

        inputs = {"First": None, "Second": None}
        input_pattern = re.compile(
            r"Enter\s+`([^`]*)`\s+into\s+the\s+(First|Second)\s+number\s+field"
            r"|Leave\s+the\s+(First|Second)\s+number\s+field\s+blank",
            re.IGNORECASE,
        )
        for match in input_pattern.finditer(test_steps):
            number = match.group(2) or match.group(3)
            value = match.group(1) if match.group(1) is not None else ""
            inputs[number.title()] = value

        if any(value is None for value in inputs.values()):
            raise ValueError(f"Could not parse both number inputs in {case_path.name}")

        expected_result_text = get_table_field(markdown, "Expected Result")
        expected_error_match = re.search(
            r"[\"“](Number\s+[12]\s+is\s+not\s+a\s+number)[\"”]",
            expected_result_text,
            re.IGNORECASE,
        )
        expected_value_match = re.search(r"`([^`]*)`", expected_result_text)
        if expected_error_match:
            expected = {"expected_error": expected_error_match.group(1)}
        elif expected_value_match:
            expected = {"expected": expected_value_match.group(1)}
        else:
            raise ValueError(f"Could not parse Expected Result in {case_path.name}")

        test_cases.append(
            {
                "id": test_id_match.group(0).upper(),
                "file": case_path.name,
                "name": get_table_field(markdown, "Test Name"),
                "first": inputs["First"],
                "second": inputs["Second"],
                "integer_only": bool(
                    re.search(r"\b(?:Check|Tick)\s+\*\*Integers only\*\*", test_steps, re.IGNORECASE)
                ),
                "expected_result_text": expected_result_text,
                **expected,
            }
        )

    if not test_cases:
        raise FileNotFoundError(
            f"No test case Markdown files found in {CASE_DIR}"
        )

    return test_cases


def result_matches(test_case, actual_result):
    """
    Compare the actual result with the expected result.
    Supports both numeric results and expected error messages.
    """

    expected_error = test_case.get("expected_error")

    if expected_error:
        return expected_error.casefold() in actual_result.casefold()

    try:
        return Decimal(actual_result) == Decimal(test_case["expected"])

    except (InvalidOperation, TypeError, ValueError):
        return False


# ============================================================
# RUN ONE TEST CASE
# ============================================================

def run_test_case(driver, test_case):

    # Select build
    Select(
        driver.find_element(By.ID, "selectBuild")
    ).select_by_visible_text(BUILD_NAME)

    # Clear previous data
    driver.find_element(By.ID, "clearButton").click()

    # Locate input fields
    first_input = driver.find_element(By.ID, "number1Field")
    second_input = driver.find_element(By.ID, "number2Field")

    # Clear input fields
    first_input.clear()
    second_input.clear()

    # Enter first number
    if test_case["first"]:
        first_input.send_keys(test_case["first"])

    # Enter second number
    if test_case["second"]:
        second_input.send_keys(test_case["second"])

    # Configure "Integers only"
    integer_checkbox = driver.find_element(By.ID, "integerSelect")

    if integer_checkbox.is_selected() != test_case["integer_only"]:
        integer_checkbox.click()

    # Select subtraction operation
    Select(
        driver.find_element(By.ID, "selectOperationDropdown")
    ).select_by_visible_text("Subtract")

    # Click Calculate
    driver.find_element(By.ID, "calculateButton").click()

    # Check whether an alert appears
    try:
        alert = WebDriverWait(driver, 1).until(
            EC.alert_is_present()
        )

        actual_result = f"Alert: {alert.text}"
        alert.accept()

    except TimeoutException:

        # No alert -> read Answer field
        answer_field = driver.find_element(
            By.ID,
            "numberAnswerField"
        )

        try:
            WebDriverWait(driver, 2).until(
                lambda current_driver:
                answer_field.get_attribute("value") != ""
            )

        except TimeoutException:
            pass

        actual_result = (
            answer_field.get_attribute("value")
            or "Answer field is empty"
        )

    # Determine verdict
    verdict = (
        "PASS"
        if result_matches(test_case, actual_result)
        else "FAIL"
    )

    return actual_result, verdict, ""


# ============================================================
# WRITE SUMMARY REPORT
# ============================================================

def write_summary(results, run_time):

    rows = [
        "# Subtraction Test Run",
        "",
        f"- **Build:** {BUILD_NAME}",
        f"- **Executed At:** {run_time}",
        "",
        "| Test ID | Test Name | Expected Result | Actual Result | Verdict |",
        "| ------- | --------- | --------------- | ------------- | ------- |",
    ]

    for test_case, actual_result, verdict in results:

        safe_result = escape_markdown_table(actual_result)
        safe_expected = escape_markdown_table(
            test_case["expected_result_text"]
        )
        safe_name = escape_markdown_table(test_case["name"])

        rows.append(
            f'| {test_case["id"]} | '
            f'{safe_name} | '
            f'{safe_expected} | '
            f'{safe_result} | '
            f'{verdict} |'
        )

    summary_path = REPORT_DIR / "sub.md"

    summary_path.write_text(
        "\n".join(rows) + "\n",
        encoding="utf-8"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    # Create report directory
    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    driver = None
    setup_error = ""
    results = []

    run_time = (
        datetime.now()
        .astimezone()
        .isoformat(timespec="seconds")
    )

    # --------------------------------------------------------
    # SETUP SELENIUM
    # --------------------------------------------------------

    try:

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(CALCULATOR_URL)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "selectBuild")
            )
        )

    except Exception as error:

        setup_error = (
            f"{type(error).__name__}: {error}"
        )

    # --------------------------------------------------------
    # EXECUTE TEST CASES
    # --------------------------------------------------------

    try:

        test_cases = load_test_cases()

        for test_case in test_cases:

            # Selenium setup failed
            if setup_error:

                actual_result = "Test could not start"
                verdict = "ERROR"
                error_details = setup_error

            else:

                try:

                    actual_result, verdict, error_details = (
                        run_test_case(
                            driver,
                            test_case
                        )
                    )

                except Exception as error:

                    actual_result = "Test execution failed"
                    verdict = "ERROR"

                    error_details = (
                        f"{type(error).__name__}: {error}"
                    )

            # Store result
            results.append(
                (
                    test_case,
                    actual_result,
                    verdict
                )
            )

            # Console output
            print(
                f'[{verdict}] '
                f'{test_case["id"]}: '
                f'{actual_result}'
            )

        # Write summary
        write_summary(
            results,
            run_time
        )

    finally:

        # Close browser
        if driver is not None:
            driver.quit()

    # Return exit code
    return (
        1
        if any(
            verdict != "PASS"
            for _, _, verdict in results
        )
        else 0
    )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    raise SystemExit(main())