is_raining = bool(int(input("Is it raining 0/1: ")))
no_of_goals_f = int(input("France golas : "))
no_of_goals_s = int(input("Spain golas : "))

next_round_result = not (is_raining) and (no_of_goals_f > no_of_goals_s)
print("France next round status : ", next_round_result)