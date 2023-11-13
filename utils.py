import uuid
import datetime

def generateUniqueID():
    return str(uuid.uuid4())

def getCurrentDate():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
