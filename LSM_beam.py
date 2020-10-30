from tkinter import *
import pandas as pd
import datetime
import math

def getvals():
    print(f"The value of clear span is {uservalue1.get()}")
    print(f"The value of UDL is {uservalue2.get()}")
    print(f"The value of concrete strength is {uservalue3.get()}")
    print(f"The value of steel strength is {uservalue4.get()}")
    print(f"Thickness of wall is {uservalue5.get()}")
    print(f"The value of required breadth is {uservalue6.get()}")
    print(f"The value of thickness of effective cover is {uservalue7.get()}")
    print(f"Diameter of steel bar is {uservalue8.get()}")
    print(f"Diameter of stirrups bar is {uservalue9.get()}")
    print(f"Wellcome {uservalue10.get()}")
    user11 = Label(root, text="Values taken and the result is saved in LSM.txt file").grid(row=17, column=2)

    
        
root = Tk()
root.wm_iconbitmap('ib.ico')
root.geometry("655x333")
root.title("RCC Beam desgning using LSM")
# label*****************************************************************************
user0 = Label(root, text="")
user1 = Label(root, text="Length of clear span in mm", justify='left')
user2 = Label(root, text="Value of UDL in KN/m", justify='left')
user3 = Label(root, text="Value of concrete strength in MPa", justify='left')
user4 = Label(root, text="Value of steel strengthin MPa", justify='left')
user5 = Label(root, text="Thickness of wall in mm", justify='left')
user6 = Label(root, text="Required breadth of the beam in mm", justify='left')
user7 = Label(root, text="Effective cover in mm", justify='left')
user8 = Label(root, text="Diameter of steel bar in mm", justify='left')
user9 = Label(root, text="Diameter of stirrups bar in mm", justify='left')
user10 = Label(root, text="Your Name")
user12 = Label(root, text="This program is created by Debayan Ghosh.", justify='left')
user1.grid(row=0, column=0)
user2.grid(row=1, column=0)
user3.grid(row=2, column=0)
user4.grid(row=3, column=0)
user5.grid(row=4, column=0)
user6.grid(row=5, column=0)
user7.grid(row=6, column=0)
user8.grid(row=7, column=0)
user9.grid(row=8, column=0)
user10.grid(row=9, column=0)
user12.grid(row=17, column=0)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
# bar********************************************************************************
uservalue1 = DoubleVar()
uservalue2 = DoubleVar()
uservalue3 = DoubleVar()
uservalue4 = DoubleVar()
uservalue5 = DoubleVar()
uservalue6 = DoubleVar()
uservalue7 = DoubleVar()
uservalue8 = DoubleVar()
uservalue9 = DoubleVar()
uservalue10 = StringVar()

userentry1 = Entry(root, textvariable=uservalue1)
userentry2 = Entry(root, textvariable=uservalue2)
userentry3 = Entry(root, textvariable=uservalue3)
userentry4 = Entry(root, textvariable=uservalue4)
userentry5 = Entry(root, textvariable=uservalue5)
userentry6 = Entry(root, textvariable=uservalue6)
userentry7 = Entry(root, textvariable=uservalue7)
userentry8 = Entry(root, textvariable=uservalue8)
userentry9 = Entry(root, textvariable=uservalue9)
userentry10 = Entry(root, textvariable=uservalue10)

userentry1.grid(row=0, column=1)
userentry2.grid(row=1, column=1)
userentry3.grid(row=2, column=1)
userentry4.grid(row=3, column=1)
userentry5.grid(row=4, column=1)
userentry6.grid(row=5, column=1)
userentry7.grid(row=6, column=1)
userentry8.grid(row=7, column=1)
userentry9.grid(row=8, column=1)
userentry10.grid(row=9, column=1)

Button(text="Submit", command=getvals).grid(row=14, column=1)
l = Label(root)
l.grid(row=15, column=0)
var1 = StringVar()
var2 = StringVar()
c1 = Checkbutton(root, text='Detailed Solution',variable=var1, onvalue='1', offvalue='0')
c1.grid(row=10, column=1)
c2 = Checkbutton(root, text='gist solution',variable=var2, onvalue='1', offvalue='0')
c2.grid(row=11, column=1)
tick1 = var1.get()
tick2 = var2.get()

root.mainloop()


clearSpan = uservalue1.get()
udl = uservalue2.get()
Fck = uservalue3.get()
Fy = uservalue4.get()
bearing = uservalue5.get()
breadth = uservalue6.get()
effCov = uservalue7.get()
barDia = uservalue8.get()
stiDia = uservalue9.get()
Name = uservalue10.get()

#*************************************************************************************************************


