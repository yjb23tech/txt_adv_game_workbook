#print("Then you don't like SEC football!")

class FootballPlayer:

    def __init__(self, str_name, int_age, str_position, arr_special_moves):
        self.str_name = str_name
        self.int_age = int_age
        self.str_position = str_position 
        self.arr_special_moves = arr_special_moves 

    def __str__(self):
        return (f"Name: {self.str_name}, Age: {self.int_age}, Position: {self.str_position}, Special Moves: {self.arr_special_moves}") 

    def birth_year(self): 
        return (2015 - self.age) 

#Meta Methods 

def fp_str_name():
    return input("\nWhat is your name?\n")

def fp_int_age():
    return int(input("\nWhat is your age?\n"))

def fp_str_position():
    return input("\nWhat position do you play?\n")

def fp_arr_special_moves():
    ui_arr_special_moves = [] 
    while (len(ui_arr_special_moves) < 4):
        ui_special_move = input("\nDescribe one of your special moves?\n")
        ui_arr_special_moves.append(ui_special_move)

    i = 1
    print("You have access to the following moves:\n") 
    for special_move in ui_arr_special_moves:
        print(f"{i}. {special_move}")
        i += 1 
    print(" ")
    return (ui_arr_special_moves)

#Create Object
ui_nfl_player = FootballPlayer(fp_str_name(), fp_int_age(), fp_str_position(), fp_arr_special_moves())

#Print Object 
print(f"For our Pro Bowl WR {ui_nfl_player.str_name} we have the following stats:\n{ui_nfl_player}")

        
