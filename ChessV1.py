# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:39:00 2020

@author: Momin Hamdani
"""
turn = 1





#TO DO LIST
# Check mate
# Refining MovePiece command
# Move list
# TOLOWER









#Row = Position in list 'board'
#column = Position inside the nested list.


#   8x8 2D Chess board, list of lists, 
#   Board written in perspective of black so indexing stays true to real chess notation
#   EX: Board[row][column]='piece'
#   EX: board[1][1]
#   "wR"



board =  [["wR" ,  "wKn" ,"wBi" , "wQ" , "wK" , "wBi", "wKn" ,"wR"],
          ["wP" ,  "wP" , "wP" ,  "wP" , "wP" , "wP" , "wP" , "wP" ],
          ["--"  ,  "--" ,  "--" ,   "--" ,  "--" ,  "--" ,  "--" ,  "--" ], 
          ["--"  ,  "--" ,  "--" ,   "--" ,  "--" ,  "--" ,  "--" ,  "--" ], 
          ["--"  ,  "--" ,  "--" ,   "--" ,  "--" ,  "--" ,  "--" ,  "--" ], 
          ["--"  ,  "--" ,  "--" ,   "--" ,  "--" ,  "--" ,  "--" ,  "--" ], 
          ["bP"  , "bP" , "bP"  , "bP" , "bP" , "bP" ,  "bP" ,"bP"],
          ["bR" , "bKn" , "bBi" , "bQ" , "bK" , "bBi" , "bKn","bR"]]


print('')
print('Basic Chess Engine')




        
        
#If you want to use accurate numbers for rows and columns, you always count 1-8
#with white's pieces starting at row 1 and making it up to blacks pieces at 
#row 8 

#In order to fix this we first print each object in each list on 1 row for blacks
#view of the current board

#Then we reverse it for white to show it from white's perspective while maintaing 
#proper numbering 




Nothing = 123123123
#This is a third condition

LMC = []


#Tracking Rook and Kings of each color for castling






WLRM = 0 
WRRM = 0  
WKM = 0
BLRM = 0
BRRM = 0
BKM = 0






#FUNCTIONS






    
    
    


def showblackboard():
    '''
    This is to see the current state of the board.
    

    Returns each row of the chess board at it's current state
   
    '''
    
    for r in board:
       print(' '.join(r)) 
       
       
       
def showwhiteboard():
    '''
   .

    '''
    

    for r in board[::-1]:
        print(' '.join(r))
        
        
        
        
# START GAME 

print('')
showwhiteboard()    
        

#Checks which type of piece exists
def Color(string):
   x=list(string)
   if x[0] == "w":
       return True
   elif x[0] == "b":
       return False
   elif x[0] == "-":
       return Nothing
   
    
    
    
    
    
#Find direction of movement 
def direction(d):
    if d >= 0 :
        return 1
    else: 
        return -1 
    

    
    
#Turn
def Turn(ree):
    
    
    global turn 


    if turn == 1:
        print(' ')
        print('White turn over')
        # board.reverse()
        return 2
        
        #white
    elif turn == 2:
        print(' ')
        print('Black turn over')
        # board.reverse()
        return 1



def LastMove(piece,row,file,trow,tfile):
    global LMC
    
    d3 = trow - row
    d4 = tfile - file
    piece = piece
    LMC[:] = [piece,d3,d4,trow,tfile]
    
    
def RookMove(row,file):
    global WLRM
    global WRRM
    global BLRM
    global BRRM
    
    
    if turn == 1:
        if row == 0 and file == 0:            
            WLRM = WLRM + 1
            return;
        elif row == 0 and file == 7:   
            WRRM = WRRM + 1
            return;
    if turn == 2:
        if row == 7 and file == 0:
            BLRM = BLRM + 1
            return;
        if row == 7 and file == 7:
            BRRM = BRRM + 1
            return;

        
        
def KingMove():
    global WKM
    global BKM
    
    
    
    
    if turn == 1:
        WKM = WKM + 1
        return;
    if turn == 2:
        BKM = BKM + 1
        return;
    
    
    


## Diagonal helper functions
#Up and to the right
def DiagCheck1(x,y):
    global board
    global turn 
    
    
    x = x + 1
    y = y + 1
    
    
    
    
    if x > 7 or y > 7:
        return True
    while x != 7 and y != 7:
         if turn == 1: 
             if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bBi":
                             return False
                         else:
                             return True
             else: 
                     x += 1
                     y += 1
         if turn == 2:
              if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wBi":
                             return False
                         else:
                             return True
              else: 
                     x += 1
                     y += 1
                 
    if x == 7 or y == 7:
        if turn == 1:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bBi":
                             return False
                         else:
                             return True
        if turn == 2:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wBi":
                             return False
                         else:
                             return True
    else:
        return True         
    
    
    
    
    
#Up and to the left
def DiagCheck2(x,y):
    global board
    
    x = x + 1
    y = y - 1
    if x > 7 or y < 0:
        return True
    while x != 7 and y != 0: 
        if turn == 1:
             if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bBi":
                             return False
                         else:
                             return True
             else: 
                     x += 1
                     y -= 1
        if turn == 2:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wBi":
                             return False
                         else:
                             return True
            else: 
                     x += 1
                     y -= 1
                 
    if x == 7 or y == 0:
        if turn == 1:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "w":
                         return True
                     if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bBi":
                             return False
                         else:
                             return True
        if turn == 2:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "b":
                         return True
                     if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wBi":
                             return False
                         else:
                             return True

#Down and to the right          
def DiagCheck3(x,y):
    global board
    
    x = x - 1
    y = y + 1
    if x < 0 or y > 7:
        return True
    while x != 0 and y != 7:
        if turn == 1:
             if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bBi":
                             # print('Check coming from Bishop or Queen')
                             return False
                         else:
                             return True
             else: 
                     x -= 1
                     y += 1
        if turn == 2:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wBi":
                             # print('Check coming from Bishop or Queen')
                             return False
                         else:
                             return True
            else: 
                    x -= 1
                    y += 1
                 
                 
                 
    if x == 0 or y == 7:
        if turn == 1:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "w":
                         return True
                     if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bBi":
                             return False
                         else:
                             return True
        if turn == 2:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "b":
                         return True
                     if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wBi":
                             return False
                         else:
                             return True

#Down and to the left
def DiagCheck4(x,y):
    global board
    
    x = x - 1
    y = y - 1
    
    if x < 0 or y < 0: #Edgecase
        return True
    while x != 0 and y != 0:
        if turn == 1:
             if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bBi":
                             return False
                         else:
                             return True
             else: 
                         x -= 1
                         y -= 1
        if turn == 2:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wBi":
                             return False
                         else:
                             return True
            else: 
                x -= 1
                y -= 1
             
             
             
    if x == 0 or y == 0:
        if turn == 1:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "w":
                         return True
                     if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bBi":
                             return False
                         else:
                             return True
        if turn == 2:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "b":
                         return True
                     if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wBi":
                             return False
                         else:
                             return True
            
    
    
    
    

#Vertical Check Straight up
def VertCheck1(x,y):
    global board
    
    x = x + 1 
    y = y 
    
    if x > 7: #Edgecase
        return True
    while x != 7:
        if turn == 1:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bR":
                             return False
                         else:
                             return True
            else: 
                x += 1
        if turn == 2:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wR":
                             return False
                         else:
                             return True
            else: 
                x += 1
    if x == 7:
        if turn == 1:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "w":
                         return True
                     if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bR":
                             return False
                         else:
                             return True
        if turn == 2:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "b":
                         return True
                     if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wR":
                             return False
                         else:
                             return True
#Vert Check down           
def VertCheck2(x,y):
    global board
    
    x = x - 1 
    y = y 
    
    if x < 0: #Edgecase
        return True
    while x != 0:
        if turn == 1:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bR":
                             return False
                         else:
                             return True
            else: 
                x -= 1
        if turn == 2:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wR":
                             return False
                         else:
                             return True
            else: 
                x -= 1
    if x == 0:
        if turn == 1:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "w":
                         return True
                     if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bR":
                             return False
                         else:
                             return True
        if turn == 2:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "b":
                         return True
                     if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wR":
                             return False
                         else:
                             return True


#Horizontal Check right
def HorizCheck1(x,y):
    x = x  
    y = y + 1
    
    if y > 7: #Edgecase
        return True
    while y != 7:
        if turn == 1:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bR":
                             return False
                         else:
                             return True
            else: 
                y += 1
        if turn == 2:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wR":
                             return False
                         else:
                             return True
            else: 
                y += 1
    if y == 7:
        if turn == 1:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "w":
                         return True
                     if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bR":
                             return False
                         else:
                             return True
        if turn == 2:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "b":
                         return True
                     if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wR":
                             return False
                         else:
                             return True



#Horizontal Check left
def HorizCheck2(x,y):
    x = x  
    y = y - 1
    
    if y < 0: #Edgecase
        return True
    while y != 0:
        if turn == 1:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "w":
                     return True
                 if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bR":
                             return False
                         else:
                             return True
            else: 
                y -= 1
        if turn == 2:
            if board[x][y] != "--":
                 if (board[x][y])[0] == "b":
                     return True
                 if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wR":
                             return False
                         else:
                             return True
            else: 
                y -= 1
    if y == 0:
        if turn == 1:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "w":
                         return True
                     if (board[x][y])[0] == "b":
                         if board [x][y] == "bQ" or board [x][y] == "bR":
                             return False
                         else:
                             return True
        if turn == 2:
            if board[x][y] == "--":
                return True
            else:
                if board[x][y] != "--":
                     if (board[x][y])[0] == "b":
                         return True
                     if (board[x][y])[0] == "w":
                         if board [x][y] == "wQ" or board [x][y] == "wR":
                             return False
                         else:
                             return True
 
                        
#Checking for Knights 
def KnightCheck(x,y):
    
    
        global turn
    
        move1 = [x+2 , y+1] #2up 1right
        move2 = [x+2 , y-1] #2up 1left
        move3 = [x+1 , y+2] #1up 2right
        move4 = [x+1 , y-2] #1up 2left
        move5 = [x-2 , y+1] #2down 1right
        move6 = [x-2 , y-1] #2down 1left
        move7 = [x-1 , y+2] #1down 2right
        move8 = [x-1 , y-2] #1down 2 left     
        moves = [move1, move2, move3, move4, move5, move6, move7, move8]  
        edgecase = [[x,y] for x,y in moves if x>=0 and y>=0 and x < 8 and y < 8]
    
    
        i = 0 
        while i < len(edgecase):
            edgecase_copy = edgecase[:]
            x,y = edgecase_copy[i]
            if turn == 1:
                if board[x][y] == "bKn":
                    return False
                else:
                        i += 1 
            if turn == 2:
                if board[x][y] == "wKn":
                    return False
                else:
                        i += 1
        return True   
    
    
    
    
    
    
#White
def PawnCheck1(x,y):
    
    x = x + 1
    y = y + 1
    if x > 7 or y > 7: #Edgecase
        return True
    if board[x][y] == "bP" or board[x][y] == "bK":
        print(board[x][y])
        return False
    else:
        return True
    

def PawnCheck2(x,y):
    
    x = x + 1 
    y = y - 1
    if x > 7 or y < 0: #Edgecase
        return True
    if board[x][y] == "bP" or board[x][y] == "bK":
        print(board[x][y])
        return False
    else:
        return True



#Black
def PawnCheck3(x,y):
    
    x = x - 1
    y = y + 1 
    
    
    
    
    if x < 0 or y > 7: #Edgecase
        return True
    if board[x][y] == "wP" or board[x][y] == "wK":
        return False 
    else:
        return True
    
def PawnCheck4(x,y):
    
    x = x - 1
    y = y - 1 
    
    if x < 0 or y < 0:
        return True
    if board[x][y] == "wP" or board[x][y] == "wK":
        return False
    else:
        return True

    
    
    
    

#Scans for king and outwardly checks for pieces to determine if it's in check or not
def KingCheck():
    
    
    
    global board
    global turn
    
    
    search = "wK"
    search2 = "bK"
    if turn == 1:
        for sublist in board:
            for i in sublist:
                if i == search:
                    row = board.index(sublist)
                    file = sublist.index("wK")
                    
    if turn == 2:
        for sublist in board:
            for i in sublist:
                if i == search2:
                    row = board.index(sublist)
                    file = sublist.index("bK")
                    
    
                    
    # King must check if there is a knight attacking, a bishop attacking, a queen attacking, a rook attacking, or a pawn attacking.
    # The way king check is implemeneted means I alsoi have to check for a king within a space of one 
     #Diagonal Check 1
     
     
    # c1 = DiagCheck1(row,file)
    # c2 = DiagCheck2(row,file)
    # c3 = DiagCheck3(row,file)
    # c4 = DiagCheck4(row,file)
    # c5 = VertCheck1(row,file)
    # c6 = VertCheck2(row,file)
    # c7 = HorizCheck1(row,file)
    # c8 = HorizCheck2(row,file)
    # c9 = KnightCheck(row,file)
    # c10 = PawnCheck1(row,file)
    # c11 = PawnCheck2(row,file)
    # c12 = PawnCheck3(row,file)
    # c13 = PawnCheck4(row,file)


    if turn == 1:
        c1 = DiagCheck1(row,file)
        c2 = DiagCheck2(row,file)
        c3 = DiagCheck3(row,file)
        c4 = DiagCheck4(row,file)
        c5 = VertCheck1(row,file)
        c6 = VertCheck2(row,file)
        c7 = HorizCheck1(row,file)
        c8 = HorizCheck2(row,file)
        c9 = KnightCheck(row,file)
        c10 = PawnCheck1(row,file)
        c11 = PawnCheck2(row,file)
        checks = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11]
        if checks.count(False) > 0:
            return False
        else:
            return True
    if turn == 2:
        c1 = DiagCheck1(row,file)
        c2 = DiagCheck2(row,file)
        c3 = DiagCheck3(row,file)
        c4 = DiagCheck4(row,file)
        c5 = VertCheck1(row,file)
        c6 = VertCheck2(row,file)
        c7 = HorizCheck1(row,file)
        c8 = HorizCheck2(row,file)
        c9 = KnightCheck(row,file)
        c12 = PawnCheck3(row,file)
        c13 = PawnCheck4(row,file)
        checks = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c12,c13]
        if checks.count(False) > 0:
            return False
        else:
            return True


### CHECKMATE FUNCTION NOT WORKING AT THE MOMENT
# def CheckMate():
    
    
    # global turn
    # global board
    # turn = Turn(turn)
    # x = KingCheck()
    # search = "wK"
    # search2 = "bK"
    # if x == True:
    #     if turn == 1:
    #         for sublist in board:
    #             for i in sublist:
    #                 if i == search:
    #                     row = board.index(sublist)
    #                     file = sublist.index("wK")
    #     if turn == 2:
    #         for sublist in board:
    #             for i in sublist:
    #                 if i == search2:
    #                     row = board.index(sublist)
    #                     file = sublist.index("bK")
            
        
    #     pass
      
#Valid move function    
def isValidMove(piece,row,file,trow,tfile):
    
#dlr = Delta row 
#dlf = Delta  file 
  global turn    
  global LMC
  
  
    
  if piece in ["pawn","Pawn"]:
      d1 = trow - row
      d2 = tfile - file 
      dlr = direction(d1) #Vertical direction
      dlf = direction(d2) #Horizontal direction
      x = row + dlr
      y = file 
      if d1 == 1 and file == tfile:         #d1 == 1 and file == tfile means it's the white pawn
          if turn == 1:
              if board[trow][tfile] != "--":
                  print('Your path is blocked!')
                  return False
              else:
                  return True
          else:
              return False
      if d1 == -1 and file == tfile:  #d1 == -1 and file == tfile means it's the black pawn
          if turn == 2:
              if board[trow][tfile] != "--":
                  print('Your path is blocked!')
                  return False
              else:
                  return True
          else:
              return False
      elif abs(d1) == 2 and file == tfile: #Check if pawn has moved from inital row for moves of 2
          if d1 < 0:
            if row != 6:
                print('This pawn moved and can no longer move two spaces forward')
                return False
          if d1 > 0: 
            if row != 1:
                print('This pawn cant move two spaces forward')
                return False
          while x != trow :
                  if board[x][tfile] != "--":
                      print('Path blocked!')
                      return False
                  x += dlr
                  if x == trow:
                     if board[x][tfile] != "--":
                         print('A piece is blocking your path')
                         return False
          return True
      
      
      
      
      
      if d1 == 1 and d2 ==  -1: #Taking with white pawn
         if turn == 1:
            check1 = Color(board[trow][tfile]) 
            if check1 == False:
                  print('Piece Taken!')
                  return True
            else: 
               if LMC[0] in ["pawn","Pawn"] and abs(LMC[1]) == 2 and LMC[3] - 1 == row and LMC[4] - 1 == tfile: #Check for En Passant
                   print('Piece Taken via En Passant!') 
                   board[row][tfile] = "--"
                   return True
               else:
                   print('Invalid Move')
                   return False
        
         if turn == 2:
             print('Invalid Move')
             return False
         
            
         
      if d1 == (-1) and d2 == -1: #Taking with black pawn
           if turn == 2:
              check1 = Color(board[trow][tfile]) 
              if check1 == True:
                    return True
              else: 
                   if LMC[0] in ["pawn","Pawn"] and abs(LMC[1]) == 2 and LMC[3] -1 == row and LMC[4] - 1 == tfile: #Check for En Passant
                       print(' ')
                       print('Piece Taken via En Passant!') 
                       board[row][tfile] = "--"
                       return True
                   else:
                       print('Invalid Move')
                       return False
           if turn == 1:
              print('Invalid Move')
              return False
           
            
           
            
           
      if d1 == 1 and d2 == 1:
        if turn == 1:
            check1 = Color(board[trow][tfile]) 
            if check1 == False:
                print('Piece Taken!')
                return True
            else: 
               if LMC[0] in ["pawn","Pawn"] and abs(LMC[1]) == 2 and LMC[3] - 1 == row and LMC[4] - 1 == tfile: #Check for En Passant
                   print(' ')
                   print('Piece Taken via En Passant!') 
                   board[row][tfile] = "--"
                   return True
               else:
                   print('Invalid Move')
                   return False
        if turn == 2:
            print('Invalid Move')
            return False
     


      if d1 == -1  and d2 == 1:         
        if turn == 2:
            check1 = Color(board[trow][tfile]) 
            if check1 == True:
                  print('Piece Taken!')
                  return True
            else: 
               if LMC[0] in ["pawn","Pawn"] and abs(LMC[1]) == 2 and LMC[3] - 1 == row and LMC[4] - 1 == tfile: #Check for En Passant
                   print(' ')
                   print('Piece Taken via En Passant!') 
                   board[row][tfile] = "--"
                   return True
               else:
                   print('Invalid Move')
                   return False
        if turn == 1:
            print('Invalid Move')
            return False
        
             
              
             
             
        
      
      
      
      
  
       
  if piece in ["knight","Knight"]:
     
        move1 = [row+1 , file] #2up 1right
        move2 = [row+1 , file-2] #2up 1left
        move3 = [row , file+1] #1up 2right
        move4 = [row , file-3] #1up 2left
        move5 = [row-3 , file] #2down 1right
        move6 = [row-3 , file-2] #2down 1left
        move7 = [row-2 , file+1] #1down 2right
        move8 = [row-2 , file-3] #1down 2 left     
        moves = [move1, move2, move3, move4, move5, move6, move7, move8]  
        
        #Edgecase
        edgecase = [[x,y] for x,y in moves if x>=0 and y>=0 and x < 8 and y < 8]
        # avalmovetouser = [[x+1,y+1] for x,y in edgecase]
        i = 0 
        if turn == 1:
            while i < len(edgecase):
                edgecase_copy = edgecase[:]
                x,y = edgecase_copy[i]
                if board[x][y] != "--" and (board[x][y])[0] != 'b' :
                    del(edgecase[i])
                else:
                    i += 1 
            if [trow-1,tfile-1] not in edgecase:
                return False
            else:
                if (board[trow-1][tfile-1])[0] == 'b':
                    print(' ')
                    print ('Piece taken!')
                    return True
                else:
                    return True
        if turn == 2:
            while i < len(edgecase):
                edgecase_copy = edgecase[:]
                x,y = edgecase_copy[i]
                if board[x][y] != "--" and (board[x][y])[0] != 'w' :
                    del(edgecase[i])
                else:
                    i += 1 
            if [trow-1,tfile-1] not in edgecase:
                return False
            else:
                if (board[trow-1][tfile-1])[0] == 'w':
                    print(' ')
                    print ('Piece taken!')
                    return True
                else:
                    return True
            
    
        
        
      
      
      
      
  if piece in ["king","King"]:
      if abs(trow-row) > 1 or abs(tfile-file) > 1 :
          if turn == 1: #Checking for castling
              if tfile-file == 2 and trow == 0 and WRRM == 0 and WKM == 0:
                      x = row
                      dlf = direction(tfile-file)
                      y = file + dlf
                      while y != tfile:
                          if board[x][y] != "--":
                              return False
                          else:
                              board[x][y-dlf] = "--"
                              board[x][y] = "wK"
                              kc = KingCheck()
                              if kc == True:
                                  y += dlf
                              else:
                                  board[x][y-dlf] = "wK"
                                  board[x][y] = "--"
                                  return False
                      if y == tfile:
                         if board[x][y] != "--":
                             board[row][file] = "wK"
                             board[row][y-dlf] = "--"
                             return False
                         else:
                             board[x][y] = "wK"
                             board[row][y-dlf] = "--"
                             kc = KingCheck()
                             if kc == True and board[0][7] == "wR" and dlf == 1:
                                 board[x][7] = "--"
                                 board[x][y-dlf] = "wR"
                                 return True
              if tfile-file == -2 and trow == 0 and WLRM == 0 and WKM == 0:
                      x = row
                      dlf = direction(tfile-file)
                      y = file + dlf
                      while y != tfile:
                          if board[x][y] != "--":
                              return False
                          else:
                              board[x][y-dlf] = "--"
                              board[x][y] = "wK"
                              kc = KingCheck()
                              if kc == True:
                                  y += dlf
                              else:
                                  board[x][y-dlf] = "wK"
                                  board[x][y] = "--"
                                  return False
                      if y == tfile:
                         if board[x][y] != "--":
                             board[row][file] = "wK"
                             board[row][y-dlf] = "--"
                             return False
                         else:
                             board[x][y] = "wK"
                             board[row][y-dlf] = "--"
                             kc = KingCheck()
                             if kc == True and board[0][0] == "wR" and dlf == -1:
                                  board[x][0] = "--"
                                  board[x][y-dlf] = "wR"
                                  return True
          if turn == 2:
              if tfile-file == 2 and trow == 7 and BRRM == 0 and BKM == 0:
                      x = row
                      dlf = direction(tfile-file)
                      y = file + dlf
                      while y != tfile:
                          if board[x][y] != "--":
                              return False
                          else:
                              board[x][y-dlf] = "--"
                              board[x][y] = "bK"
                              kc = KingCheck()
                              if kc == True:
                                  y += dlf
                              else:
                                  board[x][y-dlf] = "bK"
                                  board[x][y] = "--"
                                  return False
                      if y == tfile:
                         if board[x][y] != "--":
                             board[row][file] = "bK"
                             board[row][y-dlf] = "--"
                             return False
                         else:
                             board[x][y] = "bK"
                             board[row][y-dlf] = "--"
                             kc = KingCheck()
                             if kc == True and board[0][7] == "bR" and dlf == 1:
                                 board[x][7] = "--"
                                 board[x][y-dlf] = "bR"
                                 return True
              if tfile-file == -2 and trow == 0 and BLRM == 0 and BKM == 0:
                      x = row
                      dlf = direction(tfile-file)
                      y = file + dlf
                      while y != tfile:
                          if board[x][y] != "--":
                              return False
                          else:
                              board[x][y-dlf] = "--"
                              board[x][y] = "bK"
                              kc = KingCheck()
                              if kc == True:
                                  y += dlf
                              else:
                                  board[x][y-dlf] = "bK"
                                  board[x][y] = "--"
                                  return False
                      if y == tfile:
                         if board[x][y] != "--":
                             board[row][file] = "bK"
                             board[row][y-dlf] = "--"
                             return False
                         else:
                             board[x][y] = "bK"
                             board[row][y-dlf] = "--"
                             kc = KingCheck()
                             if kc == True and board[0][0] == "bR" and dlf == -1:
                                  board[x][0] = "--"
                                  board[x][y-dlf] = "bR"
                                  return True
                  
                  
      if abs(trow-row) <= 1 and abs(tfile - file) <= 1 : 
          
          
          
          #Checking if the user accidentally doesn't move thier piece
          if trow - row == 0 and tfile - file == 0 :
              return False
          
            
          
            
      #King condition 1 cell in every direction
      # Can use queen code but limit to one cell
      #Queen has bishop movement and rook movement so I reused the bishop and rook code.
    
          
     #Diagonal movement of Queen; Bishop movement
          if trow != row and tfile != file and abs(trow-row) == abs(tfile - file):
            d1 = trow - row
            d2 = tfile - file 
            dlr = direction(d1) #Vertical direction
            dlf = direction(d2) #Horizontal direction
            x = row + dlr
            y = file + dlf
            
            if turn == 1:
                if abs(d1) and abs(d2) == 1: 
                    if board [x][y] != "--" and (board[x][y])[0] != 'b': #Checking for a specific case of bishop movement of 1 
                        return False
                if x == trow and y == tfile :
                    if board[trow][tfile] != "--" and (board[trow][tfile])[0] != 'b':
                        return False
            return True
            if turn == 2:
                if abs(d1) and abs(d2) == 1: 
                    if board [x][y] != "--" and (board[x][y])[0] != 'w': #Checking for a specific case of bishop movement of 1 
                        return False
                if x == trow and y == tfile :
                    if board[trow][tfile] != "--" and (board[trow][tfile])[0] != 'w':
                        return False
            return True
    # Checked, works, can cut down later. 
      
     #Vertical movement ; Rook Movement
          if trow == row and tfile != file : #Conditions of possible rook Movement
            d1 = tfile - file  #Find # of cells to move
            dlf =  direction(d1) #Find direction
            x = row #Moving along file
            y = file + dlf 
            if turn == 1:
                if abs(d1) == 1 : 
                    if board[x][y] != "--" and (board[trow][tfile])[0] != 'b' :
                      return False
                if x == trow and y == tfile : 
                      if board[trow][tfile] != "--" and (board[trow][tfile])[0] != 'b':
                       
                          return False
                return True
            if turn == 2:
                if abs(d1) == 1 : 
                    if board[x][y] != "--" and (board[trow][tfile])[0] != 'w' :
                      return False
                if x == trow and y == tfile : 
                      if board[trow][tfile] != "--" and (board[trow][tfile])[0] != 'w':
                          return False
            return True
         
            
          elif trow != row and tfile == file : #Another condition of possible rook movement
              d2 = trow - row 
              dlr = direction(d2)
              x = row + dlr 
              y = file
              
              
              if turn == 1:
                   if abs (d2) == 1 : #Special case of movement of 1 cell
                     if board[x][y] != "--" and (board[x][y])[0] != 'b' :
                       return False
              if turn == 2:
                   if abs (d2) == 1 : #Special case of movement of 1 cell
                     if board[x][y] != "--" and (board[x][y])[0] != 'w' :
                       return False
          return True 
    
    
      else:
         return False
         
        
  if piece in ["rook","Rook"]:
      
      
      
      
      
      #Can't input same square
      if trow - row == 0 and tfile - file == 0 :
         return False
          
      
      
      if trow == row and tfile != file : #Conditions of possible rook Movement
         d1 = tfile - file  #Find # of cells to move
         dlf =  direction(d1) #Find direction
         x = row #Moving along file
         y = file + dlf 
         if abs(d1) == 1 : 
             if turn == 1:  
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b': #Check if square 1 square away is empty or occupuied
                     return False
             if turn == 2 : 
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w': #Check if square 1 square away is empty or occupuied
                     return False
         while y != tfile: #Checks for empty squares
            if board[x][y] != "--":
                return False
            y += dlf
         if x == trow and y == tfile:
             if turn == 1:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b':
                     return False
             if turn == 2:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w':
                     return False          
         return True
         
            
      elif trow != row and tfile == file : #Another condition of possible rook movement
          d2 = trow - row 
          dlr = direction(d2)
          x = row + dlr 
          y = file
          if abs (d2) == 1 : #Special case of movement of 1 cell
              if turn == 1:  
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b': #Check if square 1 square away is empty or occupuied
                     return False
              if turn == 2 : 
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w': #Check if square 1 square away is empty or occupuied
                     return False
          while x != trow :
              if board[x][y] != "--":
                  return False
              x += dlr
          if x == trow and y == tfile:
              if turn == 1:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b':
                     return False
              if turn == 2:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w':
                     return False
          return True 
    
    
      else:
          return False
          
          
        
        
  if piece in ["bishop","Bishop"]:
      
  
      if trow - row == 0 and tfile - file == 0 :
              return False
      

      if trow != row and tfile != file and abs(trow-row) == abs(tfile - file): #Bishop movement has these conditions
            d1 = trow - row
            d2 = tfile - file 
            dlr = direction(d1) #Vertical direction
            dlf = direction(d2) #Horizontal direction
            x = row + dlr
            y = file + dlf
            
            
            
            if abs(d1) and abs(d2) == 1: 
              if turn == 1:  
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b': #Check if square 1 square away is empty or occupuied
                     return False
              if turn == 2 : 
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w': #Check if square 1 square away is empty or occupuied
                     return False
            while x != trow and  y != tfile: 
                if board[x][y] != "--" : # Making sure cells are empty so move is valid
                    return False
                x += dlr
                y += dlf
            if x == trow and y == tfile:
             if turn == 1:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b':
                     return False
             if turn == 2:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w':
                     return False      
            return True
        
        
  if piece in ["queen","Queen"]:
      
      #Queen has bishop movement and rook movement so I reused the bishop and rook code.
      
      if trow - row == 0 and tfile - file == 0 :
              return False
      




      #Up and Down Movement ; Rook Movement
      if trow == row and tfile != file : #Conditions of possible rook Movement
                 d1 = tfile - file  #Find # of cells to move
                 dlf =  direction(d1) #Find direction
                 x = row #Moving along file
                 y = file + dlf 
                 if abs(d1) == 1 : 
                     if turn == 1:  
                         if board[x][y] != "--" and (board[trow][tfile])[0] != 'b': #Check if square 1 square away is empty or occupuied
                             return False
                     if turn == 2 : 
                         if board[x][y] != "--" and (board[trow][tfile])[0] != 'w': #Check if square 1 square away is empty or occupuied
                             return False
                 while y != tfile: #Checks for empty squares
                    if board[x][y] != "--":
                        return False
                    y += dlf
                 if x == trow and y == tfile:
                     if turn == 1:
                         if board[x][y] != "--" and (board[trow][tfile])[0] != 'b':
                             return False
                     if turn == 2:
                         if board[x][y] != "--" and (board[trow][tfile])[0] != 'w':
                             return False          
                 return True
         
            
      if trow != row and tfile == file : #Another condition of possible rook movement
      

          d2 = trow - row 
          dlr = direction(d2)
          x = row + dlr 
          y = file
          if abs (d2) == 1 : #Special case of movement of 1 cell
              if turn == 1:  
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b': #Check if square 1 square away is empty or occupuied
                     return False
              if turn == 2 : 
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w': #Check if square 1 square away is empty or occupuied
                     return False
          while x != trow :
              if board[x][y] != "--":
                  return False
              x += dlr
          if x == trow and y == tfile:
              if turn == 1:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b':
                     return False
              if turn == 2:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w':
                     return False
          return True 
    

  
      #Diagonal Movement ; Bishop Movement 
      if trow != row and tfile != file and abs(trow-row) == abs(tfile - file): #Bishop movement has these conditions
            d1 = trow - row
            d2 = tfile - file 
            dlr = direction(d1) #Vertical direction
            dlf = direction(d2) #Horizontal direction
            x = row + dlr
            y = file + dlf
            
            
            if abs(d1) and abs(d2) == 1: 
              if turn == 1:  
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b': #Check if square 1 square away is empty or occupuied
                     return False
              if turn == 2 : 
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w': #Check if square 1 square away is empty or occupuied
                     return False
            while x != trow and  y != tfile: 
                if board[x][y] != "--" : # Making sure cells are empty so move is valid
                    return False
                x += dlr
                y += dlf
            if x == trow and y == tfile:
             if turn == 1:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'b':
                     return False
             if turn == 2:
                 if board[x][y] != "--" and (board[trow][tfile])[0] != 'w':
                     return False      
            return True
      
      else:
           return False  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
     

     
#Main function to move pieces on the board 
          
      

def MovePiece(piece, row, file):
    
    global turn
    global board
    
    
    if piece in ["pawn", "Pawn"]:
        if turn == 1:
           assert board[row-1][file-1] == "wP", 'No pawn is there'
           trow = int(input('Which row would you like to go to? '))
           tfile = int(input('Which file would you like to go to? '))
           x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
           if x == True: 
               if trow == 8:
                   torowpiece = board[trow-1][tfile-1]
                   board[row-1][file-1] = "--"
                   board [trow-1][tfile-1] = "wQ"
                   a = KingCheck()
                   if a == True:
                        showwhiteboard()
                        turn = Turn(turn)
                        LastMove(piece,row,file,trow,tfile)
                   else:
                        board[row-1][file-1] = "wP"
                        board[trow-1][tfile-1] = torowpiece
                        print('Invalid Move, King would be in check')
                        return;
               else:
                   torowpiece = board[trow-1][tfile-1]
                   board[row-1][file-1] = "--"
                   board [trow-1][tfile-1] = "wP"
                   a = KingCheck()
                   if a == True:
                        showwhiteboard()
                        turn = Turn(turn)
                        LastMove(piece,row,file,trow,tfile)
                   else:
                        board[row-1][file-1] = "wP"
                        board[trow-1][tfile-1] = torowpiece
                        print('Invalid Move, King would be in check')
                        return;
               return;
           else:
            print('This is not a valid move')
        elif turn == 2:
           assert board[row-1][file-1] == "bP", 'No pawn is there'
           trow = int(input('Which row would you like to go to? '))
           tfile = int(input('Which file would you like to go to? '))
           x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
           if x == True:
               if trow == 0:
                   torowpiece = board[trow-1][tfile-1]
                   board[row-1][file-1] = "--"
                   board [trow-1][tfile-1] = "bQ"
                   a = KingCheck()
                   if a == True:
                        showwhiteboard()
                        turn = Turn(turn)
                        LastMove(piece,row,file,trow,tfile)
                   else:
                        board[row-1][file-1] = "bP"
                        board[trow-1][tfile-1] = torowpiece
                        print('Invalid Move, King would be in check')
                        return;
               else:
                   torowpiece = board[trow-1][tfile-1]
                   board[row-1][file-1] = "--"
                   board [trow-1][tfile-1] = "bP"
                   a = KingCheck()
                   if a == True:
                        print('True')
                        showwhiteboard()
                        turn = Turn(turn)
                        LastMove(piece,row,file,trow,tfile)
                   else:
                        board[row-1][file-1] = "bP"
                        board[trow-1][tfile-1] = torowpiece
                        print('Invalid Move, King would be in check')
                        return;
           else:
            print('This is not a valid move')

                   
        
    if piece in ["knight","Knight"]:
        if turn == 1:
            assert board[row-1][file-1] == "wKn" , 'No knight is there! Enter in a valid move.'
            trow = int(input('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row, file, trow, tfile)
            if x == True:
                torowpiece = board[trow-1][tfile-1]
                board[row-1][file-1] = "--"
                board[trow-1][tfile-1] = "wKn"
                a = KingCheck()
                if a == True:
                    showwhiteboard()
                    turn = Turn(turn)
                    LastMove(piece,row,file,trow,tfile)
                else:
                    board[row-1][file-1] = "wKn"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
                    return;
                return;
            else:
               print('This is not a valid move')
        elif turn == 2:
            assert board[row-1][file-1] == "bKn" , 'No knight is there! Enter in a valid move.'
            trow = int(input('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row, file, trow, tfile)
            if x == True:
                torowpiece = board[trow-1][tfile-1]
                board[row-1][file-1] = "--"
                board [trow-1][tfile-1] = "bKn"
                a = KingCheck()
                if a == True:
                    showwhiteboard()
                    turn = Turn(turn)
                    LastMove(piece,row,file,trow,tfile)
                else:
                    board[row-1][file-1] = "bKn"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
                    return;
                return;
            else:
               print('This is not a valid move')
        
    if piece in ["king","King"]:
        if turn == 1:
            assert board[row-1][file-1] == "wK" , 'No king is there! Enter in a valid move.'
            trow = int(input('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
            if x == True:
                torowpiece = board[trow-1][tfile-1]
                board[row-1][file-1] = "--"
                board [trow-1][tfile-1] = "wK"
                a = KingCheck()
                if a == True:
                    showwhiteboard()
                    LastMove(piece,row,file,trow,tfile)
                    KingMove()
                    turn = Turn(turn)
                else:
                    board[row-1][file-1] = "wK"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
                    return;
                return;
            else:
                print('This is not a valid move')
        elif turn == 2:
            assert board[row-1][file-1] == "bK" , 'No king is there! Enter in a valid move.'
            trow = int(input('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
            if x == True:
                torowpiece = board[trow-1][tfile-1]
                board[row-1][file-1] = "--"
                board [trow-1][tfile-1] = "bK"
                a = KingCheck()
                if a == True:
                    showwhiteboard()
                    LastMove(piece,row,file,trow,tfile)
        
                    turn = Turn(turn)
                else:
                    board[row-1][file-1] = "bK"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
                    return;
                return;
            else:
                print('This is not a valid move')
        
            
    if piece in ["rook","Rook"]:
        if turn == 1:
            assert board[row-1][file-1] == "wR" , 'No rook is there! Enter in a valid move.'
            trow = int(input('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
            if x == True:
                torowpiece = board[trow-1][tfile-1]
                board[row-1][file-1] = "--"
                board [trow-1][tfile-1] = "wR"
                a = KingCheck()
                if a == True:
                    showwhiteboard()                   
                    LastMove(piece,row,file,trow,tfile)
                    RookMove(row-1,file-1)
                    turn = Turn(turn)
                else:
                    board[row-1][file-1] = "wR"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
                    return;
            else:
                print('This is not a valid move, your path is blocked!')
        elif turn == 2:
            assert board[row-1][file-1] == "bR" , 'No rook is there! Enter in a valid move.'
            trow = int(input('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
            if x == True:
                torowpiece = board[trow-1][tfile-1]
                board[row-1][file-1] = "--"
                board [trow-1][tfile-1] = "bR"
                a = KingCheck()
                if a == True:
                    showwhiteboard()
                    LastMove(piece,row,file,trow,tfile)
                    RookMove(row-1,file-1)
                    turn = Turn(turn)
                else:
                    board[row-1][file-1] = "bR"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
                    return;
                return;
            else:
                print('This is not a valid move, your path is blocked!')
                
                
    if piece in ["bishop","Bishop"]:
        
        
        if turn == 1: 
            assert board[row-1][file-1] == "wBi", 'No bishop is there! Enter in a valid move.'
            trow = int(input('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
            if x == True:
                torowpiece = board[trow-1][tfile-1]
                board[row-1][file-1] = "--"
                board [trow-1][tfile-1] = "wBi"
                a = KingCheck()
                if a == True:
                    showwhiteboard()
                    turn = Turn(turn)
                    LastMove(piece,row,file,trow,tfile)
                else:
                    board[row-1][file-1] = "wBi"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
                    return;
                return;
            else:
                print('This is not a valid move, your path is blocked!')
                
                
        elif turn == 2:
            assert board[row-1][file-1] == "bBi", 'No bishop is there! Enter in a valid move.'
            trow = int(input('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
            if x == True:
                torowpiece = board[trow-1][tfile-1]
                board[row-1][file-1] = "--"
                board[trow-1][tfile-1] = "bBi"
                a = KingCheck()
                if a == True:
                    showwhiteboard()
                    turn = Turn(turn)
                    LastMove(piece,row,file,trow,tfile)
                else:
                    board[row-1][file-1] = "bBi"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
                    return;
                return;
            else:
                print('This is not a valid move, your path is blocked!')
            
            
    if piece in ["queen","Queen"]:
        
        
        if turn == 1:
            assert board[row-1][file-1] == "wQ" , 'No queen  is there! Enter in a valid move.'
            trow = int(input ('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
            if x == True:
               torowpiece = board[trow-1][tfile-1]
               board[row-1][file-1] = "--"
               board [trow-1][tfile-1] = "wQ"
               a = KingCheck()
               if a == True:
                    showwhiteboard()
                    turn = Turn(turn)
                    LastMove(piece,row,file,trow,tfile)
               else:
                    board[row-1][file-1] = "wQ"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
               return;
            else: 
                print('This is not a valid move your path is blocked ')
                
                
                
                
        if turn == 2:
            assert board[row-1][file-1] == "bQ" , 'No queen  is there! Enter in a valid move.'
            trow = int(input ('Which row would you like to go to? '))
            tfile = int(input('Which file would you like to go to? '))
            x = isValidMove(piece, row-1, file-1, trow-1, tfile-1)
            if x == True:
               torowpiece = board[trow-1][tfile-1]
               board[row-1][file-1] = "--"
               board [trow-1][tfile-1] = "bQ"
               a = KingCheck()
               if a == True:
                    showwhiteboard()
                    turn = Turn(turn)
                    LastMove(piece,row,file,trow,tfile)
               else:
                    board[row-1][file-1] = "bQ"
                    board[trow-1][tfile-1] = torowpiece
                    print('Invalid Move, King would be in check')
               return;
            else: 
                print('This is not a valid move your path is blocked ')
            

    
                
                
                
                
                
                
                
        
        
            
        
        
        
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    






        
        
        
        
