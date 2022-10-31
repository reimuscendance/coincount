typeofcoin = [200, 100, 50, 20, 10, 5, 2, 1]
maxamount = [2000, 2000, 1000, 1000, 500, 500, 100, 100]
weight = [12.0, 8.75, 8.0, 5.0, 6.5, 2.35, 7.12, 3.56]
maxweight = [120.0, 87.5, 160.0, 250.0, 650.0, 235.0, 356.0, 356.0]

with open('CoinCount.txt') as f:
    for line in f:
        print(line.strip())

donating = True
times_donated = 0
while donating:
    with open("CoinCount.txt") as f:
        lines = f.readlines()
    
    name = input('Enter your name:')
    print(f'Hello, {name}')
    print("These are the coins that are accepted:")
    print(typeofcoin)

    type_of_coin = int(input("Please enter a type of coin thats accepted    "))
    if type_of_coin in typeofcoin:
        coin_index = typeofcoin.index(type_of_coin)
        print("max amount: ", maxamount[coin_index])
        print("weight ", weight[coin_index])
        print("maxweight",maxweight[coin_index])
        amountofcoins = int(input("Please input the amount of coins in your bag:    "))
        usercoinweight = float(weight[coin_index]) * float(amountofcoins)
        print(f"your bag should weigh {usercoinweight}")

    if type_of_coin not in typeofcoin:
        print("Please enter a type of coin that is accepted")
    userweight = float(input("Please enter weight of bag:   "))

    if userweight not in weight:
        amount_off = float(maxweight[coin_index]) - float(userweight)
        print(f"You are {amount_off}g off the max weight")
    
        totalamount = float(maxamount[coin_index]) - float(userweight)          # This takes away the users inputed weight of coins from the max amount they can input.
    coins_needed = (float(totalamount) / float(maxweight[coin_index]))      # This finds the amount the user puts in and then divides it by the max weight the user can input and then displays how many coins they need to add to make the max weight.
    roundedcoin = round(coins_needed, 0)
    print(f"You need to add {roundedcoin} many coins to have max weight" )

    previousentries = input("Do you want to see the previous entries?")
    if previousentries == ("yes"):
        print(line.strip())
    if previousentries == ("no"):
        print("Thank you for donating! ")    
    
    with open('CoinCount.txt', 'a') as f:
        f.write(f"User Name: {name} | User Weight: {userweight} | Users Coin Type: {type_of_coin} | Amount user was off by in weight: {float(maxweight[coin_index]) - float(userweight)}  \n ")
    
    end = input("Would you like to make another entry?  ")
    if end == ("no"):
        break
    if end == ("yes"):
        print("Okay Running program again.")
        times_donated = times_donated + 1
    print (f"this program has run {times_donated} this many times")