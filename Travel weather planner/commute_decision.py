# ------------------------------------------------------------
# Transportation Decision Program
# ------------------------------------------------------------
# This program determines whether a person can travel based on:
# - Distance to the destination
# - Weather conditions
# - Available transportation options
#
# Decision Rules:
# 1. Walk if the destination is within 1 mile and it is not raining.
# 2. Do not walk if it is raining.
# 3. For distances between 1 and 6 miles, riding a bike is required.
# 4. For distances greater than 6 miles, a car or ride-sharing service
#    must be available.
# ------------------------------------------------------------

# -----------------------
# Input Variables
# -----------------------
distance_mi = 4
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

# -----------------------
# Transportation Decision
# -----------------------

# Ensure a valid distance is provided.
if not distance_mi:
    print("False")

else:

    # Walking is only allowed for very short distances in good weather.
    if distance_mi <= 1 and not is_raining:
        print("True")

    # Walking is not recommended when it is raining.
    elif distance_mi <= 1 and is_raining:
        print("False")

    # Medium distance requires a bike.
    # If it is raining and no bike is available, travel is not possible.
    elif 1 < distance_mi <= 6 and is_raining and not has_bike:
        print("False")

    # Without a bike, medium-distance travel is not possible,
    # even when the weather is clear.
    elif 1 < distance_mi <= 6 and not is_raining and not has_bike:
        print("False")

    # Bike travel is allowed for medium distances when it is not raining.
    elif 1 < distance_mi <= 6 and has_bike and not is_raining:
        print("True")

    # For long-distance travel, a ride-sharing service is acceptable.
    elif distance_mi > 6 and has_ride_share_app:
        print("True")

    # A personal car can also be used for long-distance travel.
    elif distance_mi > 6 and has_car:
        print("True")

    # Travel is not possible if neither a car nor ride-sharing
    # service is available.
    elif distance_mi > 6 and not has_car and not has_ride_share_app:
        print("False")