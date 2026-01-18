import html


class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def check_answer(self, user_input, correct_answer):
        if user_input == correct_answer:
            self.score += 1
            print(f"Correct! Your score is {self.score}/{self.question_number}")
        else:
            print(f"Wrong! Your score is {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_question = html.unescape(current_question)
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_input = input(f"Q{self.question_number}. {current_question} True or False? ").title()

        self.check_answer(user_input, correct_answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)