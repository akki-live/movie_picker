import smtplib
import ssl


def send_mails(message):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "akash.jaiswal36@gmail.com"
    receiver_mail = "akashjaiswal@live.in"
    password = "jpzfttdimmsqzrhe"


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_mail, message)
            print("Mail sent.....")

        except:
            print("Could not login or send mail..")