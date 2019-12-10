import random
class Agent(): # Create class
    
    # Add functions to class. Init function runs whenever new agent is created.
    def __init__(self, environment, agents, y, x):
        # Create x from web scrape data, use random if missing x value
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        # Create y from web scrape data, use random if missing y value
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
        self.environment = environment
        self.agents = agents
        self.store = 0 # How much each agent has "stored/eaten" at the start
    
     
    def __str__(self):
        """ For representing this as a string
        Returns:
            A string representation
        """
        return "x=" + str(self.x) + ", y=" + str(self.y) + ", store " + str(self.store) # X coord, Y coord and storage amount
    
    # Function to randomly move the agents.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    # Function to "eat" and store the environment.            
    def eat(self): 
        if self.environment[self.y][self.x] > 10: # If RGB/pixel value (in.txt) greater than 10 (they all are)
            self.environment[self.y][self.x] -= 10 # Reduce value by 10 for "in.txt" RGB values / changes the environment colour
            self.store += 10 # Adds 10 to store/amount eaten for each agent
        
            
    # Function to share storage with neighbours
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents: # Loop through the agents in self.agents            
            distance = self.distance_between(agent) # Calculate the distance between self and the current other agent:            
            if distance <= neighbourhood: # If distance is less than or equal to the neighbourhood                
                sum = self.store + agent.store # Sum self.store and agent.store               
                ave = sum /2 # Divide sum by two to calculate average                
                self.store = ave # self.store = average                
                agent.store = ave # agent.store = average
                #print("sharing " + str(dist) + " " + str(ave))

    # Function to create pythag formula to calculate distance between co-ordinates
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    
    
    
    
    
class wolf_agent(): # Create class
    
    # Add functions to class. Init function runs whenever new agent is created.
    def __init__(self, environment, wolf_agents, agents, y, x):
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        self.environment = environment
        self.wolf_agents = wolf_agents
        self.agents = agents
        self.store = 0 # How much each agent has "stored/eaten" at the start
    
    
    # Function to randomly move the agents.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
        
            
    # Function to eat sheep
    def eat_sheep(self, neighbourhood):
        for agent in self.agents: # Loop through the agents in self.agents            
            distance = self.sheep_distance(agent) # Calculate the distance between self and the current other agent:            
            if distance <= neighbourhood: # If distance is less than or equal to the neighbourhood                
                self.agents.remove(agent) # eat agent
                print("sheep eaten")

    # Function to create pythag formula to calculate distance between co-ordinates
    def sheep_distance(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
             