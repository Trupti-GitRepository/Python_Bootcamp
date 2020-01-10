guest_list = ['sandra bullock', 'Tom cruise', 'Jeniffer Lopez']
print(" Dinner Guest List : " + str(guest_list))
# insert guests
guest_list.insert(0, 'selena gomez')
guest_list.insert(2, 'Nick Jonas')
guest_list.append('priyanka chopra')
print("\nNew Dinner Guest List : " + str(guest_list))
for name in guest_list:
    print("\n****Dinner Invitation****" + "\n\t" + name.title() + ", \nThe honour of your presence\n\t is requested"
                                                                "\nfor Dinner and Dancing."
                                                                "\n\ton Wednesday,\n14th Feb 2019 at 7:30 P.M."
                                                                "\nat Vintage Club,Rockville,MD."
                                                                  "\n\tPlease RSVP.\n----------------------")