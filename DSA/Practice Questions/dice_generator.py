import random
import logging

def dice_generator():
    dice_nums = ["One", "Two", "Three", "Four", "Five", "Six"]
    dice_number = random.randint(0,6)
    print(dice_nums[dice_number])
    
dice_generator()