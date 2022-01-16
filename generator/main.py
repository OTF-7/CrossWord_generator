from utilities.terminal_colors import Fore as f, Back as b, Style as s
from generator.generator import Generator

cross_word_letters = [["Y", "E", "M", "E", "N", "-"],
                      ["E", "A", "S", "Y", "-", "F"],
                      ["A", "-", "-", "-", "-", "R"],
                      ["R", "I", "N", "G", "-", "O"],
                      ["-", "_", "F", "R", "O", "G"],
                      ["A", "H", "M", "E", "D", "-"]]


def main():
    global cross_word_letters
    g = Generator()
    cross_word_letters = g.generate(cross_word_letters)
    print_crossword()


def print_crossword():
    print(f"""
        {f.BLUE}                        0      1      2      3      4      5   {f.RESET} 
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


if __name__ == "__main__":
    main()
