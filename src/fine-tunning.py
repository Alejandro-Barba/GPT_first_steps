import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.File.create(
  file=open("./data/mydata.jsonl", "rb"),
  purpose='fine-tune'
)

openai.FineTuningJob.create(training_file="file-abc123", model="gpt-3.5-turbo")