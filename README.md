This document contains all supporting instructions to run the project successfully.

You will want to install python on your computer and python interpreter for VS code user. 
Download the repository files in one folder. And then install a virtual environment and activate it. 

To run the codes, there is need to setup virtual environment advisablly in the directory containing same as the files of this project and activate it. 
Then install the json and jsonschema modules all with the virtual environment activated in the same working directory.

------modules to install---------------------
Install virtual environment: "python -m virtualenv virtulenvname". 
Install json module: "pip install json"
Install jsnschema: "pip install jsonschema"

Recommend: The main.py and schema.json files can be access using any support editor but i will recommend using VS Code since it can work with entire directory in one workspace.

----------Guidelines-------------------- 
1. Open the entire directory containing all the dependencies on VS code
2. Go to the terminal and navigate to the directory containing the files
3. Activate the virtual environment "myvenv". To activate,
	for windows: .\myvenv\Scripts\activate
	for Linux: source myvenv/bin/activate
4 Install json and jsonschema modules
4. Load the main.py and run the program

------Files in the directory-----------------
1. .vscode
2. myvenv(virtual environment)
3. main.py
4. schema.json
5. similar data.json
6. README.md

Note: For full support function the program, the above listed files must be available in the working directory