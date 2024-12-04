number=int(input("Enter The Number :"))
if number %15==0:
    print("FIZZBuzz") 
elif number % 5==0:
    print("BUZZ") 
elif number %3==0:
    print("FIZZ") 
else:
    print("Invalid Number") 