import os
import openai
openai.api_key = "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"
completion = openai.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)