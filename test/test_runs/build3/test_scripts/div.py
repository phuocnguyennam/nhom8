# -*- coding: utf-8 -*-
"""
div.py - Test script for Divide operation
Trang web: https://testsheepnz.github.io/BasicCalculator.html

Cach chay:
    python div.py <build_number>
    Vi du: python div.py 1

Ket qua duoc ghi vao: test_runs/div.md
"""

import sys
import os
import time
import io
from datetime import datetime

# Fix Unicode encoding on Windows terminal
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, WebDriverException
)

# ────────────────────────────────────────────────────────────
# Cấu hình
# ────────────────────────────────────────────────────────────
URL = "https://testsheepnz.github.io/BasicCalculator.html"
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 10


# ────────────────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────────────────
def get_driver():
    """Khởi tạo WebDriver Chrome (headless tùy chọn)."""
    from selenium.webdriver.chrome.options import Options
    options = Options()
    # Bỏ comment dòng dưới nếu muốn chạy headless
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(IMPLICIT_WAIT)
    return driver


def open_calculator(driver, build_number: int):
    """Mở trang tính và chọn build."""
    driver.get(URL)
    wait = WebDriverWait(driver, EXPLICIT_WAIT)
    build_dropdown = wait.until(
        EC.presence_of_element_located((By.ID, "selectBuild"))
    )
    Select(build_dropdown).select_by_value(str(build_number))
    time.sleep(0.5)


def clear_and_calculate(driver, first: str, second: str,
                         integers_only: bool = False):
    """Nhập giá trị, chọn Divide, bấm Calculate."""
    wait = WebDriverWait(driver, EXPLICIT_WAIT)

    # First number
    fn = driver.find_element(By.ID, "number1Field")
    fn.clear()
    fn.send_keys(first)

    # Second number
    sn = driver.find_element(By.ID, "number2Field")
    sn.clear()
    sn.send_keys(second)

    # Operation = Divide (value="3" in dropdown, use visible text to be safe)
    op = Select(driver.find_element(By.ID, "selectOperationDropdown"))
    op.select_by_visible_text("Divide")

    # Integers only checkbox
    cb = driver.find_element(By.ID, "integerSelect")
    if cb.is_selected() != integers_only:
        cb.click()

    # Calculate
    driver.find_element(By.ID, "calculateButton").click()
    time.sleep(0.3)


def get_answer(driver) -> str:
    """Lấy giá trị trong ô Answer."""
    try:
        return driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
    except NoSuchElementException:
        return ""


def get_error(driver) -> str:
    """Lấy nội dung thông báo lỗi (nếu có)."""
    try:
        el = driver.find_element(By.ID, "errorMsgField")
        return el.text.strip()
    except NoSuchElementException:
        return ""


def press_clear(driver):
    """Bấm nút Clear."""
    driver.find_element(By.ID, "clearButton").click()
    time.sleep(0.3)



def check_clear_state(driver) -> dict:
    """Kiểm tra trạng thái sau khi bấm Clear."""
    answer = get_answer(driver)
    error = get_error(driver)
    cb = driver.find_element(By.ID, "integerSelect")
    cb_checked = cb.is_selected()
    return {
        "answer_empty": answer == "",
        "error_empty": error == "",
        "checkbox_unchecked": not cb_checked,
    }


# ────────────────────────────────────────────────────────────
# Định nghĩa test cases
# ────────────────────────────────────────────────────────────
class TestResult:
    def __init__(self, tc_id: str, title: str, status: str,
                 expected: str, actual: str, note: str = ""):
        self.tc_id = tc_id
        self.title = title
        self.status = status      # "PASS" | "FAIL" | "ERROR"
        self.expected = expected
        self.actual = actual
        self.note = note


