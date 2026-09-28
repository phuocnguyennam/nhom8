# AI AUDIT REPORT

- **Mã số sinh viên:** 23120073
- **Họ và tên:** Nguyễn Nam Phước
- **Học phần:** Kiểm thử Phần mềm (Software Testing)
- **Nhóm:** Nhóm 8
- **Ứng dụng kiểm thử:** Basic Calculator (`https://testsheepnz.github.io/BasicCalculator.html`)
- **Phạm vi chức năng:** Operation Divide (Phép chia) & Quản lý thực thi kiểm thử trên 8 bản Build (Build 1 đến Build 8)
- **Thời gian thực hiện:** 28/09/2026

---

## 1. Tuyên bố Sử dụng AI (AI Usage Declaration)

> **"Tôi sử dụng các công cụ AI cho những tác vụ sau:"**
>
> 1. **Khảo sát hệ thống và phân tích mã nguồn ứng dụng web:** Truy cập đường dẫn `https://testsheepnz.github.io/BasicCalculator.html`, trích xuất cấu trúc giao diện HTML, các phần tử DOM (`number1Field`, `number2Field`, `selectOperationDropdown`, `integerSelect`, `calculateButton`, `clearButton`, `numberAnswerField`, `errorMsgField`) và phân tích logic JavaScript của từng phiên bản Build (từ Prototype đến Build 8) nhằm xác định các lỗi chủ đích (intentional bugs).
> 2. **Thiết kế và chuẩn hóa bộ ca kiểm thử cho chức năng Phép chia (Divide):** Xây dựng bộ 18 test cases theo đúng cấu trúc template Markdown quy định, áp dụng đầy đủ các kỹ thuật thiết kế ca kiểm thử hộp đen: Phân vùng tương đương (Equivalence Partitioning), Phân tích giá trị biên (Boundary Value Analysis), Đoán lỗi (Error Guessing), Kiểm thử chuyển đổi trạng thái (State Transition).
> 3. **Phân phối và tổ chức dữ liệu kiểm thử:** Tự động tạo lập hệ thống thư mục lưu trữ test case tại `test/test_cases/divide/` đảm bảo tính nhất quán và dễ dàng bảo trì trong dự án.
> 4. **Lập trình kịch bản kiểm thử tự động (Automation Test Scripts):** Viết script Python `div.py` sử dụng thư viện Selenium WebDriver kết hợp cơ chế kiểm thử tự động, tích hợp toàn bộ 18 test cases cho từng bản build từ `build1` đến `build8`.
> 5. **Thực thi và sinh Báo cáo Thực thi Kiểm thử (Test Run Reports):** Chạy tự động kiểm thử trên toàn bộ 8 bản build và xuất kết quả thực thi chi tiết ra các file `div.md` trong thư mục `test_runs` của từng build tương ứng.
> 6. **Phân tích lỗi và khiếm khuyết phần mềm (Defect Analysis):** Nhận diện, phân loại và phân tích nguyên nhân gốc rễ (Root Cause) của từng lỗi phát sinh trên từng bản build đối với phép chia.
> 7. **Lập báo cáo minh bạch việc sử dụng Trí tuệ Nhân tạo (AI Audit Report):** Ghi chép trung thực toàn bộ nhật ký tương tác, câu lệnh và các sản phẩm do AI sinh ra.

---

## 2. Nhật Ký Chi Tiết Các Lần Tương Tác Với AI (AI Interaction Logs)

### Lần tương tác 1: Khảo sát ứng dụng và Thiết kế bộ Test Cases cho Operation Divide

