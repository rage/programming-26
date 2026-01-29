num = int(input("Number: "))

if num % 3 == 0:
    print("Fizz", end="")
if num % 5 == 0:
    print(f"Buzz")

# -----=========-----


# def split_names_into_rows(name_list, modulus=2):
#     for index, name in enumerate(name_list, start=1):
#         print(f"{name:-^15} ", end="")
#         if index % modulus == 0:
#             print("First Print")
#     print("Second rint")

# names = ["Picard", "Riker", "Troi", "Crusher", "Worf", "Data", "La Forge"]
# split_names_into_rows(names)

# -----=========-----

# import turtle
# import random

# def draw_with_cyclic_iteration():
#     colors = ["green", "cyan", "orange", "purple", "red", "yellow", "white"]

#     turtle.bgcolor("gray8") # Hex: #333333
#     turtle.pendown()
#     turtle.pencolor(random.choice(colors)) # First color is random

#     i = 0 # Initial index

#     while True:
#         i = (i + 1) % 6 # Update the index
#         turtle.pensize(i) # Set pensize to i
#         turtle.forward(225)
#         turtle.right(170)

#         # Pick a random color
#         if i == 0:
#             turtle.pencolor(random.choice(colors))
