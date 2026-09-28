# Báo cáo Tổng hợp Kiểm thử: Module Addition (Test Summary Report)

> **Tài liệu:** Báo cáo Tổng hợp & Đánh giá Chất lượng Kiểm thử Module Phép cộng (Addition)  
> **Dự án:** Basic Calculator Automated & Manual Testing  
> **Hệ thống kiểm thử:** [Basic Calculator](https://testsheepnz.github.io/BasicCalculator)  
> **Ngày lập báo cáo:** 2026-09-28  
> **Đơn vị thực hiện:** Nhóm Kiểm thử (QA Team)

---

## 1. Mục tiêu & Phạm vi kiểm thử (Objectives & Scope)

### 1.1. Mục tiêu
- Đánh giá toàn diện chức năng **Phép cộng (Addition)** trên toàn bộ các phiên bản phần mềm có sẵn: từ bản chuẩn **Prototype (Build 0)** đến các phiên bản dị biệt **Build 1 đến Build 8**.
- Xác định khả năng phát hiện lỗi (Defect Detection Efficiency) của bộ kịch bản kiểm thử đối với từng lỗi có chủ đích được cài cắm trong các phiên bản build.
- Cung cấp dữ liệu thực thi chi tiết làm căn cứ nghiệm thu, đánh giá chất lượng phần mềm và đưa ra quyết định release.

### 1.2. Phạm vi kiểm thử
- **Chức năng kiểm thử:** Phép toán `Add` trên form tính toán (`#calcForm`).
- **Tập dữ liệu đầu vào:**
  - Số nguyên dương, số nguyên âm, số 0.
  - Số thực / thập phân có phần lẻ (ví dụ: `5.5 + 2.3 = 7.8`, `15.8 + 4.3 = 20.1`, `10.25 + 5.5 = 15.75`).
  - Dữ liệu biên: số 9 chữ số, số 10 chữ số chạm ngưỡng `maxlength=10`.
  - Định dạng đặc biệt: tiền tố dấu `+`, chữ số 0 ở đầu (leading zeros), khoảng trắng (whitespace padding), ký hiệu số mũ khoa học (`1e3`).
  - Dữ liệu không hợp lệ: chuỗi ký tự chữ cái (`abc`, `xyz`) ở toán hạng 1 và toán hạng 2.
  - Luồng tương tác kết hợp: Tùy chọn *Integers only* và chức năng xóa kết quả bằng nút *Clear*.

---

## 2. Kế hoạch & Thiết kế Test Cases (Test Design Summary)

Bộ kịch bản kiểm thử cho module `addition` được chuẩn hóa thành **20 Test Cases** (`TC-ADD-001` đến `TC-ADD-020`), lưu trữ trực tiếp tại [`test/test_cases/addition/`](../../test_cases/addition/).

### Bảng danh mục 20 Test Cases chuẩn:

| Mã Test Case | Tên kịch bản kiểm thử | Yêu cầu (Req ID) | Kỹ thuật áp dụng | Dữ liệu đầu vào (num1 + num2) | Kỳ vọng (Expected) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-ADD-001** | Cộng hai số nguyên dương hợp lệ | `FR-ADD-01` | Equivalence Partitioning | `15 + 25` | `40` |
| **TC-ADD-002** | Cộng hai số nguyên âm | `FR-ADD-01` | Boundary Value Analysis | `-10 + -20` | `-30` |
| **TC-ADD-003** | Cộng số dương và số âm (kết quả bằng 0) | `FR-ADD-01` | Equivalence Partitioning | `50 + -50` | `0` |
| **TC-ADD-004** | Cộng số nguyên với số 0 | `FR-ADD-01` | Boundary Value Analysis | `1234 + 0` | `1234` |
| **TC-ADD-005** | Cộng hai số thập phân dương cho kết quả lẻ | `FR-ADD-02` | Boundary Value Analysis | `5.5 + 2.3` | `7.8` |
| **TC-ADD-006** | Cộng số đạt giới hạn độ dài 10 chữ số | `FR-ADD-03` | Boundary Value Analysis | `999999999 + 1` | `1000000000` |
| **TC-ADD-007** | Cộng số 0 với số 0 | `FR-ADD-01` | Boundary Value Analysis | `0 + 0` | `0` |
| **TC-ADD-008** | Cộng hai số có tiền tố dấu dương (+) | `FR-ADD-01` | Equivalence Partitioning | `+25 + +15` | `40` |
| **TC-ADD-009** | Cộng số có chữ số 0 ở đầu (Leading Zeros) | `FR-ADD-01` | Equivalence Partitioning | `0007 + 0080` | `87` |
| **TC-ADD-010** | Cộng hai số thập phân âm cho kết quả lẻ | `FR-ADD-02` | Boundary Value Analysis | `-3.25 + -2.5` | `-5.75` |
| **TC-ADD-011** | Cộng số thập phân triệt tiêu | `FR-ADD-02` | Boundary Value Analysis | `14.5 + -14.5` | `0` |
| **TC-ADD-012** | Cộng hai số có khoảng trắng ở đầu hoặc cuối | `FR-ADD-01` | Robustness Testing | ` 30  +  70 ` | `100` |
| **TC-ADD-013** | Cộng hai số lớn có 9 chữ số | `FR-ADD-03` | Boundary Value Analysis | `100000000 + 200000000` | `300000000` |
| **TC-ADD-014** | Cộng số lớn với số âm lớn triệt tiêu | `FR-ADD-01` | Boundary Value Analysis | `999999999 + -999999998` | `1` |
| **TC-ADD-015** | Cộng hai số thập phân dương (Integers only tắt) | `FR-ADD-02` | Boundary Value Analysis | `15.8 + 4.3` | `20.1` |
| **TC-ADD-016** | Cộng số dạng ký hiệu khoa học (Scientific) | `FR-ADD-01` | Equivalence Partitioning | `1e3 + 500` | `1500` |
| **TC-ADD-017** | Xác thực First number chứa ký tự chữ cái | `FR-VAL-01` | Negative / Error Guessing | `abc + 10` | Báo lỗi `Number 1 is not a number` |
| **TC-ADD-018** | Xác thực Second number chứa ký tự chữ cái | `FR-VAL-02` | Negative / Error Guessing | `10 + xyz` | Báo lỗi `Number 2 is not a number` |
| **TC-ADD-019** | Kiểm tra xóa kết quả sau phép cộng bằng nút Clear | `FR-CLR-01` | Functional / State Reset | `15 + 25`, bấm Clear | Nút Clear enabled, Answer rỗng |
| **TC-ADD-020** | Cộng hai số thập phân có 2 chữ số sau dấu phẩy | `FR-ADD-02` | Boundary Value Analysis | `10.25 + 5.5` | `15.75` |

---

## 3. Ma trận Kết quả Thực thi Kiểm thử (Builds 1 - 8)

Đợt kiểm thử thực thi tự động qua test script `add.py` độc lập trên từng build.  
- **Tổng số lượt chạy (Test Executions):** $20 \text{ Test Cases} \times 8 \text{ Builds} = 160 \text{ lượt}$.
- **Tổng số lỗi phát hiện:** **45 lỗi** (chiếm tỷ lệ thất bại trung bình 28.1% trên toàn bộ các build).

### 3.1. Bảng tổng hợp kết quả theo Build

| Phiên bản | Đặc tính của Build | Tổng TCs | Passed | Failed | Tỷ lệ Pass | Tình trạng kiểm thử | Chi tiết báo cáo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Prototype (Build 0)** | Bản chuẩn mẫu (Ground Truth) | 20 | 20 | 0 | **100.0%** | ✅ **PASSED** (Baseline) | N/A |
| **Build 1** | Không kiểm tra `isNaN` (bỏ qua validate số) | 20 | 18 | 2 | **90.0%** | ❌ **FAILED (2 Bugs)** | [add.md](../../test_runs/build1/test_runs/add.md) |
| **Build 2** | Hoán đổi phép `Add` thành `Concatenate` | 20 | 2 | 18 | **10.0%** | ❌ **FAILED (Critical - 18 Bugs)** | [add.md](../../test_runs/build2/test_runs/add.md) |
| **Build 3** | Luôn ép kiểu `isNumber = true` | 20 | 20 | 0 | **100.0%** | ✅ **PASSED** (Phép cộng số học đúng) | [add.md](../../test_runs/build3/test_runs/add.md) |
| **Build 4** | Khóa cứng tùy chọn *Integers only* | 20 | 16 | 4 | **80.0%** | ❌ **FAILED (4 Bugs)** | [add.md](../../test_runs/build4/test_runs/add.md) |
| **Build 5** | Nút `Clear` bị vô hiệu hóa (`disabled`) | 20 | 19 | 1 | **95.0%** | ❌ **FAILED (1 Bug)** | [add.md](../../test_runs/build5/test_runs/add.md) |
| **Build 6** | Không kiểm tra chia cho 0 | 20 | 20 | 0 | **100.0%** | ✅ **PASSED** (Không ảnh hưởng phép cộng) | [add.md](../../test_runs/build6/test_runs/add.md) |
| **Build 7** | Ghi đè `num1` bằng kết quả cũ (`answer`) | 20 | 2 | 18 | **10.0%** | ❌ **FAILED (Critical - 18 Bugs)** | [add.md](../../test_runs/build7/test_runs/add.md) |
| **Build 8** | Hoán đổi vị trí toán hạng `num1` và `num2` | 20 | 18 | 2 | **90.0%** | ❌ **FAILED (2 Bugs)** | [add.md](../../test_runs/build8/test_runs/add.md) |
| **TỔNG HỢP** | **Toàn bộ đợt kiểm thử** | **160** | **115** | **45** | **71.9%** | **Phát hiện 45 lỗi trên 8 builds** | — |

---

## 4. Phân tích Chi tiết Lỗi theo từng Phiên bản Build

### 4.1. Build 1 - Lỗi bỏ qua kiểm tra số hợp lệ (Pass: 18/20, Fail: 2)
- **Hành vi lỗi:** Khi nhập ký tự chữ cái vào ô nhập liệu (`abc`, `xyz`), hệ thống không thực hiện kiểm tra `isNaN()`, không hiển thị thông báo lỗi `Number X is not a number` mà âm thầm thực hiện `+num1 + +num2`, dẫn tới kết quả hiển thị là `NaN`.
- **Test cases phát hiện:**
  - `TC-ADD-017`: `abc + 10` $\rightarrow$ Thực tế ra `NaN (No validation error)` thay vì thông báo lỗi.
  - `TC-ADD-018`: `10 + xyz` $\rightarrow$ Thực tế ra `NaN (No validation error)` thay vì thông báo lỗi.
- **Mức độ nghiêm trọng:** High.

### 4.2. Build 2 - Lỗi hoán đổi phép toán Add và Concatenate (Pass: 2/20, Fail: 18)
- **Hành vi lỗi:** Khi người dùng chọn phép tính `Add` (giá trị 0), mã nguồn của Build 2 tự động chuyển đổi thành `Concatenate` (giá trị 4) và gán `isNumber = false`. Do đó, mọi phép tính cộng số học đều bị biến thành phép nối chuỗi (ví dụ: `15 + 25` ra `1525` thay vì `40`; `15.8 + 4.3` ra `15.84.3`).
- **Test cases phát hiện:** Thất bại trên 18/20 test case số học (`TC-ADD-001` đến `TC-ADD-016`, `TC-ADD-018`, `TC-ADD-020`).
- **Mức độ nghiêm trọng:** Critical (Lỗi chức năng cốt lõi).

### 4.3. Build 3 - Luôn ép kiểu số (Pass: 20/20, Fail: 0)
- **Hành vi:** Build 3 luôn đặt `isNumber = true`. Do phép cộng bản chất là phép toán số học (`isNumber = true`), nên toàn bộ 20 test case của module Addition đều vượt qua. Lỗi của Build 3 chỉ bộc lộ khi thực hiện ghép chuỗi ở module `concatenation`.

### 4.4. Build 4 - Lỗi khóa cứng Integers only (Pass: 16/20, Fail: 4)
- **Hành vi lỗi:** Checkbox *Integers only* bị khóa cứng ở trạng thái `checked = true` và `disabled = true`. Mọi kết quả phép cộng có phần thập phân lẻ đều bị hàm `parseInt()` cắt cụt phần thập phân.
- **Test cases phát hiện:**
  - `TC-ADD-005`: `5.5 + 2.3` $\rightarrow$ Kỳ vọng `7.8`, thực tế bị ép thành `7`.
  - `TC-ADD-010`: `-3.25 + -2.5` $\rightarrow$ Kỳ vọng `-5.75`, thực tế bị ép thành `-5`.
  - `TC-ADD-015`: `15.8 + 4.3` $\rightarrow$ Kỳ vọng `20.1`, thực tế bị ép thành `20`.
  - `TC-ADD-020`: `10.25 + 5.5` $\rightarrow$ Kỳ vọng `15.75`, thực tế bị ép thành `15`.
- **Mức độ nghiêm trọng:** High (Mất mát độ chính xác số học).

### 4.5. Build 5 - Lỗi vô hiệu hóa nút Clear (Pass: 19/20, Fail: 1)
- **Hành vi lỗi:** Sau khi thực hiện phép cộng ra kết quả trong ô Answer, người dùng không thể nhấn nút `Clear` do thuộc tính `disabled = true` bị khóa cứng.
- **Test cases phát hiện:**
  - `TC-ADD-019`: Kiểm tra Clear sau phép cộng $\rightarrow$ Nút Clear không bấm được, kết quả không được xóa rỗng.
- **Mức độ nghiêm trọng:** Medium.

### 4.6. Build 6 - Không kiểm tra chia cho 0 (Pass: 20/20, Fail: 0)
- **Hành vi:** Build 6 chỉ chứa lỗi ở phép chia (`case 3: Divide`). Chức năng phép cộng không bị ảnh hưởng và hoạt động chuẩn xác 20/20 test case.

### 4.7. Build 7 - Lỗi ghi đè First number bằng Answer cũ (Pass: 2/20, Fail: 18)
- **Hành vi lỗi:** Hệ thống thực thi lệnh `num1 = answer`. Khi thực hiện liên tiếp các phép tính, giá trị người dùng nhập vào ô `First number` bị vứt bỏ, thay bằng kết quả của phép tính liền trước.
- **Test cases phát hiện:** Thất bại trên 18/20 test case (`TC-ADD-001` đến `TC-ADD-017`, `TC-ADD-020`).
- **Mức độ nghiêm trọng:** Critical (Lỗi tràn bộ nhớ đệm / hỏng dữ liệu tính toán).

### 4.8. Build 8 - Lỗi hoán đổi vị trí hai toán hạng (Pass: 18/20, Fail: 2)
- **Hành vi lỗi:** Hệ thống hoán đổi `num1` và `num2` trước khi tính toán và validate (`var temp = num1; num1 = num2; num2 = temp;`).
  - *Đối với tính toán số học:* Do phép cộng có tính chất giao hoán ($a + b = b + a$), kết quả số học vẫn ra đúng.
  - *Đối với thông báo lỗi validate:* Khi nhập `First number = 10, Second number = xyz`, hệ thống đảo lại thành `num1 = xyz, num2 = 10`, dẫn tới thông báo lỗi hiển thị sai vị trí: báo `Number 1 is not a number` thay vì `Number 2`.
- **Test cases phát hiện:**
  - `TC-ADD-017`: `abc + 10` $\rightarrow$ Báo lỗi nhầm thành `Number 2 is not a number`.
  - `TC-ADD-018`: `10 + xyz` $\rightarrow$ Báo lỗi nhầm thành `Number 1 is not a number`.
- **Mức độ nghiêm trọng:** Medium / High (Báo lỗi sai lệch gây hoang mang cho người dùng).

---

## 5. Đánh giá Mức độ Bao phủ Yêu cầu (Traceability & Coverage)

Căn cứ theo [Traceability Matrix](../../test_summary/traceability-matrix.md):
- **Độ bao phủ yêu cầu (Requirements Coverage):** **100%**.
  - `FR-ADD-01` (Cộng số nguyên): Được bao phủ bởi 10 Test Cases (`TC-ADD-001`, `002`, `003`, `004`, `007`, `008`, `009`, `012`, `014`, `016`).
  - `FR-ADD-02` (Cộng số thực / thập phân): Được bao phủ bởi 5 Test Cases (`TC-ADD-005`, `010`, `011`, `015`, `020`).
  - `FR-ADD-03` (Giá trị biên độ dài): Được bao phủ bởi 2 Test Cases (`TC-ADD-006`, `013`).
  - `FR-VAL-01`, `FR-VAL-02` (Kiểm tra hợp lệ số): Được bao phủ bởi 2 Test Cases (`TC-ADD-017`, `018`).
  - `FR-CLR-01` (Tương tác nút Clear): Được bao phủ bởi 1 Test Case (`TC-ADD-019`).

---

## 6. Kết luận & Đề xuất (Conclusion & Recommendations)

### 6.1. Kết luận nghiệm thu
1. **Bản mẫu chuẩn (Prototype - Build 0):** Hoạt động hoàn hảo 100% trên tất cả 20 test case của module Addition, đáp ứng đầy đủ tiêu chuẩn nghiệm thu và làm cơ sở đo lường (Benchmark).
2. **Hiệu quả của bộ Test Cases:**
   - Bộ 20 test cases được thiết kế cực kỳ hiệu quả, giúp bóc trần toàn bộ các lỗi có chủ đích trên 8 bản build của ứng dụng Basic Calculator.
   - Phát hiện thành công cả các lỗi chức năng lớn (Hoán đổi phép toán trên Build 2, Ghi đè biến trên Build 7), lỗi nghiệp vụ số học (Làm tròn sai trên Build 4, Bỏ qua validate trên Build 1), lỗi giao diện (Khóa nút Clear trên Build 5) và lỗi logic hoán đổi vị trí validate trên Build 8.

### 6.2. Đề xuất hành động
- **Từ chối (REJECT):** Không chấp thuận phát hành các bản **Build 2** và **Build 7** do chứa lỗi mức độ Critical làm sai lệch toàn bộ chức năng cốt lõi.
- **Yêu cầu sửa lỗi (Fix Requests):**
  - Khắc phục lỗi kiểm tra `isNaN` trên Build 1.
  - Mở khóa checkbox *Integers only* cho phép người dùng tùy chọn bật/tắt trên Build 4.
  - Mở khóa thuộc tính `disabled` của nút Clear trên Build 5.
  - Sửa vị trí hoán đổi toán hạng để tránh làm sai lệch câu thông báo lỗi trên Build 8.
- **Tiếp tục kế hoạch kiểm thử:** Duy trì bộ 20 test cases này trong bộ kiểm thử hồi quy tự động (Regression Suite) và triển khai các bộ kiểm thử tương tự cho các module tiếp theo (`subtraction`, `multiplication`, `division`, `concatenation`).
