import msvcrt

def getChar():
    entered = msvcrt.getch().decode('ASCII')
    return entered

def correspond(num, team1, team2, team3):
    if num == '1':
        print("\nBuzz: " + team1)
    if num == '2':
        print("\nBuzz: " + team2)
    if num == '3':
        print("\nBuzz: " + team3)
        
def gameProcess(team1,team2,team3):
    unanswered = ['1','2','3',' ']
    entered = '0'
    
    print("\nBUZZ NOW! (Press space if out of time)")
    
    while entered not in unanswered:
        entered = getChar()
    
    if entered == ' ':
        return
    
    correspond(entered, team1, team2, team3)
    unanswered.remove(entered)
                
    print("Click 'c' for correct, 'f' for incorrect")
        
    while entered not in ['c','f']:
        entered = getChar()
        
    print(entered)
    
    if entered == 'c':
        return
    if entered == 'f':
        
        
        print("\nBUZZ NOW! (Press space if out of time)")
        
        while entered not in unanswered:
            entered = getChar()
            
        if entered == ' ':
            return
        
        correspond(entered, team1, team2, team3)
        unanswered.remove(entered)
        
        print("Click 'c' for correct, 'f' for incorrect")
        
        while entered not in ['c','f']:
            entered = getChar()
            
        print(entered)
        
        if entered == 'c':
            return
        if entered == 'f':
            
            print("\nBUZZ NOW! (Press space if out of time)")
            
            while entered not in unanswered:
                entered = getChar()
            
            if entered == ' ':
                return

            correspond(entered, team1, team2, team3)


team1 = input("Enter team one name:\n")
team2 = input("Enter team two name:\n")
team3 = input("Enter team three name:\n")

while True:
    start = '0'
    print("\n===================================")
    print("Press Space to start buzzing period")
    
    while start != ' ':
        start = getChar()
        
    gameProcess(team1,team2,team3)
