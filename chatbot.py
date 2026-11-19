import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found. Check your .env file.")

client = Groq(api_key=api_key)

# Three system prompts
prompts = {
    "1": "You are a patient coding tutor. Explain technical concepts in simple language with examples.",
    "2": "You are a professional interview assistant. Give clear, structured and professional answers.",
    "3": "You are a friendly AI assistant. Communicate casually, warmly and helpfully."
}

# Select chatbot personality
print("\n===== SELECT CHATBOT PERSONALITY =====")
print("1. Coding Tutor")
print("2. Interview Assistant")
print("3. Friendly Assistant")

choice = input("\nChoose personality (1/2/3): ").strip()

if choice not in prompts:
    print("Invalid choice. Selecting Friendly Assistant.")
    choice = "3"

system_prompt = prompts[choice]

# Get temperature
while True:
    try:
        temperature = float(input("Enter temperature (0 to 2): "))
        if 0 <= temperature <= 2:
            break
        print("Enter a value between 0 and 2.")
    except ValueError:
        print("Please enter a valid number.")

# Initialize conversation history
messages = [
    {"role": "system", "content": system_prompt}
]

print("\n===== AI CHATBOT STARTED =====")
print("Type 'exit' or 'quit' to end.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("\nBot: Goodbye! Thank you for chatting.")
        break

    if not user_input:
        print("Bot: Please enter a message.\n")
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=temperature
        )

        ai_reply = response.choices[0].message.content

        messages.append({
            "role": "assistant",
            "content": ai_reply
        })

        print(f"\nBot: {ai_reply}\n")

    except Exception as e:
        messages.pop()
        print(f"\nAPI Error: {e}")
        print("Please try again.\n")

# Save conversation history to JSON after exiting
with open("sample_conversation.json", "w", encoding="utf-8") as file:
    json.dump(messages, file, indent=4, ensure_ascii=False)

print("\nConversation saved successfully!")
print("File: sample_conversation.json")
