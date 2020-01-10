# creating a list of famous people to invite for dinner.
guest_list = ['sandra bullock', 'Tom cruise', 'Angelina  jolie']
print(" Dinner Guest List : " + str(guest_list))
print("\n" + guest_list[2] + " can't make to the dinner.")

# Modifying list.
guest_list[2] = 'Jeniffer Lopez'

print(" New guest_list : " + str(guest_list))
# dinner invitation message.
for name in guest_list:
    print("\n****Dinner Invitation****" + "\n\t" + name.title() + ", \nThe honour of your presence\n\t is requested"
                                                                "\nfor Dinner and Dancing."
                                                                "\n\ton Wednesday,\n14th Feb 2019 at 7:30 P.M."
                                                                "\nat Vintage Club,Rockville,MD."
                                                                  "\n\tPlease RSVP.\n----------------------")