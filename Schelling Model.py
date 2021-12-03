import random
import matplotlib.pyplot as plt
from IPython import display
import time

random.seed(32) # seed for reproducible random numbers
group_affinity_threshold = .51

class Agent():
    def __init__(self, xlocation, ylocation):
        self.x = xlocation
        self.y = ylocation
        

agent1 = Agent(22, 55)
agent2 = Agent(66, 88)


def map_all_agents(listofagents):
    agents_XCoordinate = [] # empty list that will store our X-coordinates
    agents_YCoordinate = [] # empty list that will store our y-coordinates
    
    # use a for loop to add all the x attributes from the list of objects to the agents_XCoordinate list and all the y attributes from the list of objects to the agents_YCoordinate list
    for agent in agents_list:
      agents_XCoordinate.append(agent.x)
      agents_YCoordinate.append(agent.y)

    fig, ax = plt.subplots(figsize = (5, 5))
    ax.set_facecolor('azure')
    ax.plot(agents_XCoordinate, agents_YCoordinate, 'o', markerfacecolor = 'purple')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()
    

agents_list = [agent1, agent2]


def moveagents(listofagents):
    for each_agent in listofagents:
        each_agent.x = random.randint(0,100)
        each_agent.y = random.randint(0,100)
        

def make_agents_dance(agentslist, num_steps = 10):
    #random.seed(66)
    for i in range(0, num):
        moveagents(list_of_agents)
        map_all_agents(list_of_agents)
        time.sleep(1)
        display.clear_output(wait = True)
        

New_List_of_Agents = [Agent(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 12)]


class AgentNew(Agent):
    def __init__(self, xlocation, ylocation, group, status = "unhappy"):
        super().__init__(xlocation, ylocation)
        self.group = group
        self.status = status


# The class AgentNew randomly picks whether an agent will be purple or gold.
# We create two subclasses of AgentNew to specify the color of an agent.

class PurpleAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group = "Purple", status = "unhappy"):
        super().__init__(xlocation, ylocation, group, status = "unhappy")
        
class GoldAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group = "Gold", status = "unhappy"):
        super().__init__(xlocation, ylocation, group, status = "unhappy")


b1 = PurpleAgents(3,6)
b2 = GoldAgents(6,3)
print(b1.group)
print(b2.group)


random.seed(15)
List_of_PurpleAgents = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 12)]  # uses list comprehension to make 12 PurpleAgents
List_of_GoldAgents = [GoldAgents(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 12)] # uses list comprehension to make 12 GoldAgents
CombinedList = List_of_PurpleAgents + List_of_GoldAgents


def map_colorful_agents(agentlist):
    Purple_XCoordinate = [agent.x for agent in agentlist if agent.group == "Purple"]
    Purple_YCoordinate = [agent.y for agent in agentlist if agent.group == "Purple"]
    Gold_XCoordinate = [agent.x for agent in agentlist if agent.group == "Gold"]
    Gold_YCoordinate = [agent.y for agent in agentlist if agent.group == "Gold"]

    fig, ax = plt.subplots(figsize = (5, 5))
    ax.set_facecolor('azure')
    ax.plot(Purple_XCoordinate, Purple_YCoordinate, 'o', markerfacecolor='purple')
    ax.plot(Gold_XCoordinate, Gold_YCoordinate, 'o', markerfacecolor='gold')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()


map_colorful_agents(CombinedList)


# We create a new method to AgentNew that allows agents to move if they are unhappy.

random.seed(38)


class AgentNew(Agent):
    def __init__(self, xlocation, ylocation, group, status = "unhappy"):
        super().__init__(xlocation, ylocation)
        self.group = group
        self.status = status

    def move_if_unhappy(self):
        if self.status == "unhappy":
            self.x = random.randint(0, 100)
            self.y = random.randint(0, 100)


a55 = AgentNew(24, 11, "Purple")
55.move_if_unhappy()
print(a55.x)


# Class method 'check_neighbors' will identify the agents that are within 10 x-coordinate AND 10 y-coordinate spaces of a given agent.
# Once those agents are identified, we'll calculate if enough of them are of the same group to meet our pre-determined threshold.

class AgentNew(Agent):

    def __init__(self, xlocation, ylocation, group, status = "unhappy"):
        super().__init__(xlocation, ylocation)
        self.group = group
        self.status = status

    def move_if_unhappy(self):
        if self.status == "unhappy":
            self.x = random.randint(0, 100)
            self.y = random.randint(0, 100)

    def check_neighbors(self, agentlist, group_affinity_threshold):
        # first get the distance between them then filter out the ones that aren't within 10 spaces far
        zlist = list(filter(lambda a: abs(a.x - self.x) <= 10, agentlist)) # use a filter and a lambda function to find all agents in a list who are within 10 spaces in the X direction of the agent that is calling the method
        zlist = list(filter(lambda a: abs(a.y - self.y) <= 10, zlist)) # filter for agents within 10 spaces in the y direction
        
        same_group_neighbor =  [agent for agent in zlist if agent.group == self.group] # use list comprehension to only keep members of zlist who are of the same group as this agent
        opposite_group_neighbor = [agent for agent in zlist if agent.group != self.group] # use list comprehension to only keep members of zlist who are of the opposite group as this agent
        
        #print(len(same_group_neighbor), "same group neighbors,", len(opposite_group_neighbor), "opposite group neighbors, and", len(zlist), "total neighbors" ) # diagnostic to make sure its working
        
        if (len(same_group_neighbor) + .01)/(len(zlist) + .01) > group_affinity_threshold: # check the percentage of same group neighbors against some threshold to determine the agents' happiness
            self.status = "happy"
        else:
            self.status = "unhappy"
       
       
