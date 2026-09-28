# AI AUDIT REPORT

- **Mã số sinh viên:** 23120367
- **Học phần:** Kiểm thử Phần mềm (Software Testing)
- **Ứng dụng kiểm thử:** Basic Calculator (`https://testsheepnz.github.io/BasicCalculator`)
- **Thời gian thực hiện:** 28/09/2026

---

## 1. Tuyên bố Sử dụng AI (AI Usage Declaration)

> **"Tôi sử dụng các công cụ AI cho những tác vụ sau,"**
>
> 1. **Phân tích yêu cầu và hệ thống:** Khảo sát cấu trúc trang web Basic Calculator, các phiên bản build (từ Prototype 0 đến Build 9), các phần tử giao diện (inputs, operations, checkbox integers only, calculate button, answer area) và các bug tiềm ẩn được gài vào từng bản build.
> 2. **Thiết kế và chuẩn hóa Test Cases:** Tạo lập và định dạng các ca kiểm thử theo đúng template chuẩn của môn học, phân loại theo từng module tính năng (`addition`, `subtraction`, `multiplication`, `division`, `concatenation`, `validation`, `integers_only`, `clear`, `build_selection`, `ui_ux`).
> 3. **Tối ưu hóa và mở rộng bộ kiểm thử Phép cộng (Addition):** Thiết kế bổ sung các ca kiểm thử biên (Boundary Value Analysis), phân vùng tương đương (Equivalence Partitioning) và các trường hợp đặc biệt nhằm tối đa hóa khả năng phát hiện lỗi (Defect Detection Rate) trên các bản build từ Build 1 đến Build 8.
> 4. **Lập trình kịch bản kiểm thử tự động (Automation Test Scripts):** Viết mã nguồn Python cho từng bản build (`build1` đến `build8`) để thực thi tự động toàn bộ 20 test cases của phép cộng, so sánh kết quả thực tế với kết quả kỳ vọng và ghi nhận lỗi.
> 5. **Sinh và chuẩn hóa Báo cáo Thực thi Kiểm thử (Test Run Reports):** Tự động xuất và định dạng các file báo cáo thực thi `add.md` theo chuẩn 5 phần trong từng thư mục build tương ứng, xử lý và sửa lỗi định dạng bảng Markdown.
> 6. **Tổng hợp Báo cáo Kiểm thử Tổng thể (Test Summary Report):** Xây dựng báo cáo tổng kết theo chuẩn IEEE 829 / ISTQB, ma trận truy vết yêu cầu (Traceability Matrix) và đánh giá độ phủ kiểm thử cho chức năng Phép cộng.
> 7. **Lập báo cáo minh bạch việc sử dụng Trí tuệ Nhân tạo (AI Audit Report):** Ghi chép chi tiết, trung thực và đầy đủ các mốc tương tác, câu lệnh và sản phẩm sinh ra bởi AI.

---

## 2. Nhật Ký Chi Tiết Các Lần Tương Tác Với AI (AI Interaction Logs)

### Lần tương tác 1

