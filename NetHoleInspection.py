from cognitiveServices import Server


class NetHoleDetection(Server):
    def __init__(self):
        self.httpAddress = 'australiaeast.api.cognitive.microsoft.com'
        self.subAddress = "/customvision/v3.0/Prediction/0081ddad-4c13-4705-ac6b-819068f863f8/classify/iterations/Fishnet_Holes_Detection/image"
        self.predKey = 'bd5db334ffa249f1bd8ca2d43ccf5da3'
        self.contentType = 'application/octet-stream'
        self.predkey = '/subscriptions/16e8c7d2-4877-4c8f-bb77-ae2931dd33eb/resourceGroups/Test/providers/Microsoft.CognitiveServices/accounts/Test_Prediction'
        super().__init__(self.httpAddress, self.subAddress, self.predKey, self.contentType, self.predkey)

    def predict(self, img):
        """
        a function that returns:
            string: yes, no, can't determine
        """