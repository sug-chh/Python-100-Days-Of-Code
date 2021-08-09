from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_text = data['text']
    question_answer = data['answer']
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