- **Tên công cụ AI:** Google Antigravity (LLM Model: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 14:20:33 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  Link web test: https://testsheepnz.github.io/BasicCalculator
  Phân tích web trên và phát sinh các test case tương ứng và tuân thủ theo template như ảnh. Test cases phải chia theo module, mỗi module là 1 folder là lưu trong test/test_cases
  ```
  *(Kèm theo 3 ảnh đính kèm mô tả template mẫu test case của môn học)*
- **Kết quả do AI tạo ra:**
  - Khảo sát và phân tích toàn diện trang web Basic Calculator: xác định các trường dữ liệu (`number1Field`, `number2Field`), danh sách phép toán (`selectOperationDropdown`), danh sách phiên bản (`selectBuild`), checkbox `integerSelect`, nút `calculateButton`, `clearButton` và trường hiển thị `numberAnswerField`.
  - Thiết lập cấu trúc thư mục lưu trữ test case tại `test/test_cases/` chia thành 10 module chức năng.
  - Sinh 56 test cases chuẩn tuân thủ chính xác template hình ảnh cung cấp (chứa đầy đủ: Test Case ID, Title, Description, Preconditions, Test Steps, Expected Result, Status, Severity, Priority, Module).
  - Khởi tạo file ma trận truy vết `test/test_summary/traceability-matrix.md` và các mẫu báo cáo lỗi GitHub Issue templates trong thư mục `.github/ISSUE_TEMPLATE/`.

---

### Lần tương tác 2

- **Tên công cụ AI:** Google Antigravity (LLM Model: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 14:33:19 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  tạo thêm test case cho chức năng addition
  ```
- **Kết quả do AI tạo ra:**
  - Mở rộng phạm vi kiểm thử module Phép cộng (`addition`) từ 6 ca ban đầu lên 16 ca kiểm thử độc lập (`TC-ADD-001` đến `TC-ADD-016`).
  - Bổ sung nhiều trường hợp kiểm thử biên và giá trị đặc thù:
    - `TC-ADD-007`: Cộng hai số bằng 0 (`0 + 0 = 0`).
    - `TC-ADD-008`: Số có dấu `+` tường minh phía trước (`+12 + +34 = 46`).
    - `TC-ADD-009`: Số có các số 0 ở đầu (leading zeros) (`007 + 008 = 15`).
    - `TC-ADD-010`: Cộng hai số thực âm (`-3.25 + -4.75 = -8`).
    - `TC-ADD-011`: Hai số thực đối xứng triệt tiêu (`12.345 + -12.345 = 0`).
    - `TC-ADD-012`: Xử lý khoảng trắng thừa hai đầu (`  25   +   75   = 100`).
    - `TC-ADD-013`: Số nguyên 9 chữ số gần giới hạn (`999999999 + 1 = 1000000000`).
    - `TC-ADD-014`: Hai số cực lớn đối nhau triệt tiêu (`999999999 + -999999999 = 0`).
    - `TC-ADD-015`: Kiểm thử kết hợp số thập phân và checkbox *Integers only*.
    - `TC-ADD-016`: Đầu vào dạng ký hiệu khoa học (`1e3 + 200 = 1200`).

---

### Lần tương tác 3

- **Tên công cụ AI:** Google Antigravity (LLM Model: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 15:15:20 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  dựa trên tất cả các testcase trong test/test_cases/addition, vs mỗi build trong test/test_runs hãy sinh test script cho tất cả các test case của addition chạy trên build đó và tổng hợp kết quả thực thi theo format chuẩn trong file add.md trong thư mục test_runs của build tương ứng
  ```
- **Kết quả do AI tạo ra:**
  - Cấu trúc lại toàn bộ kịch bản kiểm thử theo đúng sơ đồ thư mục của dự án:
    - Tạo 8 file script riêng biệt: `test/test_runs/build[1-8]/test_scripts/add.py`.
    - Tự động thực thi từng kịch bản và xuất kết quả ra 8 file báo cáo tương ứng: `test/test_runs/build[1-8]/test_runs/add.md`.
  - Định dạng chuẩn 5 phần cho từng file `add.md`:
    1. Thông tin chung (Test Run Information: Build version, Module, Date, Tester).
    2. Tóm tắt kết quả (Summary Metrics: Total, Passed, Failed, Pass Rate).
    3. Chi tiết kết quả thực thi (Detailed Results: bảng chi tiết từng test case kèm thời gian thực thi).
    4. Bảng ghi nhận lỗi (Defects Log: Defect ID, Title, Severity, Expected vs Actual).
    5. Đánh giá & Khuyến nghị (Observations & Recommendations).

---

### Lần tương tác 4

- **Tên công cụ AI:** Google Antigravity (LLM Model: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 15:42:52 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  thêm/chỉnh sửa các test case để mỗi bản build đều phát hiện lỗi nhiều nhất có thể
  ```
- **Kết quả do AI tạo ra:**
  - Tối ưu hóa sâu sắc bộ test case Addition nhằm tối đa hóa tỷ lệ phát hiện khiếm khuyết (Defect Detection Rate) trên cả 8 bản build:
    - Điều chỉnh các test case số thực (`TC-ADD-005`: `5.5 + 4.3 = 9.8`, `TC-ADD-010`: `-3.2 + -4.7 = -7.9`, `TC-ADD-015`: `15.8 + 4.3 = 20.1`) sang `Integers only = Unchecked` để phát hiện lỗi làm tròn/ép kiểu nguyên vô cớ của **Build 4**.
    - Thêm `TC-ADD-017`: `0 + 50 = 50` để bắt triệt để lỗi nối chuỗi `"0" + "50" = "050"` của **Build 1**.
    - Thêm `TC-ADD-018`: `-10 + 20 = 10` để bắt lỗi của **Build 1** (`"-1020"`) và **Build 8**.
    - Thêm `TC-ADD-019`: `7 + 8 = 15` để bắt lỗi cộng bù 1 (`16`) của **Build 5**.
    - Thêm `TC-ADD-020`: `11 + 13 = 24` để phát hiện lỗi tính sai của **Build 6**.
    - Thêm `TC-ADD-021`: Phép cộng kiểm tra lỗi của **Build 3**.
    - Thêm `TC-ADD-022`: Phép cộng số thực 2 chữ số thập phân `10.25 + 5.5 = 15.75`.
  - Cập nhật đồng bộ các file `add.py` và tái thực thi kiểm thử trên toàn bộ 8 build, phát hiện tổng cộng 48 defects.

---

### Lần tương tác 5

- **Tên công cụ AI:** Google Antigravity (LLM Model: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 15:56:15 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  bỏ test case 20, 21 va cập nhật test case 22 thành test case 20
  ```
- **Kết quả do AI tạo ra:**
  - Xóa bỏ 2 file `TC-ADD-020.md` và `TC-ADD-021.md`.
  - Đổi tên và cập nhật nội dung file `TC-ADD-022.md` thành `TC-ADD-020.md` (Phép cộng hai số thực có 2 chữ số thập phân: `10.25 + 5.5 = 15.75`).
  - Chuẩn hóa bộ test case Addition thành đúng 20 ca kiểm thử hoàn chỉnh (`TC-ADD-001` đến `TC-ADD-020`).
  - Cập nhật lại logic trong 8 script `test/test_runs/build[1-8]/test_scripts/add.py` và chạy lại để làm mới dữ liệu cho 8 file `test/test_runs/build[1-8]/test_runs/add.md`.

---

### Lần tương tác 6

- **Tên công cụ AI:** Google Antigravity (LLM Model: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 16:03:07 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  fix lỗi định dạng của add.md trong test_runs
  ```
  *(Kèm ảnh chụp màn hình hiển thị bảng mục "4. Ghi nhận lỗi (Defects Log)" bị vỡ cấu trúc cột)*
- **Kết quả do AI tạo ra:**
  - Xác định chính xác nguyên nhân lỗi hiển thị Markdown: dòng kẻ phân cách tiêu đề (`|:---|...|`) chứa 8 cột phân cách trong khi dòng tiêu đề bảng chỉ có 7 cột (`Defect ID`, `Test Case ID`, `Title`, `Severity`, `Expected Result`, `Actual Result`, `Bug Category`).
  - Chỉnh sửa dòng phân cách về đúng 7 cột chuẩn trên toàn bộ 8 file `test/test_runs/build[1-8]/test_runs/add.md`.
  - Cập nhật mã nguồn Python trong 8 file `add.py` để đảm bảo các lần sinh báo cáo tự động tiếp theo không bao giờ gặp lại lỗi định dạng này.
  - Chạy script kiểm tra định dạng Markdown tự động xác nhận 100% bảng hiển thị chuẩn xác.

---

### Lần tương tác 7

- **Tên công cụ AI:** Google Antigravity (LLM Model: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 16:06:16 (GMT+7)
- **Câu lệnh (prompt) của bạn:**
  ```text
  viết báo cáo .md tổng hợp cho addition trong test/test_summary/addition
  ```
- **Kết quả do AI tạo ra:**
  - Soạn thảo Báo cáo Tổng hợp Kiểm thử (Test Summary Report) toàn diện theo chuẩn IEEE 829 / ISTQB tại đường dẫn `test/test_summary/addition/test_summary_addition.md`.
  - Báo cáo gồm 6 phần chuyên sâu:
    1. Tổng quan & Phạm vi thực thi (Executive Summary & Scope).
    2. Danh mục chi tiết 20 ca kiểm thử chức năng Phép cộng.
    3. Ma trận kết quả thực thi tổng thể trên 8 bản build (160 lượt chạy: 115 Passed, 45 Failed).
    4. Phân tích khiếm khuyết chi tiết theo từng bản build (từ Build 1 đến Build 8).
    5. Đánh giá độ phủ kiểm thử (Test Coverage đạt 100%) và hiệu quả phát hiện lỗi.
    6. Kết luận & Khuyến nghị nghiệm thu (Chỉ định duy nhất Build 7 đạt chất lượng release với tỷ lệ Pass 100%).
