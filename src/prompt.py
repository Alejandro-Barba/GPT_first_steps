import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Eres un experto en Lovecraft y diseñador de juegos de mesa"},
    {"role": "user", "content": "Ayudame a generar la idea de un juego de mesa sobre una investigación de un culto que quiere despetar a Cthulhu"}
  ]
)

print(completion.choices[0].message)