
close_program = 1

board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]

moves = 0

start = 0

players = [ 'X ' , 'O ' ]

counter = 2

columns = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' ]


def print_board (): # prints the board

    print(' the current board')
    print( '[' , board[0] , ' |' , board[1] , ' |' , board[2] , ' |' , board[3] , ' |' , board[4] , ' |' , board[5] , ' |' , board[6] , ' ]' )
    print( '[' , board[7] , ' |' , board[8] , ' |' , board[9] , '|' , board[10] , '|' , board[11] , '|' , board[12] , '|' , board[13] , ']' )
    print( '[' , board[14] , '|' , board[15] , '|' , board[16] , '|' , board[17] , '|' , board[18] , '|' , board[19] , '|' , board[20] , ']' )
    print( '[' , board[21] , '|' , board[22] , '|' , board[23] , '|' , board[24] , '|' , board[25] , '|' , board[26] , '|' , board[27] , ']' )
    print( '[' , board[28] , '|' , board[29] , '|' , board[30] , '|' , board[31] , '|' , board[32] , '|' , board[33] , '|' , board[34] , ']' )
    print( '[' , board[35] , '|' , board[36] , '|' , board[37] , '|' , board[38] , '|' , board[39] , '|' , board[40] , '|' , board[41] , ']' )
    print( '[' ,'a' , ' |' , 'b' , ' |' , 'c' , ' |' , 'd' , ' |' , 'e' , ' |' , 'f' , ' |' , 'g' , ' ]' )

def mover():

    global moves,start,counter,columns
    moves = input('please choose a column from a to g: ')
    moves = moves.lower()

    if moves not in columns :
        print('invalid input please choose a column from a to g: ')
        mover()
    elif moves == 'a' :
        start = 36
    elif moves == 'b' :
        start = 37
    elif moves == 'c' :
        start = 38
    elif moves == 'd' :
        start = 39
    elif moves == 'e' :
        start = 40
    elif moves == 'f' :
        start = 41
    elif moves == 'g' :
        start = 42
        
    for i in range (0,7) :
        if start in board :
            board[start-1] = players[counter % 2]
            counter += 1
            break
        else : 
            start -= 7

        
def winner(): #checks for  the winner

    global close_program
    if counter > 8 :
            for i in range (0,7) :
                    for j in range (0,3) :
                        if board[ i + (j * 7)] == board[ i + 7 + (j * 7)] and board[ i + (j * 7)] == board[ i + 14 + (j * 7)] and board[ i + (j * 7)] == board[ i + 21 + (j * 7)] :
                            print ('player ' , (counter - 1) % 2 + 1 , ' is the winner')
                            close_program += 1
                            break
            for i in range (0,6) :
                    for j in range (0,4) :
                        if board[ ( i * 7 ) + j ] == board[ ( i * 7 ) + j + 1 ] and board[ ( i * 7 ) + j ] == board[ ( i * 7 ) + j + 2 ] and board[ ( i * 7 ) + j ] == board[ ( i * 7 ) + j + 3 ] :
                            print ('player ' , (counter - 1) % 2 + 1 , ' is the winner')
                            close_program += 1
                            break
            for i in range (0,3) :
                    for j in range (0,4) :
                        if board[( i * 7 ) + j ] == board[( i * 7 ) + j + 8 ] and board[( i * 7 ) + j ] == board[( i * 7 ) + j + 16 ] and board[( i * 7 ) + j ] == board[( i * 7 ) + j + 24 ] :
                            print ('player ' , (counter - 1) % 2 + 1 , ' is the winner')
                            close_program += 1
                            break
            for i in range (0,3) :
                    for j in range (0,4) :
                        if board[ ( 7 * i ) +  6 - j ] == board[ ( 7 * i ) +  6 - j + 6 ] and board[ ( 7 * i ) +  6 - j ] == board[ ( 7 * i ) +  6 - j + 12 ] and board[ ( 7 * i ) +  6 - j ] == board[ ( 7 * i ) +  6 - j + 18 ] :
                            print ('player ' , (counter - 1) % 2 + 1 , ' is the winner')
                            close_program += 1
                            break


def check_column(): # checks if a column is full

    global columns
    for i in range (0,7) :
        if board[i] != i + 1 :
            columns[i] = '????'
            print (columns)





print_board()
while close_program == 1 : #runs the program
    mover()
    print_board()
    winner()
    check_column()