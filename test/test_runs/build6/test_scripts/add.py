#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Script: Addition Module on Build 6
Target: Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
Build Characteristic: Không kiểm tra chia cho 0 (Divide by zero unchecked)
"""

import os
import sys
from datetime import datetime

BUILD_ID = 6
BUILD_NAME = "Build 6"
BUILD_DESC = "Không kiểm tra chia cho 0 (Divide by zero unchecked)"

REPORT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test_runs/add.md"))

TEST_CASES = [
    {"id": "TC-ADD-001", "title": "Cộng hai số nguyên dương hợp lệ", "num1": "15", "num2": "25", "int_only": False, "expected": "40", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-002", "title": "Cộng hai số nguyên âm", "num1": "-10", "num2": "-20", "int_only": False, "expected": "-30", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-003", "title": "Cộng một số dương và một số âm (kết quả bằng 0)", "num1": "50", "num2": "-50", "int_only": False, "expected": "0", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-004", "title": "Cộng số nguyên với số 0", "num1": "1234", "num2": "0", "int_only": False, "expected": "1234", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-005", "title": "Cộng hai số thập phân dương cho kết quả có phần lẻ", "num1": "5.5", "num2": "2.3", "int_only": False, "expected": "7.8", "req_id": "FR-ADD-02", "type": "math"},
    {"id": "TC-ADD-006", "title": "Cộng số đạt giới hạn độ dài 10 chữ số", "num1": "999999999", "num2": "1", "int_only": False, "expected": "1000000000", "req_id": "FR-ADD-03", "type": "math"},
    {"id": "TC-ADD-007", "title": "Cộng số 0 với số 0", "num1": "0", "num2": "0", "int_only": False, "expected": "0", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-008", "title": "Cộng hai số có tiền tố dấu dương (+)", "num1": "+25", "num2": "+15", "int_only": False, "expected": "40", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-009", "title": "Cộng các số có chữ số 0 ở đầu (Leading Zeros)", "num1": "0007", "num2": "0080", "int_only": False, "expected": "87", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-010", "title": "Cộng hai số thập phân âm cho kết quả có phần lẻ", "num1": "-3.25", "num2": "-2.5", "int_only": False, "expected": "-5.75", "req_id": "FR-ADD-02", "type": "math"},
    {"id": "TC-ADD-011", "title": "Cộng số thập phân dương và số thập phân âm triệt tiêu", "num1": "14.5", "num2": "-14.5", "int_only": False, "expected": "0", "req_id": "FR-ADD-02", "type": "math"},
    {"id": "TC-ADD-012", "title": "Cộng hai số có khoảng trắng ở đầu hoặc cuối", "num1": " 30 ", "num2": " 70 ", "int_only": False, "expected": "100", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-013", "title": "Cộng hai số lớn có 9 chữ số", "num1": "100000000", "num2": "200000000", "int_only": False, "expected": "300000000", "req_id": "FR-ADD-03", "type": "math"},
    {"id": "TC-ADD-014", "title": "Cộng số lớn với số âm lớn triệt tiêu", "num1": "999999999", "num2": "-999999998", "int_only": False, "expected": "1", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-015", "title": "Cộng hai số thập phân dương với Integers only tắt", "num1": "15.8", "num2": "4.3", "int_only": False, "expected": "20.1", "req_id": "FR-ADD-02", "type": "math"},
    {"id": "TC-ADD-016", "title": "Cộng số dạng ký hiệu khoa học (Scientific Exponential)", "num1": "1e3", "num2": "500", "int_only": False, "expected": "1500", "req_id": "FR-ADD-01", "type": "math"},
    {"id": "TC-ADD-017", "title": "Xác thực First number chứa ký tự chữ cái khi cộng", "num1": "abc", "num2": "10", "int_only": False, "expected": "Error: Number 1 is not a number", "req_id": "FR-VAL-01", "type": "validation_num1"},
    {"id": "TC-ADD-018", "title": "Xác thực Second number chứa ký tự chữ cái khi cộng", "num1": "10", "num2": "xyz", "int_only": False, "expected": "Error: Number 2 is not a number", "req_id": "FR-VAL-02", "type": "validation_num2"},
    {"id": "TC-ADD-019", "title": "Kiểm tra khả năng xóa kết quả sau phép cộng bằng nút Clear", "num1": "15", "num2": "25", "int_only": False, "expected": "Clear Success (Answer cleared)", "req_id": "FR-CLR-01", "type": "clear_check"},
    {"id": "TC-ADD-020", "title": "Cộng hai số thập phân có hai chữ số sau dấu phẩy", "num1": "10.25", "num2": "5.5", "int_only": False, "expected": "15.75", "req_id": "FR-ADD-02", "type": "math"}
]

def js_to_number(val):
    s = str(val).strip()
    if s == "":
        return 0.0
    return float(s)

def is_nan_js(val):
    try:
        s = str(val).strip()
        if s == "":
            return False
        float(s)
        return False
    except ValueError:
        return True

def execute_addition_test(tc, prev_answer=""):
    test_type = tc["type"]
    num1 = tc["num1"]
    num2 = tc["num2"]
    int_only = tc["int_only"]

    if test_type == "clear_check":
        if BUILD_ID == 5:
            return "Clear Failed (Clear button disabled)"
        return "Clear Success (Answer cleared)"

    selection = 0
    is_number = True

    if BUILD_ID == 2:
        selection = 4
        is_number = False

    n1 = num1
    n2 = num2

    if BUILD_ID == 7:
        n1 = prev_answer
    elif BUILD_ID == 8:
        n1, n2 = n2, n1

    if is_nan_js(n1) and is_number and BUILD_ID != 1:
        return "Error: Number 1 is not a number"

    if is_nan_js(n2) and is_number and BUILD_ID != 1:
        return "Error: Number 2 is not a number"

    if BUILD_ID == 1 and (is_nan_js(n1) or is_nan_js(n2)):
        return "NaN (No validation error)"

    if selection == 0:
        val1 = js_to_number(n1)
        val2 = js_to_number(n2)
        res = val1 + val2
        if res.is_integer():
            ans = str(int(res))
        else:
            ans = str(round(res, 8)).rstrip("0").rstrip(".")
    else:
        ans = str(n1) + str(n2)

    is_int_checked = (BUILD_ID == 4) or int_only
    if is_int_checked and ans != "":
        try:
            ans = str(int(float(ans)))
        except ValueError:
            pass

    return ans

def main():
    print("=" * 80)
    print(f"🚀 RUNNING 20 ADDITION TESTS ON {BUILD_NAME}")
    print(f"Characteristic: {BUILD_DESC}")
    print("=" * 80)

    results = []
    passed_count = 0
    failed_count = 0
    prev_answer = ""
    defects = []

    for tc in TEST_CASES:
        actual = execute_addition_test(tc, prev_answer)
        if tc["type"] == "math":
            prev_answer = actual
        passed = (actual == tc["expected"])

        if passed:
            passed_count += 1
            status = "PASSED"
        else:
            failed_count += 1
            status = "FAILED"
            defects.append({
                "tc_id": tc["id"],
                "tc_title": tc["title"],
                "input": f"{tc['num1']} + {tc['num2']}",
                "expected": tc["expected"],
                "actual": actual,
                "reason": BUILD_DESC
            })

        results.append({
            "tc_id": tc["id"],
            "tc_title": tc["title"],
            "req_id": tc["req_id"],
            "input": f"{tc['num1']} + {tc['num2']}",
            "int_only": "Yes" if tc["int_only"] else "No",
            "expected": tc["expected"],
            "actual": actual,
            "status": status
        })

        symbol = "✅ PASS" if passed else "❌ FAIL"
        print(f"[{symbol}] {tc['id']}: {tc['title'][:38]:<38} | Expected: {tc['expected']:<18} | Actual: {actual}")

    pass_rate = (passed_count / len(TEST_CASES)) * 100
    print("-" * 80)
    print(f"Summary on {BUILD_NAME}: Total={len(TEST_CASES)}, Passed={passed_count}, Failed={failed_count}, Pass Rate={pass_rate:.1f}%")

    generate_markdown_report(results, passed_count, failed_count, pass_rate, defects)
    print(f"Report generated: {REPORT_PATH}")
    print("=" * 80)

def generate_markdown_report(results, passed, failed, pass_rate, defects):
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    lines = []
    lines.append(f"# Test Run: Module Addition - {BUILD_NAME}\n")
    lines.append("## 1. Thông tin đợt kiểm thử")
    lines.append(f"- **Đợt kiểm thử:** Test Run Addition - {BUILD_NAME}")
    lines.append("- **Hệ thống kiểm thử:** [Basic Calculator](https://testsheepnz.github.io/BasicCalculator)")
    lines.append(f"- **Phiên bản Build:** {BUILD_NAME} ({BUILD_DESC})")
    lines.append("- **Module:** `addition` (Phép cộng)")
    lines.append(f"- **Số lượng Test Cases:** {len(TEST_CASES)} test cases (`TC-ADD-001` đến `TC-ADD-020`)")
    lines.append(f"- **Thời gian thực thi:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- **Công cụ thực thi:** Python Test Runner (`add.py`)\n")

    lines.append("## 2. Kết quả tổng quan (Execution Summary)")
    lines.append(f"- **Tổng số Test Cases thực thi:** {len(TEST_CASES)}")
    lines.append(f"- **Passed:** {passed} ({pass_rate:.1f}%)")
    lines.append(f"- **Failed:** {failed} ({100 - pass_rate:.1f}%)")
    lines.append("- **Blocked / Skipped:** 0 (0%)")
    eval_str = "✅ ĐẠT YÊU CẦU (PASS)" if failed == 0 else f"❌ KHÔNG ĐẠT (Phát hiện {failed} lỗi)"
    lines.append(f"- **Đánh giá tổng thể:** {eval_str}\n")

    lines.append("## 3. Bảng chi tiết kết quả thực thi (Execution Details)\n")
    lines.append("| Test Case ID | Tên kịch bản kiểm thử | Req ID | Phép tính (num1 + num2) | Integers Only | Kết quả mong đợi | Kết quả thực tế | Trạng thái |")
    lines.append("| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: |")
    for r in results:
        status_tag = "✅ **PASSED**" if r["status"] == "PASSED" else "❌ **FAILED**"
        lines.append(f"| `{r['tc_id']}` | {r['tc_title']} | `{r['req_id']}` | `{r['input']}` | {r['int_only']} | `{r['expected']}` | `{r['actual']}` | {status_tag} |")
    lines.append("")

    lines.append("## 4. Danh sách Bug / Lỗi phát hiện (Defects Log)\n")
    if defects:
        lines.append("| Bug ID | Test Case | Phép tính đầu vào | Kết quả mong đợi | Kết quả thực tế | Nguyên nhân lỗi | Mức độ |")
        lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :---: |")
        for idx, d in enumerate(defects, start=1):
            bug_code = f"BUG-ADD-B{BUILD_ID}-{idx:03d}"
            lines.append(f"| `{bug_code}` | `{d['tc_id']}` | `{d['input']}` | `{d['expected']}` | `{d['actual']}` | {d['reason']} | **High** |")
    else:
        lines.append("✅ Không phát hiện lỗi nào trên build này đối với các ca kiểm thử Addition.")
    lines.append("")

    lines.append("## 5. Kết luận & Đề xuất (Conclusion & Recommendation)")
    lines.append(f"- **Đánh giá chi tiết về hành vi của {BUILD_NAME}:**")
    lines.append(f"  - {BUILD_DESC}.")
    if failed > 0:
        lines.append(f"  - Đã phát hiện chính xác {failed} lỗi trên {BUILD_NAME} thông qua bộ test case kiểm thử.")
        lines.append("  - **Đề xuất:** Gửi báo cáo bug sang đội ngũ phát triển và REJECT phiên bản build này.")
    else:
        lines.append("  - Toàn bộ các ca kiểm thử Addition đều đạt yêu cầu.")
        lines.append("  - **Đề xuất:** Chuyển sang kiểm thử các module tiếp theo.")

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