def run_tc_div_001(driver, build: int) -> TestResult:
    """TC-DIV-001: Chia hai số nguyên dương chia hết (10 / 2 = 5)."""
    tc_id, title = "TC-DIV-001", "Chia hai số nguyên dương chia hết"
    expected = "5"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "10", "2", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}", không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_002(driver, build: int) -> TestResult:
    """TC-DIV-002: Chia hai số nguyên dương cho kết quả là số thập phân (5 / 2 = 2.5)."""
    tc_id, title = "TC-DIV-002", "Chia cho kết quả là số thập phân"
    expected = "2.5"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "5", "2", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}", không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_003(driver, build: int) -> TestResult:
    """TC-DIV-003: Chia số nguyên dương cho 1 (18 / 1 = 18)."""
    tc_id, title = "TC-DIV-003", "Chia số nguyên dương cho 1"
    expected = "18"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "18", "1", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}", không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_004(driver, build: int) -> TestResult:
    """TC-DIV-004: Chia số 0 cho một số nguyên dương khác 0 (0 / 9 = 0)."""
    tc_id, title = "TC-DIV-004", "Chia số 0 cho số nguyên dương"
    expected = "0"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "0", "9", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}", không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_005(driver, build: int) -> TestResult:
    """TC-DIV-005: Chia số nguyên âm cho số nguyên dương (-20 / 4 = -5)."""
    tc_id, title = "TC-DIV-005", "Chia số nguyên âm cho số nguyên dương"
    expected = "-5"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "-20", "4", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}", không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_006(driver, build: int) -> TestResult:
    """TC-DIV-006: Chia số nguyên dương cho số nguyên âm (15 / -3 = -5)."""
    tc_id, title = "TC-DIV-006", "Chia số nguyên dương cho số nguyên âm"
    expected = "-5"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "15", "-3", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}", không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_007(driver, build: int) -> TestResult:
    """TC-DIV-007: Chia hai số nguyên âm (-36 / -6 = 6)."""
    tc_id, title = "TC-DIV-007", "Chia hai số nguyên âm"
    expected = "6"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "-36", "-6", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}", không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_008(driver, build: int) -> TestResult:
    """TC-DIV-008: Chia hai số thập phân dương (7.5 / 2.5 = 3)."""
    tc_id, title = "TC-DIV-008", "Chia hai số thập phân dương"
    expected = "3"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "7.5", "2.5", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}", không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_009(driver, build: int) -> TestResult:
    """TC-DIV-009: Chia cho số 0 - Division by zero (10 / 0)."""
    tc_id, title = "TC-DIV-009", "Chia cho số 0 (Division by zero)"
    expected_error = "Divide by zero error!"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "10", "0", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (expected_error in error and answer != "Infinity")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Lỗi chứa "{expected_error}", không hiển thị "Infinity"',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected_error, "", str(e))


def run_tc_div_010(driver, build: int) -> TestResult:
    """TC-DIV-010: Chia số 0 cho số 0 (0 / 0)."""
    tc_id, title = "TC-DIV-010", "Chia số 0 cho số 0"
    expected_error = "Divide by zero error!"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "0", "0", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (expected_error in error and answer != "NaN")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Lỗi chứa "{expected_error}", không hiển thị "NaN"',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected_error, "", str(e))


