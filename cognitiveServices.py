import cv2
import http.client, urllib.request, urllib.parse, urllib.error, base64

class Server:
    def __init__(self, httpAddress, subscriptionAddress, predictionKey, contentType, predictionKeyTwo):
        self.httpAddress = httpAddress
        self.subscriptionAddress  = subscriptionAddress
        self.headers = {
            # Request headers
            'Prediction-Key': predictionKey,
            'Content-Type': contentType,
            'Prediction-key': predictionKeyTwo,
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'application': '{string}',
        })


    def getPrediction(self, img):
        """
        a function that gets prediction list from Azure service
        """

