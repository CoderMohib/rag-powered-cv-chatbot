from services.cv_service import ask_cv

def main():
    print("💼 CV Assistant — type 'exit' to quit\n")

    while True:
        user_input = input("👤 You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Chat closed!")
            break

        answer = ask_cv(user_input)
        print("🤖 AI:", answer)


if __name__ == "__main__":
    main()