#for LSM span  / 15 = d
effDep = clearSpan / 15
toDep = effDep + effCov
toDep
selWtBeam = breadth * toDep * 25 / 10**6 # unit wt of conc 25 kn/m^3
toUDL = selWtBeam + udl
ultUDL = 1.5 * toUDL # for LSW Ultimate Load = 1.5 * Total load
ultUDL

#Calculation of effective span
effSp1 = clearSpan + effDep
effSp2 = clearSpan + bearing
#Lowest value will be the length of effective span
if effSp1 <= effSp2:
    effSp = effSp1/1000
else:
    effSp = effSp2/1000
effSp


#Shear force and Bending moment Calculation
Mu = ultUDL * effSp**2 / 8
SF = ultUDL * effSp / 2
SF

#Req depth caculation fro FE415 steel.
depReq = (Mu*10**6/0.138/Fck/breadth)**(1/2)
depReq
Mulim = 0.138 * Fck *  breadth/100 * (effDep/100)**2
Mulim

if (effDep >= depReq and Mu <= Mulim):
    print("Under Reinforced Section")

#Calculation of area of steel
Ast = (0.5 * Fck / Fy) * (1 - (1 - (4.6*Mu*10**6/(Fck * breadth * effDep**2)))**(1/2)) * breadth * effDep
Ast


#using bar dia meter 20phi


ast = math.pi * barDia**2 / 4
ast
noOfBar = Ast / ast
noOfBarFinal = math.ceil(noOfBar)
noOfBarFinal

#actual steel areas
actAst = noOfBarFinal * ast

#min of Ast
minAst = 0.85 * breadth * effDep / Fy

#max of Ast
maxAst = 0.04 * breadth * toDep

#steel area checking
if (actAst < maxAst and actAst > minAst ):
    print("Steel area is ok.")


#Shear reinforced
#Nominal Shear Stress
Vu = SF
nss = Vu * 10**3 / (breadth * effDep)
nss
# % of tension reinforcement
p = actAst * 100 / (breadth * effDep)
p

### table19 value extraction

df = pd.read_csv('table19.csv')
df
#import matplotlib.pyplot as plt
#plt.plot(df.p, df.M15, 'b.-')
#plt.show()

a = []
m = []
i = 0
a = df['p']
if Fck == 15:
    m = df['M15']
elif Fck == 20:
    m = df['M20']
elif Fck == 25:
    m = df['M25']
elif Fck == 30:
    m = df['M30']
elif Fck == 35:
    m = df['M35']
elif Fck == 40:
    m = df['M40']

while (p >= a[i]):
    q = i
    i = i + 1
else:
    print(q)

a[q + 1]
var1 = (p - a[q]) * (m[q + 1] - m[q])
taoC = m[q] + (var1 / (a[q + 1] - a[q]))
taoC

#algorithm for table 19 is456:2000 for calcuation design shear strength
#Interpolation method
#taoC = 0.5685
if nss>taoC:
    print("we need to provide vertical strups")

#Shear resistance by the concrete
Vuc = taoC * breadth * effDep / 10**3
Vuc
#sherups carried by stirrups
Vus = Vu - Vuc
Vus


#stirrups 2LVS 8mm phi bar

stiAsv = math.pi * stiDia**2 * 2 / 4
stiAsv

#spacing  Vus = 0.87 * Fy * Asv * effDep / Sv
Sv1 = 0.87 * Fy * stiAsv * effDep / Vus / 10**3
Sv2 = stiAsv *0.87 *Fy / 0.4 / breadth
Sv2
Sv3 = 0.75 * effDep
Sv3
# checkign for spacing
print(Sv1,Sv2,Sv3)
print("provide 8mm phi 2LVS @ 300 mm c/c")




#Result Output
'''
print("The length of clear span:  ",clearSpan)
print("Effective clear cover:",effCov)
print("Total Depth of the beam(with clear cover):",toDep)
print("Total Breadth of the beam",breadth)
print("concrete M",Fck)
print("Steel Fe",Fy)
print("Self weight of the beam",selWtBeam)
print("Total uniformly distributed load on the beam including self wt. is ",toUDL)
print("Ultimate UDL after applyiny safety factor 1.5 is",ultUDL)
print("The effective length of the beam",effSp)
print("Beading moment on the both end of the beam",Mu)
print("Shear Force of the beam",SF)

print("Now depth checking.")
print("Required depth of the beam",depReq)
print("Provided depth of the beam",effDep)
print("so...")

print("Maximum moment can be taken by the beam",Mulim)
print("Bendign moment generate ",Mu)
print("so ..")

print("Area of the steel required",Ast)
print("Provide", noOfBarFinal," - " ,barDia   , "mm phi @ tension side.")
print("So, the area of the steel will be",actAst)
print("Minimum and Maximum steel required in tension side",minAst,"and",maxAst)
print("so..")

print("Nominal shear stress",nss)
print("Persentage of nominal reinforcement",p)
print("From IS456:2000 tablw 19 critical shear will be",taoC)
print("As the critical shear is less than nominal shear so, we will provide vertical stirrups.")
print("Shear resistance of concrete",Vuc)
print("Shear carried by the stirrups",Vus)
print("Some spacing values for providing stirrups",Sv1,Sv2,Sv3)
print("So, provide ", stiDia ," mm phi 2LVS @ 300mm c/c.")

'''




