| Test Case ID | Module | Operation                |   Expected |     Result | Verdict | Related Bug | Note                            |
| ------------ | ------ | ------------------------ | ---------: | ---------: | ------- | ----------- | ------------------------------- |
| TC-MUL-001   | mul    | 5 \* 10                  |         50 |         50 | Pass    | N/A         |                                 |
| TC-MUL-002   | mul    | 25 \* 0                  |          0 |          0 | Pass    | N/A         |                                 |
| TC-MUL-003   | mul    | 0 \* 0                   |          0 |          0 | Pass    | N/A         |                                 |
| TC-MUL-004   | mul    | 1 \* 1                   |          1 |          1 | Pass    | N/A         |                                 |
| TC-MUL-005   | mul    | -5 \* 10                 |        -50 |        -50 | Pass    | N/A         |                                 |
| TC-MUL-006   | mul    | 2.5 \* 4.2               |       10.5 |         10 | Pass    | N/A         | Integer Only is forced to be on |
| TC-MUL-007   | mul    | 3.5 \* 4                 |         14 |         14 | Pass    | N/A         |                                 |
| TC-MUL-008   | mul    | 2.5 \* 3 (Integers Only) |          7 |          7 | Fail    | N/A         |                                 |
| TC-MUL-009   | mul    | 100000 \* 20000          | 2000000000 | 2000000000 | Pass    | N/A         |                                 |
| TC-MUL-010   | mul    | 12345 \* 1               |      12345 |      12345 | Pass    | N/A         |                                 |
| TC-MUL-011   | mul    | -2.5 \* -4               |         10 |         10 | Pass    | N/A         |                                 |
| TC-MUL-012   | mul    | -2.5 \* 1.2              |         -3 |         -3 | Pass    | N/A         |                                 |
| TC-MUL-013   | mul    | 0.001 \* 0.002           |   0.000002 |          0 | Pass    | N/A         | Integer Only is forced to be on |
| TC-MUL-014   | mul    | 5 \* 10 then clear       |          0 |         50 | Fail    | N/A         |                                 |
| TC-MUL-015   | mul    | 5 \* blank               |          0 |          0 | Pass    | N/A         |                                 |
