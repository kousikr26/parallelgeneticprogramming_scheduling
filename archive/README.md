# parallelgeneticprogrammingscheduling
Parallel genetic programming for constraint project scheduling

### Features
- A parallelised implementation of using genetic programming to evolve priority rules for the Resource Constrained Project Scheduling Problem
- Other methods used to evolve rules are Map-elites and coevolution 


### Instance
Each instance of the benchmark is represented as an object which contains within itself all the variables and information of the problem instance

The class instance when initialised with a filepath of a psplib problem instance reads all information from the file. The parameter combination type, instance type etc are all automatically determined from the filename and the correspomding values are read and stored
Next the precedence relations are read from the file and stored in a typical adjacency list format.
Then the recource consumption and duration of each job is read.


Finally the networkx and pygraphviz library are used to draw the graph for visualisation (if required)

### Requirements
matplotlib, networkx, pygraphviz are the only dependencies and all are required for visualisation purposes
They can be installed with `pip3 install <module_name>`

### Visualising the dependency directed acyclic graph
![demo](demo.png?raw=true "Demo image")


### Member functions:

- init(): The constructor for instance class. Should be initialised with filepath to .sm file

- read_data() : Reads data from file and updates all attributes

- draw(): visualise precedence relations

- calculate_et,lt,mts,grpw,grd(): Calculates the priority values for each rule

- Serial_sgs(): implements the serial schedule generation scheme

- Parallel_sgs(): implements the parallel schedule generation scheme

- calculate _dynamic_priority_rules(): calculates the priority functions such as irsm,wcs,acs which can not be precomputed and computed at schedule time

- Calculate_activity_attributes(): Normalises and calculates activity attributes which will be used as attributes in the GP 

- Earliest_start(): Calculates E(i,j). The first time j can be scheduled if i is scheduled at the current time




### GP
Using GP to evolve the priority rules we get a lower % deviation than any of the priority rules


Evolved function tree 

![tree](gp_trees/25.9_run_0.png?raw=true "GP tree")
