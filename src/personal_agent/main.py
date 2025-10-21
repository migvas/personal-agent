from dotenv import load_dotenv
from personal_agent.agent import PersonalAgent

load_dotenv(override=True)

if __name__ == "__main__":
    print("Welcome to your file agent. Type 'exit' to quit.")
    
    pa = PersonalAgent("gpt-oss", 0.2)

    while True:
        u = input("You: ")
        if u.strip().lower() in ("exit", "quit"):
            break
        resp = pa.send_message(message=u)
        print("Agent:", resp)
