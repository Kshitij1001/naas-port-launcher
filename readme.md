## Running in the python virtual environment
> ### Note: The naas_env folder was created for windows OS
> - Open cmd or powershell and cd into the project folder 
> - enter `./naas_env/Scripts/activate`  
> this will activate the naas_env virtual environment
> - enter `python main.py`  
> this will run the flask server at port 1234
> - use ctrl+C to stop the server
> - to exit virtual env, enter `deactivate`

## Running with system installed python
> - Open cmd/powershel/bash terminal and cd into the project folder
> - install the required dependencies with command `pip install -r ./requirements.txt`
> - Assuming python is added in the path variables, enter `python main.py`  
> this will run the flask server at port 1234
> - use ctrl+C to stop the server

### Swagger UI will be available at `http://localhost:1234/docs`