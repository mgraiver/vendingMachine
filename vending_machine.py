
TOONIES=200
LOONIES=100
QUARTERS=25
DIMES=10
NICKELS=5

no_TOONIES=5
no_LOONIES=5
no_QUARTERS=20
no_DIMES=30
no_NICKELS=8
    
def display_welcome_menu():
    '''
    function that displays options to user 
    (none)-->none
    
    >>>display_welcome_menu()
    Welcome to the COMP 202 virtual Vending Machine!
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    
    '''
    print("Welcome to the COMP 2O2 virtual Vending Machine.")
    print("Here are your options:")
    print("1. Candy bar $2.95")
    print("2. Cookies $3.90")
    print("3. Soda $4.00")
    print("4. Chips $3.90")
    print("5. No snacks for me today!")

def get_snack_price(customer_choice):
    
    '''
    function that returns value based on users input
    (bool)-->num
    
    >>>get_snack_price(4):
    390
    >>>get_snack_price(1):
    295
    >>>get_snack_price(-3):
    0
    >>>get_snack_price(0):
    0
    
    '''
    if (customer_choice==1):
        return(295)
    elif (customer_choice==2):
        return(390)
    elif (customer_choice==3):
        return(400)
    elif(customer_choice==4):
        return(390)
    else:
        return(0)


def get_num_of_coins(amount_in_change,value_of_coin,no_of_coins):
    '''
    function that takes change, value of coin, number of coins
    and returns max number of coins that can be given
    (float,int,int)-->int
    
    >>>get_num_of_coins(100,100,5)
    1
    >>>get_num_of_coins(800,100,8)
    8
    >>>get_num_of_coins(799,100,8)
    7
    >>>get_num_of_coins(401,200,3)
    2
    
    '''

# variable that finds no of coins that should be returned for given change
# & value of coin

# if/else statement: Can't return more coins than the # coins the machine has
    division= amount_in_change//value_of_coin
    
    if value_of_coin>amount_in_change:
        return(0)
    
    elif (division >= no_of_coins):
        return (no_of_coins)
    
    else:
        return(division)

# helper function to find leftover change after a coin is used
def new_change(leftover_change,coin,no_coin):
    return leftover_change-(get_num_of_coins(leftover_change,coin,no_coin)*coin)
    '''
    function that finds new change leftover given previous coin value,
    and no. of coins used to pay back customer
    (int,int,int)-->float
    
    >>>new_change(100,QUARTERS,3)
    25
    >>>new_change(100,10,10)
    0
    >>>new_change(112,NICKELS,23)
    2
    >>>new_change(117,NICKELS,23)
    2
    >>> new_change(10,20,1)
    10
    
    '''
        
def compute_and_display_change(change):
    
    '''
    function that takes change and returns no. of coins per coin for change,
    using lowest number of coins
    (int)-->str,int
    
    >>>compute_and_display_change(560)
    TOONIES X 2
    LOONIES X 1
    QUARTERS X 2
    DIMES X 1
    NICKELS X 0
    True
    
    >>>compute_and_display_change(20)
    TOONIES X 0
    LOONIES X 0
    QUARTERS X 0
    DIMES X 2
    NICKELS X 0
    
    >>>compute_and_display_change(2500)
    TOONIES X 5
    LOONIES X 5
    QUARTERS X 20
    DIMES X 30
    NICKELS X 8
    True
    
    >>>compute_and_display_change(2499)
    False
    
    >>>compute_and_display_change(413)
    False
    
    >>>compute_and_display_change(2600)
    False
    
    '''

# boolean variable that determines if should compute_display change
# change needs to be > $25 (total amount) & divisible by smallest coin (nickel)
    b=change
    
    if b<=2500 and b%NICKELS==0:
       
