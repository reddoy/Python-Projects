"""File: battleship.py

   Author: Rohan O'Malley

   Purpose: The purpose of this program is to create a one-sided
   battleship game. Program creates a board with different types
   of ships on it. Can also print out the board and the current status
   of each of the ships, whether they are sunk or if they are hit or
   missed. Program has 2 main classes: Board and Ship. These 2 interact
   by updating the ship dictionary in the ship class.
"""

class Board:
    '''
    Class builds a one sided battleship. It is in
    x, y grid form. Size is determined by user and
    the ships are added in by the user. This class
    takes information about the status of the ships
    from the Ship class

    Fields:
        - board_size - an integer that user passes in
        to determine how large the grid will be

        - ship_arr - an array which holds all the ship
        objects on the board

        - moves - an array with all the moves
         done by the user, hits and misses
         each element is an x, y tuple

        - miss - an array with all the missed
        shots he user has taken each element
        is an x, y tuple
    
    Methods:
        - add_ship - checks to see if ship is in
        domain and range of board and adds it.

        - print - prints out the current status
        of the board, with the status of the ships
        as well

        - has_been_used - checks to see if the 
        position user is trying to hit has already
        been shot at

        - attempt_move - user's position they want 
        to hit is checked to see if the hit or miss
        at that position and then adds it to the board
    '''
    def __init__(self, size):
        assert size > 0
        self.board_size = size
        self.ship_arr = []
        self.moves = []
        self.miss = []

    def add_ship(self, ship, position):
        '''
        This function checks to see if the x, y coords
        passed in are within the board range and domain.
        Then it will add the ship's location to the board
        and create a dictionary for each spot to hit. Then
        the ship object is added to the ship array.

        Params:
            - ship - a reference to a ship object
            - position- an x, y tuple
        '''
        x = position[0]
        y = position[1]

        assert x < self.board_size
        assert y < self.board_size

        new_dict = {}
        for pos in ship.shape_dict:
            new_x = pos[0] + position[0]
            new_y = pos[1] + position[1]
            new_dict[(new_x, new_y)] = '.'
        
        ship.shape_dict = new_dict
        self.ship_arr.append(ship)
        

    def print(self):
        '''
        Function prints out the current status of
        the board. Prints out X's for sunk ships.
        .'s for unhit spots, o's for missed shots
        and *'s for ships hit. Prints out the whole
        grid according to the board size.

        Params:
            - None
        '''
        y = self.board_size - 1
        top_bot = (self.board_size * 2 + 1)
        print('   +' + '-' * top_bot + '+')

        while y >= 0:

            x = 0
            if y > 9:
                print(f'{y} | ', end = '')
            else:
                print(f' {y} | ', end = '')

            while x <= self.board_size - 1:

                curr_coord = (x,y)

                if self.ship_arr == []:
                    print('. ', end='')
                else:
                    ship_found = False
                    for ship in self.ship_arr:
                        if curr_coord in ship.shape_dict:
                            if ship.shape_dict[curr_coord] == '*':
                                print('* ', end='')
                            elif ship.shape_dict[curr_coord] == 'X':
                                print('X ', end='')
                            else:
                                print(f'{ship.ship_name[0]} ', end='')
                            ship_found = True
                    
                    if curr_coord in self.miss:
                        print('o ', end= '')
                    elif ship_found is False:
                        print('. ', end='')
                    
                x += 1
            print('|')
            y -= 1
        
        print('   +' + '-' * top_bot + '+')

        # prints the bottom x - axis
        y = self.board_size - 1
        print('    ',end='')
        # this runs if the x axis is greater than 10
        if y > 10:
            for space in range(y):
                if space < 10:
                    print('  ',end='')
                else:
                    num = str(space)
                    print(' ' + num[0], end='')
            num = str(y)
            print(f' {num[0]}')

            print('    ',end='')
            for low in range(y):
                if low < 10:
                    print(' ' + str(low), end='')
                else:
                    num = str(low)
                    print(' ' + num[1],end='')
            num = str(y)
            print(f' {num[1]}')
        # runs if x axis is less than 10
        else:
            for space in range(y):
                print(' '+ str(space),end='')
            print(f' {y}')
        


    def has_been_used(self, position):
        '''
        Function takes in an x, y tuple and
        looks to see if the position has already
        been shot at. 

        Params:
            - position - an x, y tuple of a spot on the 
            board user wants to hit
        
        Returns:
            - True - if position has already been shot
            - False - if position has not been shot at yet
        '''
        if position in self.moves:
            return True
        else:
            return False

    def attempt_move (self, position):
        '''
        Function checks to see if a move can
        be completed. If so position will
        update if current position sunk a ship,
        missed a shot or hit a ship

        Params:
            - position - an x, y tuple of position
            user wants to move on
        
        Returns:
            - Hit - a string if ship has been hit
            - Miss - a string if no ship was hit
            - Sunk {ship name} - string if ship has 
            been shot and sunk
        '''
        assert position[0] <= self.board_size - 1
        assert position[1] <= self.board_size - 1
        assert self.has_been_used
        
        # if position hits a ship or not
        hit = False
        for ship in self.ship_arr:
            if position in ship.shape_dict:
                hit = True
                self.moves.append(position)
                ship.shape_dict[position] = '*'
                sunk = True
                for mark in ship.shape_dict:
                    if ship.shape_dict[mark] != '*':
                        sunk = False
                if sunk is True:
                    for pos in ship.shape_dict:
                        ship.shape_dict[pos] = 'X'
                    return f'Sunk ({ship.ship_name})'
                else:
                    return 'Hit'
                
        
        # if position had no ships then it is a miss
        if hit is False:
            self.moves.append(position)
            self.miss.append(position)
            return 'Miss'



