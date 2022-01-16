from utilities.questions import words_list
import random
from utilities.terminal_colors import Fore as f, Back as b, Style as s

cross_word_letters = [["-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-"]]
indexed_word_list = []
question_list = []
row_index = column_index = 0
direction = True


def print_crossword():
    print(f"""

                        {f.CYAN}{s.BRIGHT}{question_list}{f.RESET}{s.RESET_ALL}
        
        {f.BLUE}                         0      1      2      3      4      5   {f.RESET} 
                        ------------------------------------------------
                         {f.RED}0{f.RESET}   |   {f.MAGENTA}{cross_word_letters[0][0]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[0][1]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[0][2]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[0][3]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[0][4]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[0][5]}{f.RESET}  | 
                             |------|------|------|------|------|------|     
                         {f.RED}1{f.RESET}   |   {f.MAGENTA}{cross_word_letters[1][0]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[1][1]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[1][2]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[1][3]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[1][4]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[1][5]}{f.RESET}  |  
                             |------|------|------|------|------|------|    
                         {f.RED}2{f.RESET}   |   {f.MAGENTA}{cross_word_letters[2][0]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[2][1]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[2][2]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[2][3]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[2][4]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[2][5]}{f.RESET}  |  
                             |------|------|------|------|------|------| 
                         {f.RED}3{f.RESET}   |   {f.MAGENTA}{cross_word_letters[3][0]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[3][1]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[3][2]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[3][3]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[3][4]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[3][5]}{f.RESET}  |   
                             |------|------|------|------|------|------|    
                         {f.RED}4{f.RESET}   |   {f.MAGENTA}{cross_word_letters[4][0]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[4][1]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[4][2]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[4][3]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[4][4]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[4][5]}{f.RESET}  | 
                             |------|------|------|------|------|------|      
                         {f.RED}5{f.RESET}   |   {f.MAGENTA}{cross_word_letters[5][0]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[5][1]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[5][2]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[5][3]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[5][4]}{f.RESET}  |   {f.MAGENTA}{cross_word_letters[5][5]}{f.RESET}  |      
                         -----------------------------------------------

    """)


def initialize():
    for l in "abcdefghijklmnopqrstuvwxyz":
        sub_dict = dict()
        answers = list()
        for d in words_list:
            answer, question = d.values()
            if str(answer).startswith(l):
                answers.append(answer)
        if len(answers) > 0:
            sub_dict[l] = answers
            indexed_word_list.append(sub_dict)


def swap():
    global row_index, column_index
    temp = row_index
    row_index = column_index
    column_index = temp


class Generator:
    def __init__(self):
        pass

    @staticmethod
    def generate():
        initialize()
        global row_index, column_index, direction
        while words_list:
            dictionary = dict(random.choice(words_list))
            answer, question = dictionary.values()
            words_list.remove(dictionary)
            Generator.fill(answer)
            question_list.append({question, f"from ({row_index}) to (" + str(len(answer) - 1) + ")"})
            row_index += 1
            if row_index == 6:
                row_index = 0
            break
        print_crossword()

    @staticmethod
    def fill(word):
        global cross_word_letters, row_index, column_index, direction
        if not direction:
            swap()
        for x in word:
            cross_word_letters[row_index][column_index] = x
            column_index += 1
        if column_index < 5:
            column_index += 1
            cross_word_letters[row_index][column_index] = "-"
        column_index = 0
        if not direction:
            direction = not direction
            swap()

    @staticmethod
    def check(word, row_index, column_index):
        return True

