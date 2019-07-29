from cognitiveServices import Server

"""
Getting index of tag is not working
"""

class NetHoleDetection(Server):
    def __init__(self):
        self.httpAddress = 'australiaeast.api.cognitive.microsoft.com'
        self.subAddress = "/customvision/v3.0/Prediction/1a9e8456-5cd6-4b76-8861-f47b6f4a7f2a/classify/iterations/Iteration1/image"
        self.predKey = 'bd5db334ffa249f1bd8ca2d43ccf5da3'
        self.contentType = 'application/octet-stream'
        self.predkey = '/subscriptions/16e8c7d2-4877-4c8f-bb77-ae2931dd33eb/resourceGroups/Test/providers/Microsoft.CognitiveServices/accounts/Test_Prediction'
        super().__init__(self.httpAddress, self.subAddress, self.predKey, self.contentType, self.predkey)

    def predict(self, img):
        """
        a function that returns:
            string: yes, no, can't determine
        """
        prediction = str(self.getPrediction(img))
        tag_index = str(prediction).find("tagId") + 8
        if(prediction[tag_index:tag_index+1] == '7'):
            return "no"
        elif(prediction[tag_index:tag_index+1] == '0'):
            return "yes"
        else:
            return "can't determine"



n = NetHoleDetection()
print(n.predict("/home/abdullahsalah96/Pictures/scene00211.png"))
