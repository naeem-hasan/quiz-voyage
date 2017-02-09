from question_set import Question, QuestionSet


class TriviaQuestions(QuestionSet):
    def __init__(self, filename="db/questions.lst"):
        QuestionSet.__init__(self)
        with open(filename) as qdb:
            all_questions = qdb.read()[:-1].split("\n")
            for each in all_questions:
                each = each.split(", ")
                self.questions.append(Question(each[0], each[1], int(each[2])))
