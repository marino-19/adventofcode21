import sys
import numpy as np

TEST = 'test'

class FuelCalculator():
    def __init__(self, min_position, max_position,step_fine=False):
        self.min_position = min_position
        self.max_position = max_position
        self.step_fine = step_fine

    def get_fuel_array(self, position):
        return [ self.get_walk_cost(abs(i-position)) 
                for i in range(self.min_position,self.max_position+1)]

    def get_walk_cost(self,steps):
        return steps if not self.step_fine else steps*(steps+1)/2
         
class CrabOrganizer():
    def __init__(self, crab_positions, fuel_calculator):
        self.fuel_arrays = []
        for crab_position in crab_positions:
            fuel_array = fuel_calculator.get_fuel_array(crab_position)
            self.fuel_arrays.append(fuel_array)

    def calculate_minimal_fuel(self):
        matrix = np.array(self.fuel_arrays)    
        return np.amin(np.sum(matrix, axis=0))

def get_crab_positions(input_array):
    tmp = input_array[0].split(',')
    return [int(i) for i in tmp]

def puzzle1(input_array, test_indication):
    crab_positions = get_crab_positions(input_array)
    max_pos = np.amax(np.array(crab_positions))
    fuel_calculator = FuelCalculator(0,max_pos,step_fine=False)
    crab_organizer = CrabOrganizer(crab_positions,fuel_calculator)
    i = crab_organizer.calculate_minimal_fuel()
    print(f'nr = {i}')

def puzzle2(input_array, test_indication):
    crab_positions = get_crab_positions(input_array)
    max_pos = np.amax(np.array(crab_positions))
    fuel_calculator = FuelCalculator(0,max_pos,step_fine=True)
    crab_organizer = CrabOrganizer(crab_positions,fuel_calculator)
    i = crab_organizer.calculate_minimal_fuel()
    print(f'nr = {i}')
    

if __name__ == "__main__":
    puzzle_nr = sys.argv[1] 
    test_indication = sys.argv[2] if len(sys.argv) > 2 else None

    if test_indication == TEST:
        read_input_file = open('test_input').readlines()
    else:
        read_input_file = open('input').readlines()
    input_array = [line.strip('\n') for line in read_input_file]

    if puzzle_nr == '1':
        puzzle1(input_array,test_indication)
    else:
        puzzle2(input_array,test_indication) 

