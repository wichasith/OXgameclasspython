#6201012610079 วิชญ์สิฏฐ์ ใช้ศรีทอง
#6201012620104 ธราดล บ้านเนิน
#6201012620201 พีรพัฒน์ อัมพะวัน

class Board :
    def __init__(self) :
        self.board = [["   ","   ","   "],["   ","   ","   "],["   ","   ","   "]]
        self.player = " O "
        self.turn_count = 1
        self.still_play = True
        self.board_show = [[" 1 "," 2 "," 3 "],[" 4 "," 5 "," 6 "],[" 7 "," 8 "," 9 "]]
    def display_board1(self,position) :
        print(position[2][0] + '|' + position[2][1] + '|' + position[2][2])
        print('-----------')
        print(position[1][0] + '|' + position[1][1] + '|' + position[1][2])
        print('-----------')
        print(position[0][0] + '|' + position[0][1] + '|' + position[0][2])

    def display_board2(self,position) :
        print(position[0][0] + '|' + position[0][1] + '|' + position[0][2])
        print('-----------')
        print(position[1][0] + '|' + position[1][1] + '|' + position[1][2])
        print('-----------')
        print(position[2][0] + '|' + position[2][1] + '|' + position[2][2])

    def add_position(self,row,column) :
        self.board[row][column] = self.player
    def change_player(self) :
        if self.player == " O " :
            self.player = " X "
        elif self.player == " X " :
            self.player = " O "
        return self.player
    def check_winner(self) :
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != "   " :
            print(self.player , "is winner ")
            self.still_play = False
            
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != "   " :
            print(self.player , "is winner ")
            self.still_play = False
 
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != "   "  :
            print(self.player , "is winner ")
            self.still_play = False
 
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != "   "  :
            print(self.player , "is winner ")
            self.still_play = False
 
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != "   "  :
            print(self.player , "is winner ")
            self.still_play = False
 
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != "   "  :
            print(self.player , "is winner ")
            self.still_play = False
 
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "   "  :
            print(self.player , "is winner ")
            self.still_play = False
 
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "   "  :
            print(self.player , "is winner ")
            self.still_play = False

        if self.turn_count == 9 and self.still_play == True :
            print("this game is tie")
            self.still_play = False
      
        return self.still_play


    def start_game(self) :
        print("Welcome to OX Game")
        self.display_board1(self.board)
        mode = Input_Processor.mode_checker()
        if(mode == 1) :
            self.display_board1(self.board_show)
        elif(mode == 2) :
            self.display_board2(self.board_show)
        while self.still_play == True :
            print("this is " , self.player , " turn")
            new_position = Input_Processor.input_checker()
            for i in range(1,10) :
                if new_position == i :
                    intinput = new_position - 1
                    row = intinput % 3
                    column = intinput // 3
                    if self.board[column][row] == '   ' :
                        self.board[column][row] = self.player
                        if(mode == 1) :
                            self.display_board1(self.board_show)
                            print("===================")
                            self.display_board1(self.board)
                        elif(mode == 2) :
                            self.display_board2(self.board_show)
                            print("===================")
                            self.display_board2(self.board)
                        self.check_winner()
                        self.turn_count += 1
                        self.player = self.change_player()


class Input_Processor :
    def input_checker() :
        position = int(input("Press number 1-9 here ===> "))
        return position 

    def mode_checker() :
        mode = int(input("which mode do you want numpad(press 1) normal(press 2) ====> "))
        return mode

    def error_check() :
        pass


OX_game = Board()
OX_game.start_game()
