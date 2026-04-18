# app.py
def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts second number from the first."""
    return a - b

if __name__ == "__main__":
    # Sample usage
    print(f"Add 5 + 3 = {add(5, 3)}")
    print(f"Subtract 5 - 3 = {subtract(5, 3)}")