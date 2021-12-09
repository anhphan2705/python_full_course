Nums = int(input("Please enter n: "))
mainNums = Nums
largerPrimes = []
smallerPrimes = []
countLargerPrimes = 0
countSmallerPrimes = 0
lowerThanOrEqual0 = False
isLargerPrimes = False
isSmallerPrimes = False
presentDigit = None
presentDigit2 = None

def largerPrimesCounter() :
    global countLargerPrimes
    for i in largerPrimes:
        countLargerPrimes = countLargerPrimes + 1
        
def smallerPrimesCounter() :
    global countSmallerPrimes
    for i in smallerPrimes:
        countSmallerPrimes = countSmallerPrimes + 1
    
def findLargerPrimes() :
    global countLargerPrimes
    for i in range(1,50):
        for a in range(2,mainNums):
            if (mainNums + i)% a != 0:
                isLargerPrimes = True
                presentDigit = mainNums + i
            else:
                isLargerPrimes = False
                break
        if isLargerPrimes:
            if isLargerPrimes:
                largerPrimesCounter()
                if countLargerPrimes < 6:
                    largerPrimes.append(presentDigit)
                    countLargerPrimes = 0
                else:
                    countLargerPrimes = 0
                    break
    isLargerPrimes = False

def findSmallerPrimes() :
    global countSmallerPrimes, lowerThanOrEqual0, presentDigit2
    for i in range(1,50):
        for a in range(2,mainNums):
            if (mainNums - i) > 0:
                if ((mainNums - i)% a != 0 or ((mainNums - i) == a)):
                    isSmallerPrimes = True
                    presentDigit2 = mainNums - i
                else:
                    isSmallerPrimes = False
                    break
            else:
                lowerThanOrEqual0 = True
                break
        if lowerThanOrEqual0 == True:
            break
        elif isSmallerPrimes:
            smallerPrimesCounter()
            if countSmallerPrimes < 6:
                smallerPrimes.append(presentDigit2)
                countSmallerPrimes = 0
            else:
                countSmallerPrimes = 0
                break
    isSmallerPrimes = False
    
def output():
    global countSmallerPrimes
    print("Larger Primes: "+str(largerPrimes[0])+ " "+str(largerPrimes[1])+ " "+str(largerPrimes[2])+ " "+str(largerPrimes[3])+ " "+str(largerPrimes[4]))
    countSmallerPrimes = 0
    smallerPrimesCounter()
    if countSmallerPrimes == 0:
        print("Smaller Primes: nothing")
    elif countSmallerPrimes == 1:
        print("Smaller Primes: "+str(smallerPrimes[0]))
    elif countSmallerPrimes == 2:
        print("Smaller Primes: "+str(smallerPrimes[0])+" "+str(smallerPrimes[1])+" ")
    elif countSmallerPrimes == 3:
        print("Smaller Primes: "+str(smallerPrimes[0])+" "+str(smallerPrimes[1])+" "+str(smallerPrimes[2]))
    elif countSmallerPrimes == 4:
        print("Smaller Primes: "+str(smallerPrimes[0])+" "+str(smallerPrimes[1])+" "+str(smallerPrimes[2])+" "+str(smallerPrimes[3]))
    elif countSmallerPrimes == 5:
        print("Smaller Primes: "+str(smallerPrimes[0])+" "+str(smallerPrimes[1])+" "+str(smallerPrimes[2])+" "+str(smallerPrimes[3])+" "+str(smallerPrimes[4]))
    
while countLargerPrimes < 6 and (countSmallerPrimes < 6 or lowerThanOrEqual0== False):
    countLargerPrimes = 0
    countSmallerPrimes = 0
    largerPrimesCounter()
    smallerPrimesCounter()
    if countLargerPrimes < 6:
        presentDigit = 0
        countLargerPrimes = 0
        findLargerPrimes()
    if countSmallerPrimes < 6 or lowerThanOrEqual0:
        countSmallerPrimes = 0
        findSmallerPrimes()
    else:
        break
    
output()