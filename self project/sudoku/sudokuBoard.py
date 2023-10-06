class SudokuBoard(object):
    def __init__(self, board_file):
        self.board = self.__create_board(board_file)

    def __create_board(self, board_file):
        board = []
        for i in range(1, 10):
            if len(board_file[i]) != 9:
                board = []
                print("Mỗi dòng trong sudoku phải có 9 kí tự")
            #thêm 1 list cho mỗi dòng
            board.append([])
            #lặp qua từng kí tự trong để thêm vào list
            for c in board_file[i]:
                if not c.isdigit():
                    print("Giá trị trong mỗi ô từ 0 - 9")
                #thêm vào hàng cuối
                board[-1].append(int(c))
        
        if len(board) != 9:
            print("Mỗi màn sudoku phải có 9 dòng")

        return board