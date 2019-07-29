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
        headers = {
            # Request headers
            'Content-Type': 'multipart/form-data',
            'Prediction-key': '{subscription key}',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'iterationId': '{string}',
            'application': '{string}',
        })

        try:
            # conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
            conn = http.client.HTTPSConnection(self.httpAddress)
            conn.request("POST", "/customvision/v1.0/Prediction/{projectId}/image?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
