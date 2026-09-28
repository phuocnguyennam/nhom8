# ĐÁNH GIÁ VÀ NHẬN XÉT VỀ CÔNG CỤ AI (AI CRITIQUE)

- **MSSV:** 23120184
- **Học phần:** Kiểm thử Phần mềm (Software Testing)
- **Bài tập:** Kiểm thử ứng dụng Basic Calculator (`https://testsheepnz.github.io/BasicCalculator.html`)

---

AI hỗ trợ tốt trong việc khởi đầu và tổ chức công việc. Gemini giúp đề xuất test case, giải thích một số lỗi Git và phác thảo hướng tự động hóa bằng Python/Selenium. Sau khi người dùng làm rõ phạm vi chỉ tập trung vào phép trừ, nội dung được thu hẹp thành bộ test case Subtract. Copilot tiếp tục hỗ trợ chạy script trên nhiều build và tổng hợp kết quả thành báo cáo. Nhờ đó, kết quả của 8 build được trình bày thống nhất: 64 lượt chạy, gồm 48 PASS và 16 FAIL.

Tuy nhiên, chất lượng đầu ra phụ thuộc đáng kể vào độ rõ của yêu cầu. Prompt ban đầu nhắc đến toàn bộ chức năng và Prototype/Build 7, trong khi phạm vi bài tập sau đó được xác định là phép trừ trên nhiều build. Người dùng phải chủ động sửa lại hướng làm. Đây là lời nhắc rằng AI có thể làm đúng theo cách hiểu ban đầu nhưng vẫn lệch mục tiêu thực tế nếu phạm vi và tiêu chí chưa được nêu rõ.

Một khoảng cách quan trọng nằm giữa thiết kế và thực thi kiểm thử. Audit ghi nhận bộ thiết kế có 13 test case Subtract, nhưng thư mục testcase hiện chỉ có 8 file và mỗi build chạy 8 ca, tạo thành 64 lượt chạy. Vì vậy, 5 ca còn lại chưa được xác nhận tự động; đặc biệt các tình huống nhập trống, ký tự không hợp lệ và khoảng trắng chưa nằm trong phạm vi kết quả 48 PASS / 16 FAIL. Không nên xem thống kê này là độ bao phủ đầy đủ của toàn bộ bộ 13 ca.

Kết quả cũng cần được diễn giải thay vì chỉ chấp nhận nhãn PASS/FAIL. Build 4 thất bại ở TC-SUBTRACT-008 vì kết quả là `6.3` trong khi mong đợi `6`; Build 7 thất bại cả 8 ca và Build 8 chỉ đạt 1/8. Những sai khác này hữu ích để phát hiện vấn đề, nhưng cần đối chiếu test steps, expected result, cấu hình **Integers only** và hành vi từng build để phân biệt lỗi ứng dụng với kỳ vọng kiểm thử chưa chính xác.

Bài học rút ra là nên dùng AI như công cụ hỗ trợ, không thay thế việc kiểm soát chất lượng của người kiểm thử. Người dùng cần xác định rõ phạm vi, kiểm tra test case có thực sự được script chạy hay không, đối chiếu actual result với expected result, và rà soát báo cáo trước khi kết luận. Việc ghi lại prompt, kết quả và những điểm cần xác minh giúp quá trình sử dụng AI minh bạch và có thể kiểm chứng hơn.