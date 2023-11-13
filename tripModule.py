from utils import generateUniqueID

class Trip:
    def __init__(self,startingLocation,destination,startDate,endDate):
        self.tripID = generateUniqueID()
        self.startingLocation = startingLocation
        self.destination = destination
        self.startDate = startDate
        self.endDate = endDate
        self.users = []
        self.expenses = []
        self.reciepts = []

    def addExpense(self, expenseID):
        self.expenses.append(expenseID)

    def removeExpense(self, expenseID):
        self.expenses.remove(expenseID)

    def getExpenses(self):
        return self.expenses
