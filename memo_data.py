
class Form:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_ans1
        self.wrong_answer2 = wrong_ans2
        self.wrong_answer3 = wrong_ans3


class FormView:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.form = Form(question, answer, wrong_ans1, wrong_ans2, wrong_ans3)

    def show(self):
        print("Питання:", self.form.question)
        print("Правильна відповідь:", self.form.answer)
        print("Неправильні відповіді:")
        print("1)", self.form.wrong_answer1)
        print("2)", self.form.wrong_answer2)
        print("3)", self.form.wrong_answer3)






