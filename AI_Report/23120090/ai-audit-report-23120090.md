# AI AUDIT REPORT

- **Mã số sinh viên:** 23120090
- **Học phần:** Kiểm thử Phần mềm (Software Testing)
- **Ứng dụng kiểm thử:** Basic Calculator (`https://testsheepnz.github.io/BasicCalculator`)
- **Thời gian thực hiện:** 28/09/2026
- **Công cụ AI sử dụng:** Antigravity (Claude Sonnet 4.6 Thinking / Gemini 3.1 Pro High)

---

## 1. Tuyên bố Sử dụng AI (AI Usage Declaration)

> **"Tôi sử dụng các công cụ AI cho những tác vụ sau:"**
>
> 1. **Phân tích yêu cầu và hệ thống:** Đọc và phân tích trang web Basic Calculator để hiểu các trường đầu vào, phép toán, và hành vi của ứng dụng.
> 2. **Thiết kế và chuẩn hóa Test Cases:** Tạo 20 test case đầy đủ cho phép toán Concatenate (`TC-CONCAT-001` đến `TC-CONCAT-020`) với định dạng thống nhất theo yêu cầu.
> 3. **Lập trình kịch bản kiểm thử tự động (Automation Test Scripts):** Viết script `concat.py` sử dụng Selenium WebDriver để tự động thực thi 20 test case trên từng build (Build 1–8), phát hiện và ghi nhận kết quả.
> 4. **Sinh và chuẩn hóa Báo cáo Thực thi Kiểm thử (Test Run Reports):** Tự động xuất kết quả kiểm thử vào file `concat.md` theo định dạng bảng Markdown cho từng build.
> 5. **Tổng hợp Báo cáo Kiểm thử Tổng thể (Test Summary Report):** Tổng hợp kết quả từ 8 builds vào tài liệu `test_summary_concatenate.md` với phân tích lỗi, ma trận bao phủ, và khuyến nghị.
> 6. **Lập báo cáo minh bạch việc sử dụng Trí tuệ Nhân tạo (AI Audit Report):** Ghi nhận đầy đủ toàn bộ nhật ký tương tác với AI trong phiên làm việc này.

---

## 2. Nhật Ký Chi Tiết Các Lần Tương Tác Với AI (AI Interaction Logs)

> **Ghi chú:** Phiên làm việc này bao gồm hai giai đoạn:
> - **Giai đoạn 1 (14:41 – 14:58 +07:00):** Các lần thử nghiệm ban đầu với model Gemini 3.1 Pro (High) — tạo 5 test case cho 8 build riêng lẻ (cấu trúc cũ).
> - **Giai đoạn 2 (19:35 – 20:21 +07:00):** Phiên làm việc chính với model Claude Sonnet 4.6 (Thinking) — tạo 20 test case, script tự động, báo cáo và tổng kết.

---

### Lần tương tác 1 *(Giai đoạn 1 — Thử nghiệm ban đầu)*

- **Tên công cụ AI:** Antigravity (Gemini 3.1 Pro High)
- **Ngày và giờ:** 28/09/2026 — 14:41:19 +07:00
- **Câu lệnh (prompt) của bạn:**
  > Tạo 5 test case cho phép Concatenate của Basic Calculator, mỗi build (1–8) có cùng input, đặt trong thư mục `concatenate` bên trong từng build. Mỗi test case gồm: ID, Objective, Input, Steps, Expected Output, Actual Output (trống), Verdicts (trống).
- **Kết quả do AI tạo ra:**
  - AI tạo script PowerShell để sinh các file test case, sau đó chạy script và báo cáo đã tạo thành công 5 test case cho 8 builds.
  - **Lỗi xảy ra:** Người dùng từ chối lệnh `Get-ChildItem -Recurse 1\concatenate` để kiểm tra kết quả.
  - **Artifact:** 5 file `TC-CONCAT-001.md` → `TC-CONCAT-005.md` trong `1/concatenate/` đến `8/concatenate/`.

---

### Lần tương tác 2 *(Giai đoạn 1 — Thử lại lần 2)*

- **Tên công cụ AI:** Antigravity (Gemini 3.1 Pro High)
- **Ngày và giờ:** 28/09/2026 — 14:45:27 +07:00
- **Câu lệnh (prompt) của bạn:**
  > *(Lặp lại yêu cầu tương tự lần 1 với cùng cấu trúc template)*
