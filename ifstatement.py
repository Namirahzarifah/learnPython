#if statement within function

def schoolAgeCalculator(age,name): #to get two values: age and name of child
    if age < 5:
        print("Enjoy the time at home!", name, "is only", age)
    elif age == 5:
        print("Enjoy kindergarten", name)
    else: 
        print("They grow up so fast!")

schoolAgeCalculator(3, "Thomas")
schoolAgeCalculator(5, "Dales")
schoolAgeCalculator(8, "Charles")