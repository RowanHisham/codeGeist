import sendgrid
import os
import base64
from UserClass import User
from sendgrid.helpers.mail import *
# # from ExportToExcel import ExcelConverter
class emailNotifier():
    def __init__(self, user, temp):
        """
        Constructor to the emailNotifier class, takes sender and recipient email addresses
        """
        self.user = user
        self.sender = Email("NO-REPLY@pisces.com")
        self.recipient = Email(user.getEmail())
        self.sg = sendgrid.SendGridAPIClient(apikey = "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")
        self.content = Content("text/plain", "WARNING Temperature is " + temp)

    def sendEmail(self):
        """
        a function that sends an email to the user with his fish farm data
        """
        subject = "WARNING!!! Temperature above threshold"
        self.mail = Mail(self.sender, subject, self.recipient, self.content)
        response = self.sg.client.mail.send.post(request_body = self.mail.get())
        print(response.status_code)
        print(response.body)
        # print(response.headers)

