import os
import json
import coverage
from coverage.report import get_analysis_to_report

config_file = os.getcwd() + "/.coveragerc"

cov = coverage.Coverage(config_file=config_file)
cov.load()

for file_report, analysis in get_analysis_to_report(cov, []):
  print(json.dumps({
    'file': file_report.filename,
    'statements': list(analysis.statements),
    'missing': list(analysis.missing),
    'covered': list(analysis.statements - analysis.missing)
  }, indent=2))

  cov.html_report()