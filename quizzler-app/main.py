from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


# ------------------------ using API to get question and ans ---------------------------------------
question_bank = []
parameters = {
    'amount' : 10,
    # 'category' : 18,
    'type': "boolean",
}
response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
data = response.json()
for Ques in data["results"]:
    question_text = Ques['question']
    question_answer = Ques['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    

# -------------------------------------------------------------------------------------------------- 



quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
