# Oliver Rogers - student number: 201485161 

## Programming for GIS
This is a agent based modelling program for Assignment 1.

## Installation
This program has been tested and works in Python version 3.8. Using Anaconda ensure that the graphics backend is Tkinter.

## Usage
When all files in a directory. Run the file ABM.py and it will open a GUI named Agent Based Modelling. 

![ABM_GUI](https://user-images.githubusercontent.com/80906276/114885821-f43fad80-9dfe-11eb-9d28-7cce08a81201.JPG)

Click on file and Run model. 

![Run_model](https://user-images.githubusercontent.com/80906276/114885921-06215080-9dff-11eb-862a-0f810a5ddae1.JPG)


This will run through the code moving the agents through an environment grazing through it causing the raster image to change colour as pixels are esentially eaten away.

![image](https://user-images.githubusercontent.com/80906276/114999208-8ac0ad00-9e99-11eb-9ab9-8d694138deaa.png)

You can change the default values of how many agents, iterations and neighbours within the ABM.py 


![default settings](https://user-images.githubusercontent.com/80906276/115000427-a9737380-9e9a-11eb-8e63-04e755e4dc05.JPG)


The below code is commented out in the ABM.py but can be utilised if there is a need to write out the envirnoment into a file and also append the amount stored by the agents during the model run.

Write environment to csv
 
f2 = open('environment_out.csv', 'w', newline='')
writer = csv.writer(f2, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in environment:
    writer.writerow(environment) # List of values.
f2.close()

Append total sum of agents store

f2 = open('Store_out.txt', 'a', newline='')
writer = csv.writer(f2, delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
for row in agents :
    writer.writerow([sum]) # List of values.
f2.close()

## Supporting files
A few files need to be present in the directory when running the "ABM.py". 
They are inside this repository. 

rasterimage.txt This is the environment file.

agentframework.py Ths contains the agent class.

## License
This Program has a MIT License which is enclosed in the repository. 
