# Dinner guest list. # Exercise 3.7
guest_list = ['selena gomez', 'sandra bullock', 'Nick Jonas', 'Tom cruise', 'Jeniffer Lopez', 'priyanka chopra']
print(len(guest_list))

print("\nAt dinner venue, new table can't be delivered in time. Only have space for two guests.")

# Remove guest until two guests will left.
for guest in guest_list:
    if len(guest_list) != 2:
        popped_guest = guest_list.pop()
        print(popped_guest + ", \n\tYou are not invited for the dinner as new table can't be delivered in time."
                             "Only have space for two guests."
                             "\n\tI apologize for the inconvenience it may have caused.\n ")
    else:
        print(guest.title() + " You are still invited for the dinner.")

print(len(guest_list))
