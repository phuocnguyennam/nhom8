# TC-DIV-010: Chia số 0 cho số 0

## Requirement ID
FR-DIV-02

## Module / Test type / Technique
Divide / Functional / Error Guessing

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | 0 |
| Second number | 0 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "0" vào ô "First number"
3. Nhập "0" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Bấm nút "Calculate"

## Expected result
Hệ thống chặn phép tính và hiển thị thông báo lỗi màu đỏ tại errorMsgField: "Divide by zero error!". Không trả về kết quả "NaN" tại ô Answer.

## Status / Related bugs
Not Run / None

## Actual result and Verdict
- **Build 1:** Actual: Answer="", lỗi="Divide by zero error!" | Verdict: ✅ PASS
- **Build 2:** Actual: Answer="", lỗi="Divide by zero error!" | Verdict: ✅ PASS
- **Build 3:** Actual: Answer="", lỗi="Divide by zero error!" | Verdict: ✅ PASS
- **Build 4:** Actual: Answer="", lỗi="Divide by zero error!" | Verdict: ✅ PASS
- **Build 5:** Actual: Answer="", lỗi="Divide by zero error!" | Verdict: ✅ PASS
- **Build 6:** Actual: Answer="NaN", lỗi="" | Verdict: ❌ FAIL
- **Build 7:** Actual: Answer="", lỗi="Divide by zero error!" | Verdict: ✅ PASS
- **Build 8:** Actual: Answer="", lỗi="Divide by zero error!" | Verdict: ✅ PASS
