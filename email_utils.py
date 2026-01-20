import smtplib
from email.message import EmailMessage

def send_email(to_email, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = to_email

    msg.set_content("Please find attached the TOPSIS result file.")

    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("garimasingla732@gmail.com", "fjxoqaeqwldghyqv")
        server.send_message(msg)
