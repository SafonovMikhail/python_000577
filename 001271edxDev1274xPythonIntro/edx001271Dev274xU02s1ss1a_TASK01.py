# https://dev274x-ms33.notebooks.azure.com/j/notebooks/Mod1_2-1.1_Intro_Python.ipynb#Work-with-individual-string-characters

# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters
street_name = 'Suzdalsky'
print(street_name[1])
print(street_name[3])
print(street_name[5])

# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else
team_name = 'Linda'
if team_name[1].lower() == 'i':
    print('Winner! second letter "i": ', team_name )
elif team_name[1].lower() == 'o':
    print('Winner! second letter "o": ', team_name)
elif team_name[1].lower() == 'u':
    print('Winner! second letter "u": ', team_name)
else:
    print('Sorry, next time: ', team_name )