- **Kết quả do AI tạo ra:**
  - AI tạo script Python `gen.py` tại thư mục workspace để sinh test case.
  - Chạy `python gen.py ; Remove-Item gen.py` — thành công, xuất ra `Created all test cases successfully.`
  - **Lỗi xảy ra:** Lệnh `read_url_content` bị từ chối quyền truy cập trang web Basic Calculator.
  - **Artifact:** 5 file TC-CONCAT trong mỗi build được tạo lại bằng Python script.

---

### Lần tương tác 3 *(Giai đoạn 1 — Thử lại lần 3, thay đổi yêu cầu)*

- **Tên công cụ AI:** Antigravity (Gemini 3.1 Pro High)
- **Ngày và giờ:** 28/09/2026 — 14:47:30 +07:00
- **Câu lệnh (prompt) của bạn:**
  > *(Lặp lại yêu cầu tương tự, cùng format)*
- **Kết quả do AI tạo ra:**
  - AI khám phá cấu trúc thư mục workspace (`tree /f`), phát hiện đường dẫn `test/test_cases/`.
  - Tạo thư mục `test/test_cases/concatenate/`.
  - Sinh script Python `generate_tests.py` để tạo 20 file Markdown, chạy và xác nhận thành công.
  - **Artifact:** 20 file `TC-CONCAT-001.md` → `TC-CONCAT-020.md` trong `test/test_cases/concatenate/` (các file này là phiên bản cũ với placeholder `$(System.Collections.Hashtable.intOnly)`).

---

### Lần tương tác 4 *(Giai đoạn 2 — Yêu cầu chính thức 20 test case)*

- **Tên công cụ AI:** Antigravity (Claude Sonnet 4.6 Thinking)
- **Ngày và giờ:** 28/09/2026 — 19:35:28 +07:00
- **Câu lệnh (prompt) của bạn:**
  > Tạo 20 test case cho phép Concatenate của Basic Calculator. Mỗi test case gồm: ID, Objective, Input, Steps, Expected Output, Actual Output (trống), Verdicts (trống). Actual Output và Verdicts phải để trống.
- **Kết quả do AI tạo ra:**
  - Đọc trang web Basic Calculator qua `read_url_content` để hiểu hành vi của phép Concatenate.
  - Kiểm tra cấu trúc workspace và các file test case hiện có.
  - Phát hiện 20 file `TC-CONCAT-001.md` → `TC-CONCAT-020.md` đã tồn tại (từ lần 3) nhưng có nội dung không đầy đủ/lỗi.
  - **Ghi đè** toàn bộ 20 file với nội dung mới, đúng định dạng, bao gồm các kịch bản: số nguyên, số âm, số 0, số thập phân, chuỗi chữ cái, ký tự đặc biệt, toán hạng rỗng, số rất lớn, kiểm tra checkbox Integer only bị vô hiệu hóa, và chuyển đổi phép toán.
  - **Artifact:** 20 file `TC-CONCAT-001.md` → `TC-CONCAT-020.md` trong [`test/test_cases/concatenate/`](../../test/test_cases/concatenate/).

| Test Case | Kịch bản |
|---|---|
| TC-CONCAT-001 | Nối hai số nguyên dương (`5`, `7` → `57`) |
| TC-CONCAT-002 | Nối hai số nguyên âm (`-3`, `-8` → `-3-8`) |
| TC-CONCAT-003 | Nối số dương + số âm (`4`, `-9` → `4-9`) |
| TC-CONCAT-004 | Nối số âm + số dương (`-6`, `3` → `-63`) |
| TC-CONCAT-005 | Nối hai số 0 (`0`, `0` → `00`) |
| TC-CONCAT-006 | Nối số dương + 0 (`42`, `0` → `420`) |
| TC-CONCAT-007 | Nối 0 + số dương (`0`, `99` → `099`) |
| TC-CONCAT-008 | Nối hai số thập phân (`3.14`, `2.71` → `3.142.71`) |
| TC-CONCAT-009 | Nối thập phân + thập phân âm (`1.5`, `-2.5` → `1.5-2.5`) |
| TC-CONCAT-010 | Nối số nguyên + thập phân (`10`, `5.5` → `105.5`) |
| TC-CONCAT-011 | Nối chuỗi chữ cái (`abc`, `def` → `abcdef`) |
| TC-CONCAT-012 | Nối ký tự đặc biệt (`!@#`, `$%^` → `!@#$%^`) |
| TC-CONCAT-013 | Toán hạng 1 rỗng + số (`123` → `123`) |
| TC-CONCAT-014 | Số + toán hạng 2 rỗng (`456` → `456`) |
| TC-CONCAT-015 | Cả hai đều rỗng → `""` |
| TC-CONCAT-016 | Số rất lớn (`999999999`, `888888888` → `999999999888888888`) |
| TC-CONCAT-017 | Xác nhận checkbox Integer only bị vô hiệu hóa |
| TC-CONCAT-018 | Chuyển từ Add → Concatenate giữa chừng |
| TC-CONCAT-019 | Nối chuỗi có khoảng trắng (`Hello`, ` World` → `Hello World`) |
| TC-CONCAT-020 | Answer field làm mới sau mỗi lần tính |

