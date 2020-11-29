def find_king_legal_moves(self,coordinates):
    upper_input_letter = coordinates[0].upper()
    get_letter_index = self._letters.index(upper_input_letter)
    get_number_index = int(coordinates[1])-1

    legal_moves_list=[]

    search_depth_min = -1
    search_depth_max = 2

    for letter_row in range(search_depth_min,search_depth_max):
        for column_number in range(search_depth_min,search_depth_max):
            neighbour_square_letter = get_letter_index + letter_row
            neighbour_square_number = get_number_index + column_number

            legal_square = True

            if neighbour_square_letter < 0 or neighbour_square_letter > 7:
                legal_square = False

            if neighbour_square_number <0 or neighbour_square_number > 7:
                legal_square = False

            if legal_square:
                legal_moves_list.append(self._board_grid[neighbour_square_letter][neighbour_square_number])

    refactored_coordinates = upper_input_letter + coordinates[1]
    if refactored_coordinates in legal_moves_list:
        legal_moves_list.remove(refactored_coordinates)

    return legal_moves_list

def print_kings_legal_moves(self, legal_list):
    print (f'King\'s Legal Moves:')
    for each in legal_list:
        print(f'{each}')
