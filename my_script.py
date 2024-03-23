import random
import math

name = "snek"



def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
def moveResource(minResource,pirate):
    top  = pirate.investigate_up()
    ne = pirate.investigate_ne()
    right = pirate.investigate_right()
    se = pirate.investigate_se()
    down = pirate.investigate_down()
    sw = pirate.investigate_sw()
    left = pirate.investigate_left()
    nw = pirate.investigate_nw()

    # if top

def checkIsland(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    move = -1
    islandID = None
    if (up[0][0:-1] == "island" or down[0][0:-1] == "island") and (left[0][0:-1] == "island" or right[0][0:-1] == "island"):
        if up[0][0:-1] == "island":
            islandID = up[0][-1]
            move = 1
        elif down[0][0:-1] == "island":
            islandID = down[0][-1]

            move=3
        elif left[0][0:-1] == "island":
            islandID = left[0][-1]

            move = 4
        elif right[0][0:-1] == "island":
            islandID = right[0][-1]

            move = 2
        

            
        
        
        return (True,move,islandID)
    else:
        return (False,move,islandID)
    


def ActPirate(pirate):
    x,y = pirate.getPosition()
   

    
    current= pirate.investigate_current()
    up  = pirate.investigate_up()
    ne = pirate.investigate_ne()
    right = pirate.investigate_right()
    se = pirate.investigate_se()
    down = pirate.investigate_down()
    sw = pirate.investigate_sw()
    left = pirate.investigate_left()
    nw = pirate.investigate_nw()
    
    # pirate.setTeamSignal(f"{pirate.getID()}")

    rum = pirate.getTotalRum()
    Wood = pirate.getTotalWood()
    Gunpowder = pirate.getTotalGunpowder()
    

    minResource = min(rum,Wood,Gunpowder)
    
    states = pirate.trackPlayers()
    # here we will check for island 

    # 1. checking for island 
    # 2. if  not captured then go there 
    sig =pirate.getTeamSignal()
    avail, move, islandID = checkIsland (pirate)
    # 4. another pirate come see captured will go away if opp is not capturing 
    if (
        (islandID=="1" and states[0]=="myCaptured") or 
        (islandID=="2" and states[1]=="myCaptured") or 
        (islandID=="3" and states[2]=="myCaptured")
    ):
        #then move along
        if current[0][0:-1] =="island":
                # 3. that pirate will stay there forever
                return 0 
     
    else  :
        if (avail):
            # if (islandID=="1"):
            #     sig=sig+f" 1:({x},{y}) "
            # elif (islandID=="2"):
            #     sig=sig+f" 2:({x},{y}) "
            # else:
            #     sig=sig+f" 3:({x},{y}) "

            
            
            _move = move
            
            if current[0][0:-1] =="island":
                # 3. that pirate will stay there forever
                _move = 0
            # pirate.setTeamSignal(sig)
            return _move
    # print(pirate.getTeamSignal())
    # if int(pirate.getID())%4==0:
    #     sig = pirate.getTeamSignal()
    #     if (states[3]=="oppCapturing"):  
    #         x=0
    #         y=0
    #         for i in range(len(sig)):
    #             if sig != "":
                     
    #                 if sig[i]=="(":
    #                     x= x*10+ int(sig[i+1]) 
    #                     y = y*10+int(sig[i+4])
    #                     break
    #         moveTo(x,y,pirate)
    #     elif (states[4]=="oppCapturing"):
    #         x=0
    #         y=0
    #         for i in range(len(sig)):
    #             if sig != "":
                        
    #                 if sig[i]=="2":
    #                     x= int(sig[i+2]) 
    #                     y = int(sig[i+4])
    #                     break
    #         moveTo(x,y,pirate)
    #     elif (states[5]=="oppCapturing"):
    #         x=0
    #         y=0
    #         for i in range(len(sig)):
    #             if sig != "":
                        
    #                 if sig[i]=="3":
    #                     x= int(sig[i+2]) 
    #                     y = int(sig[i+4])
    #                     break
    #         moveTo(x,y,pirate)    
     


    
    
    
   

    
    
    
    # avoiding enemy pirates 
    
    # 1/3 of pirates are going to chase 

    if int(pirate.getID())%3==0:

        if up[1]=="enemy":
            return 1
        elif right[1] =="enemy":
            return 2
        elif left[1]=="enemy":
            return 4
        elif down[1]=="enemy":
            return 3
    else:
        if up[1]=="enemy":
            return 3
        elif right[1] =="enemy":
            return 4
        elif left[1]=="enemy":
            return 2
        elif down[1]=="enemy":
            

            
            return 1

    move  = random.randint(1,4) # for blank movements 
    if pirate.getSignal()!='':
                
        if move == 1 and int(pirate.getSignal()) ==3 :
                move = random.randint(2,4)
        elif move ==3  and int(pirate.getSignal()) ==1:
                move = 4 if random.randint(1,2)==2 else random.randint(1,2)
        elif move ==2  and int(pirate.getSignal()) ==4:
                move = 1 if random.randint(1,2)==2 else random.randint(3,4)
        elif move ==4  and int(pirate.getSignal()) ==2:
                move = random.randint(1,3)
    pirate.setSignal(f"{move}")
              
    return move






def ActTeam(team):


    
    # if team.getSignal
    s=team.getTeamSignal()

    # print(s)
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)