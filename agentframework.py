import random

# create agent class
#agents generated randomly anywhere within a 300x300 square to match environment
# link agents to interact with environment  
class Agent:
    def __init__ (self,environment,agents):
        self.environment = environment
        self.agents = agents #puts agent info inside itself
        self.store = 0
        self._x = random.randint(0,300)      
        self._y = random.randint(0,300)
     

#object orientated protection of x and y - create set and get properties for _x and _y        
    def getx(self):
        return self._x
     
    def setx(self, value):
        self._x = value
        

    def gety(self):
        return self._y
     
    def sety(self, value):
        self._y = value
        

# create info associated with agents
# move x coordinate randomly
# build a torus to stop agents falling off the edge of the environment             
    def move(self):
        if random.random() <0.5:
            self._x = (self._x + 1) %300
        else:
            self._x = (self._x - 1) %300
# move y coordinate randomly
        if random.random() <0.5:
            self._y = (self._y + 1) %300
        else:
            self._y = (self._y - 1) %300
                
    print(move)


# add eat method to agents, when agent eats, store increases by 10
# make agents eat the rest- if environment less than 10, eat one at a time. 
# will only eat if environment more than 0, avoid negative numbers
    def eat(self):
            if self.environment [self._y] [self._x] > 10:
                self.environment [self._y] [self._x] -=10
                self.store += 10
            elif self.environment [self._y] [self._x] >0:
                self.environment [self._y] [self._x] -=1
                self.store += 1
    print(eat)

# make agents vomit if they eat more than 100 units
# avoid re-scaling background colour by vomiting less if environment value would exceed 250
    def vomit(self):      
            if self.store >= 100:
                if self.store + self.environment [self._y] [self._x] <250:
                    self.environment [self._y] [self._x] += (self.store)
                    self.store -= (self.store)
                else: 
                    self.environment [self._y] [self._x] += (250 - self.environment [self._y] [self._x])
                    self.store -= (250 - self.store)
                    
              
                                                
#make a behavioural method allowing neighbour interaction
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
             dist = self.distance_between(agent)
             if dist <= neighbourhood:
                 sum = self.store + agent.store
                 ave = sum/2
                 self.store = ave
                 agent.store = ave
                 #print("sharing" + str(dist) + " " + str(ave))
                 
                     
#pythagoras formula to calculate distance between
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
#loop through the agents in self.agents           
#calculate the distance between self and current other agent
#end if end loop                
  