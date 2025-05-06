import argparse
from datetime import datetime

def parse_list(raw: str) -> list[str]:
    """Parse a comma-separated string into a list of trimmed items."""
    return [item.strip() for item in raw.split(',') if item.strip()]


def prompt_list(prompt: str) -> list[str]:
    raw = input(f"{prompt} (comma-separated, leave blank if none): ").strip()
    return parse_list(raw) if raw else []


def prompt_bool(prompt: str) -> bool:
    ans = input(f"{prompt} (yes/no): ").strip().lower()
    while ans not in ('yes', 'y', 'no', 'n'):
        ans = input("Please answer 'yes' or 'no': ").strip().lower()
    return ans in ('yes', 'y')


def prompt_choice(prompt: str, choices: list[str]) -> str:
    choices_str = ', '.join(choices)
    ans = input(f"{prompt} (choose from {choices_str}): ").strip().lower()
    while ans not in choices:
        print(f"Invalid choice. Please choose one of {choices_str}.")
        ans = input(f"{prompt} (choose from {choices_str}): ").strip().lower()
    return ans


def compose_email(
    business_name: str,
    founder_name: str,
    visit_date: str,
    documents_shared: list[str],
    sector: str,
    prior_investment: bool,
    existing_partnerships: list[str],
    need_type: str,
    needs_iMBEJU_account: bool
) -> tuple[str, str]:
    """Return (subject, body) for the follow-up email."""
    try:
        dt = datetime.fromisoformat(visit_date)
        visit_str = dt.strftime('%B %d, %Y')
    except ValueError:
        visit_str = visit_date

    subject = f"Uni Launch and Scale DD Follow-Up | {business_name}"
    lines = []
    lines.append(f"Dear {founder_name},")
    lines.append("")
    lines.append(
        f"It was a pleasure visiting {business_name} on {visit_str} to learn more about your operation and vision."
    )
    lines.append("")

    if documents_shared:
        lines.append("Thank you for sharing the following documents:")
        for doc in documents_shared:
            lines.append(f"- {doc}")
    else:
        lines.append("We’d appreciate it if you could share the following documents/information at your convenience.")
    lines.append("")

    lines.extend([
        "Please provide the following materials for our due diligence:",
        "Investor Pitch Deck",
        "Organizational Chart & Team Bios (founders and key hires)",
        "Incorporation Documents",
        "Financial Data:",
        "2024 revenue",
        "Q1 2025 revenue",
        "12-month financial projection",
        "Historical financial reports or audited statements (if available)",
        ""
    ])

    if sector == 'tech-enabled':
        lines.append("Product Roadmap")
        lines.append("")

    if prior_investment:
        lines.append(
            "Investment Memo: including investor name(s), amount, instrument type, and year."
        )
        lines.append("")

    lines.append("Capitalization Table: shareholders and ownership percentages.")
    lines.append("")

    if existing_partnerships:
        lines.append(
            "Existing Partnerships: list current partners and attach any agreements."
        )
        lines.append("")

    if needs_iMBEJU_account:
        lines.append(
            "Sharron (cc’d) and her team from CRDB Bank Foundation will follow up on the iMBEJU account setup."
        )
        lines.append("")

    lines.append(
        "Expect to hear from us within two weeks of today’s date."
    )
    lines.append(
        "If you have any questions or need clarification, please do not hesitate to reach out."
    )

    body = "\n".join(lines)
    return subject, body


def main():
    business_name = input("Enter business name: ").strip()
    founder_name = input("Enter founder name: ").strip()
    visit_date = input("Enter visit date (YYYY-MM-DD): ").strip()
    documents_shared = prompt_list("List any documents already shared")
    sector = prompt_choice(
        "Enter sector",
        ['tech-enabled', 'agribusiness', 'manufacturing', 'trading']
    )
    prior_investment = prompt_bool("Has this business raised capital before?")
    existing_partnerships = prompt_list("List existing partnerships")
    need_type = prompt_list(
        "Enter current needs (e.g., fund, partnership, technical_support)"
    )
    needs_iMBEJU_account = prompt_bool("Do they need an iMBEJU account?")

    subject, body = compose_email(
        business_name,
        founder_name,
        visit_date,
        documents_shared,
        sector,
        prior_investment,
        existing_partnerships,
        need_type,
        needs_iMBEJU_account
    )

    print(f"Subject: {subject}\n")
    print(body)

if __name__ == '__main__':
    main()
