from phi.agent import Agent
from phi.model.groq import Groq 
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv() # This function will load the GROQ_API_KEY which contains teh groq API key as an environment variable that this program or the llama model can use, This function expects a .env file

def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "ChipBook": "MSFT", # ChipBook is not a publicly listed company, we have just mapped it to microsoft's symbol
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")

finance_agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Use tables to display data.",
        "If you need to find the symbol for a company, use the get_company_symbol tool.",
    ],
    debug_mode=True,
) # This model only has static knowledge, that's knowledge upto a certain point of time

finance_agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and ChipBook. Show in tables.", stream=True)



