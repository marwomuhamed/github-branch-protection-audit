# GitHub Branch Protection Audit

## Overview

This project is a simple Python audit tool that checks whether the default branch of every repository in a GitHub organisation requires at least one approved pull request review before changes can be merged.

The script was developed as a **one-time audit tool** and is intentionally kept simple, readable and easy to maintain.

The script is **read-only** and does **not** make any changes to GitHub.

---

## Features

- Connects to a GitHub organisation using a Personal Access Token (PAT)
- Automatically discovers all repositories in the organisation
- Excludes repositories defined in an exclusion list
- Detects each repository's default branch
- Checks whether branch protection requires at least one approving review
- Reports the result for each repository as:
  - ✅ PASS
  - ❌ FAIL
  - ⏭️ SKIPPED
- Displays an audit summary

---

## Excluded Repositories

The following repositories are excluded from the audit:

- `config`
- `config-test`

---

## Requirements

- Python 3.x
- PyGithub
- python-dotenv

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_personal_access_token
GITHUB_ORG=pcf-branch-protection-lab
```

---

## Running the Script

```bash
python audit.py
```

---

## Example Output

```text
Repository: good-service-1
Status: PASS

Repository: bad-service-1
Status: FAIL

Repository: config
Status: SKIPPED

=========================
Audit Summary
=========================
Passed : 5
Failed : 3
Skipped: 2
=========================
```