class Question(object):
    def __init__(self, question, answer, point, hint=""):
        self.question = question
        self.answer = answer
        self.hint = hint
        self.point = point

    def __str__(self):
        return self.question


class QuestionSet(object):
    def __init__(self):
        self.questions = []
        self.current_index = -1

    def get_next_question(self):
        self.current_index += 1
        return self.questions[self.current_index]

    def is_next_available(self):
        return not (self.current_index >= len(self.questions) - 1)
