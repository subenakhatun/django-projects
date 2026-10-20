""" 
registration form create korbo.
varaibale nibo
name, email, password, lastname, phone,address,city, sate,
country,birthdate, gender 
"""
name = input('enter first name: ')
def fname(name):
    for fname in name:
        if fname.isdigit():
            fname = True
            break
    if fname:
        print("wrong")
    else:
        return fname
fname(name)
print(name)


# name = input("Enter your name:")
# print(name)

# Question: name tho likhlam, name er length ki hobe?
# name er moddhe jodi number dey thahole ki hobe?
# answer : name er length bole dei 10 er niche hobe, ar jodi nam er moddhe kunu digit thakhe thahole seta hobe na
# so seta k 2 ta way te bola jay. ak isdigit diye ba puru nam k string likhe . akon somossa ase, string tho number o hote pare
# tar mane name er protita charater k checkkora lagbe jeno kunu number na hoy. jodi kunu number hoy thahole error dekhabe

# name = input("Enter your name:")
# number ki na check kore isdigit()
n = input("enter any number:")
# if len(n) >= 0 and not n.isdigit():
#     print(n)
# else:
#     print("not valid")

# check n string or int


# print(int(n))