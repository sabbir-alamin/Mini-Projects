# ----------------------------
# Ticket Booking System
# ----------------------------
# This script simulates booking a movie/event ticket.
# It checks age eligibility, applies discounts, and adds extra
# charges, and calculates the final ticket price.
 
# ---- Input values (can be changed to test different cases) ----
base_price = 15          # base price of the ticket
age = 21                 # age of the user booking the ticket
seat_type = 'Gold'       # seat category: Premium, Gold, or Standard
show_time = 'Evening'    # show timing: Morning, Afternoon, Evening, etc.
 
# ---- Check basic age eligibility for booking ----
if age > 17:
    print('User is eligible to book a ticket')
 
# ---- Check eligibility specifically for Evening shows ----
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')
 
# ---- Membership and weekend flags ----
is_member = False    # whether the user is a registered member
is_weekend = False   # whether the booking is for a weekend show
 
# ---- Apply membership discount (only for members aged 21+) ----
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)
 
# ---- Apply extra charges for weekend or evening shows ----
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)
 
# ---- Final booking condition check ----
# Booking is allowed if:
# - user is 21 or older, OR
# - user is 18+ AND (show is not evening OR user is a member)
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
 
    # ---- Calculate service charges based on seat type ----
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
 
    # ---- Calculate final ticket price ----
    final_price = (base_price + extra_charges + service_charges) - discount
 
    print('Final price of ticket:', final_price)
