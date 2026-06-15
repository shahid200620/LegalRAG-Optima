import os
import random

os.makedirs("data/raw", exist_ok=True)

templates = [
    """
    This Agreement is made between Party A and Party B.
    The term of this agreement shall begin on the effective date and continue for five years.
    Confidential information disclosed under this agreement shall remain protected.
    Termination may occur upon written notice of thirty days.
    Liability shall be limited to direct damages only.
    """,

    """
    The employee agrees to comply with all company policies.
    Compensation shall be paid monthly according to the agreed salary.
    Intellectual property created during employment belongs to the employer.
    Termination can occur with a sixty-day notice period.
    Disputes shall be resolved under applicable labor law.
    """,

    """
    The seller agrees to deliver goods within thirty business days.
    Payment shall be completed before delivery.
    Any defects must be reported within fifteen days.
    The buyer may reject goods that fail inspection.
    Warranty shall remain valid for one year.
    """,

    """
    The tenant shall pay rent on the first day of every month.
    The landlord is responsible for structural repairs.
    Security deposit shall be refundable after inspection.
    Subleasing is prohibited without written permission.
    This lease shall terminate after twelve months unless renewed.
    """,

    """
    This Non-Disclosure Agreement protects proprietary information.
    Both parties agree not to disclose trade secrets.
    Breach of confidentiality may result in legal action.
    Obligations survive for three years after termination.
    Jurisdiction shall be governed by the laws of the state.
    """
]

for i in range(150):
    content = random.choice(templates)

    content = content * random.randint(5, 15)

    with open(f"data/raw/contract_{i+1}.txt", "w", encoding="utf-8") as file:
        file.write(content)

print("150 legal files saved")