#File Input

if (tick1 == '1') & (tick2 == '0'):
    f = open("LSW.txt", "a")
    dt = datetime.datetime.today()
    f.write("\nWelcome %ls"%Name)
    f.write(" %ls" % dt)
    f.write("\nThe length of clear span: %d "%clearSpan)
    f.write(" mm.")
    f.write("\nEffective clear cover:%d "%effCov)
    f.write(" mm.")
    f.write("\nTotal Depth of the beam(with clear cover):%d "%toDep)
    f.write(" mm.")
    f.write("\nTotal Breadth of the beam %d "%breadth)
    f.write(" mm.")
    f.write("\nconcrete M%d "%Fck)
    f.write("\nSteel Fe%d "%Fy)
    f.write("\nSelf weight of the beam %d "%selWtBeam)
    f.write(" KN.")
    f.write("\nTotal uniformly distributed load on the beam including self wt. is %d "%toUDL)
    f.write(" KN/m.")
    f.write("\nUltimate UDL after applyiny safety factor 1.5 is %d "%ultUDL)
    f.write(" KN/m.")
    f.write("\nThe effective length of the beam %d "%effSp)
    f.write(" mm.")
    f.write("\nBeading moment on the both end of the beam %d "%Mu)
    f.write(" KN-m.")
    f.write("\nShear Force of the beam %d "%SF)
    f.write(" KN.")

    f.write("\nNow depth checking.")
    f.write("\nRequired depth of the beam %d "%depReq)
    f.write(" mm.")
    f.write("\nProvided depth of the beam %d "%effDep)
    f.write(" mm.")
    f.write("\nso...")

    f.write("\nMaximum moment can be taken by the beam %d "%Mulim)
    f.write(" KN/m.")
    f.write("\nBendign moment generate %d "%Mu)
    f.write(" KN/m.")
    f.write("\nso ..")

    f.write("\nArea of the steel required %d "%Ast)
    f.write(" mm^2.")

    f.write("\nProvide " )
    f.write("%d " %noOfBarFinal )
    f.write(" - ")
    f.write("%d"%barDia)
    f.write("mm phi @ tension side.")

    f.write("\nSo, the area of the steel will be %d "%actAst)
    f.write(" mm^2.")

    f.write("\nMinimum and Maximum steel required in tension side ")
    f.write("%d" %minAst)
    f.write(" mm^2.")
    f.write("and %d "%maxAst)
    f.write(" mm^2.")


    f.write("\nso..")


    f.write("\nNominal shear stress %d "%nss)
    f.write(" KN.")
    f.write("\nPersentage of nominal reinforcement %d "%p)
    f.write("\nFrom IS456:2000 tablw 19 critical shear will be %d "%taoC)
    f.write(" KN.")
    f.write("\nAs the critical shear is less than nominal shear so, we will provide vertical stirrups.")
    f.write("\nShear resistance of concrete %d "%Vuc)
    f.write(" KN.")
    f.write("\nShear carried by the stirrups %d "%Vus)
    f.write(" KN.")

    f.write("\nSome spacing values for providing stirrups (in mm)%ls, "%Sv1)
    f.write(" %ls, "%Sv2 )
    f.write(" %ls " %Sv3)

    f.write("\nSo, provide ")
    f.write("%d" %stiDia)
    f.write(" mm phi 2LVS @ 300mm c/c.")
    f.write("\n")
    f.write("\n")
    f.close()
elif (tick1 == 0) & (tick2 == 1):
    f = open("LSW_summary.txt", "a")
    dt = datetime.datetime.today()
    f.write("\nWelcome %ls"%Name)
    f.write("\nRequired depth of the beam %d "%depReq)
    f.write(" mm.")
    
    f.write("\nProvided depth of the beam %d "%effDep)
    f.write(" mm.")
        
    f.write("\nProvide " )
    f.write("%d " %noOfBarFinal )
    f.write(" - ")
    f.write("%d"%barDia)
    f.write("mm phi @ tension side.")

    f.write("\nSo, provide ")
    f.write("%d" %stiDia)
    f.write(" mm phi 2LVS @ 300mm c/c.")
 
    f.write("\nMaximum moment can be taken by the beam %d "%Mulim)
    f.write(" KN/m.")
    f.write("\n")
    f.close()
