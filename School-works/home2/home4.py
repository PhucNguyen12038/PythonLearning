fn = input("Enter first name: ")
sn = input("Enter second name: ")

fn = fn.replace("Ü","u")    

fn = fn.replace("Õ","o")

fn = fn.replace("Ä","a")

fn = fn.lower()
    
sn = sn.replace("Ü","u")    

sn = sn.replace("Õ","o")

sn = sn.replace("Ä","a")

sn = sn.lower()
print(fn + "." + sn)