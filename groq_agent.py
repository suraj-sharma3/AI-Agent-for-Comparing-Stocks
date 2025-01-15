from phi.agent import Agent
from phi.model.groq import Groq 
from dotenv import load_dotenv

load_dotenv() # This function will load the GROQ_API_KEY which contains teh groq API key as an environment variable that this program or the llama model can use, This function expects a .env file

agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile")
)

agent.print_response("Generate a 16 bar verse in the style of J. cole")

