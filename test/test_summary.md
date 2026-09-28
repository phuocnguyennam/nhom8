# Multiplication Test Summary

## Scope

This summary covers the 15 multiplication test cases in `test_cases/multiplication/` and the recorded results in `test_runs/build1` through `test_runs/build8`.

Pass and fail percentages are calculated against all 15 test cases:

`Percentage = count / 15 x 100`

## Test Cases

| Test ID    | Test case                                              | Inputs / action                       | Expected result                                                        |
| ---------- | ------------------------------------------------------ | ------------------------------------- | ---------------------------------------------------------------------- |
| TC-MUL-001 | Multiplication of two positive integers                | `5 x 10`                              | `50`                                                                   |
| TC-MUL-002 | Multiplication by zero                                 | `25 x 0`                              | `0`                                                                    |
| TC-MUL-003 | Multiplication of two zero values                      | `0 x 0`                               | `0`                                                                    |
| TC-MUL-004 | Multiplication of a negative and positive integer      | `-5 x 10`                             | `-50`                                                                  |
| TC-MUL-005 | Multiplication of two negative integers                | `-5 x -10`                            | `50`                                                                   |
| TC-MUL-006 | Multiplication of two positive decimal numbers         | `2.5 x 4.2`                           | `10.5`                                                                 |
| TC-MUL-007 | Multiplication of a decimal and an integer             | `3.5 x 4`                             | `14`                                                                   |
| TC-MUL-008 | Integer-only result for a decimal multiplication       | `2.5 x 3`, with Integers Only enabled | Integer result, recorded as `7` in the build files                     |
| TC-MUL-009 | Multiplication of large positive integers              | `100000 x 20000`                      | `2000000000`                                                           |
| TC-MUL-010 | Multiplication by one                                  | `12345 x 1`                           | `12345`                                                                |
| TC-MUL-011 | Multiplication of two negative decimal values          | `-2.5 x -4`                           | `10`                                                                   |
| TC-MUL-012 | Multiplication of negative and positive decimal values | `-2.5 x 1.2`                          | `-3`                                                                   |
| TC-MUL-013 | Multiplication of very small decimal values            | `0.001 x 0.002`                       | `0.000002`                                                             |
| TC-MUL-014 | Clear button resets the calculation                    | Calculate `5 x 10`, then click Clear  | Answer and entered values are cleared; build files record expected `0` |
| TC-MUL-015 | Missing second number is rejected                      | `5 x` blank                           | Validation/error response; build files record expected `0`             |

## Results by Build

| Build   | Pass | Fail | Pass percentage | Fail percentage | Total |
| ------- | ---: | ---: | --------------: | --------------: | ----: |
| Build 1 |   14 |    1 |          93.33% |           6.67% |    15 |
| Build 2 |   14 |    1 |          93.33% |           6.67% |    15 |
| Build 3 |   14 |    1 |          93.33% |           6.67% |    15 |
| Build 4 |   13 |    2 |          86.67% |          13.33% |    15 |
| Build 5 |   14 |    1 |          93.33% |           6.67% |    15 |
| Build 6 |   14 |    1 |          93.33% |           6.67% |    15 |
| Build 7 |    3 |   12 |          20.00% |          80.00% |    15 |
| Build 8 |   14 |    1 |          93.33% |           6.67% |    15 |

## Test Result Matrix

`P` = Pass, `F` = Fail

| Test ID    | Build 1 | Build 2 | Build 3 | Build 4 | Build 5 | Build 6 | Build 7 | Build 8 |
| ---------- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| TC-MUL-001 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-002 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-003 |    P    |    P    |    P    |    P    |    P    |    P    |    P    |    P    |
| TC-MUL-004 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-005 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-006 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-007 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-008 |    P    |    P    |    P    |    F    |    P    |    P    |    F    |    P    |
| TC-MUL-009 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-010 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-011 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-012 |    P    |    P    |    P    |    P    |    P    |    F    |    P    |    P    |
| TC-MUL-013 |    P    |    P    |    P    |    P    |    P    |    P    |    F    |    P    |
| TC-MUL-014 |    F    |    F    |    F    |    F    |    F    |    P    |    P    |    F    |
| TC-MUL-015 |    P    |    P    |    P    |    P    |    P    |    P    |    P    |    P    |

## Build Notes

- Builds 1, 2, 3, 5, 6, and 8 have the same result pattern: TC-MUL-014 fails and the other 14 tests pass.
- Build 4 fails TC-MUL-008 and TC-MUL-014. Its recorded notes state that Integer Only is forced on, producing `10` for TC-MUL-006 and `0` for TC-MUL-013 while those rows are still marked Pass.
- Build 7 fails 12 tests and passes only TC-MUL-003, TC-MUL-014, and TC-MUL-015.
- The percentages above are calculated from the verdict rows in each build's `mul.md` file. No separate Skip, Observe, or Error verdicts are recorded in those eight files.