def run_tc_div_011(driver, build: int) -> TestResult:
    """TC-DIV-011: Thực hiện phép chia khi bật tùy chọn Integers only (7 / 2 = 3)."""
    tc_id, title = "TC-DIV-011", "Phép chia với Integers only được bật"
    expected = "3"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "7", "2", integers_only=True)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}" (phần nguyên), không có lỗi',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_012(driver, build: int) -> TestResult:
    """TC-DIV-012: Kiểm tra thứ tự toán hạng (20 / 4 = 5, không phải 4 / 20 = 0.2)."""
    tc_id, title = "TC-DIV-012", "Kiểm tra thứ tự toán hạng (First/Second)"
    expected = "5"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "20", "4", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (answer == expected and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Answer="{expected}" (20/4, không phải 4/20=0.2)',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected, "", str(e))


def run_tc_div_013(driver, build: int) -> TestResult:
    """TC-DIV-013: Nhập ký tự không phải số vào First number ("abc" / 5)."""
    tc_id, title = "TC-DIV-013", "Nhập ký tự không phải số vào First number"
    expected_error = "Number 1 is not a number"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "abc", "5", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (expected_error in error)
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Lỗi chứa "{expected_error}"',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected_error, "", str(e))


def run_tc_div_014(driver, build: int) -> TestResult:
    """TC-DIV-014: Nhập ký tự không phải số vào Second number (10 / "xyz")."""
    tc_id, title = "TC-DIV-014", "Nhập ký tự không phải số vào Second number"
    expected_error = "Number 2 is not a number"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "10", "xyz", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (expected_error in error)
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Lỗi chứa "{expected_error}"',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected_error, "", str(e))


def run_tc_div_015(driver, build: int) -> TestResult:
    """TC-DIV-015: Nhập ký tự đặc biệt vào First number ("@#$" / 2)."""
    tc_id, title = "TC-DIV-015", "Nhập ký tự đặc biệt vào trường nhập liệu"
    expected_error = "Number 1 is not a number"
    try:
        open_calculator(driver, build)
        clear_and_calculate(driver, "@#$", "2", integers_only=False)
        answer = get_answer(driver)
        error = get_error(driver)
        passed = (expected_error in error)
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Lỗi chứa "{expected_error}"',
                          f'Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected_error, "", str(e))


def run_tc_div_016(driver, build: int) -> TestResult:
    """TC-DIV-016: Kiểm tra giới hạn độ dài nhập tối đa 10 ký tự."""
    tc_id, title = "TC-DIV-016", "Kiểm tra giới hạn độ dài nhập tối đa 10 ký tự"
    input_11_chars = "12345678901"
    expected_truncated = "1234567890"
    expected_answer = "1234567890"
    try:
        open_calculator(driver, build)
        fn = driver.find_element(By.ID, "number1Field")
        fn.clear()
        fn.send_keys(input_11_chars)
        actual_value = fn.get_attribute("value")

        sn = driver.find_element(By.ID, "number2Field")
        sn.clear()
        sn.send_keys("1")

        op = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        op.select_by_visible_text("Divide")


        cb = driver.find_element(By.ID, "integerSelect")
        if cb.is_selected():
            cb.click()

        driver.find_element(By.ID, "calculateButton").click()
        time.sleep(0.3)

        answer = get_answer(driver)
        error = get_error(driver)
        truncated_ok = (actual_value == expected_truncated)
        answer_ok = (answer == expected_answer)
        passed = truncated_ok and answer_ok and error == ""
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Ô nhận tối đa "{expected_truncated}" (10 ký tự), Answer="{expected_answer}"',
                          f'Giá trị nhận="{actual_value}", Answer="{answer}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected_answer, "", str(e))


def run_tc_div_017(driver, build: int) -> TestResult:
    """TC-DIV-017: Phép tính chia độc lập, không dùng lại kết quả Answer trước (50/5=10, sau đó 100/2=50)."""
    tc_id, title = "TC-DIV-017", "Phép tính chia độc lập (không dùng lại Answer cũ)"
    expected_second = "50"
    try:
        open_calculator(driver, build)

        # Lần 1: 50 / 5 = 10
        clear_and_calculate(driver, "50", "5", integers_only=False)
        answer_first = get_answer(driver)

        # Lần 2: không bấm Clear, nhập 100 / 2
        fn = driver.find_element(By.ID, "number1Field")
        fn.clear()
        fn.send_keys("100")
        sn = driver.find_element(By.ID, "number2Field")
        sn.clear()
        sn.send_keys("2")
        driver.find_element(By.ID, "calculateButton").click()
        time.sleep(0.3)

        answer_second = get_answer(driver)
        error = get_error(driver)
        passed = (answer_second == expected_second and error == "")
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          f'Lần 1 Answer="10", Lần 2 Answer="{expected_second}" (100/2, không dùng lại 10)',
                          f'Lần 1 Answer="{answer_first}", Lần 2 Answer="{answer_second}", lỗi="{error}"')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR", expected_second, "", str(e))


