class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        q = self.question_list[self.question_no]
        correct_answer = q.answer
        self.question_no = self.question_no + 1
        user_answer = input(f'Q.{self.question_no}. {q.text} (True/False) ? ')
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right hooray!!!")
            print(f"Your current score is {self.score}/{len(self.question_list)}")
        else:
            print("That's wrong")
            print(f'The correct answer was : {correct_answer}')
            print(f"Your current score is {self.score}/{len(self.question_list)}")
