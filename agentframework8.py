import random
import csv


class Agent():
    def __init__ (self, x, y, environment, agentslist):
        self.y = y
        self.x = x
        self.environment = environment
        self.store = 0
        self.agentslist = agentslist
        
            
    def __str__ (self):
        return "y=" + str(self.y) + " x=" + str(self.x)
        
    def move (self,fig):
        fig.clear()
        #print("move")
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
            
    def eat (self): 
        #print("eat")
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
            
    def distance_between(self, agent):
        return (((self.x - self.x)**2) + ((self.y - self.y)**2))**0.5
        
    def share_with_neighbours(self, neighbourhood):
        #print ("sharing")
        for agent in self.agentslist:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print ("sharing " + str(dist) + " " + str(ave))              
              
        

        
        
    