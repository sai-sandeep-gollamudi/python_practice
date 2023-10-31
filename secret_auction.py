import os

while(True):
    auction_entrees = {}
    ch=1
    while(ch):
        print("Details for bid.")
        os.system('cls') #to clear the screen
        name = input("Enter your name: ")
        bid = int(input("Enter your bid amount in $: "))
        auction_entrees[name] = bid
        choice = input("Are there any other auctioners willing to bid, type yes or no: ")
        if(choice!= "Yes" and choice!= "yes" and choice!="YES"):
           ch=0
    highest_amount = 0
    for k,v in  auction_entrees.items():

        if(v>highest_amount):
            name=k
            highest_amount = v
    print(f"The winner of this auctions is {name} for bid of ${highest_amount}")
    fa = input("Are there any other auctions? Type yes or no: ")
    if(fa!= 'yes' and fa!='Yes' and fa!='YES'):
        break