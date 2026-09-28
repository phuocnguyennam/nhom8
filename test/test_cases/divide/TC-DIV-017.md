# TC-DIV-017: Kiểm tra phép tính chia độc lập không sử dụng lại kết quả Answer trước đó

## Requirement ID
FR-DIV-01

## Module / Test type / Technique
Divide / Functional / Defect Testing

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| Lần 1 - First number | 50 |
| Lần 1 - Second number | 5 |
| Lần 2 - First number | 100 |
| Lần 2 - Second number | 2 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Thực hiện phép tính lần 1: Nhập "50" vào "First number", "5" vào "Second number", chọn "Divide", bấm "Calculate" -> Answer là "10"
3. Không bấm Clear, nhập tiếp giá trị lần 2: Nhập "100" vào "First number", "2" vào "Second number"
4. Bấm nút "Calculate"

## Expected result
Phép tính lần 2 lấy đúng giá trị mới nhập trong "First number" là 100 chia cho 2. Trường "Answer" hiển thị "50" (không lấy kết quả cũ là 10 để tính 10 / 2 = 5).

## Status / Related bugs
Not Run / None
