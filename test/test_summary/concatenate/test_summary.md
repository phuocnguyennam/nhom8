# Báo cáo Tổng hợp Kiểm thử: Module Concatenate (Test Summary Report)

> **Tài liệu:** Báo cáo Tổng hợp & Đánh giá Chất lượng Kiểm thử Module Phép nối chuỗi (Concatenate)  
> **Dự án:** Basic Calculator Automated Testing  
> **Hệ thống kiểm thử:** [Basic Calculator](https://testsheepnz.github.io/BasicCalculator)  
> **Ngày lập báo cáo:** 2026-09-28  
> **Người thực hiện:** Trần Ngọc Diễm Thúy

---

## 1. Mục tiêu & Phạm vi kiểm thử (Objectives & Scope)

### 1.1. Mục tiêu

- Đánh giá toàn diện chức năng **Phép nối chuỗi (Concatenate)** trên toàn bộ các phiên bản phần mềm có sẵn: từ bản chuẩn **Prototype (Build 0)** đến các phiên bản dị biệt **Build 1 đến Build 8**.
- Xác định khả năng phát hiện lỗi (Defect Detection Efficiency) của bộ kịch bản kiểm thử đối với từng lỗi có chủ đích được cài cắm trong các phiên bản build.
- Cung cấp dữ liệu thực thi chi tiết làm căn cứ nghiệm thu, đánh giá chất lượng phần mềm và đưa ra quyết định release.

### 1.2. Phạm vi kiểm thử

- **Chức năng kiểm thử:** Phép toán `Concatenate` (giá trị `4`) trên form tính toán, được chọn qua dropdown `selectOperationDropdown`.
- **Đặc thù của Concatenate:**
  - Hệ thống xử lý hai toán hạng dưới dạng **chuỗi ký tự (string)**, không thực hiện kiểm tra số hợp lệ (`isNaN`).
  - Checkbox **Integer only** bị vô hiệu hóa (`disabled`) khi chọn Concatenate.
  - Kết quả là phép nối chuỗi `num1 || num2` (nối trái sang phải).
- **Tập dữ liệu đầu vào:**
  - Số nguyên dương, số nguyên âm, số 0.
  - Số thực / thập phân (ví dụ: `3.14`, `-1.5`).
  - Số rất lớn (15 chữ số mỗi toán hạng) — kiểm tra giới hạn độ dài.
  - Chuỗi ký tự chữ cái (`abc`, `def`), chuỗi hỗn hợp chữ-số (`test`, `xyz`).
  - Ký tự đặc biệt (`!@#`, `$%^`).
  - Chuỗi rỗng (empty) ở một hoặc cả hai toán hạng.

---

## 2. Kế hoạch & Thiết kế Test Cases (Test Design Summary)

Bộ kịch bản kiểm thử cho module `concatenate` được chuẩn hóa thành **20 Test Cases** (`TC-CONCAT-001` đến `TC-CONCAT-020`), lưu trữ tại [`test/test_cases/concatenate/`](../../test_cases/concatenate/).

### Bảng danh mục 20 Test Cases chuẩn:

| Mã Test Case        | Tên kịch bản kiểm thử                           | Kỹ thuật áp dụng         | num1              | num2              | Kỳ vọng (Expected)              |
| :------------------ | :---------------------------------------------- | :----------------------- | :---------------- | :---------------- | :------------------------------ |
| **TC-CONCAT-001**   | Nối hai số nguyên dương                         | Equivalence Partitioning | `5`               | `7`               | `57`                            |
| **TC-CONCAT-002**   | Nối hai số nguyên âm                            | Equivalence Partitioning | `-3`              | `-8`              | `-3-8`                          |
| **TC-CONCAT-003**   | Nối số dương và số âm                           | Equivalence Partitioning | `4`               | `-9`              | `4-9`                           |
| **TC-CONCAT-004**   | Nối số âm và số dương                           | Equivalence Partitioning | `-6`              | `2`               | `-62`                           |
| **TC-CONCAT-005**   | Nối hai số 0                                    | Boundary Value Analysis  | `0`               | `0`               | `00`                            |
| **TC-CONCAT-006**   | Nối số dương với số 0                           | Boundary Value Analysis  | `15`              | `0`               | `150`                           |
| **TC-CONCAT-007**   | Nối số 0 với số dương                           | Boundary Value Analysis  | `0`               | `42`              | `042`                           |
| **TC-CONCAT-008**   | Nối hai số thập phân dương                      | Equivalence Partitioning | `3.14`            | `2.71`            | `3.142.71`                      |
| **TC-CONCAT-009**   | Nối hai số thập phân âm                         | Equivalence Partitioning | `-1.5`            | `-2.5`            | `-1.5-2.5`                      |
| **TC-CONCAT-010**   | Nối số nguyên với số thập phân                  | Equivalence Partitioning | `10`              | `5.5`             | `105.5`                         |
| **TC-CONCAT-011**   | Nối số thập phân với số nguyên                  | Equivalence Partitioning | `7.25`            | `100`             | `7.25100`                       |
| **TC-CONCAT-012**   | Nối hai số rất lớn (15 chữ số)                  | Boundary Value Analysis  | `999999999999999` | `888888888888888` | `999999999999999888888888888888` |
| **TC-CONCAT-013**   | Nối hai chuỗi ký tự chữ cái                     | Equivalence Partitioning | `abc`             | `def`             | `abcdef`                        |
| **TC-CONCAT-014**   | Nối chuỗi chữ cái với số nguyên                 | Equivalence Partitioning | `test`            | `123`             | `test123`                       |
| **TC-CONCAT-015**   | Nối số nguyên với chuỗi chữ cái                 | Equivalence Partitioning | `456`             | `xyz`             | `456xyz`                        |
| **TC-CONCAT-016**   | Nối hai chuỗi ký tự đặc biệt                    | Robustness Testing       | `!@#`             | `$%^`             | `!@#$%^`                        |
| **TC-CONCAT-017**   | Toán hạng 1 rỗng, toán hạng 2 có giá trị        | Boundary Value Analysis  | *(empty)*         | `50`              | `50`                            |
| **TC-CONCAT-018**   | Toán hạng 1 có giá trị, toán hạng 2 rỗng        | Boundary Value Analysis  | `100`             | *(empty)*         | `100`                           |
| **TC-CONCAT-019**   | Cả hai toán hạng đều rỗng                       | Boundary Value Analysis  | *(empty)*         | *(empty)*         | *(empty)*                       |
| **TC-CONCAT-020**   | Nối hai số thập phân (Integer only bị vô hiệu)  | Equivalence Partitioning | `4.8`             | `2.3`             | `4.82.3`                        |

---

## 3. Ma trận Kết quả Thực thi Kiểm thử (Builds 1 - 8)

Đợt kiểm thử thực thi hoàn toàn tự động qua test script `concat.py` (Selenium WebDriver) độc lập trên từng build.

- **Tổng số lượt chạy (Test Executions):** $20 \text{ Test Cases} \times 8 \text{ Builds} = 160 \text{ lượt}$.
- **Tổng số lỗi phát hiện:** **47 lỗi** (tỷ lệ thất bại trung bình **29.4%** trên toàn bộ các build).

### 3.1. Bảng tổng hợp kết quả theo Build

| Phiên bản               | Đặc tính của Build                                   | Tổng TCs | Passed  | Failed | Tỷ lệ Pass | Tình trạng kiểm thử                              |                      Chi tiết báo cáo                       |
| :---------------------- | :--------------------------------------------------- | :------: | :-----: | :----: | :--------: | :----------------------------------------------- | :---------------------------------------------------------: |
| **Prototype (Build 0)** | Bản chuẩn mẫu (Ground Truth)                         |    20    |   20    |   0    | **100.0%** | ✅ **PASSED** (Baseline)                          |                             N/A                             |
| **Build 1**             | Giới hạn độ dài số đầu vào (~10 ký tự mỗi số)       |    20    |   19    |   1    | **95.0%**  | ❌ **FAILED (1 Bug)**                             | [concat.md](../../test_runs/build1/test_runs/concat.md)     |
| **Build 2**             | Hoán đổi phép `Concatenate` thành `Add`              |    20    |    2    |   18   | **10.0%**  | ❌ **FAILED (Critical — 18 Bugs)**               | [concat.md](../../test_runs/build2/test_runs/concat.md)     |
| **Build 3**             | Luôn ép kiểu `isNumber = true` (bỏ qua chuỗi)       |    20    |   15    |   5    | **75.0%**  | ❌ **FAILED (5 Bugs)**                            | [concat.md](../../test_runs/build3/test_runs/concat.md)     |
| **Build 4**             | Khóa cứng _Integers only_ (không ảnh hưởng concat)  |    20    |   19    |   1    | **95.0%**  | ❌ **FAILED (1 Bug)**                             | [concat.md](../../test_runs/build4/test_runs/concat.md)     |
| **Build 5**             | Nút `Clear` bị vô hiệu hóa (không ảnh hưởng concat) |    20    |   19    |   1    | **95.0%**  | ❌ **FAILED (1 Bug)**                             | [concat.md](../../test_runs/build5/test_runs/concat.md)     |
| **Build 6**             | Không kiểm tra chia cho 0 (không ảnh hưởng concat)  |    20    |   19    |   1    | **95.0%**  | ❌ **FAILED (1 Bug)**                             | [concat.md](../../test_runs/build6/test_runs/concat.md)     |
| **Build 7**             | Chỉ trả về toán hạng 2, bỏ qua toán hạng 1          |    20    |    2    |   18   | **10.0%**  | ❌ **FAILED (Critical — 18 Bugs)**               | [concat.md](../../test_runs/build7/test_runs/concat.md)     |
| **Build 8**             | Hoán đổi vị trí toán hạng (`num2 ∥ num1`)           |    20    |    4    |   16   | **20.0%**  | ❌ **FAILED (Critical — 16 Bugs)**               | [concat.md](../../test_runs/build8/test_runs/concat.md)     |
| **TỔNG HỢP**            | **Toàn bộ đợt kiểm thử**                             | **160**  | **113** | **47** | **70.6%**  | **Phát hiện 47 lỗi trên 8 builds**               | —                                                           |

### 3.2. Biểu đồ tỷ lệ Pass/Fail theo Build

```
Build 1  ████████████████████░  95.0%  Pass / 5.0%  Fail
Build 2  ██░░░░░░░░░░░░░░░░░░░  10.0%  Pass / 90.0% Fail  ⚠ CRITICAL
Build 3  ███████████████░░░░░░  75.0%  Pass / 25.0% Fail
Build 4  ████████████████████░  95.0%  Pass / 5.0%  Fail
Build 5  ████████████████████░  95.0%  Pass / 5.0%  Fail
Build 6  ████████████████████░  95.0%  Pass / 5.0%  Fail
Build 7  ██░░░░░░░░░░░░░░░░░░░  10.0%  Pass / 90.0% Fail  ⚠ CRITICAL
Build 8  ████░░░░░░░░░░░░░░░░░  20.0%  Pass / 80.0% Fail  ⚠ CRITICAL
```

---

## 4. Phân tích Chi tiết Lỗi theo từng Phiên bản Build

### 4.1. Build 1 — Lỗi giới hạn độ dài đầu vào (Pass: 19/20, Fail: 1)

- **Hành vi lỗi:** Khi nhập hai chuỗi số rất dài (15 chữ số mỗi toán hạng), hệ thống bị giới hạn số ký tự được chấp nhận trong ô nhập liệu (khoảng 10 ký tự/số). Kết quả trả về bị cắt bớt từ 30 ký tự xuống còn ~20 ký tự (`99999999998888888888` thay vì `999999999999999888888888888888`).
- **Test case phát hiện:**
  - `TC-CONCAT-012`: `999999999999999` ∥ `888888888888888` → Thực tế ra `99999999998888888888` thay vì `999999999999999888888888888888`.
- **Mức độ nghiêm trọng:** High (Mất mát dữ liệu khi xử lý chuỗi lớn).

### 4.2. Build 2 — Lỗi hoán đổi phép Concatenate thành Add (Pass: 2/20, Fail: 18)

- **Hành vi lỗi:** Khi người dùng chọn `Concatenate` (giá trị 4), mã nguồn của Build 2 tự động ánh xạ sang `Add` (giá trị 0) và đặt `isNumber = true`. Do đó, mọi phép nối chuỗi đều bị biến thành phép cộng số học (ví dụ: `5 ∥ 7` ra `12`; `3.14 ∥ 2.71` ra `5.85`; chuỗi chữ cái như `abc ∥ def` ra `""` vì Add yêu cầu số hợp lệ).
- **Test cases phát hiện:** Thất bại trên 18/20 test cases (toàn bộ trừ TC-017 và TC-018 do một trong hai toán hạng rỗng).
- **Mức độ nghiêm trọng:** Critical (Lỗi chức năng cốt lõi — sai toàn bộ logic phép toán).

### 4.3. Build 3 — Lỗi ép kiểu isNumber = true cho Concatenate (Pass: 15/20, Fail: 5)

- **Hành vi lỗi:** Build 3 luôn đặt `isNumber = true`. Đối với phép Concatenate, điều này kích hoạt validation số học, khiến các đầu vào là chuỗi chữ cái hoặc ký tự đặc biệt bị từ chối và trả về kết quả rỗng (`""`).
- **Test cases phát hiện:**
  - `TC-CONCAT-012`: Số 15 chữ số bị cắt cụt (lỗi giới hạn độ dài, giống Build 1).
  - `TC-CONCAT-013`: `abc ∥ def` → Thực tế ra `""` thay vì `abcdef`.
  - `TC-CONCAT-014`: `test ∥ 123` → Thực tế ra `""` thay vì `test123`.
  - `TC-CONCAT-015`: `456 ∥ xyz` → Thực tế ra `""` thay vì `456xyz`.
  - `TC-CONCAT-016`: `!@# ∥ $%^` → Thực tế ra `""` thay vì `!@#$%^`.
- **Mức độ nghiêm trọng:** High (Vi phạm đặc tả: Concatenate không được kiểm tra tính hợp lệ của số).

### 4.4. Build 4 — Lỗi khóa cứng Integers only (Pass: 19/20, Fail: 1)

- **Hành vi lỗi:** Checkbox _Integers only_ bị khóa cứng (`checked = true`, `disabled = true`). Tuy nhiên, do phép Concatenate **đã vô hiệu hóa** checkbox này theo thiết kế, lỗi của Build 4 không ảnh hưởng trực tiếp đến hành vi Concatenate. Lỗi duy nhất phát hiện là TC-012 (giới hạn độ dài giống Build 1).
- **Test case phát hiện:**
  - `TC-CONCAT-012`: Số 15 chữ số bị cắt cụt.
- **Mức độ nghiêm trọng:** High (Giới hạn độ dài); lỗi _Integers only_ không bộc lộ trong module Concatenate.

### 4.5. Build 5 — Lỗi vô hiệu hóa nút Clear (Pass: 19/20, Fail: 1)

- **Hành vi lỗi:** Nút `Clear` bị vô hiệu hóa (`disabled = true`) sau khi có kết quả. Hành vi Concatenate không bị ảnh hưởng. Lỗi duy nhất phát hiện là TC-012 (giới hạn độ dài).
- **Test case phát hiện:**
  - `TC-CONCAT-012`: Số 15 chữ số bị cắt cụt.
- **Mức độ nghiêm trọng:** High (Giới hạn độ dài); lỗi Clear không bộc lộ trong module Concatenate.

### 4.6. Build 6 — Không kiểm tra chia cho 0 (Pass: 19/20, Fail: 1)

- **Hành vi:** Build 6 chỉ chứa lỗi ở phép chia (`case 3: Divide`). Chức năng Concatenate không bị ảnh hưởng. Lỗi duy nhất phát hiện là TC-012 (giới hạn độ dài).
- **Test case phát hiện:**
  - `TC-CONCAT-012`: Số 15 chữ số bị cắt cụt.
- **Mức độ nghiêm trọng:** High (Giới hạn độ dài); lỗi chia cho 0 không bộc lộ trong module Concatenate.

### 4.7. Build 7 — Lỗi chỉ trả về toán hạng 2 (Pass: 2/20, Fail: 18)

- **Hành vi lỗi:** Hệ thống thực thi `answer = num2` thay vì `answer = num1 + num2`. Toán hạng đầu tiên bị bỏ qua hoàn toàn; kết quả chỉ là chuỗi của toán hạng 2 (ví dụ: `5 ∥ 7` ra `7`; `abc ∥ def` ra `def`). Nếu toán hạng 2 rỗng thì kết quả cũng rỗng.
- **Test cases phát hiện:** Thất bại trên 18/20 test cases (toàn bộ trừ TC-017 — toán hạng 1 rỗng, và TC-019 — cả hai rỗng).
- **Mức độ nghiêm trọng:** Critical (Lỗi mất dữ liệu — toán hạng đầu hoàn toàn bị bỏ qua).

### 4.8. Build 8 — Lỗi hoán đổi vị trí hai toán hạng (Pass: 4/20, Fail: 16)

- **Hành vi lỗi:** Hệ thống hoán đổi `num1` và `num2` trước khi nối chuỗi (`answer = num2 ∥ num1`). Kết quả là thứ tự đầu ra bị đảo ngược hoàn toàn (ví dụ: `5 ∥ 7` ra `75`; `abc ∥ def` ra `defabc`; `3.14 ∥ 2.71` ra `2.713.14`).
  - Ngoại lệ: TC-005 (`0 ∥ 0` → `00`) và các trường hợp toán hạng rỗng (TC-017, TC-018, TC-019) không bị ảnh hưởng vì kết quả đối xứng.
- **Test cases phát hiện:** Thất bại trên 16/20 test cases.
- **Mức độ nghiêm trọng:** Critical (Sai thứ tự chuỗi đầu ra — vi phạm hoàn toàn đặc tả Concatenate).

---

## 5. Ma trận Lỗi tổng hợp theo Test Case × Build

Bảng sau thể hiện kết quả Pass ✅ / Fail ❌ cho từng Test Case trên mỗi Build:

| Test Case ID      | Kịch bản                          | Build 1 | Build 2 | Build 3 | Build 4 | Build 5 | Build 6 | Build 7 | Build 8 |
| :---------------- | :-------------------------------- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| TC-CONCAT-001     | Nối 2 số nguyên dương             | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-002     | Nối 2 số nguyên âm                | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-003     | Nối số dương + số âm              | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-004     | Nối số âm + số dương              | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-005     | Nối 2 số 0                        | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ✅      |
| TC-CONCAT-006     | Nối số dương + 0                  | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-007     | Nối 0 + số dương                  | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-008     | Nối 2 số thập phân dương          | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-009     | Nối 2 số thập phân âm             | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-010     | Nối số nguyên + số thập phân      | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-011     | Nối số thập phân + số nguyên      | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-012     | Nối 2 số rất lớn (15 chữ số)      | ❌      | ❌      | ❌      | ❌      | ❌      | ❌      | ❌      | ❌      |
| TC-CONCAT-013     | Nối 2 chuỗi chữ cái               | ✅      | ❌      | ❌      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-014     | Nối chuỗi + số nguyên             | ✅      | ❌      | ❌      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-015     | Nối số nguyên + chuỗi             | ✅      | ❌      | ❌      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-016     | Nối 2 chuỗi ký tự đặc biệt       | ✅      | ❌      | ❌      | ✅      | ✅      | ✅      | ❌      | ❌      |
| TC-CONCAT-017     | Toán hạng 1 rỗng                  | ✅      | ✅      | ✅      | ✅      | ✅      | ✅      | ✅      | ✅      |
| TC-CONCAT-018     | Toán hạng 2 rỗng                  | ✅      | ✅      | ✅      | ✅      | ✅      | ✅      | ❌      | ✅      |
| TC-CONCAT-019     | Cả 2 toán hạng đều rỗng           | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ✅      | ✅      |
| TC-CONCAT-020     | Nối 2 số thập phân (int-only N/A) | ✅      | ❌      | ✅      | ✅      | ✅      | ✅      | ❌      | ❌      |
| **Tổng Passed**   |                                   | **19**  | **2**   | **15**  | **19**  | **19**  | **19**  | **2**   | **4**   |
| **Tổng Failed**   |                                   | **1**   | **18**  | **5**   | **1**   | **1**   | **1**   | **18**  | **16**  |

---

## 6. Đánh giá Mức độ Bao phủ Yêu cầu (Requirements Coverage)

| Nhóm yêu cầu                      | Req ID         | Test Cases bao phủ                                          | Độ bao phủ |
| :--------------------------------- | :------------- | :---------------------------------------------------------- | :--------: |
| Nối chuỗi số nguyên                | `FR-CONCAT-01` | TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007      | ✅ 100%    |
| Nối chuỗi số thực                  | `FR-CONCAT-02` | TC-008, TC-009, TC-010, TC-011, TC-020                      | ✅ 100%    |
| Nối chuỗi ký tự phi số             | `FR-CONCAT-03` | TC-013, TC-014, TC-015, TC-016                              | ✅ 100%    |
| Giá trị biên — toán hạng rỗng      | `FR-CONCAT-04` | TC-017, TC-018, TC-019                                      | ✅ 100%    |
| Giá trị biên — chuỗi rất lớn       | `FR-CONCAT-05` | TC-012                                                      | ✅ 100%    |
| Integer only bị vô hiệu hóa        | `FR-CONCAT-06` | TC-020 (xác nhận checkbox disabled)                         | ✅ 100%    |

- **Độ bao phủ yêu cầu tổng thể:** **100%** — Toàn bộ 6 nhóm yêu cầu đều được bao phủ bởi bộ 20 test cases.

---

## 7. Phân tích Lỗi Xuyên suốt (Cross-Build Bug Analysis)

### 7.1. Lỗi phổ biến nhất — TC-012 (Xuất hiện trên tất cả 8 Builds)

- **Mô tả:** TC-CONCAT-012 thất bại trên **tất cả 8 builds**, cho thấy đây là một **lỗi hệ thống** (systemic bug) không phụ thuộc vào từng build cụ thể mà bắt nguồn từ giới hạn độ dài ô nhập liệu của trang HTML (thuộc tính `maxlength` hoặc giới hạn JavaScript Number).
- **Khuyến nghị:** Cần điều tra và nâng giới hạn độ dài ô nhập liệu hoặc chuyển xử lý sang dạng BigInt/String thuần túy.

### 7.2. Phân loại lỗi theo mức độ nghiêm trọng

| Mức độ      | Số lỗi | Builds bị ảnh hưởng | Nguyên nhân gốc rễ                                  |
| :---------- | :----: | :------------------ | :-------------------------------------------------- |
| 🔴 Critical | 52     | Build 2, 7, 8       | Sai logic phép toán cốt lõi                         |
| 🟠 High     | 8      | Build 1, 3, 4, 5, 6 | Giới hạn độ dài / ép kiểu validation sai            |

---

## 8. Kết luận & Đề xuất (Conclusion & Recommendations)

### 8.1. Kết luận nghiệm thu

1. **Bộ Test Cases đạt hiệu quả cao:** 20 test cases được thiết kế đã thành công phát hiện **47 lỗi** trên 8 phiên bản build, bao gồm các lỗi mức Critical, High và lỗi hệ thống xuyên suốt.
2. **Bản mẫu chuẩn (Prototype):** Hoạt động hoàn hảo 100% trên tất cả 20 test case, đáp ứng đầy đủ tiêu chuẩn nghiệm thu và được dùng làm baseline đo lường.
3. **Bộ test đặc biệt hiệu quả trong việc phát hiện:**
   - Lỗi **hoán đổi phép toán** (Build 2): Toàn bộ 18 test case số học thất bại ngay lập tức.
   - Lỗi **bỏ qua toán hạng đầu** (Build 7): 18 test case thất bại, dễ dàng nhận diện pattern.
   - Lỗi **đảo ngược chuỗi** (Build 8): 16 test case thất bại, phát hiện nhờ các test case có `num1 ≠ num2`.
   - Lỗi **ép kiểu validation** (Build 3): Phát hiện nhờ các test case chuỗi phi số (TC-013 đến TC-016).

### 8.2. Đề xuất hành động

| Hành động       | Build    | Nội dung                                                                                 |
| :-------------- | :------- | :--------------------------------------------------------------------------------------- |
| 🔴 **REJECT**   | Build 2  | Hoán đổi phép toán Concatenate → Add. Lỗi Critical, ảnh hưởng toàn bộ chức năng.        |
| 🔴 **REJECT**   | Build 7  | Bỏ qua toán hạng 1. Lỗi Critical, mất dữ liệu người dùng.                               |
| 🔴 **REJECT**   | Build 8  | Đảo ngược thứ tự toán hạng. Lỗi Critical, kết quả sai hoàn toàn.                        |
| 🟠 **Fix & Retest** | Build 1 | Nâng giới hạn độ dài ô nhập liệu hoặc xử lý chuỗi lớn bằng BigString.               |
| 🟠 **Fix & Retest** | Build 3 | Bỏ điều kiện `isNumber = true` khi phép toán là Concatenate.                         |
| 🟠 **Fix & Retest** | Build 4 | Không ảnh hưởng Concatenate. Cần fix riêng cho module Addition/Subtraction/...       |
| 🟠 **Fix & Retest** | Build 5 | Không ảnh hưởng Concatenate. Cần fix nút Clear cho các module khác.                  |
| 🟠 **Fix & Retest** | Build 6 | Không ảnh hưởng Concatenate. Cần fix chia cho 0 cho module Division.                 |
| 🔵 **Monitor**  | TC-012 (tất cả builds) | Lỗi giới hạn độ dài là lỗi hệ thống, cần điều tra ở tầng HTML/JS chung.  |

### 8.3. Tiếp tục kế hoạch kiểm thử

- Duy trì bộ 20 test cases này trong **Regression Suite** tự động (`concat.py`) cho mọi lần phát hành build mới.
- Bổ sung test case cho **TC-CONCAT-012** với mức chuỗi vừa phải (ví dụ: 9 ký tự mỗi toán hạng) như một test case riêng biệt kiểm tra giới hạn chính xác của `maxlength`.
- Triển khai bộ kiểm thử tương tự cho các module chưa hoàn thiện: `substract`, `multiplication`, `division`.
