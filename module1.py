from random import*
from gtts import gTTS
import os
def sonastik():
        sonastik={}
        countries=[]
        capitals=[]
        file=open("countries.txt","r")
        for line in file:
            k, v=line.strip().split("-")
            sonastik[k.strip()]=v.strip()
            countries.append(k)
            capitals.append(sonastik[k.strip()])
        file.close()
        print(sonastik)
        print("countries: ")
        print(countries)
        print("capitals:")
        print(capitals)
        s=gTTS(text=capitals[6],lang="en",slow=True).save("countries.mp3")
        os.system("countries.mp3")
        a=input()
def country ():
	countries=input("Введите страну - ")
	capitals=input("Введите столицу - ")
	with open("countries.txt", "a") as countries:
		countries.write(country+"\n")
	with open("capitals.txt", "a") as capitals: 
		capitals.write(capital+"\n")

