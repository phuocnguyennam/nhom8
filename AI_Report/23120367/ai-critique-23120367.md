# ĐÁNH GIÁ VÀ NHẬN XÉT VỀ CÔNG CỤ AI (AI CRITIQUE)

- **MSSV:** 23120367
- **Học phần:** Kiểm thử Phần mềm (Software Testing)
- **Bài tập:** Kiểm thử ứng dụng Basic Calculator (`https://testsheepnz.github.io/BasicCalculator`)

---

Trong quá trình thực hiện kiểm thử, AI dễ bộc lộ thiên kiến xác nhận và thiếu sót khi chỉ tập trung kiểm tra tính đúng đắn của kết quả số học ở “luồng thuận” mà xem nhẹ các trạng thái biên hay tác dụng phụ ngầm. Cụ thể, ở Build 8, do phép cộng có tính giao hoán ($a + b = b + a$), AI có xu hướng kết luận tính năng hoạt động hoàn hảo và dễ bỏ sót lỗi hoán đổi biến nếu con người không chủ động thiết kế các ca kiểm thử bất đối xứng như xác thực chuỗi ký tự (TC-ADD-017, 018).

Nguyên nhân cốt lõi là AI thiếu góc nhìn toàn cục về ngữ cảnh hệ thống và trải nghiệm người dùng thực tế; mô hình hoạt động dựa trên logic so khớp mẫu tĩnh và giả định môi trường độc lập thay vì tư duy phản biện để “bẻ gãy” phần mềm. Bài học lớn nhất rút ra về nguyên tắc cộng tác với AI là không bao giờ tin tưởng tuyệt đối vào kết quả hay kịch bản AI đề xuất ban đầu. Con người cần giữ vai trò kiến trúc sư: thiết lập chiến lược kiểm thử nghiêm ngặt, định hướng các ca kiểm thử tiêu cực (negative testing) và liên tục rà soát phản biện các giả định của AI thay vì phó mặc toàn bộ quy trình QA.