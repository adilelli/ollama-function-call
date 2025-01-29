# ollama-function-call
function call for AI agents via ollama, backend via Fast API, db via MongoDB

#### Testing the API

##### Sample request scheme
https://go.postman.co/workspace/My-Workspace~4812f66d-622c-41b3-83fa-1276f89adb6f/documentation/22734567-2baf8128-51f4-48e0-8a9b-1e35bb0e4dc7?entity=request-7195da85-e887-4b1e-8b2c-50d2c5bfb41a

##### Create a Virtual Environment:

````
cd backend
python3 -m venv llama
````

This will create a llama directory in your project folder.
Activate the Virtual Environment (Mac and Linux):

````
source llama/bin/activate
````

Activate the Virtual Environment (Windows):

````
llama\Scripts\activate
````

After activation, you should see (llama) at the beginning of your terminal prompt, indicating that the virtual environment is active.

##### Install Packages 
You can now install Python packages specific to this environment using pip:
````

pip install -r requirements.txt
````

##### Start the backend
````
uvicorn main:app --reload
````
