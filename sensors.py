import requests

class Sensors():
    def __init__(self, url):
        self.url = url

    def scrapeUrl(self, url):
        """
        a function that returns a string of the
        scraped website
        """
        r = requests.get(url)
        return(r.text)

    def getTemperature(self):
        """
        a function that returns the temperature
        reading
        """
        text = str(self.scrapeUrl(self.url))
        tempIndex = text.find("temperature") + 2
        temperature = text[tempIndex: tempIndex+2]
        return temperature
