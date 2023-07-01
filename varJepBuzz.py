import msvcrt

def getChar():
    entered = msvcrt.getch().decode('ASCII')
    return entered
        
def gameProcess(teamList):
    unanswered = [' ']
    for i in range(len(teamList)):
        unanswered.append(str(i+1))
        
    entered = '0'
    
    for _ in teamList:
        
        print("\nBUZZ NOW! (Press space if out of time)")
        
        while entered not in unanswered:
            entered = getChar()
        
        if entered == ' ':
            return
        
        print("\nBuzz: " + teamList[int(entered)-1])
        
        unanswered.remove(entered)
                    
        print("Click 'c' for correct, 'f' for incorrect")
            
        while entered not in ['c','f']:
            entered = getChar()
            
        print(entered)
        
        if entered == 'c':
            return
        if entered == 'f':
            continue


numTeam = 10
teamList = []
while (numTeam > 9 or numTeam <= 0):
    numTeam = int(input("How many teams are playing? (Up to 9)\n"))

for i in range(numTeam):
    teamList.append(input("Enter team " + str(i+1) + " name:\n"))


while True:
    start = '0'
    print("\n===================================")
    print("Press Space to start buzzing period")
    
    while start != ' ':
        start = getChar()
        
    gameProcess(teamList)
