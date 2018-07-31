#!/usr/bin/env python3
import numpy as np

class DeusExMachina:
    """
    42
    """
    def __init__(self):
        self.started = False
        self.collecting = False
        self.stopped = True
        self.processing = False
        self.previous = 'none'
        self.current = 'stopped'

    def getPreviousState(self):
        return self.previous

    def getCurrentState(self):        
        return self.current
    
    def setInput(self, input):
        if input == 'stop':
            return 'stopped'
        elif input == 'start':
            return 'started'
        elif input == 'collect':
            return 'collecting'
        elif input == 'process':
            return 'processing'
        else:
            return 'False statment.'
        
    
    
    def setCurrentState(self, user_input):
        new_input = self.setInput(user_input)
        #print(new_input)
        if self.getCurrentState() == new_input:
            print('Input equals to current state.')    
            return False
        if (user_input == 'start') & (self.current=='stopped'):
            self.started = True
        elif (user_input == 'collect') & ((self.current=='started') or (self.current=='processing')):
            self.collecting = True
        elif user_input == 'stop':
            self.stopped = True
        elif (user_input == 'process') & (self.current=='collecting'):
            self.processing = True
        else:
            print('Invalid input.')
            return False
        
        #print('setting ' + self.current + ' to false.')
        #set previous to false
        if self.current == 'started':
            self.started = False
        elif self.current == 'collecting':
            self.collecting = False
        elif self.current == 'stopped':
            self.stopped = False
        elif self.current == 'processing':
            self.processing = False
            
        self.previous = self.current
        self.current = new_input
        
        '''
        if self.current == 'collecting':
            matrix = self.collectData()
        elif self.current == 'processing':
            self.processData(matrix)
        '''
        
        
        #print('Set state to ' + self.current + '.')
        return True
            

    def collectData(self):
        #print('Collecting...')
        if self.collecting == False:
            print('Can not collect outside collecting state.')
            return
        matrix = np.random.uniform(low=1, high=9, size=(3,3))

        #self.setCurrentState('process')
        
        print(matrix)
        
        user_input = input('Do you want to continue do processing stage? yes/no: ')
        if user_input == 'yes':
            self.setCurrentState('process')
            self.processData(matrix)
            
        return matrix
            
    def info(self):
        print('started = ', self.started)
        print('stoped = ', self.stopped)
        print('collecting = ', self.collecting)
        print('processing = ', self.processing)
        print('current = ', self.current)
        print('previous = ', self.previous)
    
    def processData(self, matrix):
        #print('Processing...')
        if self.processing == False:
            print('Can not process outside processing state.')
            return False
        matrix = (matrix*5).transpose()
        print(matrix)
        
        user_input = input('Do you want to continue do collecting stage? yes/no: ')
        if user_input == 'yes':
            self.setCurrentState('collect')
            self.collectData()
        self.setCurrentState('stop')
        return True
        
new_DeusEx = DeusExMachina()
user_input = input('Choose next stage: ')
while user_input != 'fim':
    if user_input == 'info':
        new_DeusEx.info()
        
    else:
        vrf = new_DeusEx.setCurrentState(user_input)
        if (user_input == 'collect') & vrf:
            new_DeusEx.collectData()
        elif (user_input == 'process') & vrf:
            matrix = input('Input matrix: ')
            new_DeusEx.processData(matrix)
    user_input = input('Choose next stage: ')
    