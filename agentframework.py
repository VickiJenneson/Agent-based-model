import random

# create agent class
# link agents to interact with environment  
class Agent:
    def __init__ (self,environment,agents):
        self.environment = environment
        self.agents = agents #puts agent info inside itself
        self.store = 0
        self.x = random.randint(0,100)      
        self.y = random.randint(0,100)
#how to protect these using set and get?

#how to randomly shuffle order of agent list?
#sample(x, k=len(x))

# create info associated with agents
# move x coordinate randomly
# build a torus to stop agents falling off the edge of the environment             
    def move (self):
            if random.random() <0.5:
                self.x = (self.x + 1) %100
            else:
                self.x = (self.x - 1) %100
# move y coordinate randomly
            if random.random() <0.5:
                self.y = (self.y + 1) %100
            else:
                self.y = (self.y - 1) %100
                
    #print(move)


# add eat method to agents, when agent eats, store increases by 10
    def eat(self):
            if self.environment [self.y] [self.x] > 10:
                self.environment [self.y] [self.x] -=10
                self.store += 10
    #print(eat)

          
                                      
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
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
#loop through the agents in self.agents           
#calculate the distance between self and current other agent
#end if end loop                
  