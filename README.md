# pants python raw coverage issue

When generating a raw coverage report, all statements are marked as missing.
However, generating any different kind of report (json/html) shows 100% coverage.

## How to reproduce
- Run the tests `pants test ::`
- Generate a raw report by running the `check.py` script. The script will show the stats from the raw coverage report, and use it to generate an html report. You can see the html data by running `open htmlcov/index.html`. The report shows 0% coverage.
- Generate an html report by changing the `[coverage-py]` `report` value to `html`, and run `rm -rf htmlcov && pants test ::`. The new report will show 100% coverage.
