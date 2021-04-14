import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import random
import operator
import agentframework8
import csv
import tkinter


#def distance_between(a, b):
    #return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5

# Set the random seed to make the results repeatable
#random.seed(0)
#random.seed(1)

# read in raster text file and create 2d list
f = open('in.txt', newline='')
reader= csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
       

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

agents = []
agentslist = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework8.Agent(random.randint(0,300), random.randint(0,300), environment, agentslist))

  
                
# List of agents
for i in range (num_of_agents):
    agentslist = (agents[i].y, agents[i].x)
    #print(agentslist)
    
#Test that agents are returning other agents positions    
    print (agents[2], agentslist)
    
# Total number of agents check
num_of_agents = len(agents)
print("num_of_agents", num_of_agents)

# Print out agents
for i in range(num_of_agents):
    print(agents[i])


def update(frame_number):

    # Move, eat,share the agents.
    # building plots
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            random.shuffle(agents)
            #print("agents move", agents[i])
            agents[i].move(fig)
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    
    matplotlib.pyplot.imshow(environment)

    # Move, eat,share the agents.
    for i in range(num_of_agents):    
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i]) 

# Run the GUI and animation
def run():
        animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=num_of_iterations)
        canvas.draw()
# GUI setup
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() # Wait for interactions.    



        
# calculate total store in agents
sum = 0
for a in agents:
    sum = sum + a.store
print ("total stores", sum)



# Write environment to csv
#f2 = open('environment_out.csv', 'w', newline='')
#writer = csv.writer(f2, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
#for row in environment:
#    writer.writerow(environment) # List of values.
#f2.close()

# Append total sum of agents store
#f2 = open('Store_out.txt', 'a', newline='')
#writer = csv.writer(f2, delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
#for row in agents :
    #writer.writerow([sum]) # List of values.
#f2.close()


