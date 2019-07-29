import sendgrid
import os
import base64
from UserClass import User
from sendgrid.helpers.mail import *
# # from ExportToExcel import ExcelConverter
class emailNotifier():
    def __init__(self, sender, user):
        """
        Constructor to the emailNotifier class, takes sender and recipient email addresses
        """
        self.user = user
        self.sender = Email(sender)
        # self.recipient = Email(user.getEmail())
        self.recipient = Email("abdullahsalah96@outlook.com")
        self.sg = sendgrid.SendGridAPIClient(apikey = "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")
        self.content = Content("text/html", "html_content")

    def sendEmail(self):
        """
        a function that sends an email to the user with his fish farm data
        """
        from_email = Email(self.sender)
        subject = "subject"
        to_email = Email(self.recipient)
        content = Content("text/html", "email_body")

        mail = Mail(from_email, subject, to_email, content)

        response = self.sg.client.mail.send.post(request_body=mail.get())

        print(response.status_code)
        print(response.body)
        print(response.headers)
#
#
u = User("ab", "b", "abdullahsalah96", "fdsa", "abdullahsalah96@outlook.com", None, None, None, None)
e = emailNotifier(sender= "yo@gmail.com", user = u)
e.sendEmail()
