bill_per_person = 12.1
# округление до второго знака
print(f"{bill_per_person:.2f}")

bill = float(input("What was the total bill, $: "))
people = int(input("amount of people: "))
tip = int(input("tip amount (10,12,15), %: "))
bill_per_person = bill / people
bill_per_person_with_tip = bill_per_person * (tip / 100 + 1)
print(f"bill per person: {bill_per_person_with_tip:.2f}")
