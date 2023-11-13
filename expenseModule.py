from utils import generateUniqueID

class Expense:
    def __init__(self, category, ammount, description):
        self.expenseID = generateUniqueID()
        self.category = category
        self.ammount = ammount
        self.description = description
        self.reciepts = []

    def addReciept(self, recieptID):
        self.reciepts.append(recieptID)

    def removeReciept(self, recieptID):
        self.reciepts.remove(recieptID)

    def getReciepts(self):
        return self.reciepts
