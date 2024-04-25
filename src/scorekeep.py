#from v2_reinforceAgents import ReinforceAgent  # Adjust the import path accordingly
import subprocess
import matplotlib.pyplot as plt  # Common import for matplotlib
import numpy as np
import random
import os

# Generating layouts
filenames=os.listdir("layouts")
val2=[]
laylay=[]
for f in filenames:
    val2 = (f.replace(".lay",""))
    laylay.append(val2)
numbo= 10
float_list=[]

rando=random.choice(laylay)
command= [
        "python",
        "pacman.py",
        "-p", "ReinforceAgent",
        "-n", "{0}".format(numbo),
        "--frameTime", "0",
        "-l", "{0}".format(rando)
    ]

result = subprocess.run(command, capture_output=True, text=True)
output=result.stdout

lines=output.splitlines()
value1=None
value2=[]
    
for line in lines:
    if 'Score:' in line:
        value1 = (line.split(":")[1].strip())  # Extract integer value
        value2 = (value1.split(", "))
        float_list1=[float(value) for value in value2] 
        float_list.append(float_list1)
i=np.arange(len(float_list))+1
plt.plot(i,float_list,'r',label="Reinforcement")
label=["Reinforcement"]
plt.title('Learning Algorithms vs. Training Numbers')
plt.xticks(i)
plt.xlabel('Training Episode')
plt.ylabel('Score per Episode')
plt.legend(label)
