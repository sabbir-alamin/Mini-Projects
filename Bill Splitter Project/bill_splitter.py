# ----------------------------
# Bill Splitter Calculator
# ----------------------------
# This script calculates a restaurant bill, adds a tip,
# and splits the total equally among a group of friends.

# ---- Running total of the bill ----
running_total = 0

# ---- Number of people splitting the bill ----
num_of_friends = 4

# ---- Cost breakdown of the order ----
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# ---- Add up all order items into the running total ----
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# ---- Calculate a 25% tip on the total bill ----
tip = running_total * 0.25
print('Tip amount:', tip)

# ---- Add the tip to the running total ----
running_total += tip
print('Total with tip:', running_total)

# ---- Divide the total bill (with tip) among all friends ----
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# ---- Round each person's share to 2 decimal places ----
each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)
