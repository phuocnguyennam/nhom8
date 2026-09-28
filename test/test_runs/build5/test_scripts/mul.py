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
BUILD = "5"


# ============================================================
# TEST CASES
# ============================================================

test_cases = [

    {
        "id": "TC-MUL-001",
        "name": "Verify multiplication of two positive integers",
        "first": "5",
        "second": "10",
        "integer_only": False,
        "expected": "50",
    },

    {
        "id": "TC-MUL-002",
        "name": "Verify multiplication by zero",
        "first": "25",
        "second": "0",
        "integer_only": False,
        "expected": "0",
    },

    {
        "id": "TC-MUL-003",
        "name": "Verify multiplication of two zero values",
        "first": "0",
        "second": "0",
        "integer_only": False,
        "expected": "0",
    },

    {
        "id": "TC-MUL-004",
        "name": "Verify negative multiplied by positive",
        "first": "-5",
        "second": "10",
        "integer_only": False,
        "expected": "-50",
    },

    {
        "id": "TC-MUL-005",
        "name": "Verify negative multiplied by negative",
        "first": "-5",
        "second": "-10",
        "integer_only": False,
        "expected": "50",
    },

    {
        "id": "TC-MUL-006",
        "name": "Verify multiplication of decimal numbers",
        "first": "2.5",
        "second": "4.2",
        "integer_only": False,
        "expected": "10.5",
    },

    {
        "id": "TC-MUL-007",
        "name": "Verify decimal multiplied by integer",
        "first": "3.5",
        "second": "4",
        "integer_only": False,
        "expected": "14",
    },

    {
        "id": "TC-MUL-008",
        "name": "Verify Integers only option",
        "first": "2.5",
        "second": "3",
        "integer_only": True,

        # Observation-based because the exact integer
        # conversion behavior depends on the build.
        "expected": None,
    },

    {
        "id": "TC-MUL-009",
        "name": "Verify multiplication of large positive integers",
        "first": "100000",
        "second": "20000",
        "integer_only": False,
        "expected": "2000000000",
    },

    {
        "id": "TC-MUL-010",
        "name": "Verify multiplication by one",
        "first": "12345",
        "second": "1",
        "integer_only": False,
        "expected": "12345",
    },

    {
        "id": "TC-MUL-011",
        "name": "Verify negative decimal multiplied by negative integer",
        "first": "-2.5",
        "second": "-4",
        "integer_only": False,
        "expected": "10",
    },

    {
        "id": "TC-MUL-012",
        "name": "Verify negative decimal multiplied by positive decimal",
        "first": "-2.5",
        "second": "1.2",
        "integer_only": False,
        "expected": "-3",
    },

    {
        "id": "TC-MUL-013",
        "name": "Verify multiplication of very small decimal values",
        "first": "0.001",
        "second": "0.002",
        "integer_only": False,
        "expected": "0.000002",
    },

    {
        "id": "TC-MUL-014",
        "name": "Verify Clear button",
        "first": "5",
        "second": "10",
        "integer_only": False,
        "expected": "50",
    },

    {
        "id": "TC-MUL-015",
        "name": "Verify multiplication with missing second number",
        "first": "5",
        "second": "",
        "integer_only": False,

        # Observation-based because the exact validation
        # behavior depends on the selected build.
        "expected": None,
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

    # Allow build-specific JavaScript to update the page.
    page.wait_for_timeout(200)


def set_integer_only(page, enabled):
    """
    Enable or disable the Integer Only checkbox.

    Returns:
        True  -> checkbox is available
        False -> checkbox is disabled
    """

    checkbox = page.locator("#integerSelect")

    # Some builds disable this feature.
    if checkbox.is_disabled():
        return False

    if enabled:
        if not checkbox.is_checked():
            checkbox.check()

    else:
        if checkbox.is_checked():
            checkbox.uncheck()

    page.wait_for_timeout(100)

    return True


def get_answer(page):
    """Read the Answer field."""

    return normalize(
        page.locator("#numberAnswerField").input_value()
    )


# ============================================================
# RUN ONE TEST CASE
# ============================================================

def run_test(page, test):

    # --------------------------------------------------------
    # Open calculator
    # --------------------------------------------------------

    page.goto(URL)
    page.wait_for_load_state("domcontentloaded")

    # --------------------------------------------------------
    # Select Build
    # --------------------------------------------------------

    select_build(page)

    # ========================================================
    # TC-MUL-008
    #
    # Integer Only must be checked separately because this
    # feature may be disabled in some builds.
    # ========================================================

    if test["id"] == "TC-MUL-008":

        checkbox = page.locator("#integerSelect")

        # Check availability before doing the test.
        if checkbox.is_disabled():

            return {
                "actual": "N/A",
                "verdict": "SKIP",
                "details": (
                    "Integer Only checkbox is disabled "
                    "in this build."
                ),
            }

        # --------------------------------------------
        # Enter numbers
        # --------------------------------------------

        page.locator("#number1Field").fill(
            test["first"]
        )

        page.locator("#number2Field").fill(
            test["second"]
        )

        # --------------------------------------------
        # Select Multiply
        # --------------------------------------------

        page.locator(
            "#selectOperationDropdown"
        ).select_option("2")

        # --------------------------------------------
        # Calculate normally first
        # --------------------------------------------

        page.locator(
            "#calculateButton"
        ).click()

        page.wait_for_timeout(300)

        answer_before_integer_only = get_answer(page)

        # --------------------------------------------
        # Enable Integer Only
        # --------------------------------------------

        checkbox.check()

        page.wait_for_timeout(300)

        answer_after_integer_only = get_answer(page)

        return {
            "actual": answer_after_integer_only,
            "verdict": "OBSERVE",
            "details": (
                f"Before Integer Only='{answer_before_integer_only}', "
                f"After Integer Only='{answer_after_integer_only}'"
            ),
        }

    # ========================================================
    # Normal test cases
    # ========================================================

    # --------------------------------------------------------
    # Enter numbers
    # --------------------------------------------------------

    page.locator("#number1Field").fill(
        test["first"]
    )

    page.locator("#number2Field").fill(
        test["second"]
    )

    # --------------------------------------------------------
    # Select Multiply
    #
    # 0 = Add
    # 1 = Subtract
    # 2 = Multiply
    # 3 = Divide
    # 4 = Concatenate
    # --------------------------------------------------------

    page.locator(
        "#selectOperationDropdown"
    ).select_option("2")

    # --------------------------------------------------------
    # Integer Only
    # --------------------------------------------------------

    if test["integer_only"]:

        available = set_integer_only(
            page,
            True
        )

        if not available:

            return {
                "actual": "N/A",
                "verdict": "SKIP",
                "details": (
                    "Integer Only checkbox is disabled "
                    "in this build."
                ),
            }

    else:

        set_integer_only(
            page,
            False
        )

    # --------------------------------------------------------
    # Calculate
    # --------------------------------------------------------

    page.locator(
        "#calculateButton"
    ).click()

    page.wait_for_timeout(300)

    # --------------------------------------------------------
    # Read result
    # --------------------------------------------------------

    actual = get_answer(page)

    # ========================================================
    # TC-MUL-014
    # Clear button
    # ========================================================

    if test["id"] == "TC-MUL-014":

        multiplication_result = actual

        # --------------------------------------------
        # Click Clear
        # --------------------------------------------

        page.locator(
            "#clearButton"
        ).click()

        page.wait_for_timeout(300)

        # --------------------------------------------
        # Check fields after Clear
        # --------------------------------------------

        first_after_clear = normalize(
            page.locator(
                "#number1Field"
            ).input_value()
        )

        second_after_clear = normalize(
            page.locator(
                "#number2Field"
            ).input_value()
        )

        answer_after_clear = normalize(
            page.locator(
                "#numberAnswerField"
            ).input_value()
        )

        clear_pass = (
            first_after_clear == ""
            and second_after_clear == ""
            and answer_after_clear == ""
        )

        # Test passes only if both:
        # 1. Multiplication was correct
        # 2. Clear worked

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

    # ========================================================
    # TC-MUL-015
    # Missing second number
    # ========================================================

    if test["id"] == "TC-MUL-015":

        return {
            "actual": actual,
            "verdict": "OBSERVE",
            "details": (
                "Second number was left empty. "
                "Actual validation behavior recorded."
            ),
        }

    # ========================================================
    # Observation-based tests
    # ========================================================

    if test["expected"] is None:

        return {
            "actual": actual,
            "verdict": "OBSERVE",
            "details": (
                "Actual application behavior recorded."
            ),
        }

    # ========================================================
    # Normal PASS / FAIL
    # ========================================================

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

    # --------------------------------------------------------
    # Start Playwright
    # --------------------------------------------------------

    with sync_playwright() as p:

        # Use Firefox
        browser = p.firefox.launch(
            headless=False
        )

        page = browser.new_page()

        # ----------------------------------------------------
        # Header
        # ----------------------------------------------------

        print()
        print("=" * 100)
        print("TESTSHEEP BASIC CALCULATOR")
        print("MULTIPLICATION TEST SUITE")
        print("=" * 100)

        print(f"URL   : {URL}")
        print(f"BUILD : {BUILD}")

        print("=" * 100)

        # ====================================================
        # Run all test cases
        # ====================================================

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

                if test["expected"] is None:

                    expected = "Observe"

                else:

                    expected = test["expected"]

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

                expected = (
                    test["expected"]
                    if test["expected"] is not None
                    else "Observe"
                )

                results.append({
                    "id": test["id"],
                    "expected": expected,
                    "actual": f"ERROR: {e}",
                    "verdict": "ERROR",
                })

                print(
                    f"  ERROR: {e}"
                )

        # ----------------------------------------------------
        # Close browser
        # ----------------------------------------------------

        browser.close()

    # ========================================================
    # FINAL RESULTS
    # ========================================================

    print()
    print()
    print("=" * 100)
    print("FINAL RESULTS")
    print("=" * 100)

    print(
        f"{'Test ID':<15}"
        f"{'Expected':<18}"
        f"{'Actual':<25}"
        f"{'Verdict':<10}"
    )

    print("-" * 100)

    for result in results:

        print(
            f"{result['id']:<15}"
            f"{result['expected']:<18}"
            f"{result['actual']:<25}"
            f"{result['verdict']:<10}"
        )

    print("-" * 100)

    # ========================================================
    # STATISTICS
    # ========================================================

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

    skipped = sum(
        r["verdict"] == "SKIP"
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
        f"SKIP    : {skipped}"
    )

    print(
        f"ERROR   : {errors}"
    )

    print(
        f"TOTAL   : {total}"
    )

    print("=" * 100)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()