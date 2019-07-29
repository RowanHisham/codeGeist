import sendgrid
import os
from sendgrid.helpers.mail import *
import base64
from ExportToExcel import ExcelConverter
class emailNotifier():
    def __init__(self, sender, user):
        """
        Constructor to the emailNotifier class, takes sender and recipient email addresses
        """
        self.user = user
        self.sender = Email(sender)
        self.recipient = Email(user.getEmail())
        self.sg = sendgrid.SendGridAPIClient(apikey = "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")

    def sendEmail(self):
        """
        a function that sends an email to the user with his fish farm data
        """
