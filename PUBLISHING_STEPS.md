# GitHub + Zenodo publication instructions (not yet published)

Repository owner: Tiffany Freeman; affiliation: LXN Solutions, Inc.

1. Sign in to GitHub and create a **public** repository, suggested name `cmer-evidence-replication`. Do not upload confidential data, participant records, or secrets.
2. Upload the repository contents: `CMER_registry_schema.json`, `CMER_guard_dictionary.json`, both illustrative records, `CMER_replication_packet_cover_sheet.json`, `CMER_Outcome_Data_Dictionary.csv`, `CMER_Coder_Handbook.txt`, `validate_examples.py`, `mre/`, `REPOSITORY_README.md`, and `Figure_1_alt_text.txt`. Keep relative paths unchanged. Include a LICENSE only after the author chooses its terms.
3. On a fresh machine, follow `REPOSITORY_README.md` and run `python validate_examples.py` and `python mre/run_mre.py`. Record command output and confirm it matches `mre/mre_output.json`.
4. Publish a tagged GitHub release (e.g. `v1.0.0`) and connect/archive that release with Zenodo. Verify the Zenodo record is public, has a real DOI, and the GitHub URL is accessible without login.
5. Supply the exact GitHub repository URL and Zenodo DOI to update the clean manuscript, marked manuscript, and AR004 response note. Do not submit placeholders as completed AR004.
6. Confirm repository license, public sharing authority for LXN-associated work, and whether the journal requests a particular data-availability statement or artifact license.

**No repository has been published or DOI minted by this package. Publication requires the author's separate authorization and account action.**
