# Báo cáo Tổng hợp Kiểm thử: Module Division (Test Summary Report)

> **Tài liệu:** Báo cáo Tổng hợp & Đánh giá Chất lượng Kiểm thử Module Phép chia (Division)  
> **Dự án:** Basic Calculator Automated & Manual Testing  
> **Hệ thống kiểm thử:** [Basic Calculator](https://testsheepnz.github.io/BasicCalculator)  
> **Ngày lập báo cáo:** 2026-09-28  
> **Người thực hiện:** Nguyễn Nam Phước

---

## 1. Mục tiêu & Phạm vi kiểm thử (Objectives & Scope)

### 1.1. Mục tiêu

- Đánh giá toàn diện chức năng **Phép chia (Division)** trên toàn bộ các phiên bản phần mềm có sẵn: từ bản chuẩn **Prototype (Build 0)** đến các phiên bản dị biệt **Build 1 đến Build 8**.
- Xác định khả năng phát hiện lỗi (Defect Detection Efficiency) của bộ kịch bản kiểm thử đối với từng lỗi có chủ đích được cài cắm trong các phiên bản build.
- Cung cấp dữ liệu thực thi chi tiết làm căn cứ nghiệm thu, đánh giá chất lượng phần mềm và đưa ra quyết định release.

### 1.2. Phạm vi kiểm thử

- **Chức năng kiểm thử:** Phép toán `Divide` trên form tính toán (`#calcForm`), được chọn qua dropdown `selectOperationDropdown` (value = `3`).
- **Tập dữ liệu đầu vào:**
  - Số nguyên dương chia hết và không chia hết.
  - Số nguyên âm (cả tử số và mẫu số).
  - Số thực / thập phân (ví dụ: `7.5 / 2.5 = 3`).
  - Trường hợp chia cho 0 (`10 / 0`, `0 / 0`).
  - Tùy chọn _Integers only_ bật/tắt.
  - Kiểm tra thứ tự toán hạng First/Second.
  - Dữ liệu không hợp lệ: chuỗi chữ cái, ký tự đặc biệt.
  - Giới hạn độ dài nhập liệu (`maxlength=10`).
  - Phép tính độc lập (không dùng lại Answer cũ).
  - Tương tác nút Clear để reset form.

---

## 2. Kế hoạch & Thiết kế Test Cases (Test Design Summary)

Bộ kịch bản kiểm thử cho module `division` được chuẩn hóa thành **18 Test Cases** (`TC-DIV-001` đến `TC-DIV-018`), lưu trữ tại [`test/test_cases/divide/`](../../test_cases/divide/).

### Bảng danh mục 18 Test Cases:

| Mã Test Case   | Tên kịch bản kiểm thử                                         | Req ID       | Kỹ thuật áp dụng           | Dữ liệu đầu vào (num1 / num2) | Kỳ vọng (Expected)                   |
| :------------- | :------------------------------------------------------------ | :----------- | :------------------------- | :---------------------------- | :----------------------------------- |
| **TC-DIV-001** | Chia hai số nguyên dương chia hết                             | `FR-DIV-01`  | Equivalence Partitioning   | `10 / 2`                      | `5`                                  |
| **TC-DIV-002** | Chia cho kết quả là số thập phân                              | `FR-DIV-02`  | Boundary Value Analysis    | `5 / 2`                       | `2.5`                                |
| **TC-DIV-003** | Chia số nguyên dương cho 1                                    | `FR-DIV-01`  | Boundary Value Analysis    | `18 / 1`                      | `18`                                 |
| **TC-DIV-004** | Chia số 0 cho số nguyên dương                                 | `FR-DIV-01`  | Boundary Value Analysis    | `0 / 9`                       | `0`                                  |
| **TC-DIV-005** | Chia số nguyên âm cho số nguyên dương                         | `FR-DIV-01`  | Equivalence Partitioning   | `-20 / 4`                     | `-5`                                 |
| **TC-DIV-006** | Chia số nguyên dương cho số nguyên âm                         | `FR-DIV-01`  | Equivalence Partitioning   | `15 / -3`                     | `-5`                                 |
| **TC-DIV-007** | Chia hai số nguyên âm                                         | `FR-DIV-01`  | Equivalence Partitioning   | `-36 / -6`                    | `6`                                  |
| **TC-DIV-008** | Chia hai số thập phân dương                                   | `FR-DIV-02`  | Boundary Value Analysis    | `7.5 / 2.5`                   | `3`                                  |
| **TC-DIV-009** | Chia cho số 0 – Division by zero                              | `FR-DIV-03`  | Error Guessing             | `10 / 0`                      | Báo lỗi `Divide by zero error!`      |
| **TC-DIV-010** | Chia số 0 cho số 0                                            | `FR-DIV-03`  | Error Guessing             | `0 / 0`                       | Báo lỗi `Divide by zero error!`      |
| **TC-DIV-011** | Phép chia với Integers only được bật                          | `FR-DIV-04`  | Equivalence Partitioning   | `7 / 2`, Integers only ON     | `3` (lấy phần nguyên)                |
| **TC-DIV-012** | Kiểm tra thứ tự toán hạng (First/Second)                      | `FR-DIV-01`  | Boundary Value Analysis    | `20 / 4`                      | `5` (không phải `4/20 = 0.2`)        |
| **TC-DIV-013** | Nhập ký tự chữ cái vào First number                           | `FR-VAL-01`  | Negative / Error Guessing  | `abc / 5`                     | Báo lỗi `Number 1 is not a number`   |
| **TC-DIV-014** | Nhập ký tự chữ cái vào Second number                          | `FR-VAL-02`  | Negative / Error Guessing  | `10 / xyz`                    | Báo lỗi `Number 2 is not a number`   |
| **TC-DIV-015** | Nhập ký tự đặc biệt vào trường nhập liệu                      | `FR-VAL-01`  | Negative / Error Guessing  | `@#$ / 2`                     | Báo lỗi `Number 1 is not a number`   |
| **TC-DIV-016** | Kiểm tra giới hạn độ dài nhập tối đa 10 ký tự                 | `FR-DIV-05`  | Boundary Value Analysis    | `12345678901 / 1` (11 chữ số) | Trường bị cắt còn `1234567890`, Answer=`1234567890` |
| **TC-DIV-017** | Phép tính chia độc lập – không dùng lại Answer cũ             | `FR-DIV-06`  | State Transition           | `50/5=10`, sau đó `100/2`     | Lần 2 Answer=`50` (độc lập)          |
| **TC-DIV-018** | Xóa kết quả phép chia bằng nút Clear                          | `FR-CLR-01`  | Functional / State Reset   | `30/6`, bấm Clear             | Answer rỗng, lỗi rỗng, checkbox bỏ tick |

---

## 3. Ma trận Kết quả Thực thi Kiểm thử (Builds 1–8)

Đợt kiểm thử thực thi **tự động hoàn toàn** qua test script `div.py` (Selenium WebDriver) độc lập trên từng build, chạy **song song** để tiết kiệm thời gian.

- **Tổng số lượt chạy (Test Executions):** $18 \text{ Test Cases} \times 8 \text{ Builds} = 144 \text{ lượt}$.
- **Tổng số lỗi phát hiện:** **44 lỗi** (chiếm tỷ lệ thất bại trung bình **30.6%** trên toàn bộ các build).

### 3.1. Bảng tổng hợp kết quả theo Build

| Phiên bản               | Đặc tính của Build                          | Tổng TCs | Passed | Failed | Tỷ lệ Pass | Tình trạng kiểm thử                            | Chi tiết báo cáo |
| :---------------------- | :------------------------------------------ | :------: | :----: | :----: | :--------: | :--------------------------------------------- | :--------------: |
| **Prototype (Build 0)** | Bản chuẩn mẫu (Ground Truth)                |    18    |   18   |   0    | **100.0%** | ✅ **PASSED** (Baseline)                        | N/A |
| **Build 1**             | Không kiểm tra `isNaN` (bỏ qua validate số) |    18    |   13   |   5    | **72.2%**  | ❌ **FAILED (5 Bugs)**                          | [div.md](../../test_runs/build1/test_runs/div.md) |
| **Build 2**             | Hoán đổi phép `Add` ↔ `Concatenate`         |    18    |   17   |   1    | **94.4%**  | ❌ **FAILED (1 Bug)**                           | [div.md](../../test_runs/build2/test_runs/div.md) |
| **Build 3**             | Luôn ép kiểu `isNumber = true`              |    18    |   17   |   1    | **94.4%**  | ❌ **FAILED (1 Bug)**                           | [div.md](../../test_runs/build3/test_runs/div.md) |
| **Build 4**             | Khóa cứng tùy chọn _Integers only_          |    18    |   17   |   1    | **94.4%**  | ❌ **FAILED (1 Bug)**                           | [div.md](../../test_runs/build4/test_runs/div.md) |
| **Build 5**             | Nút `Clear` bị vô hiệu hóa (`disabled`)     |    18    |   16   |   2    | **88.9%**  | ❌ **FAILED (2 Bugs)**                          | [div.md](../../test_runs/build5/test_runs/div.md) |
| **Build 6**             | Không kiểm tra chia cho 0                   |    18    |   14   |   4    | **77.8%**  | ❌ **FAILED (4 Bugs – bao gồm lỗi cốt lõi)**   | [div.md](../../test_runs/build6/test_runs/div.md) |
| **Build 7**             | Ghi đè `num1` bằng kết quả cũ (`answer`)    |    18    |    5   |   13   | **27.8%**  | ❌ **FAILED (Critical – 13 Bugs)**              | [div.md](../../test_runs/build7/test_runs/div.md) |
| **Build 8**             | Hoán đổi vị trí toán hạng `num1` và `num2`  |    18    |    1   |   17   | **5.6%**   | ❌ **FAILED (Critical – 17 Bugs)**              | [div.md](../../test_runs/build8/test_runs/div.md) |
| **TỔNG HỢP**            | **Toàn bộ đợt kiểm thử**                    | **144**  | **100**| **44** | **69.4%**  | **Phát hiện 44 lỗi trên 8 builds**             | — |

### 3.2. Ma trận kết quả chi tiết theo từng Test Case

`P` = Pass &nbsp;&nbsp; `F` = Fail

| Test ID        | Build 1 | Build 2 | Build 3 | Build 4 | Build 5 | Build 6 | Build 7 | Build 8 |
| :------------- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| **TC-DIV-001** | P | P | P | P | P | P | F | F |
| **TC-DIV-002** | P | P | P | F | P | P | F | F |
| **TC-DIV-003** | P | P | P | P | P | P | F | F |
| **TC-DIV-004** | P | P | P | P | P | P | P | F |
| **TC-DIV-005** | P | P | P | P | P | P | F | F |
| **TC-DIV-006** | P | P | P | P | P | P | F | F |
| **TC-DIV-007** | P | P | P | P | P | P | F | F |
| **TC-DIV-008** | P | P | P | P | P | P | F | F |
| **TC-DIV-009** | P | P | P | P | P | F | P | F |
| **TC-DIV-010** | P | P | P | P | P | F | P | P |
| **TC-DIV-011** | P | P | P | P | P | P | F | F |
| **TC-DIV-012** | P | P | P | P | P | P | F | F |
| **TC-DIV-013** | F | P | P | P | P | P | F | F |
| **TC-DIV-014** | F | P | P | P | P | P | P | F |
| **TC-DIV-015** | F | P | P | P | P | P | F | F |
| **TC-DIV-016** | P | P | P | P | P | P | F | F |
| **TC-DIV-017** | F | P | P | P | F | F | F | F |
| **TC-DIV-018** | F | F | F | P | F | F | P | F |
| **PASS / FAIL** | **13/5** | **17/1** | **17/1** | **17/1** | **16/2** | **14/4** | **5/13** | **1/17** |

---

## 4. Phân tích Chi tiết Lỗi theo từng Phiên bản Build

### 4.1. Build 1 – Lỗi bỏ qua kiểm tra số hợp lệ (Pass: 13/18, Fail: 5)

- **Hành vi lỗi:** Khi nhập ký tự chữ cái hoặc ký tự đặc biệt vào ô nhập liệu, hệ thống không thực hiện kiểm tra `isNaN()`, không hiển thị thông báo lỗi mà âm thầm tính toán, dẫn tới kết quả hiển thị là `NaN`. Ngoài ra, nút Clear không reset checkbox về trạng thái mặc định, và hệ thống dùng lại Answer cũ làm `num1` khi tính liên tiếp.
- **Test cases phát hiện:**
  - `TC-DIV-013`: `abc / 5` → Thực tế ra `NaN` thay vì thông báo lỗi.
  - `TC-DIV-014`: `10 / xyz` → Thực tế ra `NaN` thay vì thông báo lỗi.
  - `TC-DIV-015`: `@#$ / 2` → Thực tế ra `NaN` thay vì thông báo lỗi.
  - `TC-DIV-017`: Lần 2 Answer=`10` (dùng lại Answer cũ) thay vì `50`.
  - `TC-DIV-018`: Sau Clear, checkbox `Integers only` vẫn còn được tick.
- **Mức độ nghiêm trọng:** High.

### 4.2. Build 2 – Lỗi hoán đổi phép Add và Concatenate (Pass: 17/18, Fail: 1)

- **Hành vi lỗi:** Lỗi của Build 2 nằm ở phép `Add`/`Concatenate` (hoán đổi nhau). Phép chia (`case 3: Divide`) không bị ảnh hưởng về mặt tính toán. Tuy nhiên, nút Clear không reset checkbox `Integers only`.
- **Test cases phát hiện:**
  - `TC-DIV-018`: Sau Clear, checkbox vẫn được tích.
- **Mức độ nghiêm trọng:** Low (chỉ ảnh hưởng chức năng Clear).

### 4.3. Build 3 – Luôn ép kiểu số (Pass: 17/18, Fail: 1)

- **Hành vi:** Build 3 luôn đặt `isNumber = true`. Điều này không ảnh hưởng đến phép chia số học. Tuy nhiên, nút Clear vẫn không reset checkbox.
- **Test cases phát hiện:**
  - `TC-DIV-018`: Sau Clear, checkbox vẫn được tích.
- **Mức độ nghiêm trọng:** Low.

### 4.4. Build 4 – Lỗi khóa cứng Integers only (Pass: 17/18, Fail: 1)

- **Hành vi lỗi:** Checkbox _Integers only_ bị khóa cứng ở trạng thái `checked = true` và `disabled = true`. Mọi kết quả phép chia có phần thập phân đều bị `parseInt()` cắt cụt.
- **Test cases phát hiện:**
  - `TC-DIV-002`: `5 / 2` → Kỳ vọng `2.5`, thực tế bị ép thành `2`.
- **Mức độ nghiêm trọng:** High (Mất mát độ chính xác số học với số thập phân).

### 4.5. Build 5 – Lỗi vô hiệu hóa nút Clear (Pass: 16/18, Fail: 2)

- **Hành vi lỗi:** Nút `Clear` bị thuộc tính `disabled = true` khóa cứng sau khi tính, người dùng không thể xóa kết quả. Ngoài ra, hệ thống dùng lại Answer cũ làm `num1`.
- **Test cases phát hiện:**
  - `TC-DIV-017`: Lần 2 Answer=`10` (dùng lại Answer cũ) thay vì `50`.
  - `TC-DIV-018`: Không thể bấm nút Clear.
- **Mức độ nghiêm trọng:** Medium (TC-018) / High (TC-017).

### 4.6. Build 6 – Lỗi không kiểm tra chia cho 0 (Pass: 14/18, Fail: 4)

- **Hành vi lỗi:** Build 6 bỏ qua kiểm tra `if (num2 === 0)` trước phép chia. Kết quả là `10 / 0` hiển thị `Infinity` và `0 / 0` hiển thị `NaN` thay vì thông báo lỗi `Divide by zero error!`. Ngoài ra còn lỗi dùng lại Answer cũ và không reset Clear.
- **Test cases phát hiện:**
  - `TC-DIV-009`: `10 / 0` → Thực tế `Infinity` thay vì thông báo lỗi.
  - `TC-DIV-010`: `0 / 0` → Thực tế `NaN` thay vì thông báo lỗi.
  - `TC-DIV-017`: Lần 2 Answer=`10` (dùng lại Answer cũ).
  - `TC-DIV-018`: Sau Clear, checkbox vẫn được tích.
- **Mức độ nghiêm trọng:** Critical (lỗi cốt lõi đặc thù của phép chia – Division by zero).

### 4.7. Build 7 – Lỗi ghi đè First number bằng Answer cũ (Pass: 5/18, Fail: 13)

- **Hành vi lỗi:** Hệ thống thực thi lệnh `num1 = answer` trước khi tính. Ngay từ lần đầu tiên (khi `answer = 0`), `num1` bị đặt thành 0, dẫn đến phần lớn phép chia đều trả về 0 (`0/n = 0`). Các trường hợp may mắn PASS là những TC có kỳ vọng 0 (TC-004) hoặc kiểm tra lỗi không phụ thuộc giá trị (TC-009, TC-010, TC-014, TC-018).
- **Test cases phát hiện:** Thất bại trên 13/18 test case (`TC-001~003`, `005~008`, `011~013`, `015~017`).
- **Mức độ nghiêm trọng:** Critical (Lỗi hỏng dữ liệu tính toán – toàn bộ phép chia bị sai).

### 4.8. Build 8 – Lỗi hoán đổi vị trí toán hạng num1 và num2 (Pass: 1/18, Fail: 17)

- **Hành vi lỗi:** Hệ thống hoán đổi `num1` và `num2` trước khi tính toán (`var temp = num1; num1 = num2; num2 = temp`). Đối với phép chia (không có tính giao hoán), điều này gây ra sai lệch toàn bộ:
  - `10 / 2` → tính thành `2 / 10 = 0.2` thay vì `5`.
  - `0 / 9` → tính thành `9 / 0` → Báo lỗi Divide by zero thay vì trả về `0`.
  - `10 / 0` → tính thành `0 / 10 = 0` thay vì báo lỗi Divide by zero.
  - Thông báo lỗi validate cũng bị đảo: nhập `abc` vào First → báo `Number 2 is not a number`.
- **Test case PASS duy nhất:**
  - `TC-DIV-010`: `0 / 0` → tính thành `0 / 0` → vẫn ra `Divide by zero error!` (trùng hợp đúng).
- **Test cases phát hiện:** Thất bại trên 17/18 test case.
- **Mức độ nghiêm trọng:** Critical (Lỗi logic căn bản – toàn bộ phép chia bị đảo ngược).

---

## 5. Đánh giá Mức độ Bao phủ Yêu cầu (Traceability & Coverage)

- **Độ bao phủ yêu cầu (Requirements Coverage):** **100%**.
  - `FR-DIV-01` (Chia số nguyên): Được bao phủ bởi 7 Test Cases (`TC-DIV-001`, `003`, `004`, `005`, `006`, `007`, `012`).
  - `FR-DIV-02` (Chia số thực / thập phân): Được bao phủ bởi 2 Test Cases (`TC-DIV-002`, `008`).
  - `FR-DIV-03` (Xử lý Division by zero): Được bao phủ bởi 2 Test Cases (`TC-DIV-009`, `010`).
  - `FR-DIV-04` (Integers only): Được bao phủ bởi 1 Test Case (`TC-DIV-011`).
  - `FR-DIV-05` (Giới hạn độ dài nhập liệu): Được bao phủ bởi 1 Test Case (`TC-DIV-016`).
  - `FR-DIV-06` (Tính toán độc lập): Được bao phủ bởi 1 Test Case (`TC-DIV-017`).
  - `FR-VAL-01`, `FR-VAL-02` (Kiểm tra hợp lệ số): Được bao phủ bởi 3 Test Cases (`TC-DIV-013`, `014`, `015`).
  - `FR-CLR-01` (Tương tác nút Clear): Được bao phủ bởi 1 Test Case (`TC-DIV-018`).

---

## 6. Kết luận & Đề xuất (Conclusion & Recommendations)

### 6.1. Kết luận nghiệm thu

1. **Bản mẫu chuẩn (Prototype – Build 0):** Hoạt động hoàn hảo 100% trên tất cả 18 test case của module Division, đáp ứng đầy đủ tiêu chuẩn nghiệm thu và làm cơ sở đo lường (Benchmark).
2. **Hiệu quả của bộ Test Cases:**
   - Bộ 18 test cases được thiết kế đặc thù cho phép chia, bao phủ toàn diện từ tính toán cơ bản đến các trường hợp biên, lỗi đặc thù (Division by zero), và tương tác trạng thái (Clear, Integers only).
   - Phát hiện thành công các lỗi nghiêm trọng: hoán đổi toán hạng (Build 8 – 17/18 FAIL), ghi đè `num1` bằng Answer cũ (Build 7 – 13/18 FAIL), không kiểm tra chia cho 0 (Build 6), khóa cứng Integers only (Build 4), và vô hiệu hóa nút Clear (Build 5).
3. **Tổng số lỗi phát hiện:** 44 lỗi trên 144 lượt chạy (tỷ lệ thất bại trung bình **30.6%**).

### 6.2. Đề xuất hành động

- **Từ chối (REJECT):** Không chấp thuận phát hành các bản **Build 7** và **Build 8** do chứa lỗi mức độ Critical làm sai lệch toàn bộ chức năng phép chia (lần lượt FAIL 13/18 và 17/18 test cases).
- **Yêu cầu sửa lỗi khẩn (Critical Fix Requests):**
  - **Build 6:** Bổ sung kiểm tra `if (num2 === 0)` trước khi thực hiện phép chia để tránh hiển thị `Infinity` và `NaN`.
- **Yêu cầu sửa lỗi (Fix Requests):**
  - **Build 1:** Khôi phục kiểm tra `isNaN()` cho cả hai toán hạng; sửa lỗi Clear không reset checkbox.
  - **Build 4:** Mở khóa checkbox _Integers only_ để người dùng tùy chọn bật/tắt tự do.
  - **Build 5:** Mở khóa thuộc tính `disabled` của nút Clear; sửa lỗi dùng lại Answer cũ.
  - **Build 2 & 3:** Sửa lỗi Clear không reset checkbox về trạng thái mặc định (unchecked).
- **Tiếp tục kế hoạch kiểm thử:** Duy trì bộ 18 test cases này trong bộ kiểm thử hồi quy tự động (Regression Suite) và triển khai các bộ kiểm thử tương tự cho các module còn lại (`subtraction`, `concatenation`).
