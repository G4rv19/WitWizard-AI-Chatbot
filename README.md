# This is the Backend of the Chatbot Based on Ollama models. 
### It is called WitWizard and backend runs on 0.0.0.0 host where ur url can be send to frontend to access the messages. 
### Anyone on the same internet can access it.


# ollama_pi

This is based on running ollama webui locally on raspberry pi 4 model b. Running ollama api with models you like, and serving it in web UI.


# ollama Model for this project :- Tinyllama 
how to download it :
go to terminal and put this in : 
> curl -fsSL https://ollama.com/install.sh | sh

after it got downloaded, u can check it by typing 'ollama'

next step : u can install the tinyllama model on it

type : 
>ollama run tinyllama

The 'ollama_project.py' file is based on how the ollama running on local host can get ur prompt and reply it.
In 'ollama_project.py' u can change the ollama model in the script with the model you would like to use.
The 'main.py' is using fastapi which will host frontend and backend and run the whole model. 

Before u start with 'main.py'
'u need to download fastapi uvicorn'
> pip install fastapi uvicorn
then you can run it 


let it download it and it will run automatically and u can chat with it.

Now we gonna work on running the model locally and using it in backend to get and send requests and reponse to users.
