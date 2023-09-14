Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Height=float(input("Enter your height in centimeters: "))
... Weight=float(input("Enter your Weight in Kg: "))
... Height = Height/100
... BMI=Weight/(Height*Height)
... print("your Body Mass Index is: ",BMI)
... if(BMI>0):
... 	if(BMI<=16):
... 		print("you are severely underweight")
... 	elif(BMI<=18.5):
... 		print("you are underweight")
... 	elif(BMI<=25):
... 		print("you are Healthy")
... 	elif(BMI<=30):
... 		print("you are overweight")
... 	else: print("you are severely overweight")
