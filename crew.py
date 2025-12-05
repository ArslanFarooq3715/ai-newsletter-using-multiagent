from crewai import Process, Crew
from agents import researcher, writer, proof_reader
from tasks import research_task, writer_task, proof_reader_task


crew = Crew(
    agents=[researcher, writer, proof_reader],
    tasks=[research_task, writer_task, proof_reader_task],
    process= Process.sequential,
)

topic = "Artificial Intelligence in Finance"
result = crew.kickoff(inputs={'topic':topic})
print(result)