from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)
    print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()
