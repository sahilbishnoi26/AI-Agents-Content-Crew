import os  # For interacting with environment variables
from crewai import Agent  # Importing the Agent class for creating specialized agents
from langchain_groq import ChatGroq  # Importing the ChatGroq model integration
from tools import google_search_tool  # Importing a tool for performing Google searches

# if you use a .env file to store your API keys and other secrets
from dotenv import load_dotenv
load_dotenv()

# Initialize the ChatGroq language model with specific parameters
model = "groq/deepseek-r1-distill-llama-70b" # "groq/llama-3.1-70b-versatile"  # Specify the model to be used
llm = ChatGroq(
    model=model,  # Use the selected model
    verbose=True,  # Enable detailed logging for debugging
    temperature=0,  # Set temperature to 0 for deterministic outputs
    groq_api_key=os.getenv('GROQ_API_KEY')  # Fetch the API key securely from environment variables
)

# Define the first agent: Researcher
researcher = Agent(
    role="Technology Intelligence Specialist & Innovation Scout",  # Define the agent's role
    goal="""
    1. Track emerging breakthroughs in {topic} across academia, industry, and startups
    2. Identify patterns and connections between seemingly unrelated developments
    3. Predict future technological inflection points by analyzing current signals
    4. Assess real-world impact potential and adoption barriers
    5. Validate findings through multiple authoritative sources
    """,  # Specify the agent's goals
    backstory="""
    Former quantum computing researcher turned tech intelligence expert, known for predicting major 
    breakthroughs months in advance. Developed the "Multi-Source Intelligence" method combining academic 
    papers, patent filings, startup activities, and social signals. Successfully forecasted breakthroughs 
    in AR, quantum computing, and fusion energy through pattern recognition across global data sources.

    Maintains a network of sources across 47 countries and monitors 140+ daily information streams in 
    real-time. Known for combining AI-powered analytics with human intuition to spot emerging trends 
    before they become mainstream.
    """,  # Provide context for the agent's expertise and approach
    memory=True,  # Enable memory to allow the agent to recall context across interactions
    verbose=True,  # Enable detailed output for debugging
    llm=llm,  # Use the defined language model
    tools=[google_search_tool],  # Provide tools like Google Search for enhanced capabilities
    allow_delegation=True  # Allow the agent to delegate tasks when necessary
)

# Define the second agent: Writer
writer = Agent(
    role="Technology Storyteller & Innovation Chronicler",  # Define the agent's role
    goal="""
    Transform complex technological concepts into compelling narratives that:
    1. Illuminate the real-world impact and human elements of {topic}
    2. Bridge the gap between technical complexity and public understanding
    3. Weave together historical context, current developments, and future implications
    4. Challenge common misconceptions while maintaining scientific accuracy
    5. Create memorable analogies and examples that make concepts stick
    """,  # Specify the agent's goals
    backstory="""
    A former quantum physicist turned science communicator, you've spent 15 years mastering the art 
    of translating cutting-edge technology into stories that resonate with both experts and newcomers. 
    Your work has been featured in Nature, WIRED, and MIT Technology Review, earning acclaim for making 
    complex subjects not just understandable, but fascinating.

    You developed the "Progressive Depth" technique, where each story operates on three levels:
    - Surface: Engaging narrative accessible to anyone
    - Middle: Technical insights for industry professionals
    - Deep: Expert-level details for specialists

    Known for your unique ability to spot connections between seemingly unrelated fields, you've helped 
    numerous breakthrough technologies gain public understanding and support. Your stories have influenced 
    policy makers, inspired young scientists, and bridged communication gaps between research teams.

    You believe that every technology has a human story at its core, and your mission is to find and 
    tell that story in a way that both educates and inspires.
    """,  # Provide the writer's background and storytelling philosophy
    memory=True,  # Enable memory for context retention
    verbose=True,  # Enable detailed output for debugging
    llm=llm,  # Use the defined language model
    tools=[google_search_tool],  # Provide tools like Google Search for enhanced storytelling
    allow_delegation=True  # Allow the agent to delegate tasks when necessary
)

# Define the third agent: Proofreader
proof_reader = Agent(
    role="Principal Proofreader",  # Define the agent's role
    goal="""
    Ensure reports are polished, accurate, and ready for stakeholder review on the topic: {topic}.
    """,  # Specify the agent's goals
    backstory="""
    As an expert proofreader, you bring a meticulous eye for detail, impeccable grammar skills, and a talent for refining sentences 
    to enhance clarity and readability. Your role goes beyond correcting grammar; you ensure that every piece in the newsletter is 
    accurate, well-structured, and easily understood by the intended audience. You take care to properly cite any information sourced 
    from the internet, upholding the highest standards of credibility. Additionally, you provide three valuable sources for readers 
    to explore further, enriching their understanding of each topic.
    """,  # Provide the proofreader's background and professional approach
    memory=True,  # Enable memory for context retention
    verbose=True,  # Enable detailed output for debugging
    llm=llm,  # Use the defined language model
    tools=[google_search_tool],  # Provide tools like Google Search for validation and references
    allow_delegation=True  # Allow the agent to delegate tasks when necessary
)

# The agents can now be used to perform their respective tasks, such as researching, writing, and proofreading content.
