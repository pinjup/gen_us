import random
from necesary import names, last_n, generate_pass

choose = int(input("Choose the number of users: "))
number = 0
print('Here are your users :)')
for i in range(choose):
    random_n = random.choice(names)
    random_ln = random.choice(last_n)
    random_n_ = random.choice(names)
    random_ln_ = random.choice(last_n)
    password = generate_pass()
    number+=1
    print(number)
    print(f'-----------------------------------------------------------------------------')
    print(f"""
        First Name = {random_n}
        Second Name = {random_n_}
        First Surname = {random_ln}
        Second Surname = {random_ln_}
        Password = {password}
    """)
    print('------------------------------------------------------------------------------')
    
