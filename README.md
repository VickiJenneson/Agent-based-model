# Agent-based model

The code in the 'Model' uses the 'Agent framework' code to display agents interacting with each other and their environment, which is drawn into the model via the in.txt file.

Agents, via the Agent class, are given methods which allow them to eat from their environment, share it with those in their vicinity and vomit if they have eaten more than 100 units. The vomit method has been limited based on the environment value at the agent's current coordinate, so as not to re-scale the background colour based on the pre-set limits. 

The code can be easily adapted to run from the control panel, which enables users to specify the number of agents, number of iterations and the size of their neighbourhood, which will all influence how they interact with their environment and each other.

The model is animated using graphics which represent the background environment, showing it changing as it is nibbled and vomited back, and points which show the agents moving around. The environment is created as a torus, meaning that if agents step off the edge, they will reappear on the opposite side of the map. 

The programme prints the final coordinates for each agent in the model and also calculates the total amount eaten from the environment by all agents. This could provide the basis for a useful biological model showing the sustainability of a habitat/ecosystem's food supply based on the number of agents and their determined behaviours. 

After the code has run, an Excel file is generated which gives values for the new environment data, this file is appended on each run of the model.
