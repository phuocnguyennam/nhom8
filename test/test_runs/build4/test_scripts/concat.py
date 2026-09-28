"""
concat.py  –  Automated test runner for the Concatenate operation
Build: 1   (selectBuild value = "1")

Runs TC-CONCAT-001 … TC-CONCAT-020 against
https://testsheepnz.github.io/BasicCalculator.html
and writes the result table to:
  ../test_runs/concat.md

Requirements:
    pip install selenium
    ChromeDriver matching your Chrome version must be on PATH,
    OR use webdriver-manager:  pip install webdriver-manager
"""

import os
import sys
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ── Configuration ────────────────────────────────────────────────────────────
BUILD_NUMBER  = 4          # The build value to select in the dropdown (1-8)
BUILD_LABEL   = f"Build {BUILD_NUMBER}"
URL           = "https://testsheepnz.github.io/BasicCalculator.html"

# Paths (relative to this script's location)
SCRIPT_DIR    = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR    = os.path.join(SCRIPT_DIR, "..", "test_runs")
OUTPUT_FILE   = os.path.join(OUTPUT_DIR, "concat.md")

# ── Test-case definitions ─────────────────────────────────────────────────────
# Each entry: (tc_id, objective, num1, num2, expected_output)
# For TC-019 (both empty) expected is an empty string "".
# For TC-020 "integer only" is disabled for Concatenate → expected is plain concat.
TEST_CASES = [
    ("TC-CONCAT-001", "Concatenate two positive integers",                    "5",               "7",               "57"),
    ("TC-CONCAT-002", "Concatenate two negative integers",                    "-3",              "-8",              "-3-8"),
    ("TC-CONCAT-003", "Concatenate positive and negative integers",           "4",               "-9",              "4-9"),
    ("TC-CONCAT-004", "Concatenate negative and positive integers",           "-6",              "2",               "-62"),
    ("TC-CONCAT-005", "Concatenate two zeros",                                "0",               "0",               "00"),
    ("TC-CONCAT-006", "Concatenate positive integer and zero",                "15",              "0",               "150"),
    ("TC-CONCAT-007", "Concatenate zero and positive integer",                "0",               "42",              "042"),
    ("TC-CONCAT-008", "Concatenate two positive decimal numbers",             "3.14",            "2.71",            "3.142.71"),
    ("TC-CONCAT-009", "Concatenate two negative decimal numbers",             "-1.5",            "-2.5",            "-1.5-2.5"),
    ("TC-CONCAT-010", "Concatenate integer and decimal number",               "10",              "5.5",             "105.5"),
    ("TC-CONCAT-011", "Concatenate decimal number and integer",               "7.25",            "100",             "7.25100"),
    ("TC-CONCAT-012", "Concatenate very large numbers",                       "999999999999999", "888888888888888", "999999999999999888888888888888"),
    ("TC-CONCAT-013", "Concatenate alphabetic strings",                       "abc",             "def",             "abcdef"),
    ("TC-CONCAT-014", "Concatenate alphanumeric string and integer",          "test",            "123",             "test123"),
    ("TC-CONCAT-015", "Concatenate integer and alphanumeric string",          "456",             "xyz",             "456xyz"),
    ("TC-CONCAT-016", "Concatenate special characters",                       "!@#",             "$%^",             "!@#$%^"),
    ("TC-CONCAT-017", "Leave first number empty, provide second number",      "",                "50",              "50"),
    ("TC-CONCAT-018", "Provide first number, leave second number empty",      "100",             "",                "100"),
    ("TC-CONCAT-019", "Leave both numbers empty",                             "",                "",                ""),
    ("TC-CONCAT-020", "Concatenate two decimal numbers (integer-only N/A)",   "4.8",             "2.3",             "4.82.3"),
]


# ── Selenium helpers ──────────────────────────────────────────────────────────
def build_driver() -> webdriver.Chrome:
    """Return a headless Chrome WebDriver."""
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,800")
    try:
        # Try webdriver-manager first (auto-downloads matching ChromeDriver)
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=opts
        )
    except Exception:
        # Fall back to ChromeDriver on PATH
        driver = webdriver.Chrome(options=opts)
    return driver


def run_test(driver: webdriver.Chrome, num1: str, num2: str) -> str:
    """
    Navigate to the calculator, select the build & Concatenate operation,
    fill in the inputs, click Calculate, and return the Answer field value.
    """
    wait = WebDriverWait(driver, 15)

    driver.get(URL)

    # Select build
    build_sel = wait.until(EC.presence_of_element_located((By.ID, "selectBuild")))
    Select(build_sel).select_by_value(str(BUILD_NUMBER))

    # Select operation = Concatenate (value "4" in the page's select#selectOperationDropdown)
    op_sel = wait.until(EC.presence_of_element_located((By.ID, "selectOperationDropdown")))
    Select(op_sel).select_by_value("4")   # "4" is the value for Concatenate

    # Clear + fill First number
    num1_field = driver.find_element(By.ID, "number1Field")
    num1_field.clear()
    if num1:
        num1_field.send_keys(num1)

    # Clear + fill Second number
    num2_field = driver.find_element(By.ID, "number2Field")
    num2_field.clear()
    if num2:
        num2_field.send_keys(num2)

    # Click Calculate
    driver.find_element(By.ID, "calculateButton").click()

    # Read answer (give JS a moment to update the field)
    import time as _time
    _time.sleep(0.5)
    answer_field = driver.find_element(By.ID, "numberAnswerField")
    return answer_field.get_attribute("value") or ""