# variable for each coin representing the leftover change with each coin
       T=change
       L=new_change(change,TOONIES,no_TOONIES)
       Q=new_change(L,LOONIES,no_LOONIES)
       D=new_change(Q,QUARTERS,no_QUARTERS)
       N=new_change(D,DIMES,no_DIMES)
                       
       print("\n TOONIES X", get_num_of_coins (T,TOONIES,no_TOONIES))
       print(" LOONIES X", get_num_of_coins(L,LOONIES,no_LOONIES))
       print(" QUARTERS X", get_num_of_coins(Q,QUARTERS,no_QUARTERS))
       print(" DIMES X", get_num_of_coins(D,DIMES,no_DIMES))
       print(" NICKELS X", get_num_of_coins(N,NICKELS,no_NICKELS))
                       
       return(True)
    else:
       return(False)


def operate_machine():
    '''
    function that calls vending machine
    (none)-->none
    
    >>>operate_machine()
    Please select your choice: 3

    The item of your choice costs 400 cents

    Enter your money: $4.1
    
    You inserted 410 cents

    You should recieve back 10 cents

    TOONIES X 0
    LOONIES X 0
    QUARTERS X 0
    DIMES X 1
    NICKELS X 0

    It was a pleasure doing business with you!
    
    >>>operate_machine()
    Please select your choice: 3

    The item of your choice costs 400 cents

    Enter your money: $4.0
    
    You inserted 400 cents

    You should recieve back 0 cents

    TOONIES X 0
    LOONIES X 0
    QUARTERS X 0
    DIMES X 0
    NICKELS X 0

    It was a pleasure doing business with you!
    
    >>>operate_machine()
    Please select your choice: 4

    The item of your choice costs 390 cents

    Enter your money: $4.1333
    
    You inserted 413 cents
    
    We do not accept pennies. Come by another time!
    
    >>>operate_machine()
    Please select your choice:2

    The item of your choice costs 390 cents

    Enter your money: $3.89
    
    You inserted 389 cents

    You should recieve back 10 cents
    
    We do not accept pennies. Come by another time!
    
    >>>operate_machine()
    Please select your choice:1

    The item of your choice costs 295 cents

    Enter your money: $2.90
    
    You inserted 290 cents

    You should recieve back 10 cents
    
    You do not have enough money to buy this item. Come by another time!
    
    >>>operate_machine()
    Please select your choice: 1

    The item of your choice costs 295 cents

    Enter your money: $30.0
    
    You inserted 3000 cents

    You should recieve back 2705 cents

    This machine does not have enough coins for your change. Come by another time!
    
    >>>operate_machine()
    Please select your choice: 5

    Nothing for you today. Thanks for stopping by!
    
    >>>operate_machine()
    Please select your choice: 0

    This mode is not supported
    
    '''
    display_welcome_menu()
    
    customer_choice=int(input("\n Please select your choice: "))
    
# if statement:to return snack price,customer needs to enter # between 1-4
    if (customer_choice >= 1 and customer_choice <= 4):
        print("\n The item of your choice costs", get_snack_price(customer_choice), "cents")
        
        amount_inserted=float(input("\n Enter your money: $" ))
        
#variable that converts dollars to cents and rounds to 2 dec places
        amount_inserted_cents=int(round(amount_inserted*100,2))
        
        print("\n You inserted",amount_inserted_cents,"cents")
        
# variable that calculates change given the users snack choice, and
# money inserted
        amount_in_change=amount_inserted_cents-get_snack_price(customer_choice)
        
        if amount_inserted_cents%NICKELS !=0:
            print("\n We do not accept pennies. Come by another time!")

        elif get_snack_price(customer_choice)>amount_inserted_cents:
            print("\n You do not have enough money to buy this item. Come by another time!")
                
        elif amount_inserted_cents>2500:
            print("\n You should recieve back", amount_in_change, "cents")
            print("\n This machine does not have enough coins for your change. Come by another time!")
            
        else:
            print("\n You should recieve back", amount_in_change, "cents")
            (compute_and_display_change(amount_in_change))
            
            print("\n It was a pleasure doing business with you!")
    
    elif (customer_choice==5):
        print("\n Nothing for you today. Thanks for stopping by!")
        
    else:
        print("\n This mode is not supported")
    

    
