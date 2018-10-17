#    1       2        3
#[kitchen,bathroom,bedroom]
#[garden area,hall,playing room]
#    4       5        6
roomnames={1:'kitchen',2:'bathroom',3:'bedroom',4:'gardenarea',5:'hall',6:'playing room'}
userinput=input("Select any random number from 1 to 6\n")
userinput=int(userinput)
print("You are in ",roomnames[userinput])
while True:
    userdirection=input("Choose any direction LRUD\n")
    if(userdirection!='L' and userdirection!='R' and userdirection!='U' and userdirection!='D'):
        userdirection=input("Please select the right direction(LRUD)")
        
    decision=input("Would you like to continue(Y/N)\n")
    if(decision!='N' and decision!='n' and decision!='Y' and decision!='y'):
        decision=input("Please make a proper decision(Select either Y OR N)")
    if(decision=='N' or decision=='n'):
        break
    elif(decision=='Y' or decision=='y'):
      if(userdirection=='L'):
        if(userinput==1):
            print("You can't move in this direction\n")
            continue
        if(userinput==2):
            print("You are in kitchen\n")
            userinput=userinput-1
            continue
        if(userinput==3):
            print("You are in bathroom\n")
            userinput=userinput-1
            continue
        if(userinput==4):
            print("You can't move in this direction\n")
            continue
        if(userinput==5):
            print("You are in garden area\n")
            userinput=userinput-1
            continue
        if(userinput==6):
            print("You are in hall\n")
            userinput=userinput-1
            continue
        
      if(userdirection=='R'):
        if(userinput==1):
            print("You are in bathroom\n")
            userinput=userinput+1
            continue
        if(userinput==2):
            print("You are in bedroom\n")
            userinput=userinput+1
            continue
        if(userinput==3):
            print("You can't move in this direction\n")
            continue
        if(userinput==4):
            print("You are in hall\n")
            userinput=userinput+1
            continue
        if(userinput==5):
            print("You are in playing room\n")
            userinput=userinput+1
            continue
        if(userinput==6):
            print("You can't move in this direction\n")
            continue
        
      if(userdirection=='U'):
        if(userinput==1):
            print("You can't move in this direction\n")
            continue
        if(userinput==2):
            print("You can't move in this direction\n")
            continue
        if(userinput==3):
            print("You can't move in this direction\n")
            continue
        if(userinput==4):
            print("You are in kitchen\n")
            userinput=userinput-3
            continue
            
        if(userinput==5):
            print("You are in bathroom\n")
            userinput=userinput-3
            continue
            
        if(userinput==6):
            print("You are in bedroom\n")
            userinput=userinput-3
            continue
            
      if(userdirection=='D'):  
        if(userinput==1):
            print("You are in gardenarea\n")
            userinput=userinput+3
            continue
        if(userinput==2):
            print("You are in hall\n")
            userinput=userinput+3
            continue
        if(userinput==3):
            print("You are in playing room\n")
            userinput=userinput+3
            continue
        if(userinput==4):
            print("You can't move in this direction\n")
            continue
        if(userinput==5):
            print("You can't move in this direction\n")
            continue
        if(userinput==6):
            print("You can't move in this direction\n")
            continue
    
    
    
print("User no longer wants to continue")    
    
    
