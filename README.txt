~~~~Author~~~~~
Momin Hamdani



~~~~Description~~~~

This is a comnmand-line based chess program written for two players in python. 

~~~~Instructions~~~~

To play the game you must first run the program.
Once you run the program the console should appear as 

Basic Chess Engine

bR bKn bBi bQ bK bBi bKn bR
bP bP bP bP bP bP bP bP
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP wP wP wP wP
wR wKn wBi wQ wK wBi wKn wR



Whoever is playing the white pieces will need to go first.


To play you'll need to use the function MovePiece


MovePiece's syntax is MovePiece(piece,row,file)
- Piece is a string, the first move will likely be the pawn or the knight so you would enter in MovePiece("knight",1,2)
- Row is the current row of the piece you want to move
- File is the current file of the piece you want to move

So if you want to use the most common chess opening you'd use MovePiece("pawn", 2 , 5)
Then it should prompt 

Which row would you like to go to? 

Which file would you like to go to? 

Row is from 1-8 from the bottom row with the white pieces to the top with the black pieces as a standard chess board is.
File is also from 1-8 from left to right and does not have alphabet counterparts, in regular chess notation it does.
You can only enter in valid moves, if you don't enter in a valid move then the move will not be registered and you will have to prompt MovePiece again. 



Lets say you want to move the pawn on the 5th file so you enter in

MovePiece("pawn",2,5)

Which row would you like to go to? 3

Which file would you like to go to? 5

bR bKn bBi bQ bK bBi bKn bR
bP bP bP bP bP bP bP bP
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- wP -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi wQ wK wBi wKn wR
 
White turn over

Now it's black's turn, black will enter in the same command MovePiece.

MovePiece("knight",8,7)

Which row would you like to go to? 6

Which file would you like to go to? 6

bR bKn bBi bQ bK bBi -- bR
bP bP bP bP bP bP bP bP
-- -- -- -- -- bKn -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- wP -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi wQ wK wBi wKn wR
 
Black turn over

And you repeat the process until you get a stage in the game where the king can no longer move and is in check.


Here's a 4 move game using the scholars mate


Basic Chess Engine

bR bKn bBi bQ bK bBi bKn bR
bP bP bP bP bP bP bP bP
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP wP wP wP wP
wR wKn wBi wQ wK wBi wKn wR

MovePiece("pawn",2,5)

Which row would you like to go to? 4

Which file would you like to go to? 5

bR bKn bBi bQ bK bBi bKn bR
bP bP bP bP bP bP bP bP
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- wP -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi wQ wK wBi wKn wR
 
White turn over

MovePiece("pawn",7,5)

Which row would you like to go to? 5

Which file would you like to go to? 4
This is not a valid move

MovePiece("pawn",7,5)

Which row would you like to go to? 5

Which file would you like to go to? 5
True
bR bKn bBi bQ bK bBi bKn bR
bP bP bP bP -- bP bP bP
-- -- -- -- -- -- -- --
-- -- -- -- bP -- -- --
-- -- -- -- wP -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi wQ wK wBi wKn wR
 
Black turn over

MovePiece("bishop",1,6)

Which row would you like to go to? 4

Which file would you like to go to? 3
bR bKn bBi bQ bK bBi bKn bR
bP bP bP bP -- bP bP bP
-- -- -- -- -- -- -- --
-- -- -- -- bP -- -- --
-- -- wBi -- wP -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi wQ wK -- wKn wR
 
White turn over

MovePiece("knight",8,2)

Which row would you like to go to? 6

Which file would you like to go to? 3
bR -- bBi bQ bK bBi bKn bR
bP bP bP bP -- bP bP bP
-- -- bKn -- -- -- -- --
-- -- -- -- bP -- -- --
-- -- wBi -- wP -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi wQ wK -- wKn wR
 
Black turn over

MovePiece("queen",1,4)

Which row would you like to go to? 5

Which file would you like to go to? 8
bR -- bBi bQ bK bBi bKn bR
bP bP bP bP -- bP bP bP
-- -- bKn -- -- -- -- --
-- -- -- -- bP -- -- wQ
-- -- wBi -- wP -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi -- wK -- wKn wR
 
White turn over

MovePiece("knight",8,7)

Which row would you like to go to? 6

Which file would you like to go to? 6
bR -- bBi bQ bK bBi -- bR
bP bP bP bP -- bP bP bP
-- -- bKn -- -- bKn -- --
-- -- -- -- bP -- -- wQ
-- -- wBi -- wP -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi -- wK -- wKn wR
 
Black turn over

MovePiece("queen",5,8)

Which row would you like to go to? 7

Which file would you like to go to? 6
bR -- bBi bQ bK bBi -- bR
bP bP bP bP -- wQ bP bP
-- -- bKn -- -- bKn -- --
-- -- -- -- bP -- -- --
-- -- wBi -- wP -- -- --
-- -- -- -- -- -- -- --
wP wP wP wP -- wP wP wP
wR wKn wBi -- wK -- wKn wR
 
White turn over

MovePiece("king",8,5)

Which row would you like to go to? 7

Which file would you like to go to? 6
Invalid Move, King would be in check


MovePiece("king",8,5)

Which row would you like to go to? 7

Which file would you like to go to? 5
Invalid Move, King would be in check


As you can see, after using the scholars mate, black has no legal moves and can no longer progress the game.
A checkmate function has yet to be implemented but the game is over once the king cannot escape checkmate via blocking, taking, or moving and is noted by no matter which move entered, an invalid move is returned by the program

To restart the game simply run the program again.

OTHER FUNCTIONS

MovePiece is not the only function that can be used in the game here are some other ones that the user can do to see what's going on in the game

showwhiteboard() is a command that shows the board from white's perspective. A.K.A The white pieces are at the bottom and it goes from rows 1-8.

showblackboard() is a command that shows the board from black's perspective. A.K.A The black pieces are the the bottom and it goes from rows 8 - 1.

KingCheck() is a commmand that has a boolean output, whosever turn it is, it will check that sides king. if it is True, the king is not in check, if it is False, the king is in check.

This isn't a command but an object, LMC is a list that contains information about the last move done
LMC = [piece, rows direction and amount travelled, file direction and amount travelled, trow, tfile]
trow is the row the piece moved to 
tfile is the file the piece moved to




 
