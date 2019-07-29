import sendgrid
import os
import base64
from UserClass import User
from sendgrid.helpers.mail import *
# # from ExportToExcel import ExcelConverter
class emailNotifier():
    def __init__(self, user):
        """
        Constructor to the emailNotifier class, takes sender and recipient email addresses
        """
        self.user = user
        self.sender = Email("noreply@pisces.com")
        self.recipient = Email(user.getEmail())
        self.sg = sendgrid.SendGridAPIClient(apikey = "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")
        self.content = Content("text/plain", "EMAIL")

    def sendEmail(self):
        """
        a function that sends an email to the user with his fish farm data
        """
        subject = "Hello"
        self.mail = Mail(self.sender, subject, self.recipient, self.content)
        response = self.sg.client.mail.send.post(request_body = self.mail.get())
        print(response.status_code)
        print(response.body)
        # print(response.headers)

u = User("ab", "b", "abdullahsalah96", "fdsa", "abdullahsalah96@outlook.com", None, None, None, None)
e = emailNotifier(user = u)
e.sendEmail()