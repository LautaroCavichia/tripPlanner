from utils import generateUniqueID


class User:
    def __init__(self, username, password):
        self.userID = generateUniqueID()
        self.username = username
        self.password = password
        self.trips = []

    def getUserID(self):
        return self.userID

    def addTrip(self, tripID):
        self.trips.append(tripID)

    def removeTrip(self, tripID):
        self.trips.remove(tripID)

    def getTrips(self):
        return self.trips

    def getReceipts(self):
        return self.receipts
