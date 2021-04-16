import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import random
import operator
import agentframework
import csv
import tkinter
import requests
import bs4

#default settings
matplotlib.use('TkAgg')
agents = []
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#create plot figure and axis
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_subplot(1, 1, 1)
ax = fig.add_axes([0, 0, 300, 300,])

#ax.set_autoscale_on(False)

def loadEnvironment(txtfile):
    # read in raster text file and create 2d list
    f = open(txtfile, newline='')
    reader= csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
    return environment

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
        matplotlib.pyplot.ylim(0, 300)
        matplotlib.pyplot.xlim(0, 300)
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
        print(agents[i]) 

def parseXY(url):
    r = requests.get(url)
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    return td_xs, td_ys

def makeAgents(num_of_agents):
    agentslist = []
    # Initialisation - Make the agents.
    for i in range(num_of_agents):
        y = int(td_xs[i].text)
        x = int(td_ys[i].text)
        agents.append(agentframework.Agent ( y, x,environment, agentslist))

    # List of agents
    for i in range (num_of_agents):
        agentslist = (agents[i].y, agents[i].x)        
        #Test that agents are returning other agents positions    
        print (agents[2], agentslist)
        
    # Total number of agents check
    num_of_agents = len(agents)
    print("num_of_agents", num_of_agents)

    # Print out agents
    for i in range(num_of_agents):
        print(agents[i])

def run():
    # Run  and animation
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=num_of_iterations)
    canvas.draw() 

environment = loadEnvironment('rasterimage.txt') 
td_xs, td_ys = parseXY('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
makeAgents(num_of_agents)

# GUI setup
root = tkinter.Tk()
root.wm_title("Agent Based Modelling")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=model_menu)
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


