from src.addition import add
from src.subtraction import subtract
from src.multiplication import multiply
#from src.division import divide

def run():
    print("--- CLI Calculator App Running ---")
    print(f"Addition (5 + 3): {add(5, 3)}")
    print(f"Subtraction (10 - 4): {subtract(10, 4)}")
    print(f"Multiplication (6 * 7): {multiply(6, 7)}")
   # print(f"Division (20 / 5): {divide(20, 5)}")

if __name__ == "__main__":
    run()
