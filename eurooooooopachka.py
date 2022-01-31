from module1 import*
from random import*

Capitals=dict()
Capitals["Estonia"]="Tallinn"
Capitals["Albania"]="Tirana"
Capitals["Belgium"]="Brussels"
Capitals["Czechia"]="Prague"
Capitals["Poland"]="Warsaw"
Capitals["Portugal"]="Lisbon"
Capitals["Finland"]="Helsinki"
Capitals["France"]="Paris"
Capitals["Germany"]="Berlin"
Capitals["Sweden"]="Stockholm"
Capitals["Spain"]="Madrid"
Capitals["Serbia"]="Belgrade"
Capitals["Norway"]="Oslo"
Capitals["Moldova"]="Chisinau"
Capitals["Greece"]="Athens"
Capitals["Bulgaria"]="Sofia"
Capitals["Austria"]="Vienna"
Capitals["Switzerland"]="Bern"
Countries=["Estonia","Albania","Belgium","Czechia","Poland","Portugal","Finland","France","Germany","Sweden","Spain","Serbia","Norway","Moldova","Greece","Bulgaria","Austria","Switzerland"]
for country in Countries:
 
    country=input("Enter the country: ")
    if country in Capitals:
        print("The capital of the country "+country+": " +Capitals[country])
    else:
        print("this country was not detected " +country)
        v=input("would you like to add this country " +country+ " to the dictionary?  ")
        if v=="yes":
            ca=input("enter the country " +country+": ")
            Capitals.update({country: ca})
            p=input("continue and add capital of the country? ")
            if p=="no":
                print("whatever")
            if p=="yes":
                o=input("enter country: ")
                l=input("enter capital: ")
                Capitals.pop(country)
                Capitals.update({o: l})
        if v=="no":
            print("whatever")
  
    p=input("Want to check your knowledge? ")
    if p=="yes":
        Countries.sort()
        Countries.reverse()
        m=0
        for i in range(10):
            country=str(choice(Countries))
            print(country)
            st=input("enter the capital: ")
            if st==Capitals[country]:
                print("correct")
                m+=1
            else:
                print("wrong :( !")
        if m==0:
            print("0%")
        elif m==1:
            print("10%")
        elif m==2:
            print("20%")
        elif m==3:
            print("30%")
        elif m==4:
            print("40%")
        elif m==5:
            print("50%")
        elif m==6:
            print("60%")
        elif m==7:
            print("70%")
        elif m==8:
            print("80%")
        elif m==9:
            print("90%")
        elif m==10:
            print("100%")
    if p=="No":
        print("Bye!")