- **Tên công cụ AI:** Google Antigravity (LLM Model: Claude Sonnet 4.6 / Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 14:32:10 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  https://testsheepnz.github.io/BasicCalculator.html
  Hãy truy cập đường dẫn và viết test case cho operation devide 
  C:\Code\Nhom8\nhom8\test\test_cases
  Trung thư mục test_cases tạo các thư mục từ 1 đến 8 ứng với số build
  trong thư mục build tạo thư mục divide chứa các file markdown của test case
  tất cả các build dùng chung 1 test_cases cho mỗi operation
  Đây là format (chỉ là format chứ không phải ví dụ) cho 1 file md test_case
  # TC-LOGIN-001: Đăng nhập thành công

  ## Requirement ID
  FR-LOGIN-01

  ## Module / Test type / Technique
  Login / Functional / Equivalence Partitioning

  ## Preconditions
  - User đã có tài khoản hợp lệ
  - User đang ở trang Login

  ## Test data
  | Email | user01@gmail.com |
  | Password | Abc@123456 |

  ## Test steps
  1. Mở trang Login
  2. Nhập email và password hợp lệ
  3. Bấm Login

  ## Expected result
  Đăng nhập thành công và chuyển về Home.

  ## Status / Related bugs
  Not Run / None
  ```
- **Kết quả do AI tạo ra:**
  - Truy cập trực tiếp trang web `https://testsheepnz.github.io/BasicCalculator.html`, thu thập mã nguồn HTML và logic JavaScript xử lý của máy tính.
  - Phân tích cơ chế tính toán và các lỗi cài cắm có chủ đích theo từng bản build:
    - **Build 0 (Prototype):** Chuẩn mực, không có lỗi.
    - **Build 1:** Bỏ qua kiểm tra `isNaN` (nhập chữ không bị báo lỗi số không hợp lệ).
    - **Build 2:** Đổi chỗ phép toán Add và Concatenate (Divide không bị ảnh hưởng).
    - **Build 3:** Luôn ép kiểu về số (Divide không bị ảnh hưởng).
    - **Build 4:** Khóa cứng checkbox `Integers only` luôn được chọn (`checked = true`).
    - **Build 5:** Vô hiệu hóa nút `Clear` (`disabled = true`).
    - **Build 6:** Bỏ qua kiểm tra chia cho số 0 (`num2 == 0`).
    - **Build 7:** Dùng kết quả `answer` của phép tính trước làm số thứ nhất (`num1 = answer`).
    - **Build 8:** Đổi chỗ số thứ nhất và số thứ hai (`num1` hoán vị với `num2`).
  - Thiết kế và sinh hoàn chỉnh 18 file test case Markdown (`TC-DIV-001.md` đến `TC-DIV-018.md`) tuân thủ chính xác định dạng yêu cầu:
    - `TC-DIV-001`: Chia hai số nguyên dương chia hết ($10 / 2 = 5$).
    - `TC-DIV-002`: Chia hai số nguyên dương ra số thập phân ($5 / 2 = 2.5$).
    - `TC-DIV-003`: Chia số nguyên dương cho 1 ($18 / 1 = 18$).
    - `TC-DIV-004`: Chia số 0 cho số nguyên khác 0 ($0 / 9 = 0$).
    - `TC-DIV-005`: Chia số nguyên âm cho số nguyên dương ($-20 / 4 = -5$).
    - `TC-DIV-006`: Chia số nguyên dương cho số nguyên âm ($15 / -3 = -5$).
    - `TC-DIV-007`: Chia hai số nguyên âm ($-36 / -6 = 6$).
    - `TC-DIV-008`: Chia hai số thập phân dương ($7.5 / 2.5 = 3$).
    - `TC-DIV-009`: Chia cho số 0 (Division by zero: $10 / 0 \rightarrow$ Báo lỗi `Divide by zero error!`).
    - `TC-DIV-010`: Chia số 0 cho số 0 ($0 / 0 \rightarrow$ Báo lỗi `Divide by zero error!`).
    - `TC-DIV-011`: Phép chia khi bật tùy chọn "Integers only" ($7 / 2 \rightarrow 3$).
    - `TC-DIV-012`: Kiểm tra thứ tự toán hạng của phép chia ($20 / 4 = 5$, không bị thành $4 / 20$).
    - `TC-DIV-013`: Nhập chữ cái vào trường "First number" (Báo lỗi `Number 1 is not a number`).
    - `TC-DIV-014`: Nhập chữ cái vào trường "Second number" (Báo lỗi `Number 2 is not a number`).
    - `TC-DIV-015`: Nhập ký tự đặc biệt (@#$) vào trường dữ liệu.
    - `TC-DIV-016`: Kiểm tra giới hạn độ dài nhập liệu tối đa 10 ký tự (`maxlength="10"`).
    - `TC-DIV-017`: Phép tính chia độc lập không bị dùng lại kết quả Answer cũ.
    - `TC-DIV-018`: Xóa kết quả phép chia và thiết lập lại biểu mẫu bằng nút Clear.
  - Tổ chức và lưu trữ toàn bộ các file test case tại thư mục `test/test_cases/divide/`.

---

### Lần tương tác 2: Viết kịch bản kiểm thử tự động `div.py` cho toàn bộ 8 Build

- **Tên công cụ AI:** Google Antigravity (LLM Model: Claude Sonnet 4.6 Thinking)
- **Ngày và giờ:** 2026-09-28 15:30:33 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  Với thư mục test_run đã có folder từ 1 đến 8 bên trong mỗi folder viết 1 script div.py
  ở trong test_scripts chứa toàn bộ test case cho operation divide dựa vào các test case
  trong thư mục test_cases và ghi kết quả ra file div.md ở trong test_runs
  ```
- **Kết quả do AI tạo ra:**

  **Quy trình thực hiện:**
  1. **Khảo sát cấu trúc thư mục:** AI tự động duyệt toàn bộ cây thư mục dự án, xác nhận cấu trúc `test/test_runs/build{1-8}/test_scripts/` và `test/test_runs/build{1-8}/test_runs/`.
  2. **Đọc và phân tích 18 test cases:** Đọc toàn bộ nội dung 18 file `TC-DIV-001.md` đến `TC-DIV-018.md` tại `test/test_cases/divide/`, trích xuất dữ liệu đầu vào, điều kiện Integers only và kết quả kỳ vọng cho từng ca kiểm thử.
  3. **Khám phá DOM thực tế:** Chạy Selenium để truy cập trang web, xác định đúng các ID phần tử:
     - Dropdown Build: `selectBuild` (value `"1"` đến `"8"`)
     - Dropdown Operation: `selectOperationDropdown` (value số: Add=`0`, Subtract=`1`, Multiply=`2`, **Divide=`3`**, Concatenate=`4`) → phải dùng `select_by_visible_text("Divide")`, không phải `select_by_value("Divide")`
     - Nút tính: `calculateButton`, Nút xóa: `clearButton` (không phải `resetButton`)
     - Ô kết quả: `numberAnswerField`, Thông báo lỗi: `errorMsgField`, Checkbox: `integerSelect`
  4. **Lập trình `div.py`:** Sinh file Python (~650 dòng) triển khai Selenium WebDriver với đầy đủ 18 hàm kiểm thử độc lập (`run_tc_div_001` đến `run_tc_div_018`), class `TestResult` và hàm `write_report()` xuất file `div.md`.
  5. **Debug và sửa lỗi lặp:** Xử lý 3 lần lỗi phát sinh trong quá trình chạy thực tế:
     - `UnicodeEncodeError`: Fix bằng `io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")` và biến môi trường `PYTHONIOENCODING=utf-8`.
     - `NoSuchElementException` cho "Divide": Sửa `select_by_value("Divide")` → `select_by_visible_text("Divide")` (dropdown dùng value số, không phải text).
     - `NoSuchElementException` cho "resetButton": Sửa thành `clearButton` (ID thực tế trên trang).
  6. **Phân phối script:** Sau khi hoàn chỉnh, copy `div.py` sang tất cả 8 thư mục `build{1-8}/test_scripts/`.

  **Sản phẩm tạo ra:**
  - File `div.py` hoàn chỉnh tại `test/test_runs/build{1-8}/test_scripts/div.py` (8 bản đồng nhất).
  - Cú pháp chạy: `python div.py <build_number>` (ví dụ: `python div.py 1`).
  - Script tự động: mở Chrome, chọn đúng build, thực thi 18 test case, ghi kết quả ra `test_runs/div.md`.

  **Kết quả chạy thử Build 1:**

  | TC ID | Tên test case | Kết quả |
  |-------|---------------|---------|
  | TC-DIV-001 đến TC-DIV-012, TC-DIV-016 | Các ca phép chia cơ bản và giới hạn ký tự | ✅ PASS |
  | TC-DIV-013, TC-DIV-014, TC-DIV-015 | Nhập ký tự không hợp lệ | ❌ FAIL (Build 1 không validate, trả về NaN) |
  | TC-DIV-017 | Phép tính độc lập | ❌ FAIL (Build 1 dùng lại Answer cũ) |
  | TC-DIV-018 | Nút Clear | ❌ FAIL (Build 1 không reset checkbox sau Clear) |

  **Tóm tắt Build 1:** PASS=13, FAIL=5, ERROR=0

---

### Lần tương tác 3: Thực thi kiểm thử tự động trên toàn bộ 8 Build và tổng hợp kết quả

- **Tên công cụ AI:** Google Antigravity (LLM Model: Claude Sonnet 4.6 Thinking)
- **Ngày và giờ:** 2026-09-28 15:46:54 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  Bạn hãy chạy cho các build khác luôn đi
  ```
- **Kết quả do AI tạo ra:**

  AI khởi chạy **song song 7 tiến trình** (Build 2 đến Build 8) cùng lúc, mỗi tiến trình mở một cửa sổ Chrome riêng biệt và thực thi toàn bộ 18 test case. Kết quả được ghi vào `test_runs/div.md` của từng build tương ứng.

  **Bảng kết quả tổng hợp tất cả 8 Build:**

  | Build | ✅ PASS | ❌ FAIL | Các TC FAIL chính |
  |-------|--------|--------|-------------------|
  | Build 1 | 13 | 5 | TC-013,014,015 (validate input); TC-017 (dùng lại Answer); TC-018 (Clear) |
  | Build 2 | 17 | 1 | TC-018 (Clear không reset checkbox Integers only) |
  | Build 3 | 17 | 1 | TC-018 (Clear không reset checkbox Integers only) |
  | Build 4 | 17 | 1 | TC-002 (5/2 trả về 2 thay vì 2.5 – Integers only bị lock cứng) |
  | Build 5 | 16 | 2 | TC-017 (dùng lại Answer cũ); TC-018 (Clear bị vô hiệu hóa) |
  | Build 6 | 14 | 4 | TC-009,010 (divide by zero hiển thị Infinity/NaN); TC-017; TC-018 |
  | Build 7 | 5  | 13 | TC-001~003,005~008,011~013,015~017 (trả về 0 do dùng Answer cũ làm num1) |
  | Build 8 | 1  | 17 | Hầu hết FAIL do hoán vị num1/num2 (10/2 → 2/10=0.2) |

  **Phân tích bug theo từng Build:**
  - **Build 1:** Bỏ qua kiểm tra `isNaN` → nhập chữ không báo lỗi, trả về NaN; không reset checkbox sau Clear; dùng lại Answer cũ làm num1.
  - **Build 2 & 3:** Gần như hoàn chỉnh, chỉ còn lỗi Clear không reset `Integers only` checkbox về trạng thái mặc định.
  - **Build 4:** Khóa cứng `Integers only = true` → phép chia thập phân (5/2) bị làm tròn thành 2.
  - **Build 5:** Nút Clear bị `disabled = true` và lỗi dùng lại Answer cũ.
  - **Build 6:** Bỏ qua kiểm tra chia cho 0 → hiển thị `Infinity` (10/0) và `NaN` (0/0) thay vì báo lỗi.
  - **Build 7:** Dùng kết quả `answer` của phép tính trước làm `num1` → sau lần đầu answer=0, mọi phép tính đều cho kết quả 0.
  - **Build 8:** Hoán vị `num1` và `num2` → 10/2 bị tính thành 2/10=0.2; 0/9 bị tính thành 9/0 → Divide by zero error.

  **Sản phẩm tạo ra:** 8 file kết quả `div.md` tại `test/test_runs/build1/test_runs/div.md` đến `test/test_runs/build8/test_runs/div.md`.

---

### Lần tương tác 4: Cập nhật bộ Test Cases với Actual Result và Verdict từng Build

- **Tên công cụ AI:** Google Antigravity (LLM Model: Claude Sonnet 4.6 Thinking)
- **Ngày và giờ:** 2026-09-28 16:06:09 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  Cập nhật lại các test case trong thư mục test_cases thêm mục actual result
  chứa kết quả của từng build và verdict chứa trạng thái của từng build
  ```
- **Kết quả do AI tạo ra:**

  AI đọc toàn bộ 8 file `div.md` (từ build 1 đến build 8), trích xuất actual result và verdict cho từng test case theo từng build, sau đó cập nhật 18 file `TC-DIV-*.md` tại `test/test_cases/divide/` bằng cách bổ sung hai mục mới vào cuối mỗi file.

  **Cấu trúc bổ sung vào mỗi file test case:**

  | Build   | Actual Result               | Verdict |
  |---------|-----------------------------|---------|
  | Build 1 | (kết quả thực tế đo được)  | ✅ PASS / ❌ FAIL |
  | ...     | ...                         | ...     |
  | Build 8 | (kết quả thực tế đo được)  | ✅ PASS / ❌ FAIL |

  **Dữ liệu Actual Result nổi bật theo TC (8 build):**

  | TC ID | Build 1 | Build 2 | Build 4 | Build 6 | Build 7 | Build 8 |
  |-------|---------|---------|---------|---------|---------|---------|
  | TC-001 | PASS (5) | PASS (5) | PASS (5) | PASS (5) | FAIL (0) | FAIL (0.2) |
  | TC-002 | PASS (2.5) | PASS (2.5) | FAIL (2) | PASS (2.5) | FAIL (0) | FAIL (0.4) |
  | TC-004 | PASS (0) | PASS (0) | PASS (0) | PASS (0) | PASS (0) | FAIL (DivByZero err) |
  | TC-009 | PASS (lỗi DivByZero) | PASS | PASS | FAIL (Infinity) | PASS | FAIL (ans=0, no err) |
  | TC-013 | FAIL (NaN, không có lỗi) | PASS (Number 1 is not a number) | PASS | PASS | FAIL (ans=0) | FAIL (sai msg) |
  | TC-017 | FAIL (lần 2 = 10, dùng cũ) | PASS (50) | PASS (50) | FAIL (10) | FAIL (0) | FAIL (0.02) |
  | TC-018 | FAIL (checkbox không reset) | FAIL (checkbox không reset) | PASS | FAIL | PASS | FAIL |

  **Sản phẩm tạo ra:** 18 file test case được cập nhật tại `test/test_cases/divide/TC-DIV-001.md` đến `TC-DIV-018.md`, mỗi file bổ sung bảng **Actual Result** đầy đủ cho 8 build và cột **Verdict** tương ứng.

---

### Lần tương tác 5: Viết Test Summary Report cho Operation Divide

- **Tên công cụ AI:** Google Antigravity (LLM Model: Claude Sonnet 4.6 Thinking)
- **Ngày và giờ:** 2026-09-28 21:28:05 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  Hãy viết test summary cho phép chia dựa trên mẫu và cập nhật file ai-audit-report
  ```
- **Kết quả do AI tạo ra:**

  AI đọc 2 file mẫu hiện có trong dự án (`test_summary/addition/test_summary_addition.md` và `test_summary/multiplication/test_summary.md`), phân tích cấu trúc, sau đó tổng hợp toàn bộ dữ liệu từ 8 file `div.md` để soạn báo cáo test summary hoàn chỉnh cho phép chia.

  **File đã tạo:** `test/test_summary/division/test_summary_division.md`

  **Cấu trúc Test Summary (6 phần chính):**

  1. **Mục tiêu & Phạm vi kiểm thử:** Đánh giá chức năng Divide trên 8 build; xác định hiệu quả phát hiện lỗi; tập dữ liệu đầu vào gồm số nguyên, số âm, số thập phân, chia cho 0, ký tự không hợp lệ, giới hạn độ dài, trạng thái Clear.

  2. **Kế hoạch & Thiết kế Test Cases:** Bảng 18 test case (TC-DIV-001 đến TC-DIV-018) với đầy đủ Req ID, kỹ thuật thiết kế (EP, BVA, Error Guessing, State Transition), dữ liệu đầu vào và kỳ vọng.

  3. **Ma trận Kết quả Thực thi (Builds 1–8):**
     - Tổng số lượt chạy:  \times 8 = 144$ lượt.
     - Tổng lỗi phát hiện: **44 lỗi** (tỷ lệ thất bại trung bình **30.6%**).

     | Build | Pass | Fail | Tỷ lệ Pass | Tình trạng |
     |-------|:----:|:----:|:----------:|-----------|
     | Build 1 | 13 | 5 | 72.2% | ❌ FAILED (5 Bugs) |
     | Build 2 | 17 | 1 | 94.4% | ❌ FAILED (1 Bug) |
     | Build 3 | 17 | 1 | 94.4% | ❌ FAILED (1 Bug) |
     | Build 4 | 17 | 1 | 94.4% | ❌ FAILED (1 Bug) |
     | Build 5 | 16 | 2 | 88.9% | ❌ FAILED (2 Bugs) |
     | Build 6 | 14 | 4 | 77.8% | ❌ FAILED (4 Bugs – lỗi cốt lõi) |
     | Build 7 | 5  | 13 | 27.8% | ❌ FAILED (Critical – 13 Bugs) |
     | Build 8 | 1  | 17 | 5.6%  | ❌ FAILED (Critical – 17 Bugs) |

  4. **Phân tích chi tiết lỗi từng Build:** Mô tả hành vi lỗi, test case phát hiện và mức độ nghiêm trọng cho cả 8 build.

  5. **Đánh giá Bao phủ Yêu cầu:** Requirements Coverage 100% trên 8 Req ID (FR-DIV-01 đến FR-DIV-06, FR-VAL-01/02, FR-CLR-01).

  6. **Kết luận & Đề xuất:** REJECT Build 7 và Build 8 (Critical); Critical Fix cho Build 6 (Division by zero); Fix Requests cho Build 1, 4, 5; duy trì bộ test trong Regression Suite.

---
