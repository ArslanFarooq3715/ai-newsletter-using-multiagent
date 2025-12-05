# AI Newsletter Agent 🤖📰

An intelligent multi-agent system built with CrewAI that automatically generates high-quality newsletters on any topic using AI-powered research, writing, and proofreading agents.

## 🌟 Features

- **Multi-Agent System**: Three specialized AI agents working together
  - **Research Agent**: Identifies trends, analyzes data, and gathers insights
  - **Writer Agent**: Creates engaging, well-structured articles
  - **Proofreader Agent**: Ensures quality, accuracy, and proper citations
- **Powered by Groq**: Fast inference with Llama 3.1/3.3 models
- **Web Search Integration**: Real-time information gathering via Serper API
- **Automated Workflow**: Sequential task execution with context sharing
- **Markdown Output**: Professional newsletter format ready to publish

## 📋 Prerequisites

- Python 3.8+
- Pipenv (for dependency management)
- Groq API Key (free at [groq.com](https://groq.com))
- Serper API Key (free at [serper.dev](https://serper.dev))

## 🚀 Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ai-newsletter-agent
```

2. **Install dependencies**
```bash
pipenv install
```

Required packages:
```bash
pipenv install crewai crewai-tools litellm python-dotenv langchain-groq
```

3. **Set up environment variables**

Create a `.env` file in the project root:
```bash
GROQ_API_KEY=gsk_your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## 📁 Project Structure

```
ai-newsletter-agent/
│
├── agents.py          # Agent definitions (researcher, writer, proofreader)
├── tasks.py           # Task configurations for each agent
├── tools.py           # Tool setup (Google search integration)
├── crew.py            # Main execution file
├── .env               # Environment variables (API keys)
├── newsletter.md      # Generated newsletter output
└── README.md          # Project documentation
```

## 🔧 Configuration

### agents.py
Defines three AI agents with specific roles and backstories:
```python
from crewai import Agent, LLM
from tools import google_search_tool

llm = LLM(
    model="groq/llama-3.1-8b-instant",  # or "groq/llama-3.3-70b-versatile"
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

researcher = Agent(...)
writer = Agent(...)
proof_reader = Agent(...)
```

### tasks.py
Defines tasks for each agent:
```python
from crewai import Task

research_task = Task(...)
writer_task = Task(...)
proof_reader_task = Task(...)
```

### tools.py
Sets up web search capability:
```python
from crewai_tools import SerperDevTool

google_search_tool = SerperDevTool()
```

## 💻 Usage

1. **Activate the virtual environment**
```bash
pipenv shell
```

2. **Run the agent**
```bash
pipenv run python crew.py
```

3. **Customize the topic** (in `crew.py`):
```python
topic = "Artificial Intelligence in Finance"  # Change to your topic
result = crew.kickoff(inputs={'topic': topic})
```

4. **Check the output**
- Console: Real-time agent activity
- File: `newsletter.md` (final polished article)

## 🎯 How It Works

1. **Research Phase**: 
   - Agent searches the web for latest information
   - Identifies trends, pros/cons, and key insights
   - Generates comprehensive research report

2. **Writing Phase**:
   - Takes research findings
   - Crafts engaging, digestible article
   - Focuses on clarity and readability

3. **Proofreading Phase**:
   - Reviews article for accuracy
   - Adds proper citations
   - Includes 3 additional sources for further reading
   - Outputs final markdown file


## 📝 Example Output

The generated newsletter includes:
- Comprehensive analysis of the topic
- Latest trends and developments
- Pros and cons
- Market opportunities and risks
- Properly cited sources
- 3 additional resources for further reading

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

[Your License Here]

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent framework
- [Groq](https://groq.com) - Fast LLM inference
- [Serper](https://serper.dev) - Web search API

## 📧 Contact

Arslan

---

**Happy Newsletter Generation! 🚀**
