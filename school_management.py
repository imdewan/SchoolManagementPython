#Simple script for school management 
import json
import hashlib
import os

def is_there(path, mode='r'): 
    
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True

if not os.path.exists('data'):
    print("setting up folders")
    os.makedirs('data')
    print("done")

print("Welcome to School Management script")

adminloc = "data/admin-data"
if is_there(adminloc) :
    f = open(adminloc, "r")
    admindata = f.read()
    log = input("Enter admin password: ")
    log1 = hashlib.md5(log.encode())
    if admindata != log1.hexdigest() :
        print("wrong password")
    else :   
        print("success")
        nxt = input(" press 1 to add student \n press 2 to view student \n press 3 to delete student \n")
        if nxt == "1":
            name = input("name: ")
            age = input("age: ")
            phone = input("phone no.: ")
            data = input("other data: ")
            pathr = 'data/' + phone
            f = open(pathr,"w+")
            x = {
            "age": age,
            "name": name,
            "data": data
            }
            y = json.dumps(x)
        
            f.write(y)
            f.close() 
        if nxt == "2" :
            phone = input("Enter student's phone no : ")
            pathr = 'data/' + phone
            if is_there(pathr) :
                f=open(pathr, "r")
                contents = f.read()
                datas = json.loads(contents)
                print ("name- " + datas["name"])
                print ("age- " + datas["age"])
                print ("other data- " + datas["data"])
                f.close() 
            else :
                print("no student found")
        if nxt == "3" :
            phone = input("Enter student's phone no : ")
            pathr = 'data/' + phone
            if is_there(pathr) :
                f=open(pathr, "r")
                contents = f.read()
                datas = json.loads(contents)
                f.close() 
                c = input ("Do you want to delete " + datas["name"] + "'s record y/n :")
                if c == "y":
                    os.remove(pathr)
                

else :
       print("You need to create an new password ")
       pswrd = input("Password: ")
       hashpass = hashlib.md5(pswrd.encode()) 
       f = open(adminloc,"w+")
       f.write(hashpass.hexdigest())
       f.close()


ext = input("enter to exit: ")
exit