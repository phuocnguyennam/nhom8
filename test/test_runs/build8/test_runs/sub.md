# Subtraction Test Run

- **Build:** 8
- **Executed At:** 2026-09-28T15:59:46+07:00

| Test ID | Test Name | Expected Result | Actual Result | Verdict |
| ------- | --------- | --------------- | ------------- | ------- |
| TC-SUBTRACT-001 | Verify basic subtraction with a positive result | The Answer field displays `6`. | -6 | FAIL |
| TC-SUBTRACT-002 | Verify subtraction resulting in a negative value | The Answer field displays `-7`. | 7 | FAIL |
| TC-SUBTRACT-003 | Verify subtraction of two equal numbers | The Answer field displays `0`. | 0 | PASS |
| TC-SUBTRACT-004 | Verify subtraction of decimal numbers | The Answer field displays `6.3`. | -6.3 | FAIL |
| TC-SUBTRACT-005 | Verify subtraction with a negative first number | The Answer field displays `-15`. | 15 | FAIL |
| TC-SUBTRACT-006 | Verify subtraction of two negative numbers | The Answer field displays `-7`. | 7 | FAIL |
| TC-SUBTRACT-007 | Verify subtraction of zero from a number | The Answer field displays `15`. | -15 | FAIL |
| TC-SUBTRACT-008 | Verify decimal subtraction with "Integers only" enabled | The Answer field displays `6` (integer part only). | -6 | FAIL |
