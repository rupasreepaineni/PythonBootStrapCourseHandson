from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q= Question(question_text, question_answer)
    #print(question_text, question_answer),just to check if it is printing output or not
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    #***quiz.check_answer(user_answer,correct_answer), in quiz_brain.py file we have already called check_answer function in
    # next_question function so we don't need to call it here again.

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")



