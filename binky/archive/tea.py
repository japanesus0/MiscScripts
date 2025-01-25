#!/usr/bin/python3

from datetime import datetime
import re, pandas as pd

def getDRef():
    global dref
    cols=['id','drinkid','drink','vol','TPind','TTime']

    a=pd.read_csv(bevf, header=None, sep='|')

    dref=pd.DataFrame(a.to_numpy(), columns=cols)

    return(dref)

#def checkBrew(sel):
#    if sel[sel[:
#        bev=id.upper()
    #  print(bev)
#    else:
#        print("Invalid Reponse : " + id)
#        quit()

bevf="bev.dat"
bevtime=datetime.now()

getDRef()

print(dref)
dsel=input("\n\nPlease Make Selection: ")

print("Selection: " + dsel)

x=dref.loc[dref['id'] == '1']
print(x)

sel=dref[dref.drinkid.str.match(dsel)]

print("derps : " + sel)

#checkBrew(sel)