# ── Markdown report builder ───────────────────────────────────────────────────
def build_report(results: list, run_time: str) -> str:
    passed  = sum(1 for r in results if r["verdict"] == "PASSED")
    failed  = sum(1 for r in results if r["verdict"] == "FAILED")
    errored = sum(1 for r in results if r["verdict"] == "ERROR")
    total   = len(results)
    overall = "✅ ĐẠT" if failed == 0 and errored == 0 else "❌ KHÔNG ĐẠT"

    lines = []
    lines.append(f"# Test Run: Module Concatenate - {BUILD_LABEL}\n")

    lines.append("## 1. Thông tin đợt kiểm thử")
    lines.append(f"- **Đợt kiểm thử:** Test Run Concatenate - {BUILD_LABEL}")
    lines.append(f"- **Hệ thống kiểm thử:** [Basic Calculator]({URL})")
    lines.append(f"- **Phiên bản Build:** {BUILD_LABEL}")
    lines.append("- **Module:** `concatenate` (Phép nối chuỗi)")
    lines.append(f"- **Số lượng Test Cases:** {total} test cases (`TC-CONCAT-001` đến `TC-CONCAT-020`)")
    lines.append(f"- **Thời gian thực thi:** {run_time}")
    lines.append("- **Công cụ thực thi:** Python Selenium Test Runner (`concat.py`)\n")

    lines.append("## 2. Kết quả tổng quan (Execution Summary)")
    lines.append(f"- **Tổng số Test Cases thực thi:** {total}")
    lines.append(f"- **Passed:** {passed} ({passed/total*100:.1f}%)")
    lines.append(f"- **Failed:** {failed} ({failed/total*100:.1f}%)")
    lines.append(f"- **Error / Skipped:** {errored} ({errored/total*100:.1f}%)")
    lines.append(f"- **Đánh giá tổng thể:** {overall} (Phát hiện {failed + errored} lỗi)\n")

    lines.append("## 3. Bảng chi tiết kết quả thực thi (Execution Details)\n")
    lines.append("| Test Case ID | Tên kịch bản kiểm thử | num1 | num2 | Kết quả mong đợi | Kết quả thực tế | Trạng thái |")
    lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :---: |")

    for r in results:
        status_icon = "✅ **PASSED**" if r["verdict"] == "PASSED" else (
                      "⚠️ **ERROR**"  if r["verdict"] == "ERROR"  else "❌ **FAILED**")
        n1_disp = f"`{r['num1']}`" if r['num1'] else "*(empty)*"
        n2_disp = f"`{r['num2']}`" if r['num2'] else "*(empty)*"
        lines.append(
            f"| `{r['tc_id']}` | {r['objective']} | {n1_disp} | {n2_disp} "
            f"| `{r['expected']}` | `{r['actual']}` | {status_icon} |"
        )

    # Defect log
    defects = [r for r in results if r["verdict"] in ("FAILED", "ERROR")]
    lines.append("\n## 4. Danh sách Bug / Lỗi phát hiện (Defects Log)\n")
    if defects:
        lines.append("| Bug ID | Test Case | num1 | num2 | Kết quả mong đợi | Kết quả thực tế | Mức độ |")
        lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :---: |")
        for idx, r in enumerate(defects, 1):
            bug_id = f"BUG-CONCAT-B{BUILD_NUMBER}-{idx:03d}"
            n1_disp = f"`{r['num1']}`" if r['num1'] else "*(empty)*"
            n2_disp = f"`{r['num2']}`" if r['num2'] else "*(empty)*"
            lines.append(
                f"| `{bug_id}` | `{r['tc_id']}` | {n1_disp} | {n2_disp} "
                f"| `{r['expected']}` | `{r['actual']}` | **High** |"
            )
    else:
        lines.append("*Không phát hiện lỗi nào.*")

    lines.append("\n## 5. Kết luận & Đề xuất (Conclusion & Recommendation)")
    if failed == 0 and errored == 0:
        lines.append(f"- {BUILD_LABEL} vượt qua tất cả {total} test cases của module Concatenate.")
        lines.append("- **Đề xuất:** Chấp nhận phiên bản build này (PASS).")
    else:
        lines.append(f"- Phát hiện **{failed + errored}** lỗi trên {BUILD_LABEL} cho module Concatenate.")
        lines.append("- **Đề xuất:** Gửi báo cáo bug sang đội ngũ phát triển và REJECT phiên bản build này.")

    return "\n".join(lines) + "\n"


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[concat.py] Starting test run for {BUILD_LABEL} at {run_time}")
    print(f"[concat.py] Target URL : {URL}")
    print(f"[concat.py] Output file: {os.path.abspath(OUTPUT_FILE)}\n")

    driver = build_driver()
    results = []

    try:
        for tc_id, objective, num1, num2, expected in TEST_CASES:
            print(f"  Running {tc_id}  ({num1!r} concat {num2!r})  expected={expected!r}  ...", end=" ", flush=True)
            try:
                actual = run_test(driver, num1, num2)
                verdict = "PASSED" if actual == expected else "FAILED"
            except Exception as exc:
                actual  = f"ERROR: {exc}"
                verdict = "ERROR"
            icon = "✅" if verdict == "PASSED" else ("⚠️" if verdict == "ERROR" else "❌")
            print(f"{icon} {verdict}  (actual={actual!r})")
            results.append(
                dict(tc_id=tc_id, objective=objective, num1=num1, num2=num2,
                     expected=expected, actual=actual, verdict=verdict)
            )
    finally:
        driver.quit()

    # Write report
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    report = build_report(results, run_time)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(report)

    passed = sum(1 for r in results if r["verdict"] == "PASSED")
    failed = len(results) - passed
    print(f"\n[concat.py] Done. Passed={passed}, Failed/Error={failed}")
    print(f"[concat.py] Report saved → {os.path.abspath(OUTPUT_FILE)}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

