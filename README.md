# LLM API Homework

## Overview
This project uses Python code to interact with an LLM API instead of the web interface.

## What I did
- Sent multiple prompts to the model
- Compared outputs
- Observed how responses change based on input

## Prompts Used
1. Explain machine learning in 2 simple sentences for a college freshman.
2. Write a 3-bullet study guide for the difference between AI, machine learning, and deep learning.

## Observations
The outputs changed depending on the structure of the prompt. The first response was short and explanatory, while the second response was formatted into bullet points. This shows how prompt design impacts LLM outputs.

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Set API key:
   export OPENAI_API_KEY="your_key_here"

3. Run:
   python main.py
