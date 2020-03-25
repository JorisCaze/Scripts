# Read csv files and store them into arrays

import numpy as np
import math
import matplotlib.pyplot as plt
import sys

# Data of files are preprocessed
# Files have their text header deleted (if there is one) + comma changed to dot  

# I/O folders
dataFolder = '../data/'
saveFolder = '../plots/'

# Description files structure
# There are several series (here A & B), e.g. one per study
# Each serie has "_n" timestep extracted (here A & B have 2 timesteps)

# Files read
files = ['fileA_1.txt', 'fileA_2.txt',
		 'fileB_1.txt', 'fileB_2.txt']

fileNames = [i[:-4] for i in files]

nbSeries  = 2;                         # Number of series (here studies A & B)
nbIts     = int(len(files)/nbSeries)   # Number of timestep extracted (here 2)
its       = [1, 2]                     # Values of timestep extracted                      

if nbIts != len(its):
    sys.exit("Error: number of files and iterations extracted incompatible")
print('Number of iterations extracted:', nbIts)

lines    = []  # All lines from all files
lineFile = []  # Buffer which keeps lines of one file temporarily

# Data structure
# lines is kind of a 3D matrix:
# Each face represents data of a quantity at "_i" timestep with rows x,y,z
# Once all timesteps of a quantity is stocked we continue
# with the next quantity following the same process

#                          _____ ____ ____
# Face 3 = fileB_1        /____/____/____/|
#                        /____/____/____/||
# Face 2 = fileA_2      /____/____/___ /|/|
#                      |    |    |    | /||
# Face 1 = fileA_1     |____|____|____|/|/|
#                      |    |    |    | /||
#                      |____|____|____|/|/
#                      |    |    |    | /
#                      |____|____|____|/   
#                        x    y    z

# Read csv files and store all data into var. lines
for file in files:
    with open(dataFolder + file) as f:
        lineFile = [line.split() for line in f]
    f.close()
    lines.append(np.array(lineFile, dtype=float))


# Arrays of paramters (= rows of your files)
x_A = [] # Parameter x of study A [unit]
y_A = [] # Parameter y of study A [unit]

x_B = [] # Parameter x of study B [unit]
y_B = [] # Parameter y of study B [unit]

# Column names reminder
# 0. Quantity x
# 1. Quantity y

# Fill arrays of each row of a given quantity
for it in range(nbIts):
    x_A.append(lines[it][:,0])
    y_A.append(lines[it][:,1])

    x_B.append(lines[it+nbIts][:,0])
    y_B.append(lines[it+nbIts][:,1])

# Do some post-process and save plots into saveFolder