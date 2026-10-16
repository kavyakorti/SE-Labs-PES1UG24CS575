# Lab 5: Static Code Analysis — Issues and Fixes

## Issues Identified

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk | Security | 11 | SQL query used string formatting, which could allow malicious input to modify the query. | Used parameterized SQL queries with placeholders. |
| Unsafe shell command | Security | 30 | `os.system()` executed a shell command containing user-supplied text. | Removed shell execution and used Python's `print()` function. |
| Weak hash algorithm | Security | 16 | MD5 was used to generate a farmer token. | Replaced MD5 with SHA-256. |
| Unused import | Code quality | 2 | The `json` module was imported but not used. | Removed the unused import. |
| Inconsistent function naming | Code style | Multiple | Function names did not follow Python's `snake_case` convention. | Renamed functions, such as `recordMilk` to `record_milk`. |
| Missing docstrings | Code quality | Multiple | The original module and functions lacked explanatory documentation. | Added module and function docstrings. |
| Long lines | Code style | 7, 11 | Some lines exceeded the recommended line length. | Split long statements across multiple lines. |
| Incorrect None comparison | Code quality | 35 | The original code used `fat == None`. | Changed it to `fat is None`. |
| String formatting | Code quality | 22 | The original code used percent-based string formatting. | Replaced it with an f-string. |
| Missing final newline | Code style | End of file | The file did not end with a newline character. | Added a final newline. |

## Verification Results

- Pylint: 10.00/10.
- Bandit: No issues identified in the corrected code.
- Flake8: No errors reported in the corrected code.

The program executed successfully after the changes.