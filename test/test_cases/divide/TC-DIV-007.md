# TC-DIV-007: Chia hai số nguyên âm

## Requirement ID
FR-DIV-01

## Module / Test type / Technique
Divide / Functional / Equivalence Partitioning

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | -36 |
| Second number | -6 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "-36" vào ô "First number"
3. Nhập "-6" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Bấm nút "Calculate"

## Expected result
Trường "Answer" hiển thị giá trị dương "6".

## Status / Related bugs
Not Run / None

## Actual result and Verdict
- **Build 1:** Actual: Answer="6", lỗi="" | Verdict: ✅ PASS
- **Build 2:** Actual: Answer="6", lỗi="" | Verdict: ✅ PASS
- **Build 3:** Actual: Answer="6", lỗi="" | Verdict: ✅ PASS
- **Build 4:** Actual: Answer="6", lỗi="" | Verdict: ✅ PASS
- **Build 5:** Actual: Answer="6", lỗi="" | Verdict: ✅ PASS
- **Build 6:** Actual: Answer="6", lỗi="" | Verdict: ✅ PASS
- **Build 7:** Actual: Answer="0", lỗi="" | Verdict: ❌ FAIL
- **Build 8:** Actual: Answer="0.16666666666666666", lỗi="" | Verdict: ❌ FAIL
