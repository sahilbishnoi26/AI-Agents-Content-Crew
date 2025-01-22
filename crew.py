from crewai import Crew, Process  # Importing Crew for managing agents and processes
from agents import researcher, writer, proof_reader  # Importing predefined agents
from tasks import research_task, write_task, proof_read_task  # Importing predefined tasks

# Create a Crew object with agents and tasks
crew = Crew(
    agents=[researcher, writer, proof_reader],  # List of agents to handle tasks
    tasks=[research_task, write_task, proof_read_task],  # List of tasks to be executed
    process=Process.sequential  # Define the process flow (sequential execution)
)

# Define the topic for the tasks
topic = "Artifical Intelligence in Finance"

# Start the process by kicking off the crew with inputs
result = crew.kickoff(inputs={"topic": topic})

# Print the results of the completed tasks
print(result)
