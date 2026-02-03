def kbc_question(question, options, correct_option):
    print("\n" + question)
    for key, value in options.items():
        print(f"{key}. {value}")

    answer = input("Enter your choice (A/B/C/D): ").strip().upper()

    if answer == correct_option:
        print("✅ Correct Answer! You earned ₹10,000.")
        return True
    else:
        print("❌ Wrong Answer. Game Over!")
        return False


def kbc_game():
    score = 0

    # Question 1
    q1 = "Which planet is known as the Red Planet?"
    options1 = {
        "A": "Earth",
        "B": "Mars",
        "C": "Jupiter",
        "D": "Venus"
    }

    if kbc_question(q1, options1, "B"):
        score += 10000
    else:
        print(f"Final Score: ₹{score}")
        return

    # Question 2
    q2 = "Who wrote the Indian National Anthem?"
    options2 = {
        "A": "Bankim Chandra Chatterjee",
        "B": "Rabindranath Tagore",
        "C": "Sarojini Naidu",
        "D": "Mahatma Gandhi"
    }

    if kbc_question(q2, options2, "B"):
        score += 10000
        print("🎉 Congratulations! You won the game!")
    else:
        print("Game Over!")

    print(f"Final Score: ₹{score}")


kbc_game()
