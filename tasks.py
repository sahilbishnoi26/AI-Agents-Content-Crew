from crewai import Task  # Importing Task class for creating tasks
from agents import researcher, writer, proof_reader  # Importing predefined agents
from tools import google_search_tool  # Importing Google search tool for information gathering

# Create the research task
research_task = Task(
    description=("""
    Identify the next big trend in the topic: {topic}. Focus on identifying pros and cons and the overall narrative.
    Your final report should clearly and explicitly articulate the key points, market opportunities, and potential risks
    associated with the given topic.
    """),  # Detailed instructions for the research task
    expected_output="A comprehensive 3-paragraph-long report on the latest information on the given topic: {topic}.",  # Expected output
    tools=[google_search_tool],  # Tools the agent can use
    agent=researcher  # The agent responsible for this task
)

# Create the writing task
write_task = Task(
    description=("""
    Compose an insightful article on the topic: {topic}. Focus on the latest trends and how it is impacting the industry.
    This article should be digestible, easy to understand, engaging, and positive.
    """),  # Instructions for writing
    expected_output="A 3-paragraph-long article on the topic: {topic}, formatted as markdown.",  # Expected output
    tools=[google_search_tool],  # Tools the agent can use
    agent=writer,  # The agent responsible for this task
    async_execution=False  # Task will run synchronously
)

# Create the proofreading task
proof_read_task = Task(
    description=("""
    Finalize an insightful article on the topic: {topic}, which is already written by the writer. Focus on the information and how it is structured.
    It should not have any mistakes and should be very easy to digest. Make sure to include sources of the information where they come from.
    Also, write 3 sources for further studying of the topic. This article should be digestible, easy to understand, engaging, and positive.
    """),  # Instructions for proofreading
    expected_output="A 3-paragraph-long article on the topic: {topic}, formatted as markdown with all the relevant sources.",  # Expected output
    tools=[google_search_tool],  # Tools the agent can use
    agent=proof_reader,  # The agent responsible for this task
    async_execution=False,  # Task will run synchronously
    output_file="newsletter.md"  # Specify output file for saving the article
)
