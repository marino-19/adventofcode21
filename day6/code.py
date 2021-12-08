import sys
import numpy as np

TEST = 'test'

RESET_TIME = 6
REPRODUCE_TIME = -1
NEWBORN_TIME = 8

def get_initial_fish_list(input_array):
    tmp =  input_array[0].split(",")
    return [int(i) for i in tmp]

class FishTimeLapse():
    def __init__(self, initial_fish_time_list):
        self.fish_stack = self.convert_to_fish_stack(initial_fish_time_list)
        self.day = 0

    def convert_to_fish_stack(self, fish_time_list):
        fish_stack = [0 for i in range(NEWBORN_TIME+1)]
        for fish_time in fish_time_list:
            fish_stack[fish_time] +=1
        return fish_stack

    def tick(self):
        new_stack = self.fish_stack[1:]
        nr_reproducing_fish = self.fish_stack[0]
        new_stack.append(nr_reproducing_fish)
        new_stack[RESET_TIME] += nr_reproducing_fish
        self.fish_stack = new_stack
        self.day +=1

    def fast_forward(self,target_day):
        nr_ticks = target_day - self.day
        for i in range(nr_ticks):
            self.tick()

    def get_fish_count(self):
        return sum(self.fish_stack)


def puzzle1(input_array, test_indication):
    fish_list = get_initial_fish_list(input_array)
    time_lapse = FishTimeLapse(fish_list)
    if test_indication:
        time_lapse.fast_forward(18)
    else:
        time_lapse.fast_forward(80)
    print(f'nr = {time_lapse.get_fish_count()}')

def puzzle2(input_array, test_indication):
    fish_list = get_initial_fish_list(input_array)
    time_lapse = FishTimeLapse(fish_list)
    if test_indication:
        time_lapse.fast_forward(256)
    else:
        time_lapse.fast_forward(256)
    print(f'nr = {time_lapse.get_fish_count()}')
    




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

