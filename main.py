from openai import OpenAI

client = OpenAI()

prompts = [
    "Explain machine learning in 2 simple sentences for a college freshman.",
    "Write a 3-bullet study guide for the difference between AI, machine learning, and deep learning."
]

for i, prompt in enumerate(prompts, start=1):
    response = client.responses.create(
        model="gpt-5.4",
        input=prompt
    )

    print(f"\n--- Prompt {i} ---")
    print(prompt)
    print(f"\n--- Output {i} ---")
    print(response.output_text)
