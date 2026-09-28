# AI CRITIQUE

- **MSSV:** 23120050
- **Học phần:** Kiểm thử Phần mềm (Software Testing)
- **Bài tập:** Kiểm thử ứng dụng Basic Calculator (`https://testsheepnz.github.io/BasicCalculator`)

---

During the AI usage, it correctly took the explained outline of the web app and generated 15 test cases. As for the quality of test cases most of it focus on normal calculation such as multiply two number, decimal, leaving blank,etc but it fails to generate more complex test cases such as calculate, clear then calculate again.

During the test scripts, it correctly identify the relevant html field to generate a rough test script utilizing python + playwright. It also give a quick summary after each run for easier comparison and reference. That said it missed alot of GUi specific error such as in build #4 the Integer Only being locked. As stated before the test cases overall are simple so most of the test actually passed.

So what can be done? First on the user side, me, I could have asked it to generate a more robust test cases including more complex situation which will help in finding more obscure bug. During the script generation, additional information could be provided so the test script is more robust in detecting GUI error.

Last but not least the important lesson is to not entire trust what the AI generate is the best in any way. AI usually goes for the most simple of solutions unless asked otherwise so when it comes to software testing, its best to be very specific about what the system does and what are we testing so the AI can generate the most relevant test case and test script.
