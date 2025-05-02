from google.adk.tools import tool
import os

OUTPUT_DIR = "sent_emails"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@tool
def send_email(to: str, subject: str, body: str) -> dict:
    """
    Saves the email content to a .txt file named after the recipient/company.
    """
    try:
        # Sanitize filename from email/URL/company
        company_name = to.split("@")[0].replace(".", "_").replace("-", "_")
        filename = os.path.join(OUTPUT_DIR, f"{company_name}.txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"To: {to}\n")
            f.write(f"Subject: {subject}\n\n")
            f.write(body)

        return {"status": "saved", "file": filename}

    except Exception as e:
        return {"status": "error", "message": str(e)}