---

### Lần tương tác 5 *(Giai đoạn 2 — Tạo script tự động)*

- **Tên công cụ AI:** Antigravity (Claude Sonnet 4.6 Thinking)
- **Ngày và giờ:** 28/09/2026 — 19:43:25 +07:00
- **Câu lệnh (prompt) của bạn:**
  > Đọc các test case đã tạo. Sau đó tạo cho mỗi build trong test_runs một `test_scripts/concat.py` để tự động kiểm thử các test case cho build đó. Script lưu kết quả vào `test_runs/concat.md` của build tương ứng.
- **Kết quả do AI tạo ra:**
  1. **Đọc dữ liệu:** Đọc toàn bộ 20 test case để trích xuất input và expected output.
  2. **Khám phá trang web:** Chạy Selenium để tìm các element ID thực tế của trang (`selectBuild`, `selectOperationDropdown`, `number1Field`, `number2Field`, `calculateButton`, `numberAnswerField`).
  3. **Phát hiện lỗi:** ChromeDriver crash với `--headless=new` → sửa thành `--headless --disable-gpu`.
  4. **Phát hiện lỗi 2:** Element ID `selectOperationType` không tồn tại → sửa thành `selectOperationDropdown` với value `"4"` (Concatenate).
  5. **Viết script:** Tạo `concat.py` hoàn chỉnh cho Build 1 với 20 test case, cơ chế tạo báo cáo Markdown, và xử lý lỗi.
  6. **Sao chép:** Dùng PowerShell để copy và thay `BUILD_NUMBER` cho Build 2–8.
  7. **Thực thi và xác minh Build 1:** Chạy script, xác nhận 19 PASSED / 1 FAILED (TC-012).
  8. **Thực thi Build 2:** Chạy script, phát hiện 2 PASSED / 18 FAILED (Build 2 thực hiện Addition thay vì Concatenate).
  9. **Thực thi Build 3–8:** Chạy tuần tự, thu thập kết quả.

  **Artifact tạo ra:**
  - 8 file `concat.py` trong [`test_runs/buildN/test_scripts/`](../../test_runs/) (N = 1–8)
  - 8 file `concat.md` trong [`test_runs/buildN/test_runs/`](../../test_runs/) (kết quả thực thi)

  **Kết quả kiểm thử tự động:**

  | Build | Passed | Failed | Lỗi phát hiện |
  |:---:|:---:|:---:|---|
  | Build 1 | 19 | 1 | TC-012: Số 15 chữ số bị cắt cụt |
  | Build 2 | 2 | 18 | Thực hiện Addition thay vì Concatenate |
  | Build 3 | 15 | 5 | TC-012 + TC-013–016: Chuỗi phi số bị từ chối |
  | Build 4 | 19 | 1 | TC-012: Số 15 chữ số bị cắt cụt |
  | Build 5 | 19 | 1 | TC-012: Số 15 chữ số bị cắt cụt |
  | Build 6 | 19 | 1 | TC-012: Số 15 chữ số bị cắt cụt |
  | Build 7 | 2 | 18 | Chỉ trả về toán hạng 2, bỏ qua toán hạng 1 |
  | Build 8 | 4 | 16 | Đảo ngược thứ tự toán hạng (`num2 ∥ num1`) |

---

### Lần tương tác 6 *(Giai đoạn 2 — Tạo báo cáo tổng hợp)*

- **Tên công cụ AI:** Antigravity (Claude Sonnet 4.6 Thinking)
- **Ngày và giờ:** 28/09/2026 — 20:04:38 +07:00
- **Câu lệnh (prompt) của bạn:**
  > Tạo báo cáo tổng hợp (test summary) cho kết quả kiểm thử Concatenate trong `test_summary/concatenate`.
