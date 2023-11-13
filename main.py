from userModule import User
from tripModule import Trip
from expenseModule import Expense
from recieptModule import Receipt

# Prova

user1 = User("Mario", "1234")
user2 = User("Luigi", "1234")


trip1 = Trip("Firenze", "Milano", "01/01/2024", "03/01/2024")

user1.addTrip(trip1.tripID)
user2.addTrip(trip1.tripID)

expense1 = Expense("Cibo", 10, "Pizza")
expense2 = Expense("Cibo", 20, "Pasta")

receipt1 = Receipt(trip1.tripID, expense1.expenseID, user1.userID)
receipt2 = Receipt(trip1.tripID, expense2.expenseID, user2.userID)

expense1.addReciept(receipt1.receiptID)
expense2.addReciept(receipt2.receiptID)

trip1.addExpense(expense1.expenseID)
trip1.addExpense(expense2.expenseID)

print(f"User1 ID: {user1.userID}")
print(f"User2 ID: {user2.userID}")
print(f"Trip ID: {trip1.tripID}")
print(f"Expense1 ID: {expense1.expenseID}")
print(f"Expense2 ID: {expense2.expenseID}")
print(f"Receipt1 ID: {receipt1.receiptID}")
print(f"Receipt2 ID: {receipt2.receiptID}")

#controlliamo che il trip sia presente in entrambi gli utenti
print(f"User1 trips: {user1.getTrips()}")
print(f"User2 trips: {user2.getTrips()}")

