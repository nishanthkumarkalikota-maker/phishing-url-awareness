# Test Results

Python version used: __________ | Operating system: __________ | Date: __________

| # | Input | Expected result | Actual result (fill after running) | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs; not proof of safety |pass | |
| 2 | `http://192.0.2.10/account` | IP address + HTTP warnings | | |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol + HTTP warnings |pass | |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments warning | pass | |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname warning | pass | |

## Notes
After running all five tests, write 2–3 sentences about what you learned. Do not mark a test PASS until you have run it and checked the output.
