**# Lab 6: Code and Branch Coverage Analysis**



**## Objective**

**The objective of this lab is to test the loan eligibility application and measure code coverage and branch coverage using pytest and coverage.py.**



**## Application**

**The application is implemented in `loan\_eligibility.py`. It includes functions for determining credit score bands, checking loan eligibility, and calculating interest rates.**



**## Test Files**

**- `test\_loan\_eligibility.py` – Contains test cases for the application.**

**- `CodeCoverageTest\_PES1UG24CS575\_application.py` – Test file used for code coverage analysis.**

**- `BranchCoverageTest\_PES1UG24CS575\_application.py` – Test file used for branch coverage analysis.**



**## Code Coverage**

**The final code coverage result was 100%.**



**Screenshot: `Code\_Coverage\_After.png`**



**## Branch Coverage**

**The final branch coverage result was 100%, with 24 branches and 0 partial branches.**



**Screenshot: `Branch\_Coverage\_After.png`**



**## Before and After Screenshots**

**- `Code\_Coverage\_Before.png`**

**- `Code\_Coverage\_After.png`**

**- `Branch\_Coverage\_Before.png`**

**- `Branch\_Coverage\_After.png`**



**## Commands Used**



**### Code Coverage**

**```bash**

**python -m coverage erase**

**python -m coverage run -m pytest CodeCoverageTest\_PES1UG24CS575\_application.py**

**python -m coverage report -m**

**```**



**### Branch Coverage**

**```bash**

**python -m coverage erase**

**python -m coverage run --branch -m pytest BranchCoverageTest\_PES1UG24CS575\_application.py**

**python -m coverage report -m**

**```**



**## Conclusion**

**The loan eligibility application was tested successfully. The final tests achieved 100% code coverage and 100% branch coverage.**

**## GitHub Repository**



**\*\*Forked Repository:\*\* \[L6\_L7\_26\_loan\_eligibility](https://github.com/kavyakorti/L6\_L7\_26\_loan\_eligibility)**



**This repository contains the loan eligibility application, test cases, code coverage analysis, branch coverage analysis, and before-and-after screenshots.**

