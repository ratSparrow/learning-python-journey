from enum import Enum

class State (Enum):
    INATCIVE = 0    
    ACTIVE = 1
    # SUSPENDED = 2

print(State.ACTIVE.value)
print(State["ACTIVE"].value)
print(State["ACTIVE"])
print(list(State))
print(len(State))