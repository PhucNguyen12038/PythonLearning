c = 4.1868
tes = 5
tas = 15
cup = 220

s = input("Enter the amount: ")
fu = input("Enter the first unit: ")
su = input("Enter the second unit: ")

try:
    amount = float(s)
except:
    amount = -1

if amount >= 0:
    
    if fu == 'teaspoon' and su == 'cup':
        t = amount * tes
        t = t / cup
        strT = str(t) + " cup"
        print("This amount corresponds to ", strT)
    elif fu == 'cup' and su == 'teaspoon':
        t = amount * cup
        t = t / tes
        strT = str(t) + " teaspoon"
        print("This amount corresponds to ", strT)
    #----------------------------------------
    
    elif fu == 'teaspoon' and su == 'gram':
        t = amount * tes
        
        strT = str(t) + " gram"
        print("This amount corresponds to ", strT)
    elif fu == 'gram' and su == 'teaspoon':
        t = amount / tes
        strT = str(t) + " teaspoon"
        print("This amount corresponds to ", strT)    
    #-------------------------------
    
    elif fu == 'tablespoon' and su == 'gram':
        t = amount * tas
        strT = str(t) + " gram"
        print("This amount corresponds to ", strT)
    elif fu == 'gram' and su == 'tablespoon':
        t = amount / tas
        strT = str(t) + " teaspoon"
        print("This amount corresponds to ", strT)  
    #-------------------------------------
    elif fu == 'cup' and su == 'gram':
        t = amount * cup
        strT = str(t) + " gram"
        print("This amount corresponds to ", strT)
    elif fu == 'gram' and su == 'cup':
        t = amount / cup
        strT = str(t) + " cup"
        print("This amount corresponds to ", strT)  
    
    #------
    
    
    elif fu == 'teaspoon' and su == 'tablespoon':
        t = amount * tes
        t = t / tas
        strT = str(t) + " tablespoon"
        print("This amount corresponds to ", strT)
    elif fu == 'tablespoon' and su == 'teaspoon':
        t = amount * tas
        t = t / tes
        strT = str(t) + " teaspoon"
        print("This amount corresponds to ", strT)
        
    #--------
    elif fu == 'tablespoon' and su == 'cup':
        t = amount * tas
        t = t / cup
        strT = str(t) + " cup"
        print("This amount corresponds to ", strT)
    elif fu == 'cup' and su == 'tablespoon':
        t = amount * cup
        t = t / tas
        strT = str(t) + " tablespoon"
        print("This amount corresponds to ", strT)
    else:
        print("Please use different units.")
else:
    print("Please enter the amount as numeric value")
    
    