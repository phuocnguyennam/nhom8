from playwright.sync_api import sync_playwright


# ============================================================
# CONFIGURATION
# ============================================================

URL = "https://testsheepnz.github.io/BasicCalculator.html"

# Build selection:
# "0" = Prototype
# "1" = Build 1
# "2" = Build 2
# ...
# "9" = Build 9
BUILD = "3"


# ============================================================
# TEST CASES
# ============================================================

test_cases = [

    {
        "id": "TC-MUL-001",
        "name": "Multiply two positive integers",
        "first": "5",
        "second": "10",
        "expected": "50",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-002",
        "name": "Multiply two negative integers",
        "first": "-5",
        "second": "-10",
        "expected": "50",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-003",
        "name": "Multiply positive and negative integers",
        "first": "10",
        "second": "-5",
        "expected": "-50",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-004",
        "name": "Multiply by zero",
        "first": "12345",
        "second": "0",
        "expected": "0",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-005",
        "name": "Multiply zero by zero",
        "first": "0",
        "second": "0",
        "expected": "0",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-006",
        "name": "Multiply by one",
        "first": "1234",
        "second": "1",
        "expected": "1234",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-007",
        "name": "Multiply two decimal numbers",
        "first": "2.5",
        "second": "4.0",
        "expected": "10",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-008",
        "name": "Multiply decimal values producing a decimal result",
        "first": "2.5",
        "second": "1.5",
        "expected": "3.75",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-009",
        "name": "Integer Only with multiplication",
        "first": "5",
        "second": "6",
        "expected": "30",
        "integer_only": True,
    },

    {
        "id": "TC-MUL-010",
        "name": "Decimal multiplication with Integer Only",
        "first": "2.5",
        "second": "1.5",
        "expected": "3",
        "integer_only": True,
    },

    {
        "id": "TC-MUL-011",
        "name": "Multiply large integers",
        "first": "1000000",
        "second": "1000000",
        "expected": "1000000000000",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-012",
        "name": "Multiply with empty First number",
        "first": "",
        "second": "10",
        "expected": "0",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-013",
        "name": "Multiply with empty Second number",
        "first": "10",
        "second": "",
        "expected": "0",
        "integer_only": False,
    },

    {
        "id": "TC-MUL-014",
        "name": "Multiply with non-numeric input",
        "first": "ABC",
        "second": "10",
        "expected": None,
        "integer_only": False,
    },

    {
        "id": "TC-MUL-015",
        "name": "Clear button after multiplication",
        "first": "25",
        "second": "4",
        "expected": None,
        "integer_only": False,
    },
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def normalize(value):
    """Remove leading/trailing whitespace."""
    if value is None:
        return ""

    return value.strip()


def select_build(page):
    """Select the configured calculator build."""
    page.locator("#selectBuild").select_option(BUILD)

    # Give the build's JavaScript time to update the page.
    page.wait_for_timeout(200)


def set_integer_only(page, enabled):
    """Enable or disable the Integer Only checkbox."""

    checkbox = page.locator("#integerSelect")

    if enabled:
        if not checkbox.is_checked():
            checkbox.check()
    else:
        if checkbox.is_checked():
            checkbox.uncheck()

    page.wait_for_timeout(100)


def get_answer(page):
    """Read the Answer field."""

    return normalize(
        page.locator("#numberAnswerField").input_value()
    )


# ============================================================
# RUN ONE TEST
# ============================================================

def run_test(page, test):

    # Open calculator
    page.goto(URL)
    page.wait_for_load_state("domcontentloaded")

    # --------------------------------------------------------
    # Select Build
    # --------------------------------------------------------

    select_build(page)

    # --------------------------------------------------------
    # Enter numbers
    # --------------------------------------------------------

    page.locator("#number1Field").fill(test["first"])
    page.locator("#number2Field").fill(test["second"])

    # --------------------------------------------------------
    # Select Multiply
    # --------------------------------------------------------

    page.locator("#selectOperationDropdown").select_option("2")

    # --------------------------------------------------------
    # Integer Only
    # --------------------------------------------------------

    set_integer_only(
        page,
        test["integer_only"]
    )

    # --------------------------------------------------------
    # Calculate
    # --------------------------------------------------------

    page.locator("#calculateButton").click()

    # Allow JavaScript to update the Answer field.
    page.wait_for_timeout(300)

    # --------------------------------------------------------
    # Read result
    # --------------------------------------------------------

    actual = get_answer(page)

    # --------------------------------------------------------
    # TC-MUL-015
    # --------------------------------------------------------

    if test["id"] == "TC-MUL-015":

        multiplication_result = actual

        # Click Clear
        page.locator("#clearButton").click()

        page.wait_for_timeout(300)

        # Check whether everything was cleared.
        first_after_clear = normalize(
            page.locator("#number1Field").input_value()
        )

        second_after_clear = normalize(
            page.locator("#number2Field").input_value()
        )

        answer_after_clear = normalize(
            page.locator("#numberAnswerField").input_value()
        )

        clear_pass = (
            first_after_clear == ""
            and second_after_clear == ""
            and answer_after_clear == ""
        )

        if (
            multiplication_result == test["expected"]
            and clear_pass
        ):
            verdict = "PASS"
        else:
            verdict = "FAIL"

        return {
            "actual": multiplication_result,
            "verdict": verdict,
            "details": (
                f"After Clear -> "
                f"First='{first_after_clear}', "
                f"Second='{second_after_clear}', "
                f"Answer='{answer_after_clear}'"
            ),
        }

    # --------------------------------------------------------
    # Observation-based tests
    # --------------------------------------------------------

    if test["expected"] is None:

        return {
            "actual": actual,
            "verdict": "OBSERVE",
            "details": "Actual application behavior recorded.",
        }

    # --------------------------------------------------------
    # Normal PASS / FAIL
    # --------------------------------------------------------

    if actual == test["expected"]:
        verdict = "PASS"
    else:
        verdict = "FAIL"

    return {
        "actual": actual,
        "verdict": verdict,
        "details": "",
    }


# ============================================================
# MAIN
# ============================================================

def main():

    results = []

    with sync_playwright() as p:

        # Use Playwright's Firefox browser.
        browser = p.firefox.launch(
            headless=False
        )

        page = browser.new_page()

        print()
        print("=" * 90)
        print("TESTSHEEP BASIC CALCULATOR")
        print("MULTIPLICATION TEST SUITE")
        print("=" * 90)

        print(f"URL   : {URL}")
        print(f"BUILD : {BUILD}")

        print("=" * 90)

        # ----------------------------------------------------
        # Run all test cases
        # ----------------------------------------------------

        for test in test_cases:

            print()
            print(
                f"Running {test['id']} - "
                f"{test['name']}..."
            )

            try:

                result = run_test(
                    page,
                    test
                )

                expected = (
                    test["expected"]
                    if test["expected"] is not None
                    else "Observe"
                )

                results.append({
                    "id": test["id"],
                    "expected": expected,
                    "actual": result["actual"],
                    "verdict": result["verdict"],
                })

                print(
                    f"  Expected : {expected}"
                )

                print(
                    f"  Actual   : {result['actual']}"
                )

                print(
                    f"  Verdict  : {result['verdict']}"
                )

                if result["details"]:

                    print(
                        f"  Details  : "
                        f"{result['details']}"
                    )

            except Exception as e:

                results.append({
                    "id": test["id"],
                    "expected": (
                        test["expected"]
                        if test["expected"] is not None
                        else "Observe"
                    ),
                    "actual": f"ERROR: {e}",
                    "verdict": "ERROR",
                })

                print(
                    f"  ERROR: {e}"
                )

        browser.close()

    # ========================================================
    # FINAL SUMMARY
    # ========================================================

    print()
    print()
    print("=" * 90)
    print("FINAL RESULTS")
    print("=" * 90)

    print(
        f"{'Test ID':<15}"
        f"{'Expected':<18}"
        f"{'Actual':<22}"
        f"{'Verdict':<10}"
    )

    print("-" * 90)

    for result in results:

        print(
            f"{result['id']:<15}"
            f"{result['expected']:<18}"
            f"{result['actual']:<22}"
            f"{result['verdict']:<10}"
        )

    print("-" * 90)

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    passed = sum(
        r["verdict"] == "PASS"
        for r in results
    )

    failed = sum(
        r["verdict"] == "FAIL"
        for r in results
    )

    observed = sum(
        r["verdict"] == "OBSERVE"
        for r in results
    )

    errors = sum(
        r["verdict"] == "ERROR"
        for r in results
    )

    total = len(results)

    print(
        f"PASS    : {passed}"
    )

    print(
        f"FAIL    : {failed}"
    )

    print(
        f"OBSERVE : {observed}"
    )

    print(
        f"ERROR   : {errors}"
    )

    print(
        f"TOTAL   : {total}"
    )

    print("=" * 90)


if __name__ == "__main__":
    main()