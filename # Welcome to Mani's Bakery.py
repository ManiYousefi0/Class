# Welcome to Mani's Bakery
total_1 = 0
total_2 = 0
while True :
    Gender = input ( "what is your gender ? ")
    if Gender == "ms" :
        break
    elif Gender == "mr" :
        break
    else :
        print (" please select between (mr) or (ms)")
first_name = input (" what is your first name? ")
last_name = input (" what is your last name? ")
available_breads ={
    "barbary" : 2000 ,
    "lavash" : 1000 , 
    "taftoon" : 1500 , 
    "sangak" : 3000 ,
    "bugget" : 10000
} 
#show available breads
for nan in available_breads :
    print (nan)
customer_choice = input(" what kind of bread do you want ?")
while True :
    if customer_choice in available_breads :
        Number = int(input ( " how many breads do you want ? "))
        cost = available_breads[customer_choice] * Number
        total_1 += cost 
        break
    else :
        print (" unavailable bread . try again .")
while True :
    want_more = input ( " do you want more ? (write 'no' to exit) ")
    if want_more in available_breads :
        Number2 = int(input ( " how many breads do you want ? "))
        cost2 = available_breads[want_more] * Number2
        total_2 += cost2
    if want_more == "no":
        break
total_cost = total_1 + total_2
print (Gender , first_name , last_name ," your total cost is " , total_cost )