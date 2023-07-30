#print("Working through my progressions concerning Classes and Objects")

class ProBaller:

    def __init__(self, str_name, int_age, str_position, arr_special_moves):
        self.str_name = str_name 
        self.int_age = int_age 
        self.str_position = str_position 
        self.arr_special_moves = arr_special_moves 

    def birth_year(self):
        return (2023 - self.age)


def pb_str_name():
    return input("\nWhat is your name?\n")

def pb_int_age():
    return int(input("\nHow old are you?\n"))

def pb_str_position():
    return input("\nWhat is your position?\n")

def pb_arr_special_moves():
    ui_arr_special_moves = [] 
    while (len(ui_arr_special_moves) < 3):
        ui_special_move = input("\nWhat is your special move?\n")
        ui_arr_special_moves.append(ui_special_move)

    print("Here is a description of your special moves:\n")
    for i, value in enumerate(ui_arr_special_moves, 1):
        print(f"{i}. {value}")

    return ui_arr_special_moves 


carmeo_anthony = ProBaller(pb_str_name(), pb_int_age(), pb_str_position(), pb_arr_special_moves())

    
