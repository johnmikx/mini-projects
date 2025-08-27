from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State)               # Output: <enum 'State'>
print(State.INACTIVE)        # Output: State.INACTIVE
print(State.ACTIVE)          # Output: State.ACTIVE
print(State.INACTIVE.value) # Output: 0
print(State.ACTIVE.value) # Output: 1
print(State(0))              # Output: State.INACTIVE
print(State(1))              # Output: State.ACTIVE
print(State['INACTIVE'])     # Output: State.INACTIVE
print(State['ACTIVE'])       # Output: State.ACTIVE
print(State['INACTIVE'].value)   # Output: 0
print(State['ACTIVE'].value)     # Output: 1
print(list(State))         # Output: [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
print(len(State))          # Output: 2