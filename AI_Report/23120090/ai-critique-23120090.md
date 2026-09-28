# ĐÁNH GIÁ VÀ NHẬN XÉT VỀ CÔNG CỤ AI (AI CRITIQUE)

- **MSSV:** 23120090
- **Học phần:** Kiểm thử Phần mềm (Software Testing)
- **Bài tập:** Kiểm thử ứng dụng Basic Calculator (`https://testsheepnz.github.io/BasicCalculator`)
- **Module kiểm thử:** Concatenate (Phép nối chuỗi)

---

## Điểm mạnh của AI trong quá trình thực hiện

AI thể hiện hiệu quả cao ở các tác vụ có cấu trúc rõ ràng và lặp lại. Cụ thể, khi được cung cấp link ứng dụng và yêu cầu thiết kế 20 test case, AI đã phân tích đúng đặc thù của phép Concatenate (xử lý đầu vào như chuỗi ký tự, không validate số, checkbox *Integer only* bị vô hiệu hóa) và tự động phủ đủ các lớp tương đương cần thiết: số nguyên, số âm, số thập phân, chuỗi chữ cái, ký tự đặc biệt, đầu vào rỗng, và số rất lớn. Ở giai đoạn viết script tự động, AI chủ động phát hiện và sửa hai lỗi kỹ thuật phát sinh trong môi trường thực tế — ChromeDriver crash với cờ `--headless=new` và sai tên phần tử HTML (`selectOperationType` không tồn tại, thay bằng `selectOperationDropdown` với giá trị `"4"`) — mà không cần sự can thiệp từ người dùng. Kết quả là 160 lượt kiểm thử (20 test case × 8 build) được thực thi hoàn toàn tự động và sinh ra 8 báo cáo `concat.md` cùng một báo cáo tổng hợp theo đúng định dạng yêu cầu.

## Điểm hạn chế cần nhìn nhận

Dù kết quả đầu ra hoàn chỉnh về mặt kỹ thuật, quá trình thực hiện bộc lộ một số điểm hạn chế đáng chú ý.

**Thứ nhất, AI thiếu bộ nhớ ngữ cảnh xuyên suốt phiên.** Do giới hạn cửa sổ ngữ cảnh, nội dung của phiên làm việc trước bị tóm tắt lại và có những chi tiết bị mất hoặc sai. Cụ thể, dữ liệu kỳ vọng của TC-CONCAT-011 đến TC-CONCAT-020 trong bản tóm tắt ban đầu không khớp hoàn toàn với nội dung thực tế trong file, khiến AI phải đọc lại từng file để xác nhận input thực tế trước khi viết script. Điều này dẫn đến thời gian thực thi kéo dài hơn cần thiết.

**Thứ hai, AI ưu tiên "luồng thuận" (happy path) khi không được chỉ định rõ ràng.** Trong 20 test case được thiết kế, phần lớn là các kịch bản đầu vào hợp lệ và kết quả dự đoán được. Các kịch bản kiểm thử trạng thái GUI — ví dụ như xác minh trực tiếp rằng checkbox *Integer only* thực sự bị `disabled` (không chỉ là không ảnh hưởng kết quả), hay kiểm tra thông báo lỗi cụ thể khi xảy ra lỗi — chưa được đưa vào bộ test case. Hệ quả là TC-CONCAT-012 (số 15 chữ số) thất bại trên tất cả 8 build, nhưng script không phân biệt được đây là lỗi ở tầng HTML (`maxlength`), tầng JavaScript, hay tầng logic xử lý; nó chỉ ghi nhận kết quả sai mà không đặt câu hỏi nguyên nhân.

**Thứ ba, AI không chủ động kiểm tra ranh giới thực tế của hệ thống.** Giới hạn `maxlength=10` của các ô nhập liệu trên trang HTML đã được nhìn thấy từ đầu trong quá trình khám phá DOM, nhưng AI không tự suy luận ra rằng test case với chuỗi 15 ký tự (`TC-CONCAT-012`) sẽ chắc chắn thất bại trên *mọi* build — không phải do lỗi build mà do giới hạn thiết kế của trang. Một kiểm thử viên có kinh nghiệm sẽ phân biệt rõ "lỗi của phần mềm đang kiểm thử" với "giới hạn của môi trường kiểm thử", trong khi AI xử lý cả hai như nhau trong báo cáo.

## Bài học rút ra về cộng tác với AI

Kinh nghiệm thực tế từ bài tập này cho thấy AI hiệu quả như một **công cụ hỗ trợ**, không phải **Kiểm thử viên**. AI xuất sắc trong việc dịch yêu cầu thành code, sinh báo cáo theo template, và xử lý khối lượng công việc lặp lại lớn. Tuy nhiên, ba trách nhiệm vẫn phải thuộc về con người:

1. **Định nghĩa ranh giới kiểm thử:** Người dùng cần chỉ định rõ không chỉ "kiểm tra gì" mà còn "không kiểm tra gì".
2. **Kiểm soát chất lượng đầu ra:** Không nên chấp nhận PASS/FAIL từ script tự động mà không đối chiếu với kỳ vọng thực tế. Build 2 bị phát hiện thực hiện Addition thay vì Concatenate — đây là bug nghiêm trọng, nhưng chỉ trở nên có ý nghĩa khi người dùng hiểu tại sao 18/20 test case thất bại.
3. **Kiểm tra lại context khi làm việc xuyên phiên:** Người dùng cần chủ động cung cấp lại thông tin cần thiết thay vì giả định AI "nhớ" mọi thứ. Việc phụ thuộc vào bản tóm tắt tự động của AI có thể dẫn đến sai sót nhỏ tích lũy thành vấn đề lớn.
