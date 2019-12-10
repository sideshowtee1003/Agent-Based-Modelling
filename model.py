import agentframework
import csv
import matplotlib
import tkinter as tk
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import random
import requests
import bs4


num_of_moves = 2 # variable for how many times agent moves before refreshing
num_of_iterations = 100 # variable for total number of iterations between each refresh
neighbourhood = 1
agents = []
wolf_agents = []


# Download and print y and x data from webpage
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


# Read in file and assign to 'dataset' variable
f = open('in.txt', newline='')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) # Second argument converts to float


environment = [] # Create empty list for environment


for row in dataset: # Loop through dataset for a list of rows
    rowlist = [] # Create empty list for row data
    for value in row: # Loop through dataset for a list of values
        rowlist.append(value) # Append values to the rowlist
    environment.append(rowlist) # Append rowlist data into environment list
        # print(value) # As Floats
f.close()    
   
  
carry_on = True


def update(frame_number): # frame_number is a required parameter of the update function
    
    fig.clear() # Refreshes screen and removes previous frame
    global carry_on # Defines global variable should be used
    
    # Move the agents then eat the grass (call move + eat functions).
    for j in range(num_of_moves):
        random.shuffle(agents) # Shuffles list of agents each iteration before behaviour functions
        for i in range(len(agents)):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            wolf_agents[i].move()
            
        for i in range(num_of_agents):
            wolf_agents[i].eat_sheep(neighbourhood)
             

    # Loop through agents and set variable carry_on to false when all agents store > 500
    count = 0
    for i in range(len(agents)):
        if agents[i].store > 500:
            count = count+1
    if (count == len(agents)):
        print("Stopping Condition: All agents have exceeded store of 500")
        for i in range(len(agents)):
            print(agents[i])
            """ Testing that all agents exceed storage of 500
            Returns:
                Each agents coordinates and storage amount
            """
        carry_on = False

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='white', marker='*')
        
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(wolf_agents[i].x,wolf_agents[i].y, c='black', marker='*')

  
# Generator function to stop supply when stopping condition is met          
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
      
# Sets pop-up window/figure size
fig = matplotlib.pyplot.figure(figsize=(10, 10)) 
  
# Create function to plot animation and passes in functions/variables
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
# Create function for setting the value of num_of_agents from slider bar with w.get()   
def sel():
    
    global num_of_agents
    global td_ys
    global td_xs
    global agents
    global wolf_agents
    num_of_agents = w.get()
    # Pass in agents from web scrape, environment variable (and self as always).
    for i in range(num_of_agents):
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        #print(x, y)
        agents.append(agentframework.Agent(environment, agents, y, x))
        
    for i in range(num_of_agents):
        y = random.randint(0,100)
        x = random.randint(0,100)
        #print(x, y)
        wolf_agents.append(agentframework.wolf_agent(environment, wolf_agents, agents, y, x))


# Styling of the canvas  
# Uses toolkit function within tkinter and assigns to root variable. Main window.
root = tk.Tk() 
root.wm_title("Model") # Sets title of GUI


# Create menu in GUI
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
model_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Options", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
""" Select "Run Model"
Returns:
    Initiates the program
""" 
model_menu.add_command(label="Quit", command=root.destroy)
""" Select "Quit"
Returns:
    Closes the program
""" 

# Creates scalebar
w = tk.Scale(root,from_=10, to=100, orient=tk.HORIZONTAL, width=50, length=500, label="Number of Agents")
w.pack()


#model_menu.add_command(label="Number of agents", variable=num_of_agents)
button = tk.Button(root, text="Set Scale Value", command=sel)
button.pack()


# Passes fig settings and root into master kwarg
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root) 
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1) 


# Sets GUI to wait for events/interactions        
tk.mainloop()