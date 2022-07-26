import smtplib
import ssl
import main


def send_mails(message):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "akash.jaiswal36@gmailss.com"
    receiver_mail = "akashjaiswal@liveee.in"
    password = "jpzfttdimmsqzrhe"


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_mail, message)
            main.logger.info("Mail sent.....")

        except:
            main.logger.info("Could not send mail...")