# TC-DIV-013: Nhập ký tự không phải số vào trường First number

## Requirement ID
FR-DIV-04

## Module / Test type / Technique
Divide / Functional / Negative Testing & Equivalence Partitioning

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | abc |
| Second number | 5 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "abc" vào ô "First number"
3. Nhập "5" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Bấm nút "Calculate"

## Expected result
Hệ thống hiển thị thông báo lỗi màu đỏ tại errorMsgField: "Number 1 is not a number". Không thực hiện phép tính.

## Status / Related bugs
Not Run / None

## Actual result and Verdict
- **Build 1:** Actual: Answer="NaN", lỗi="" | Verdict: ❌ FAIL
- **Build 2:** Actual: Answer="", lỗi="Number 1 is not a number" | Verdict: ✅ PASS
- **Build 3:** Actual: Answer="", lỗi="Number 1 is not a number" | Verdict: ✅ PASS
- **Build 4:** Actual: Answer="", lỗi="Number 1 is not a number" | Verdict: ✅ PASS
- **Build 5:** Actual: Answer="", lỗi="Number 1 is not a number" | Verdict: ✅ PASS
- **Build 6:** Actual: Answer="", lỗi="Number 1 is not a number" | Verdict: ✅ PASS
- **Build 7:** Actual: Answer="0", lỗi="" | Verdict: ❌ FAIL
- **Build 8:** Actual: Answer="", lỗi="Number 2 is not a number" | Verdict: ❌ FAIL
