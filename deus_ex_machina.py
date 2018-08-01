#!/usr/bin/env python3

import numpy as np

class DeusExMachina:
    
    input_dict = {
            'stop' : 'stopped',
            'start' : 'started',
            'collect' : 'collecting',
            'process' : 'processing'
            }
    
    def __init__(self):
        self.previous = 'none'
        self.current = 'stopped'

    def getPreviousState(self):
        return self.previous

    def getCurrentState(self):        
        return self.current
    
    def setCurrentState(self, user_input, user):
        new_input = self.input_dict.get(user_input, 'none')
        
        if new_input != 'none':
            if self.getCurrentState() == user_input:
                print('Same state.')
                return False
            elif (self.getCurrentState() == 'stopped') & (user_input == 'start'):
                self.previous = self.current
                self.current = new_input
                return True
            elif (self.getCurrentState() == 'started') & ((user_input == 'collect')or(user_input == 'stop')):
                self.previous = self.current
                self.current = new_input
                return True
            elif (self.getCurrentState() == 'collecting') & ((user_input == 'process')or(user_input == 'stop')):
                self.previous = self.current
                self.current = new_input
                return True
            elif (self.getCurrentState() == 'processing') & ((user_input == 'stop')or
                  ((user_input == 'collect')&(not user))):
                self.previous = self.current
                self.current = new_input
                return True
            else:
                print('Invalid input.')
                return False          
        else:
            print('Invalid input.')
            return False            

    def collectData(self):
        #print('Collecting...')
        if self.current != 'collecting':
            print('Can not collect outside collecting state.')
            return False
        
        matrix = np.random.uniform(low=1, high=9, size=(3,3))
        
        print(matrix)
        
        user_input = input('Do you want to continue to processing stage? yes/no: ')
        while (user_input != 'yes') & (user_input != 'no'):
            user_input = input('Do you want to continue to processing stage? yes/no: ')        
        if user_input == 'yes':
            self.setCurrentState('process', False)
            self.processData(matrix)
            
        return matrix
            
    def info(self):
        print('current = ', self.current)
        print('previous = ', self.previous)
        print('current -> gives current state.\nprevious -> gives previous state.\n(action) -> set machine to new state')
    
    def processData(self, matrix):
        #print('Processing...')
        if self.current != 'processing':
            print('Can not process outside processing state.')
            return False
        matrix = (matrix*5).transpose()
        print(matrix)
        
        user_input = input('Do you want to continue to collecting stage? yes/no: ')
        while (user_input != 'yes') & (user_input != 'no'):
            user_input = input('Do you want to continue to collecting stage? yes/no: ')  
        if user_input == 'yes':
            self.setCurrentState('collect', False)
            self.collectData()
        return True
        
new_DeusEx = DeusExMachina()
user_input = input('Enter a valid command(help): ')
while user_input != 'exit':
    if user_input == 'help':
        new_DeusEx.info()
    elif (user_input == 'current'):
        print(new_DeusEx.getCurrentState())
    elif (user_input == 'previous'):
        print(new_DeusEx.getPreviousState())
    else:
        vrf = new_DeusEx.setCurrentState(user_input, True)
        if (user_input == 'collect') & vrf:
            matrix = new_DeusEx.collectData()
        elif (user_input == 'process') & vrf:
            new_DeusEx.processData(matrix)
    user_input = input('Enter a valid command(help): ')
    