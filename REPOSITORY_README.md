# CMER replication framework: repository-ready draft

This is an unpublished local artifact package. Public DOI/URL: **NOT YET ASSIGNED**. Upload to an author-controlled GitHub/OSF/Zenodo repository; mint a persistent DOI where supported; replace placeholder in manuscript only after public publication.

## Contents
- `CMER_registry_schema.json`: draft 2020-12 JSON Schema
- `CMER_guard_dictionary.json`: G01-G08 legal transitions and guards
- `CMER_illustrative_record_01.json`, `_02.json`: illustrative, nonempirical records
- `CMER_replication_packet_cover_sheet.json`: synthetic packet cover sheet
- `CMER_Outcome_Data_Dictionary.csv`: outcome definitions, measures, windows and proxies
- `CMER_Coder_Handbook.txt`: coding rules and anchor cases
- `validate_examples.py`: schema and transition checker
- `mre/`: synthetic ITT demonstration with source CSV and executable code
- `CMER_Figure_1_Process.pdf`: vector workflow diagram
- `AR001_AR010_Response_Matrix.csv`: requirement status and outstanding author tasks

## Reproduce
Install `jsonschema` and run `python3 validate_examples.py`. Then run `python3 mre/run_mre.py`. Outputs are synthetic and do not prove an empirical marketing effect. Record the final Git commit and DOI after publication.
