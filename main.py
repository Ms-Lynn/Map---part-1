###############################################################################
# Title: Simple Text Adventure Game
# coder: Ms. Lynn
# version: 001
###############################################################################
''' Program creates a simple map using nested lists that a character
    can move around on through a simple menu.'''
#------------------------------------------------------------------------------
# Current Location
row = 0     # explain row here              
col = 0
max_row = 3
max_col = 2

playing = True

# explain map
map = [
     ["Start", "EmptySpace", "SpookySpace"],
     ["EmptySpace", "EmptySpace", "EmptySpace"],
     ["SpookySpace", "Treasure", "EmptySpace"],
     ["EmptySpace", "EmptySpace", "Key"]
 ]

# Functions -------------------------------------------------------------------
def Movement():
    global row, col, max_row, max_col, playing
    while True:
        print(f"Choose a direction: ")
        if not row==0:
            print(f"-North")
        if not row==max_row:
            print(f"-South")
        if not col==max_col:
            print(f"-East")
        if not col==0:
            print(f"-West")
        dirchoice = input(f"Choice: ")
        if dirchoice == "North" and row > 0:
            row -= 1
            break
        elif dirchoice == "South" and row < max_row:
            row += 1
            break
        elif dirchoice == "East" and col < max_col:
            col += 1
            break
        elif dirchoice == "West" and col > 0:
            col -= 1
            break
        elif dirchoice == "Quit":
            playing = False
            break
        else:
            print(f"Sorry you can not move that direction.")


# Main Code --------------------------------------------------------------------
while playing:
    location_description =  map[row][col]
    if location_description == "Start":
        print(f"Welcome to my Castle!")
        print(f"Please tour around, and when your ready to leave type 'Quit'.")
        Movement()
    elif location_description == "EmptySpace":
        print(f"Nothing is in this room.")
        Movement()
    elif location_description == "SpookySpace":
        print(f"This room is very spooky, you better leave quickly!")
        Movement()
    elif location_description == "Treasure":
        print(f"There is a giant treasure chest in the middle of the room!")
        Movement()
    elif location_description == "Key":
        print(f"There is a key hanging on the wall!")
        Movement()
print(f"Thanks for playing!!!!")