elif (tick1 == 0) & (tick2 == 0):
    l.config(text='please tick any options.')
else:
    f = open("LSW_summary.txt", "a")
    dt = datetime.datetime.today()
    f.write("\nWelcome %ls"%Name)
    f.write(" %ls" % dt)
    f.write("\nRequired depth of the beam %d "%depReq)
    f.write(" mm.")
    
    f.write("\nProvided depth of the beam %d "%effDep)
    f.write(" mm.")
    f.write("\nProvide " )
    f.write("%d " %noOfBarFinal )
    f.write(" - ")
    f.write("mm phi @ tension side.")

    f.write("\nSo, provide ")
    f.write("%d" %stiDia)
    f.write(" mm phi 2LVS @ 300mm c/c.")

        
    f.write("\nMaximum moment can be taken by the beam %d "%Mulim)
    f.write(" KN/m.")
    f.write("\n")
    f.close()


    f = open("LSW.txt", "a")
    dt = datetime.datetime.today()
    f.write("\nWelcome %ls"%Name)
    f.write(" %ls" % dt)
    f.write("\nThe length of clear span: %d "%clearSpan)
    f.write(" mm.")
    f.write("\nEffective clear cover:%d "%effCov)
    f.write(" mm.")
    f.write("\nTotal Depth of the beam(with clear cover):%d "%toDep)
    f.write(" mm.")
    f.write("\nTotal Breadth of the beam %d "%breadth)
    f.write(" mm.")
    f.write("\nconcrete M%d "%Fck)
    f.write("\nSteel Fe%d "%Fy)
    f.write("\nSelf weight of the beam %d "%selWtBeam)
    f.write(" KN.")
    f.write("\nTotal uniformly distributed load on the beam including self wt. is %d "%toUDL)
    f.write(" KN/m.")
    f.write("\nUltimate UDL after applyiny safety factor 1.5 is %d "%ultUDL)
    f.write(" KN/m.")
    f.write("\nThe effective length of the beam %d "%effSp)
    f.write(" mm.")
    f.write("\nBeading moment on the both end of the beam %d "%Mu)
    f.write(" KN-m.")
    f.write("\nShear Force of the beam %d "%SF)
    f.write(" KN.")

    f.write("\nNow depth checking.")
    f.write("\nRequired depth of the beam %d "%depReq)
    f.write(" mm.")
    f.write("\nProvided depth of the beam %d "%effDep)
    f.write(" mm.")
    f.write("\nso...")

    f.write("\nMaximum moment can be taken by the beam %d "%Mulim)
    f.write(" KN/m.")
    f.write("\nBendign moment generate %d "%Mu)
    f.write(" KN/m.")
    f.write("\nso ..")

    f.write("\nArea of the steel required %d "%Ast)
    f.write(" mm^2.")

    f.write("\nProvide " )
    f.write("%d " %noOfBarFinal )
    f.write(" - ")
    f.write("%d"%barDia)
    f.write("mm phi @ tension side.")

    f.write("\nSo, the area of the steel will be %d "%actAst)
    f.write(" mm^2.")

    f.write("\nMinimum and Maximum steel required in tension side ")
    f.write("%d" %minAst)
    f.write(" mm^2.")
    f.write("and %d "%maxAst)
    f.write(" mm^2.")


    f.write("\nso..")


    f.write("\nNominal shear stress %d "%nss)
    f.write(" KN.")
    f.write("\nPersentage of nominal reinforcement %d "%p)
    f.write("\nFrom IS456:2000 tablw 19 critical shear will be %d "%taoC)
    f.write(" KN.")
    f.write("\nAs the critical shear is less than nominal shear so, we will provide vertical stirrups.")
    f.write("\nShear resistance of concrete %d "%Vuc)
    f.write(" KN.")
    f.write("\nShear carried by the stirrups %d "%Vus)
    f.write(" KN.")

    f.write("\nSome spacing values for providing stirrups (in mm)%ls, "%Sv1)
    f.write(" %ls, "%Sv2 )
    f.write(" %ls " %Sv3)

    f.write("\nSo, provide ")
    f.write("%d" %stiDia)
    f.write(" mm phi 2LVS @ 300mm c/c.")
    f.write("\n")
    f.write("\n")
    f.close()
  


