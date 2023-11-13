from utils import generateUniqueID
from utils import getCurrentDate


class Receipt:
    def __init__(self, tripID, expenseID, userID):
        self.receiptID = generateUniqueID()
        self.tripID = tripID
        self.expenseID = expenseID
        self.userID = userID
        self.date = getCurrentDate()

    def generatePDF(self):
        pass

