# AI Agents Content Crew

## Description
An AI-powered content generation pipeline using CrewAI, Groq LLMs, and SerperDevTool for internet search. Automates research, article writing, and proofreading tasks with agents designed for seamless collaboration and high-quality output.

## Features
- **Researcher Agent**: Gathers and synthesizes information on the given topic.
- **Writer Agent**: Creates engaging and easy-to-read articles formatted in markdown.
- **Proofreader Agent**: Ensures clarity, structure, and credibility by finalizing articles and adding references.
- **Dynamic Task Workflow**: Sequential execution of tasks for efficient collaboration.
- **Customizable Tools**: Integrates internet search and real-time data retrieval for comprehensive insights.
- **Output Files**: Saves final articles as markdown files.

## Technologies Used
- **CrewAI**: Framework for agent orchestration and task management.
- **Groq LLM**: Language model for natural language processing.
- **SerperDevTool**: Enables internet search capabilities.
- **Python**: Primary programming language.

## Installation
1. **Clone the Repository**  
   - `git clone https://github.com/your-username/AI_Agent_Content_Crew.git`  
   - `cd AI-Content-Workflow-Pipeline`

2. **Create and Activate a Virtual Environment**  
   - On Windows:  
     - `python -m venv venv`  
     - `venv\Scripts\activate`
   - On macOS/Linux:  
     - `python3 -m venv venv`  
     - `source venv/bin/activate`

3. **Install Dependencies**  
   - `pip install -r requirements.txt`

4. **Set Up Environment Variables**  
   - Create a `.env` file in the root directory and add the required API keys. Example:
     ```plaintext
     SERPER_API_KEY=your_api_key_here
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage
1. **Configure Agents and Tasks**  
   - Modify the agents and tasks in `agents.py` and `tasks.py` to match specific requirements.

2. **Run the Project**  
   - `python main.py`

3. **Interact with the Agents**  
   - Agents will perform tasks such as researching, writing, and proofreading based on the input topic.

4. **View Results**  
   - The final content will be saved as `newsletter.md` in the project directory.

## Troubleshooting
- **Issue**: Missing Dependencies  
  - **Solution**: Ensure all dependencies are installed with `pip install -r requirements.txt`.
- **Issue**: API Key Errors  
  - **Solution**: Verify the `.env` file contains valid keys for Serper and Groq.
- **Issue**: Task Execution Failure  
  - **Solution**: Check configurations in `agents.py` and `tasks.py`.
- **Issue**: Missing Output Files  
  - **Solution**: Ensure proper file paths are defined in the tasks' configurations.

Enjoy using this AI-driven content creation pipeline!
