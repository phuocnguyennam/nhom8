# TC-DIV-018: Xóa kết quả phép chia và thiết lập lại bằng nút Clear

## Requirement ID
FR-DIV-06

## Module / Test type / Technique
Divide / Functional / State Transition

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | 30 |
| Second number | 6 |
| Operation | Divide |
| Integers only | Checked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "30" vào ô "First number"
3. Nhập "6" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Tích chọn checkbox "Integers only"
6. Bấm nút "Calculate" và đợi hiển thị kết quả Answer là "5"
7. Bấm nút "Clear"

## Expected result
Nút "Clear" bấm được bình thường (không bị disable). Sau khi bấm Clear: trường "Answer" bị xóa trống, checkbox "Integers only" trở về trạng thái bỏ chọn (unchecked), thông báo lỗi (nếu có) được xóa.

## Status / Related bugs
Not Run / None

## Actual result and Verdict
- **Build 1:** Actual: Trước Clear Answer="5"; Sau Clear: answer_empty=False, error_empty=True, checkbox_unchecked=False | Verdict: ❌ FAIL
- **Build 2:** Actual: Trước Clear Answer="5"; Sau Clear: answer_empty=False, error_empty=True, checkbox_unchecked=False | Verdict: ❌ FAIL
- **Build 3:** Actual: Trước Clear Answer="5"; Sau Clear: answer_empty=False, error_empty=True, checkbox_unchecked=False | Verdict: ❌ FAIL
- **Build 4:** Actual: Trước Clear Answer="5"; Sau Clear: answer_empty=True, error_empty=True, checkbox_unchecked=True | Verdict: ✅ PASS
- **Build 5:** Actual: Trước Clear Answer="5"; Sau Clear: answer_empty=False, error_empty=True, checkbox_unchecked=False | Verdict: ❌ FAIL
- **Build 6:** Actual: Trước Clear Answer="5"; Sau Clear: answer_empty=False, error_empty=True, checkbox_unchecked=False | Verdict: ❌ FAIL
- **Build 7:** Actual: Trước Clear Answer="0"; Sau Clear: answer_empty=True, error_empty=True, checkbox_unchecked=True | Verdict: ✅ PASS
- **Build 8:** Actual: Trước Clear Answer="0"; Sau Clear: answer_empty=False, error_empty=True, checkbox_unchecked=False | Verdict: ❌ FAIL
