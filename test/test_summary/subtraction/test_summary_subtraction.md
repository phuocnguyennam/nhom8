# Subtraction Test Summary

**Website:** [Basic Calculator](https://testsheepnz.github.io/BasicCalculator.html)  
**Date:** 2026-09-28  
**Test script:** `test_scripts/sub.py`

## Scope

This summary covers the 8 subtraction test cases in `test_cases/substract/` and the execution reports from Build 1 through Build 8. Each build was run against all 8 cases, for 64 test executions in total. Percentages are calculated against 8 cases per build.

## Test Cases

| Test ID | Test case | Inputs / action | Expected result |
| ------- | --------- | --------------- | --------------- |
| TC-SUBTRACT-001 | Basic subtraction with a positive result | `10 - 4` | `6` |
| TC-SUBTRACT-002 | Subtraction resulting in a negative value | `5 - 12` | `-7` |
| TC-SUBTRACT-003 | Subtraction of two equal numbers | `8 - 8` | `0` |
| TC-SUBTRACT-004 | Subtraction of decimal numbers | `10.5 - 4.2` | `6.3` |
| TC-SUBTRACT-005 | Subtraction with a negative first number | `-5 - 10` | `-15` |
| TC-SUBTRACT-006 | Subtraction of two negative numbers | `-10 - (-3)` | `-7` |
| TC-SUBTRACT-007 | Subtraction of zero from a number | `15 - 0` | `15` |
| TC-SUBTRACT-008 | Decimal subtraction with Integers only enabled | `10.5 - 4.2`, Integers only enabled | `6` (integer part only) |

## Results by Build

| Build | Passed | Failed | Pass rate | Fail rate | Detailed report |
| ----- | -----: | -----: | --------: | --------: | --------------- |
| Build 1 | 8 | 0 | 100.0% | 0.0% | [sub.md](../../test_runs/build1/test_runs/sub.md) |
| Build 2 | 8 | 0 | 100.0% | 0.0% | [sub.md](../../test_runs/build2/test_runs/sub.md) |
| Build 3 | 8 | 0 | 100.0% | 0.0% | [sub.md](../../test_runs/build3/test_runs/sub.md) |
| Build 4 | 7 | 1 | 87.5% | 12.5% | [sub.md](../../test_runs/build4/test_runs/sub.md) |
| Build 5 | 8 | 0 | 100.0% | 0.0% | [sub.md](../../test_runs/build5/test_runs/sub.md) |
| Build 6 | 8 | 0 | 100.0% | 0.0% | [sub.md](../../test_runs/build6/test_runs/sub.md) |
| Build 7 | 0 | 8 | 0.0% | 100.0% | [sub.md](../../test_runs/build7/test_runs/sub.md) |
| Build 8 | 1 | 7 | 12.5% | 87.5% | [sub.md](../../test_runs/build8/test_runs/sub.md) |
| **Total** | **48** | **16** | **75.0%** | **25.0%** | **64 executions** |

## Test Result Matrix

`P` = Pass, `F` = Fail

| Test ID | Build 1 | Build 2 | Build 3 | Build 4 | Build 5 | Build 6 | Build 7 | Build 8 |
| ------- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| TC-SUBTRACT-001 | P | P | P | P | P | P | F | F |
| TC-SUBTRACT-002 | P | P | P | P | P | P | F | F |
| TC-SUBTRACT-003 | P | P | P | P | P | P | F | P |
| TC-SUBTRACT-004 | P | P | P | P | P | P | F | F |
| TC-SUBTRACT-005 | P | P | P | P | P | P | F | F |
| TC-SUBTRACT-006 | P | P | P | P | P | P | F | F |
| TC-SUBTRACT-007 | P | P | P | P | P | P | F | F |
| TC-SUBTRACT-008 | P | P | P | F | P | P | F | F |

## Build Notes

- Builds 1, 2, 3, 5, and 6 passed all 8 subtraction cases.
- Build 4 failed only TC-SUBTRACT-008: the report records `6.3`, while the test expects `6` with Integers only enabled.
- Build 7 failed all 8 cases, including equal operands (expected `0`, actual `-8`) and subtracting zero (expected `15`, actual `0`). The failures affect ordinary integer and decimal subtraction.
- Build 8 passed only TC-SUBTRACT-003, where both operands are equal. Its other actual results match the opposite sign of the expected subtraction result (for example, `10 - 4` produced `-6` and `5 - 12` produced `7`), consistent with reversed operand order.
- All 64 cases completed with either Pass or Fail; no execution errors were recorded.

## Conclusion

The suite passed 48 of 64 executions (75.0%). Build 7 and Build 8 show broad failures in subtraction, while Build 4 has a single failure involving the Integers only option. Prioritize investigation of those three builds; the other five builds passed this subtraction suite.