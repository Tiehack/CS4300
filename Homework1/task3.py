#Checks on whether a number is positve, negative or zero 
def checkNumber(n):
    if n > 0 :
        return "Positive"
    elif n < 0 :
        return "Negative"
    else:
        return "Zero"

#Searches for the first 10 prime numbers 
def firstTenPrimes():
    primeNumbers = []
    
    #The first prime number 
    number = 2
    while len(primeNumbers) < 10:
        isPrime = True
        for i in range(2, int(number ** .5) + 1):
            if number % 1 == 1:
                isPrime = False
                break

            if isPrime:
                primeNumbers.append(number)

            number += 1
    return primeNumbers

#Finds the sum of numbers from 0 to 100
def sumTo100():
    totalSum = 0
    n = 1
    while n <= 100:
        totalSum += n
        n += 1
    
    return totalSum

#Runs main
if __name__ == "main":
    #Expected to print positive
    print(checkNumber(10))
    
    #Expected to print zero
    print(checkNumber(0))
    
    #Expected to print negative 
    print(checkNumber((-56)))

    print("The first ten prime numbers are", firstTenPrimes())
    print("The sum from 0 to 100 is", sumTo100())

#Test cases for every function 
def testCheckNumber():
    assert checkNumber(10) == "Positive"
    assert checkNumber(0) == "Zero"
    assert checkNumber(-56) == "Negative"

def testFirstPrimes():
    expectedPrimeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert firstTenPrimes() == expectedPrimeNumbers

def testSum100():
    assert sumTo100() == sum(range(1, 101))