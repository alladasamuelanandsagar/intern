print("Welcome to the cricket quiz game")

name = input("Enter your Name:\n")

print(name, "You have 4 questions to answer")

cricket_questions = [
    {"question": "Who has scored the most runs in a single ODI match?", "Answer": "B"},
    {"question": "Which team won the ICC Cricket World Cup in 2019?", "Answer": "A"},
    {"question": "Who is known as the 'Sultan of Swing' in cricket?", "Answer": "C"},
    {"question": "Which cricketer has taken the most wickets in Test cricket?", "Answer": "D"}
]

cricket_answers = [
    ["A.Rohit Sharma", "B.Martin Guptill", "C.Virat Kohli", "D.Chris Gayle"],
    ["A.England", "B.Australia", "C.India", "D.New Zealand"],
    ["A.Brett Lee", "B.James Anderson", "C.Wasim Akram", "D.Glen McGrath"],
    ["A.Shane Warne", "B.Anil Kumble", "C.Curtly Ambrose", "D.Muttiah Muralitharan"]
]

score = 0

def answer(option, ans):
    if option == ans:
        return True
    else:
        return False

for question in range(len(cricket_questions)):
    print("")
    print("Question Number", question + 1)
    print(cricket_questions[question]["question"])
    for i in cricket_answers[question]:
        print(i)
        
    option = input("Enter A/B/C/D: ").upper()

    ans = cricket_questions[question]["Answer"]

    if answer(option, ans):
        print("Correct Answer!")
        score += 100
    else:
        print("Wrong Answer!")
    print(name, "your score is", score)

print(name, "your total score is:\n", score)
print(name, "your accuracy is", int((score / (len(cricket_questions) * 100) * 100)), "%")
1
