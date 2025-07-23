# Scope = 범위
enemies = 1 # Global variable

# Difference between global and local scope
# -> Where you define or where you create your variables or your function
def increase_enemies():
    enemies = 2 # Local variable
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
