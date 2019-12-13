# Python Agent Based Modelling

- This project aimed to create agents that move around an environment, interact with the environment and each other, aswell as produce a Graphical User Interface (GUI) for the end user to run the model.
- The first set of agents created were thought of as "sheep". Starting co-ordinates are scraped from the web and randomised. The sheep can move around the environment, "eat" the environment, collect "storage" when eating and share that storage with each other.
- The second set of agents created were thought of as "wolves". The wolves can move around the environment randomly and "eat" the sheep, when they are within a certain distance.
- The end user can run/quit the model through a GUI, aswell as adjust the number of agents before running (wolves and sheep).


## Getting Started and Installation

 - When developing this software, the Anaconda software was utilised, available here: https://www.anaconda.com/distribution/ 
 - The use of Anaconda is recommended, as this installation comes bundled with Python and many useful libraries.
 - This software was developed sing the Spyder Integrated Development Environment with Python version 3.7, and so is recommended when using this software.
 - If using alternative software/IDE/Python versions, the following libraries are required for the code to work:
	- matplotlib
	- random
	- requests
	- bs4
	- tkinter
	- csv
	
	
### Contents of GitHub directory

- The following includes a list of all files included within the GitHub repository for the software:
	- .gitattributes (default GitHub file)
	- LICENSE (GNU General Public License)
	- README.md (this documentation)
	- agentframework.py (python script containing code for the two agent classes - wolves and sheep)
	- in.txt (a text file containing RGB values for the starting environment)
	- model.py (main python script for software)
		

## Running the model

- The model.py file should be executed within Anaconda Spyder (or alternative). When the program is run, a GUI will be presented to the user:
	- The scale bar at the top of the GUI can be adjusted from 10-100. This sets both the amount of sheep agents and wolf agents.
	- Once the scale bar has been adjusted, the user must click the "Set Scale Value" button below the slider.
	- Once the number of agents has been selected and set, the user should click "Options" drop down in the top left corner.
	- The user should then click "Run Model" for the code to initialise.
	- Once the animation stops, the user can use the "Quit" option to close the GUI.
	
	
## The Model: Behind the Scenes

- The following has been written into the code:
	- Sheep agents are plotted with white * markers
	- Wolf agents are plotted with black * markers
	- When the sheep agents eat the environment, they will gain +1-10 towards their total storage. Each agent's storage starts at 0.
	- The sheep agents share their storage with each other, when distance between them is lower than the neighbourhood variable (currently set at 2).
	- When the wolf agents eat the sheep, they will gain +1 towards their total storage. Each wolf agent's storage starts at 0.
	- The variable for total number of iterations between each refresh is currently set to 100
	- The variable for how many times an agent moves before refreshing is currently set to 2.
	- A stopping condition is implemented within the code, that stops the model, when each of the remaining sheep have reached an excess of 500 storage.

	
## Testing

- Automated testing is set up in the code to ensure the software is working as expected. If using Spyder, testing will be printed to the console.
	- Every time a wolf agent "eats" a sheep agent, "A WOLF HAS EATEN A SHEEP! (total storage) in total!" is printed to the console, to ensure eating function is working correctly, and counting wolf agents storage.
	- To ensure the stopping condition is working as intended, upon the stopping condition being met, each of the remaining sheep agents will have their XY co-ords and storage amount printed (this should be in excess of 500 if working correctly)
	- To test that the sheep agents are sharing with their neighbours. Line 61 should be uncommented in agentframework.py. This will print the amount shared, and individual new storage total.
	
	
## License

This project is licensed under the GNU License - see the LICENSE file in the following location for details: https://github.com/sideshowtee1003/Agent-Based-Modelling/blob/master/LICENSE


## Author

- **Thomas Coleman** : 
	-(https://github.com/sideshowtee1003) GitHub Profile Page
	-(https://sideshowtee1003.github.io/) GY18TC - Agent Based Modelling html page
	-(https://github.com/sideshowtee1003/Agent-Based-Modelling) Agent Based Modelling Repository