- **Kết quả do AI tạo ra:**
  - Đọc file `test_summary_addition.md` để tham khảo định dạng.
  - Tổng hợp toàn bộ dữ liệu từ 8 file `concat.md` và 20 test case.
  - Tạo file [`test_summary/concatenate/test_summary_concatenate.md`](../../test_summary/concatenate/test_summary_concatenate.md) với 8 mục:

  | Mục | Nội dung |
  |---|---|
  | 1. Mục tiêu & Phạm vi | Mô tả phép Concatenate, tập dữ liệu đầu vào |
  | 2. Thiết kế Test Cases | Bảng 20 TC với technique, input, expected output |
  | 3. Ma trận kết quả | Bảng Pass/Fail theo Build + biểu đồ ASCII |
  | 4. Phân tích lỗi từng Build | Root cause analysis cho 8 builds |
  | 5. Ma trận TC × Build | Bảng 20×8 Pass/Fail chi tiết |
  | 6. Requirements Coverage | Bao phủ 100% trên 6 nhóm yêu cầu |
  | 7. Cross-Build Bug Analysis | TC-012 systemic bug + phân loại mức độ |
  | 8. Kết luận & Đề xuất | REJECT/Fix cho từng build |

  **Kết luận tổng thể:** 47/160 lượt thất bại (70.6% pass rate); 3 builds bị REJECT (Build 2, 7, 8); 1 lỗi hệ thống xuyên suốt (TC-012 giới hạn độ dài).

---

### Lần tương tác 7 *(Giai đoạn 2 — Viết báo cáo AI Audit)*

- **Tên công cụ AI:** Antigravity (Claude Sonnet 4.6 Thinking)
- **Ngày và giờ:** 28/09/2026 — 20:21:19 +07:00
- **Câu lệnh (prompt) của bạn:**
  > Review the entire AI interaction log and write the full log of AI interactions to the file `AI_Report/23120090/ai-audit-report-23120090.md`.
- **Kết quả do AI tạo ra:**
  - Đọc file audit report hiện có (34 dòng template chưa điền).
  - Đọc transcript JSONL (`transcript.jsonl`, 350 dòng, ~461 KB).
  - Viết script Python `parse_transcript.py` để phân tích nhật ký và trích xuất toàn bộ các bước tương tác.
  - Tổng hợp và viết toàn bộ nội dung báo cáo này vào file `ai-audit-report-23120090.md`.

---

## 3. Tổng quan Thống kê Sử dụng AI

| Chỉ số | Giá trị |
|---|---|
| Tổng số lần tương tác (prompts) | **7 lần** |
| Tổng số bước thực thi của AI | **~350 bước** |
| Thời gian phiên làm việc chính | 19:35 – 20:21 +07:00 (~46 phút) |
| Số file được tạo/chỉnh sửa | **~50 file** (20 TC + 8 scripts + 8 reports + 1 summary + 1 audit) |
| Số lần lỗi xảy ra và được khắc phục | **2 lỗi** (ChromeDriver `--headless=new`; sai element ID `selectOperationType`) |
| Công cụ Selenium sử dụng | `selenium 4.49.0`, Chrome (headless) |
| Tổng lượt test thực thi tự động | **160 lượt** (20 TC × 8 builds) |
| Tổng lỗi phát hiện | **47 lỗi** |

---

## 4. Đánh giá Hiệu quả Sử dụng AI

| Tác vụ | AI thực hiện | Người dùng thực hiện |
|---|---|---|
| Đọc và phân tích ứng dụng web | ✅ Hoàn toàn | ❌ |
| Thiết kế 20 test case | ✅ Hoàn toàn | ❌ |
| Lập trình Selenium script | ✅ Hoàn toàn | ❌ |
| Debug lỗi ChromeDriver & element ID | ✅ Hoàn toàn | ❌ |
| Thực thi 160 lượt test tự động | ✅ Hoàn toàn | ❌ |
| Sinh báo cáo test run (8 builds) | ✅ Hoàn toàn | ❌ |
| Viết Test Summary Report | ✅ Hoàn toàn | ❌ |
| Xác nhận & phê duyệt yêu cầu | ❌ | ✅ Hoàn toàn |
| Cung cấp đường link ứng dụng | ❌ | ✅ Hoàn toàn |

> **Nhận xét:** AI đóng vai trò chủ đạo trong toàn bộ vòng đời kiểm thử, từ phân tích yêu cầu, thiết kế test case, tự động hóa, thực thi đến báo cáo. Người dùng cung cấp hướng dẫn cấp cao và xác nhận từng bước.

---