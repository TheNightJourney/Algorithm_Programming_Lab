Bill = float(input("Please enter bill: "))
People = float(input("How many people are you?: "))
Tip = float(input("What is the percentage you'll be tipping today?: "))
P_Tip = Tip * 0.01
Total_Per_Person = (Bill / People)
Tip_Per_Person = P_Tip * Total_Per_Person
print("Tip per person in ($)",Tip_Per_Person)
print("Total per person in ($)", Total_Per_Person + Tip_Per_Person)