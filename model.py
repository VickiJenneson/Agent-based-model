import random
#import operator #helps us to select the second element of a list 
import matplotlib.pyplot #as plt #used to display data on a graph
import agentframework
import csv
#import sys
import matplotlib.animation 


#read in environment data from text file (f) using CSV reader
f = open ("in.txt", newline='')
reader= csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)


#create command line arguments- allows us to input values in command line 
#num_of_agents = int(sys.argv[1])
#num_of_iterations = int(sys.argv[2])
#neighbourhood = int(sys.argv[3])
#agents = []

#command line interprets everything as characters
#must define arguments as integers
#prints labels for numbers in command line
#print('{0} agents, {1} iterations, {2} neighbourhood'.format(num_of_agents, num_of_iterations, neighbourhood))


# define number of agents and iterations
num_of_agents = 20
num_of_iterations = 200
neighbourhood = 40
# create a list for agents
agents = [] 


#make an animated model
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)


#create environment list
environment = []
for line in reader: #each line in the file
    rowlist = [] #create a row list
    for value in line: #each number in the line
        rowlist.append(value) #add to the row list
# add row lists together to create the environment
#this needs to sit within line block         
    environment.append(rowlist)

# get list of agents into each agent
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents)) #puts environment info into each agent
   
#activate the agent methods
for j in range(num_of_iterations):
    random.shuffle(agents) 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours
        agents[i].vomit()
        agents[i].distance_between
 
 
#carry_on = True
#create animation
def update(frame_number):      
    
    fig.clear()
     
    global carry_on
    
    for i in range(num_of_agents):
        if random.random()<0.5:
            agents[i]._x=(agents[i]._x+1)%300
        else:
            agents[i]._x=(agents[i]._x-1)%300
            
        if random.random()<0.5:
            agents[i]._y=(agents[i]._y+1)%300
        else:
            agents[i]._y=(agents[i]._y-1)%300
            
        if random.random() < 0.1:
            carry_on = False
            print("stopping condition")
            
   
    matplotlib.pyplot.imshow(environment)#show environment being nibbled away        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
        matplotlib.pyplot.show()

           
# create a stopping function  
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#show end coordinates for all agents
print("Agent endpoints:")
for i in range(num_of_agents):
    print(agents[i]._x,agents[i]._y)
       
#animate indefinitely
#animation=matplotlib.animation.FuncAnimation(fig,update,interval=1)
        
#stop animation from iterating indefinitely (limit to 10)
animation = matplotlib.animation.FuncAnimation(fig,update,interval=1,repeat=False,frames=10)
#plot the agents and show changes in envrionment
matplotlib.pyplot.show()
fig.show()     


"""
for agent0 in agents:
    for agent1 in agents:
        distance = agents[i].distance_between(agent0,agent1)
"""                  

#work out total consumption of agents, amount in store  
#consumption is starting store (0) + amount eaten        
consumption = 0
for i in range (num_of_agents):
    consumption=(consumption + agents[i].store)
print("Total consumption:", consumption)
     
#close the file           
f.close()     
        
    
#write out the environment as a file. Opens in Excel
#stores file in same directory automatically
f2= open('environmnentout.csv', 'a', newline='')   
writer = csv.writer(f2, delimiter=',')
#adding a comma in delimiter allows each number to go in different cells in Excel
for row in environment:
    writer.writerow(row)
    
f2.close() 






