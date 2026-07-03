import os
from github import Github
from dotenv import load_dotenv

EXCLUDED_REPOS = [
    "config",
    "config-test"
]


def main():
    load_dotenv()

    token = os.getenv("GITHUB_TOKEN")
    org_name = os.getenv("GITHUB_ORG")

    github = Github(token)
    org = github.get_organization(org_name)

    total = 0
    passed = 0
    failed = 0
    skipped = 0

    print("=" * 60)
    print("GitHub Branch Protection Audit")
    print(f"Organisation: {org.login}")
    print("=" * 60)

    for repo in org.get_repos():
        total += 1

        print(f"\nRepository: {repo.name}")

        if repo.name in EXCLUDED_REPOS:
            skipped += 1
            print("Status: SKIPPED →")
            print("Reason: Excluded from audit.")
            print("-" * 60)
            continue

        default_branch = repo.default_branch
        print(f"Default Branch: {default_branch}")

        try:
            branch = repo.get_branch(default_branch)
            protection = branch.get_protection()

            review_count = (
                protection
                .required_pull_request_reviews
                .required_approving_review_count
            )

            if review_count >= 1:
                passed += 1
                print("Status: PASS ✓")
                print("Reason: Branch protection requiring at least one approving review is enabled.")
            else:
                failed += 1
                print("Status: FAIL ✗")
                print("Reason: Branch protection requiring an approving review is not enabled.")

        except Exception:
            failed += 1
            print("Status: FAIL ✗")
            print("Reason: Branch protection requiring an approving review is not enabled.")

        print("-" * 60)

    print("\n" + "=" * 60)
    print("Audit Summary")
    print("=" * 60)
    print(f"Total Repositories : {total}")
    print(f"Passed             : {passed}")
    print(f"Failed             : {failed}")
    print(f"Skipped            : {skipped}")
    print("=" * 60)


if __name__ == "__main__":
    main()