a55 = AgentNew(24, 11, "Purple")
a55.check_neighbors(CombinedList, 10)


# Child classes need to be defined again to put new AgentNew methods into effect

class PurpleAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group = "Purple", status = "unhappy"):
        super().__init__(xlocation, ylocation, group, status = "unhappy")
    
    #def move_if_unhappy(self):
    #    super().move_if_unhappy()

    #def check_neighbors(self, agentlist, group_affinity_threshold):
    #    super().check_neighbors(agentlist, group_affinity_threshold)
        
        
class GoldAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group = "Gold", status = "unhappy"):
        super().__init__(xlocation, ylocation, group, status = "unhappy")
        
    #def move_if_unhappy(self):
    #    super().move_if_unhappy()

    #def check_neighbors(self, agentlist, group_affinity_threshold):
    #    super().check_neighbors(agentlist, group_affinity_threshold)
        

random.seed(34)
p32 = PurpleAgents(14,55)
p32.move_if_unhappy()
print(p32.x)


# Now we're ready to put it all together and run a few simulations.
# First, let's run a simulation in which there are 200 Purple agents and
# 200 Gold agents.
# Notice the group_affinity_threshold is set at .51.
# This means each purple or gold agent wants to be in a 'block' in which they
# are in the majority group.
# What happens after 15 turns?

random.seed(2021)
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 200)] + [GoldAgents(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 200)] # create a testlist that has 200 PurpleAgents and 200 GoldAgents
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist, group_affinity_threshold)
    for agent in (testlist):
        agent.move_if_unhappy()
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)


# What happens if we run it again but with a threshold of only 0.4?
# Let's run this simulation with 400 of each type of agent.

random.seed(202)
group_affinity_threshold = .4
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 400)] + [GoldAgents(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 400)] # create a testlist that has 400 PurpleAgents and 400 GoldAgents
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist, group_affinity_threshold)
    for agent in (testlist):
        agent.move_if_unhappy()
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)


# Even if people don't mind being a minority in their neighborhood, you still
# get segregation pretty easily according to this model. For a long time models
# such as this were used to argue that some degree of segregation was
# inevitable, and therefore it should not be a target of policy.

# Let's challenge that assumption.
# Make 2 new subclasses, 'PurpleDiversitySeekers' and 'GoldDiversitySeekers'.
# Please use those exact names to allow for autograding.
# For these subclasses, make them seek out diversity instead of avoid it.
# Run some simulations with 300 traditional PurpleAgents, 300 traditional
# GoldAgents, 100 PurpleDiversitySeekers, and 100 GoldDiversitySeekers.
# What happens now?

class PurpleDiversitySeekers(AgentNew):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status="unhappy")
    
    # polymorphism
    def check_neighbors(self, agentlist, group_affinity_threshold):
        
        # first get the distance between them then filter out the ones that aren't within 10 spaces far
        zlist = list(filter(lambda a: abs(self.x - a.x) < 10, agentlist)) # use a filter and a lambda function to find all agents in a list who are within 10 spaces in the X direction of the agent that is calling the method
        zlist = list(filter(lambda a: abs(self.y - a.y) < 10, zlist)) # filter for agents within 10 spaces in the y direction
        
        same_group_neighbor =  [agent for agent in zlist if agent.group != self.group] # use list comprehension to only keep members of zlist who are of the same group as this agent
        opposite_group_neighbor = [agent for agent in zlist if agent.group == self.group] # use list comprehension to only keep members of zlist who are of the opposite group as this agent
        
        #print(len(same_group_neighbor), "same group neighbors,", len(opposite_group_neighbor), "opposite group neighbors, and", len(zlist), "total neighbors" ) # diagnostic to make sure its working
        
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold: # check the percentage of same group neighbors against some threshold to determine the agents happiness
            self.status = "happy"
        else:
            self.status = "unhappy"
        
        
class GoldDiversitySeekers(AgentNew):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status="unhappy")

    # polymorphism
    def check_neighbors(self, agentlist, group_affinity_threshold):
        
        # first get the distance between them then filter out the ones that aren't within 10 spaces far
        zlist = list(filter(lambda a: abs(self.x - a.x) < 10, agentlist)) # use a filter and a lambda function to find all agents in a list who are within 10 spaces in the X direction of the agent that is calling the method
        zlist = list(filter(lambda a: abs(self.y - a.y) < 10, zlist)) # filter for agents within 10 spaces in the y direction
        
        same_group_neighbor =  [agent for agent in zlist if agent.group != self.group] # use list comprehension to only keep members of zlist who are of the same group as this agent
        opposite_group_neighbor = [agent for agent in zlist if agent.group == self.group] # use list comprehension to only keep members of zlist who are of the opposite group as this agent
        
        #print(len(same_group_neighbor), "same group neighbors,", len(opposite_group_neighbor), "opposite group neighbors, and", len(zlist), "total neighbors" ) # use this as a diagnostic to make sure its working
        
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold: # check the percentage of same group neighbors against some threshold to determine the agents happiness
            self.status = "happy"
        else:
            self.status = "unhappy"
            
            
random.seed(11)
group_affinity_threshold = .51
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 300)] + [GoldAgents(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 300)] + [PurpleDiversitySeekers(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 100)] + [GoldDiversitySeekers(random.randint(0,100), random.randint(0,100)) for each_agent in range(0, 100)]
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist, group_affinity_threshold)
    for agent in (testlist):
        agent.move_if_unhappy()
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait = True)
