def number_check(question):
    while True:
        try:
            response = int(input(question))

            if response < 1 or response > 200:
                print("Please enter a number between 1-200");
            else:
                return response;
        except ValueError:
            print("Please enter a whole integer")



def findFactor(inputNumber):
    
    if inputNumber == 1:
        print("1 is unity")
        print("Factors: 1") 
        return;


    factor = []
    for i in range(1,inputNumber+1):
        if(inputNumber % i == 0):
            factor.append(i)


    if (len(factor) == 2):
        print(inputNumber,"is a prime number")
    elif ((len(factor) % 2 )> 0):
        print(inputNumber," is a perfect square number")

    print("Factors: ",factor)  
       
      
 
def mainroutine():
    inputNumber = number_check("Enter a integer to find out its factors: ");
    findFactor(inputNumber);



#Main routine starts here

print("**** Factorisation Calculator ****");

respond = input("Press <enter> to show the instructions or any key to continue")
if respond == "":
    print("Please enter an integer to discover its factors. Information about whether its a prime , perfect square or unity will be provided. You may do as many calculations as you wish.")


while True:
    mainroutine();

    response = input("Press enter to use Factorisation calculator again or other key to quit")
    if response != "":
        print("**** Thank you for using Factors Calculator ****")
        break;
      

    






 
















   










