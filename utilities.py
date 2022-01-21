# make a function that will ask me which file to import and which name should I give to the variable
import os
import pandas as pd

def get_data():
    # this works because I will keep the .py file in the same level as the notebook
    files = os.listdir('data/hollywood_market')
    
    # give the user some feedback
    print('=== AVAILABLE OPTIONS ===\n')
    for index, file in enumerate(files):
        print(f'{index} - {file}')
    
    # ask for an option
    num = int(input('\n which file would you like to load? \n(insert index number)'))
    
    df = pd.read_csv(f'data/hollywood_market/{files[num]}')
    
    # provide user with feedback about his choice
    print(f'\nYou chose {files[num]}')
    
    return df