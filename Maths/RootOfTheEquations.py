"""
    This file will gives you the root of the equation which you entered
"""
import Maths.exfunc as ef
import Maths.Bisection as b
import Maths.RegulaFalsi as rf
import Maths.NewtonRapson as nr
import Maths.Secant as s
import Maths.functions as f

print()
print()

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("X                                                                                                                                                 X")
print("X    :::::                     :::::  ::::::::::::  :::::         ::::::::::::   ::::::::::::::         :::::       :::::         ::::::::::::    X")
print("X     :::::                   :::::   ::::::::::::  :::::         ::::::::::::   ::::::::::::::        :::::::     :::::::        ::::::::::::    X")
print("X      :::::      :::::      :::::    ::::          :::::         :::::          ::::      ::::       :::::::::   :::::::::       ::::            X")
print("X       :::::    :::::::    :::::     ::::::::::::  :::::         :::::          ::::      ::::      :::::  :::::::::  :::::      ::::::::::::    X")
print("X        :::::  :::::::::  :::::      ::::::::::::  :::::         :::::          ::::      ::::     :::::    :::::::    :::::     ::::::::::::    X")
print("X         :::::::::   :::::::::       ::::          :::::         :::::          ::::      ::::    :::::      :::::      :::::    ::::            X")
print("X          :::::::     :::::::        ::::::::::::  ::::::::::::  ::::::::::::   ::::::::::::::   :::::                   :::::   ::::::::::::    X")
print("X           :::::       :::::         ::::::::::::  ::::::::::::  ::::::::::::   ::::::::::::::  :::::                     :::::  ::::::::::::    X")
print("X                                                                                                                                                 X")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print()
print("                                                            Root Of the equations welcomes you                                                     ")
flag=0
while(1):
    print("_________________________________________________________________________________________________________________________________________________________")
    print()
    print()
    print("1. Find the root")
    print("2. Help")
    print("3. About")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if ef.isInteger(choice)==1:
        choice=int(choice)

        #If Choice==1
        
        if choice==1:
            flag=0
            while(1):
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print()
                print()
                print("Choose Method: ")
                print("1. Bisection")
                print("2. Regula Falsi(False Position)")
                print("3. Newton-Rapson")
                print("4. Scecant")
                print("5. Back")
                choice=input("Enter your choice: ")
                if ef.isInteger(choice)==1:
                    choice=int(choice)
                    if choice==1:
                        #Bisection
                        b.evaluate()
                        
                    elif choice==2:
                        #Regula Flasi
                        rf.evaluate()
                        
                    elif choice==3:
                        #Newton-Rapson
                        nr.evaluate()
                        
                    elif choice==4:
                        #Scecant
                        s.evaluate()

                    elif choice==5:
                        #Break the loop
                        break
                    else:
                        print("Please Enter Valid Number")
                else:
                    print("Charecter Is Not Valid Please Enter a Number.")

        # If Choice==2
        
        elif choice==2:
            import Maths.help

        # If Choice==3
        
        elif choice==3:
            import Maths.about

        # If Choice==4
        
        elif choice==4:
            print()
            print("__________________________________________________________________________________________________________________________________________________________________")
            print()
            print("                                                                        Thank you for visiting                                                                    ")
            print()
            break

        # else
        
        else:
            print("Pease Enter Valid Number.")
    else:
        print("Charecter Is Not Valid Please Enter a Number.")
