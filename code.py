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
    #Age they start investing
    age = int(input("Age:"))
    # The amount they  invest each year
    amount = float(input("Annually investment: "))

    #Average annual interest rate
    interest = float(input("Average annual interest: "))

    #Set total amount of money to 0
    total = 0

    #Print start of table
    print("Age ✮✮ Investment ✮✮ Total")

    # For each age until age is 60:
    for m in range(age, 61):
        # Amount invested each year is added to the current total
        total += amount
    # The interest rate is added on top of the current total
        total += total * 0.1


    #round total to a whole number
        total = int(round(total, 0))

    #print each line of table
        print(f" {m}      ${amount}      ${total}")



    #while age < 61:
        #interest_num = investment * interest #=500

        #total = investment + interest_num #=5000 + 500 (5500)
        #y = interest *(total + investment) #= 10% x 10500
        #m = y + total + investment










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
