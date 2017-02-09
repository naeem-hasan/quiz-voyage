from question_set import Question, QuestionSet
from random import shuffle


class Scrambles(QuestionSet):
    def __init__(self, filename="db/names.lst"):
        QuestionSet.__init__(self)
        with open(filename) as name_db:
            name_db = name_db.read().split("\n")[:-1]
            for name in name_db:
                question = Question(self._scram(name), name, 10, hint="")
                self.questions.append(question)

    def _scram(self, text):
        text = text.strip().split()
        n = []

        for i in text:
            p = []
            for t, x in enumerate(i):
                if x in ".-'!?,":
                    p.append((t, x))

            for x in ",.-'!?":
                i = i.replace(x, "")

            i = list(i)
            shuffle(i)
            i = ''.join(i)
            for x in p:
                i = i[:x[0]] + x[1] + i[x[0]:]

            n.append(i)
        return " ".join(n).upper()
