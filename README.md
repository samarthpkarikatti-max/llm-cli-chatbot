# LLM CLI Chatbot

## Project Overview
This project is developed as part of the PromptForge
Virtual Internship Program by CodGen.

It is a Python-based command-line chatbot connected
to the Groq API using a Large Language Model (LLM).

## Features
- Real-time AI conversations
- Conversation memory
- Three chatbot personalities
- Adjustable temperature parameter
- API error handling
- JSON conversation export

## Technologies Used
- Python
- Groq API
- GPT-OSS-20B
- python-dotenv

## Installation

1. Clone this repository.

2. Install the required libraries:

   python -m pip install -r requirements.txt

3. Create a .env file.

4. Add your Groq API key:

   GROQ_API_KEY=your_groq_api_key

5. Run the chatbot:

   python chatbot.py

## Usage

Select one of the following personalities:

1. Coding Tutor
2. Interview Assistant
3. Friendly Assistant

Choose a temperature between 0 and 2.

Start chatting with the AI assistant.

Type exit or quit to end the conversation.

The conversation will be saved in
sample_conversation.json.

## Project Structure

llm-cli-chatbot/
- chatbot.py
- .env.example
- .gitignore
- requirements.txt
- reflections.md
- sample_conversation.json
- README.md

## Security
Never upload your actual API key.
The .env file must remain private.

## Internship Details
Program: PromptForge Virtual Internship
Organization: CodGen
Week: 1 of 4
Theme: LLM Fundamentals & API Basics
