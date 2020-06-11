black_list = [" "]
url = input("Please enter URL: ")
if url.find("http://") == -1:
    print("Username not found")
else:
    
    fpos = url.find('~')
    ut = "www.ut.ee"
    ut_found = url.find(ut)

    if ut_found == -1:
        print("Username not found")
    else:
        if fpos == -1:
            print("Username not found")
        else:
            if url[fpos-1] == '/':
                
                lpos = url.find('/', fpos)
                
                name = url[fpos+1:lpos]
                if name.find("username") != -1:
                    print("Username not found")
                elif name.find(" ") != -1:
                    print("Username not found")
                else:
                    print("Username is {}".format(name))
            else:
                print("Username not found")