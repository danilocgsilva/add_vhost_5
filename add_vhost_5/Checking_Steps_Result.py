class Checking_Steps_Result:

    def __init__(self):
        self.checked = None
        self.message = ""

    def setOk(self):
        self.checked = "Ok"
        return self

    def setPartial(self):
        self.checked = "Partial"
        return self

    def setProblem(self):
        self.checked = "Problem"
        return self

    def setMessage(self, message: str):
        self.message = message
        return self

    def getResponseResult(self) -> dict:
        return {
            "status": self.checked,
            "message": self.message
        }
