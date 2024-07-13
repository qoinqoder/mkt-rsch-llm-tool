from openai import OpenAI
import time
import openai

openai.api_key = ''

# def make_request():
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo-1106",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "Hello, how are you?"}
#         ]
#     )
#     return response

# try:
#     response = make_request()
#     print(response.choices[0].message['content'])
# except openai.error.OpenAIError as e:
#     print(f"An error occurred: {e}")


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
