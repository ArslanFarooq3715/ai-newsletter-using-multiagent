from dotenv import load_dotenv
load_dotenv()

import os
os.getenv("GROQ_API_KEY")

from crewai_tools import SerperDevTool

google_search_tool = SerperDevTool()
