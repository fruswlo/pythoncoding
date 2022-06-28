is_raining = bool(int(input("Is it raining ? 0/1 : ")))
france_goal = int(input("Enter france goal amount : "))
spain_goal = int(input("Enter spain goal amount : "))

going_next_round = not is_raining and (france_goal > spain_goal)

print("France next round status : ", going_next_round)