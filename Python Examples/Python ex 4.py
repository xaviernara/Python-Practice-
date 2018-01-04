# Function example 
# to create a function you have to say def 1st
# def beef():
   # print("entered the beef function")
# 
# #calling a function
# beef()
#    
# def bitcoin_to_usd(bitcoin):
#    amount = bitcoin *527
#    print ("this is the amount", amount)
# 
# bitcoin_to_usd(3.85) 
# bitcoin_to_usd(3)
# bitcoin_to_usd(.85)

#----------------------------------------------------------
#return statement example

# def allowed_dating_age(my_age):
#     girls_age = (my_age/2)+7
#     return girls_age
#     
# age_limit=allowed_dating_age(27)
# creepy = allowed_dating_age(49)
# print ("you can date girls", age_limit, "or older") 
# print ("creep can date girls", creepy, "or older") 

#----------------------------------------------------------
#default values for arguments example
# def get_gender(sex = "unknown"):
# #IS is the same as ==
   # if sex is "m":
#       sex = "male"
#    elif sex is "f":
#       sex = "female"
#    print (sex)
#    
# get_gender("m")
# get_gender("f")
# #SINCE THE paramenter isnt set to anything, sex is set to the default value unknown 
# get_gender()
# 


#----------------------------------------------------------
#variable scope example
#this example basically covers why functions cant access variable or whatever if they are below it or created and used inside of a func
#the func can only use things above it and things created inside of it
#ie globl and local variables 
# def corn():
#    num=3334
#    print(num)
#    
# def fudge ():
#    num =565
#    print(num)
#  
# corn()
# fudge()
# 

 #-------------------------------------------------------
 #keyword arguments example
 #this basically covers how you can pick and choose which func parameters you want to  
 #send 
# def dumb_sentences(name = "John", action= "ate", item = "fish"): 
#       print (name,action,item)
#       
#  
# dumb_sentences()
# dumb_sentences("sally","farts","loudly")
# dumb_sentences(item="chicken", action= "is")

#-------------------------------------------------------
#flexiable number of arguments example
#basically how to create a func that can take any number of arguments

# def add_numbers(*args): #common naming convention is to name flexiable arguments *args
#    total = 0
#    for a in args:
#       total += a
#    print(total)
#    
#  add_numbers(3)
#  add_numbers(3,44)
#  add_numbers(78,44)


#-------------------------------------------------------
#unpacking arguments example

# def health_calc(age,apples_ate,cigs_smoked):
#    answer= (100-age)+ (apples_ate*3.5) - (cigs_smoked * 2)
#    print ("answer = ", answer)
#    
# data= [20,45,0]
# health_calc(data[0],data[1],data[2])
# health_calc(*data)#unpacked arguments (ie sending a whole array (list) to a function)
#data*= accepts multiuple arguments like in a func, *data= send all arguments 

#-------------------------------------------------------
#Sets example
#this acts the same as a linked list Set form Java 
#Sets can have as many things inside of it except duplicates and it remembers the order

# groceries= {"milk","cereal","apples","beer","jam","milk" }
# print(groceries)
# 
# if "milk" in groceries:
#    print("you already have milk in the set(groceries list)")
# else:
#    print("oh yea you need milk")


#-------------------------------------------------------
#Dictionary example 
#format = (key : value)

# classmate = {"Tony": " cool but smells", "Emma": " sits behind me", "Jimmy": " sits in front of me"}  

#print(classmate)
#print(classmate["Emma"])

# for key, value, in classmate.items():
#    print(key+value)
 
 
#-------------------------------------------------------   
#Module example

def fish():
   print("I am a tunafish")



   