def shape_convert (shape_list):
    '''
    Function takes in a list of 
    x, y tuples and maps each 
    tuple to a '.' to set up the 
    dicitonary

    Params:
        - shape_list - an array of tuples
        that are positions of the current 
        ship object
    
    Returns:
        - shape_dict - a dictionary that has
        the tuples mapped to a '.'
    '''
    shape_dict = {}

    for tup in shape_list:
        shape_dict[tup] = '.'

    return shape_dict 

class Ship:
    '''
    Class creates an Ship object with its name,
    and a list of tuples that are locations of 
    points on a ship in an x, y coordinate grid

    Fields:
        - ship_name - the name of the ship passed in

        - shape_dict - a dictionary of all the tuples
        positions mapped to unhit marker: '.'

        - shape_list - array of tuples positions
    
    Constructor:
        - Builds a single ship object

    Methods:
        - print (self) - prints the current status
        of the ship in its first letter and where it
        has been hit

        - is_sunk (self) - checks to see if all
        positions on a ship have been hit

        - rotate (self, amount) - will rotate the ship
        object 90 degrees for the amount passed in
    '''
    def __init__(self, name , shape):

        self.ship_name = name
        self.shape_dict = shape_convert(shape)
        self.shape_list = shape

    def print(self):
        '''
        Function prints out the status
        of ship. Prints out first letter
        of name or an * if the spot has
        been hit.
        '''
        letter = self.ship_name[0]
        ship_letters = ''

        for key, value in self.shape_dict.items():
            if value == '*' or value == 'X':
                ship_letters += '*'
            else:
                ship_letters += letter
        spaces = ' ' * (10 - len(ship_letters))
        print(f'{ship_letters}{spaces}{self.ship_name}')

    def is_sunk (self):
        '''
        Function checks each position in the 
        shape_dict and sees if all the positions
        have been hit. If so boolean is returned

        Returns:
            - True - if all positions in the
            dictionary are hit the ship is sunk

            - False - if not all the positions 
            have not been hit ship is not sunk
        '''
        for pos in self.shape_dict:
            if self.shape_dict[pos] != 'X':
                return False
        return True

    def rotate (self, amount):
        '''
        Function takes a ship and rotates it's current
        positions by 90 degrees. For however many times
        is said by the amount passed in up until 3
        the positions will be rotated. 90, 180, or 
        270

        Params:
            - amount - an integer eithier:
            0, 1, 2, 3, determines how many 
            times the positions will be rotated
        '''
        assert amount >= 0 and amount < 4

        rotated_list = []
        if amount == 1:
            for pos in self.shape_list:
                new_x = pos[1]
                new_y = pos[0] * -1
                rotated_list.append((new_x, new_y))
        
        elif amount == 2:
            for pos in self.shape_list:
                new_x = pos[0] * -1
                new_y = pos[1] * -1
                rotated_list.append((new_x, new_y))

        elif amount == 3:
            for pos in self.shape_list:
                new_x = pos[1] * -1
                new_y = pos[0]
                rotated_list.append((new_x, new_y))
        elif amount == 0:
            rotated_list = self.shape_list
        
        self.shape_dict = shape_convert(rotated_list)




        

