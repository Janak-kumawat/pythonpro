#factorial with function :- in this program we print fact variable in for loop so it gives factorial of all steps 

def fact_f(n):
    fact=1
    for i in range(1,n+1):
      fact*=i
      print(fact)
fact_f(5)


  #factorial of only one no. :- but in this program we print fact variable outside the for loop so it gives only the factorial of given number.
  # A proper induntation is metter in python
def fact_f(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

fact_f(5)

#withot function 
num=5
factorial=1
for j in range(1,num+1):
  factorial*=j
  print(factorial)

