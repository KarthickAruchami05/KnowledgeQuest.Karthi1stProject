#Knowledge Quest Project Code:

quiz = {
    "What is the capital of India?": ['1) Mumbai', '2) Kolkata', '3) New Delhi', '4) Chennai', 3],
    "What is the largest mammal in the world?": ['1) Elephant', '2) Blue Whale', '3) Hippopotamus', '4) Rhino', 2],
    "What is the highest mountain in the world?": ['1) K2', '2) Mount Everest', '3) Kilimanjaro', '4) Mont Blanc', 2],
    "Who is the founder of Microsoft?": ['1) Bill Gates', '2) Steve Jobs', '3) Mark Zuckerberg', '4) Jeff Bezos', 1],
    "Which country gifted the Statue of Liberty to the United States?": ['1) France', '2) Germany', '3) Spain', '4) Italy', 1],
    "What is the smallest planet in our solar system?": ['1) Venus', '2) Mercury', '3) Mars', '4) Earth', 2],
    "What is the currency of Japan?": ['1) Won', '2) Yen', '3) Pound', '4) Euro', 2],
    "Which continent is the largest in the world?": ['1) Africa', '2) Europe', '3) Asia', '4) Australia', 3],
     "Which planet is known as the Red Planet?": ['1) Mars', '2) Venus', '3) Jupiter', '4) Saturn', 1],
    "What is the smallest country in the world?": ['1) Monaco', '2) Vatican City', '3) Luxembourg', '4) Liechtenstein', 2]
}

score = 0

for question in quiz:
    options = quiz[question][:4]
    answer = quiz[question][4]
    print(question)
    
    for option in options:
        print(option)
    choice = input("Enter your answer (1-4), or press s to skip: ")
    if choice == 's':
        print("Question skipped.")
        continue
    elif choice not in ['1', '2', '3', '4']:
        print("Invalid input. Question marked as zero.")
    elif int(choice) == answer:
        print("Correct!")
        score += 2
    else:
        print("Incorrect.")
        score -= 1

    print("Current score:", score)
    print()

print('final score',score)






