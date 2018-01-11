#-----------------------------------------------
#How to make exceptions example

while true:
   try: 
       number = int(input ("whATS YOUR FAV  number? \n"))
             #print (18/number)
             break
              
         except ValueError:
             print("Make sure and enter a number")
         
         except ZeroDivisionError:
             print('can divivde by 0')  
             
         except: #not good programming because it can hide alot of problems and just break the programm
                 #used for general exceptions
           break
         
         finally: #this means that this will happen regardless of what happens in the program
               print ('loop complete')
