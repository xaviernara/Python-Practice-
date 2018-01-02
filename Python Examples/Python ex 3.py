# #print ("I hope this works");
# age = 13 
# 
# if age < 21 :
#   print ("no beer for you")
#   
# #----------------------------------------
# #if and elif (else if) example 1
# name = "Xavier"
# 
# if name is "Bucky":
#    print("hey there bucky")
#    
# elif name is "Xavier":
#    print ("hey yo Xavier")
#    
# elif name is "Jay":
#    print ("not my name")
#   
# #----------------------------------------
# #if and elif (else if) example 2
# #also remember that python gives errors if you tab unexpectedly 
# names = "bob"
# if names is "Bucky":
#    print("hey there bucky")
#    
# elif names is "Xavier":
#    print ("hey yo Xavier")
#    
# elif names is "Jay":
#    print ("not my name")
#    
# else:
#    print("sign up for the site ")
# 
#----------------------------------------
#for loop example 1 
#length = len

#foods = ["tuna", "ham", "polish", "beef", "chicken"]

# for f in foods:
#    print (f)
#    print(len(f))
 
#looping thru a certain portion of a list and getting its size

#----------------------------------------
#range and while loop example
#this is the same as creating a empty array and filling with a RANGE of whatever
# for x in range (10, 40, 5): #(start num, end num, increment)
#    #print ("xavier is cool")
#    print(x)


# buttcrack = 5
# 
# while buttcrack < 10:
#    print (buttcrack)
#    buttcrack += 1
 
# #----------------------------------------
# #comment and break example
# #this finds a magic num
# magicnum=26
# 
# print(9, "xavier") #to print out unlike things (ie int and string) use the comma instead of +
# 
# #+ only works when the 2 things are alike 
# for n in range (101):
   # if n is magicnum:
      # print (n," is the magic number")
#       break
#    else:
#       print(n)
    
#----------------------------------------
#continue example:
numbersTaken = [2,3,4,5,8]
print ("heres the numbers still avaliable:")
for n in range (1,20):
   if n in numbersTaken:
     continue
   print(n)

    
    


 


