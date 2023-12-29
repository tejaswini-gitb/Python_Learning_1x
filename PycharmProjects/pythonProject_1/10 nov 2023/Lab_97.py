class Browser:
    def __init__(self,browser):
        self.browser = browser
    def openbrowser(self, browser= "chrome"):
        print("write code to open--> " + self.browser)

b = Browser("edge")
#b = Browser()   --- defalut value = chrome

b.openbrowser()