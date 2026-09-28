# TC-DIV-005: Chia số nguyên âm cho số nguyên dương

## Requirement ID
FR-DIV-01

## Module / Test type / Technique
Divide / Functional / Equivalence Partitioning

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | -20 |
| Second number | 4 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "-20" vào ô "First number"
3. Nhập "4" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Bấm nút "Calculate"

## Expected result
Trường "Answer" hiển thị giá trị âm "-5".

## Status / Related bugs
Not Run / None

## Actual result and Verdict
- **Build 1:** Actual: Answer="-5", lỗi="" | Verdict: ✅ PASS
- **Build 2:** Actual: Answer="-5", lỗi="" | Verdict: ✅ PASS
- **Build 3:** Actual: Answer="-5", lỗi="" | Verdict: ✅ PASS
- **Build 4:** Actual: Answer="-5", lỗi="" | Verdict: ✅ PASS
- **Build 5:** Actual: Answer="-5", lỗi="" | Verdict: ✅ PASS
- **Build 6:** Actual: Answer="-5", lỗi="" | Verdict: ✅ PASS
- **Build 7:** Actual: Answer="0", lỗi="" | Verdict: ❌ FAIL
- **Build 8:** Actual: Answer="-0.2", lỗi="" | Verdict: ❌ FAIL
