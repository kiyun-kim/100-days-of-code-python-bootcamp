# Modifying Global Scope

# 1️⃣ Declare a global variable `enemies` and assign it the value 1.
# This variable can be accessed from anywhere in the code.
enemies = 1


# 2️⃣ Define a function named `increase_enemies`.
# It takes one parameter called `enemy`.
def increase_enemies(enemy):
    # global enemies
    # enemies += 1
    # 4️⃣ Since there is no variable named `enemies` inside the function, Python looks for it
    # in the outer (global) scope. The value of the global `enemies` is currently 1, so this line executes.
    print(f"enemies inside function: {enemies}") # Output: enemies inside function: 1

    # 5️⃣ The function adds 1 to the `enemy` parameter it received (value: 1)
    # and returns the result, which is 2.
    return enemy + 1


# 3️⃣ Call the `increase_enemies` function.
# The current value of the global variable `enemies` (which is 1) is passed as an argument.
# The value returned by the function is then assigned back to the global variable `enemies`.
enemies = increase_enemies(enemies)

# 6️⃣ After the function call and assignment are complete, print the final value
# of the global variable `enemies`. Since the returned value 2 was stored in it, 2 will be printed.
print(f"enemies outside function: {enemies}") # Output: enemies outside function: 2

# The core idea of this code is how a function changes a global variable's value without using the global keyword.
# Passing the Value: When the function is called, the value (1) of the global variable enemies is copied into the function's local variable, enemy.
# Calculating and Returning: The function performs a calculation using its local variable enemy and returns a new value (2). It does not directly modify the global variable enemies.
# Updating: The value returned by the function (2) is assigned back to the global variable enemies. This is how the global variable's value is updated from 1 to 2.
# The commented-out lines, global enemies and enemies += 1, show an alternative method for modifying the global variable directly from within the function. However, this example uses the safer and more common practice of returning a value to handle the update.


