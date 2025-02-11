import numpy as np
msg = "Roll a dice"

arr = np.array([1, 2, 3, 4, 5, 6])

def roll_dice():
    return np.random.choice(arr)

if __name__ == "__main__":
    print(msg)
    print("You rolled a", roll_dice())