def run_tc_div_018(driver, build: int) -> TestResult:
    """TC-DIV-018: Xóa kết quả phép chia và thiết lập lại bằng nút Clear (30 / 6 = 5, sau đó Clear)."""
    tc_id, title = "TC-DIV-018", "Xóa kết quả và thiết lập lại bằng nút Clear"
    try:
        open_calculator(driver, build)

        # Tính 30 / 6 với Integers only checked
        clear_and_calculate(driver, "30", "6", integers_only=True)
        answer_before = get_answer(driver)

        # Bấm Clear
        press_clear(driver)
        state = check_clear_state(driver)

        passed = (
            state["answer_empty"]
            and state["error_empty"]
            and state["checkbox_unchecked"]
        )
        return TestResult(tc_id, title,
                          "PASS" if passed else "FAIL",
                          'Sau Clear: Answer trống, lỗi trống, Integers only bỏ tick',
                          f'Trước Clear Answer="{answer_before}"; '
                          f'Sau Clear: answer_empty={state["answer_empty"]}, '
                          f'error_empty={state["error_empty"]}, '
                          f'checkbox_unchecked={state["checkbox_unchecked"]}')
    except Exception as e:
        return TestResult(tc_id, title, "ERROR",
                          "Answer trống, lỗi trống, checkbox unchecked", "", str(e))


# ────────────────────────────────────────────────────────────
# Tạo file kết quả div.md
# ────────────────────────────────────────────────────────────
def write_report(results: list, build: int, output_path: str):
    """Ghi kết quả kiểm thử ra file div.md."""
    total = len(results)
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")
    run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "# Kết quả kiểm thử - Divide Operation",
        "",
        f"- **Build:** {build}",
        f"- **Thời gian chạy:** {run_time}",
        f"- **Tổng số test case:** {total}",
        f"- **PASS:** {passed}  |  **FAIL:** {failed}  |  **ERROR:** {errors}",
        "",
        "---",
        "",
        "## Bảng tổng hợp kết quả",
        "",
        "| TC ID | Tên test case | Kết quả |",
        "|-------|---------------|---------|",
    ]

    for r in results:
        status_icon = {"PASS": "✅ PASS", "FAIL": "❌ FAIL", "ERROR": "⚠️ ERROR"}.get(r.status, r.status)
        lines.append(f"| {r.tc_id} | {r.title} | {status_icon} |")

    lines += [
        "",
        "---",
        "",
        "## Chi tiết từng test case",
        "",
    ]

    for r in results:
        status_icon = {"PASS": "✅ PASS", "FAIL": "❌ FAIL", "ERROR": "⚠️ ERROR"}.get(r.status, r.status)
        lines += [
            f"### {r.tc_id} – {r.title}",
            "",
            f"- **Kết quả:** {status_icon}",
            f"- **Expected:** {r.expected}",
            f"- **Actual:** {r.actual}",
        ]
        if r.note:
            lines.append(f"- **Ghi chú:** {r.note}")
        lines.append("")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nĐã ghi kết quả vào: {output_path}")


# ────────────────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python div.py <build_number>")
        print("  build_number: 1 đến 8")
        sys.exit(1)

    try:
        build = int(sys.argv[1])
    except ValueError:
        print("Lỗi: build_number phải là số nguyên từ 1 đến 8.")
        sys.exit(1)

    if build < 1 or build > 8:
        print("Lỗi: build_number phải từ 1 đến 8.")
        sys.exit(1)

    # Xác định đường dẫn output dựa trên vị trí script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "..", "test_runs", "div.md")
    output_path = os.path.normpath(output_path)

    test_functions = [
        run_tc_div_001,
        run_tc_div_002,
        run_tc_div_003,
        run_tc_div_004,
        run_tc_div_005,
        run_tc_div_006,
        run_tc_div_007,
        run_tc_div_008,
        run_tc_div_009,
        run_tc_div_010,
        run_tc_div_011,
        run_tc_div_012,
        run_tc_div_013,
        run_tc_div_014,
        run_tc_div_015,
        run_tc_div_016,
        run_tc_div_017,
        run_tc_div_018,
    ]

    driver = get_driver()
    results = []

    try:
        for i, fn in enumerate(test_functions, start=1):
            tc_id = f"TC-DIV-{i:03d}"
            print(f"Đang chạy {tc_id}...", end=" ", flush=True)
            result = fn(driver, build)
            results.append(result)
            print(result.status)
            if result.status == "ERROR" and result.note:
                print(f"  [ERR] {result.note[:200]}")

    finally:
        driver.quit()

    write_report(results, build, output_path)

    # In tóm tắt
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")
    print(f"\n=== Tóm tắt: PASS={passed}, FAIL={failed}, ERROR={errors} ===")


if __name__ == "__main__":
    main()
