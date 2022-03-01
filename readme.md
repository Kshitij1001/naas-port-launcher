### Note: Install python3.x with its path added in system variables before running the app

## Running in the python virtual environment
> - Open cmd or powershell and cd into the project folder 
> - enter `python -m venv naas_venv`
> - enter `./naas_env/Scripts/activate`  
> this will activate the naas_venv virtual environment
> - install the required dependencies in naas_venv by entering `pip install -r ./requirements.txt`
> - enter `python main.py`
> this will run the flask server at port 1234
> - use ctrl+C to stop the server
> - to exit the virtual env, enter `deactivate`

## Running in system's python environment
> - Open cmd/powershel/bash terminal and cd into the project folder
> - install the required dependencies in your system by entering `pip install -r ./requirements.txt`
> - enter `python main.py`  
> this will run the flask server at port 1234
> - use ctrl+C to stop the server

### Swagger Documentation will be available at `http://localhost:1234/docs`