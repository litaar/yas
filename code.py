#BEGIN
def Moneybuckets():
    #Money buckets
    Income = float(input("Income: "))
    age = 60
    #Calculate amounts
    Blow = 0.6 * Income
    Daily = 0.6 * Blow
    Mojo = 0.2 * Blow
    Grow = 0.2 * Blow
    data_teams = ["Blow", "Mojo", "Grow"]
    format_row = "{:>11}" * (len(data_teams) + 1)
    print(format_row.format("", *data_teams))
    print(Blow)
    print(Mojo)
    print(Grow)


def Compoundinterest():
    income = float(input("Annually investment: "))
    interest = float(input("Average annual interest: "))
    age = -2
    while age < 59:
        age = age + 1
        print(age + 1)
        for age in range(1,61):
            print(income)



    investment = income * 0.10 * interest


    total = total + investment



print("Money buckets (1)""  or  Miracle of compound interest (2)")
choice = input("CHOOSE YOUR OPTIONS:")

if choice == "1":
    Moneybuckets()
elif choice == "2":
    Compoundinterest()
else:
    print("୨୧ Please choose either 1 or 2 ୨୧")
    choice = input("CHOOSE YOUR OPTIONS:")


#10 percent of current investment balance

#format_row =
