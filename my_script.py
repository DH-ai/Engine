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
    if (up[0][0:-1] == "island" or down[0][0:-1] == "island") and (left[0][0:-1] == "island" or right[0][0:-1] == "island"):
        if up[0][0:-1] == "island":
            move = 1
        elif down[0][0:-1] == "island":
            move=3
        elif left[0][0:-1] == "island":
            move = 4
        elif right[0][0:-1] == "island":
            move = 2
        
        
        
        
        return (True,move)
    else:
        return (False,move)
    


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
    
    pirate.setTeamSignal(f"{pirate.getID()}")

    rum = pirate.getTotalRum()
    Wood = pirate.getTotalWood()
    Gunpowder = pirate.getTotalGunpowder()
    

    minResource = min(rum,Wood,Gunpowder)
    
    states = pirate.trackPlayers()
    # here we will check for island 
    # print(checkIsland(pirate)) 
    # 1. checking for island 
  
    avail, move = checkIsland (pirate)
    if avail and ((not ("myCaptured" in states) ) or (("oppCapturing" in states) or ("oppCaptured" in states))):
        print(states)
        pirate.setT
            
        return move
    
    # 2. if  not captured then go there 
    # 3. that pirate will stay there forever
    # 4. another pirate come see captured will go away if opp is not capturing 
    # 5. that pirate try to kill opponent 
    # 6. leave 
    # 7. randomly exploring pirate got signal opp capturing even no. of pirates goes there to kill enem pirates
    # 8. Leave 
    # 9. complete this logic will help in further controling the randomness of pirates
        
    
    
    if (current [0][0:-1] == "island"):
        s= pirate.getID() + "Captured"
        pirate.setSignal(s)
        
        return 0

    resources=False
    
    
    
    
    # avoiding enemy pirates 
    

    if Gunpowder>=100:
         
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