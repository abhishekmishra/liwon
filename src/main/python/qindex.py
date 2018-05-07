"""
Maintain a set of indices to the actual qna objects
via various key sets for e.g.
1. questions
2. todos
3. related topics
4. category

and more...
"""


class QIndex:
    """
    An index of QnA objects by questions and related subjects for now.
    """

    def __init__(self):
        self.qnas = []
        self.questions = {}
        self.categories = {}
        self.topics = {}

    def index(self, qna):
        if (qna not in self.qnas) and (qna.q not in self.questions.keys()):
            self.qnas.append(qna)
            self.questions.setdefault(qna.q, [])
            self.questions.get(qna.q).append(qna)

            for t in qna.related:
                self.topics.setdefault(t, [])
                self.topics.get(t).append(qna)

    def get_qna_for_question(self, question):
        for q in self.questions.keys():
            if question == q:
                return self.questions[q]
        return None

    def get_qnas_for_topic(self, topic):
        for t in self.topics.keys():
            if topic == t:
                return self.topics[t]
        return None

    def __str__(self):
        s = "questions = " + str(self.questions.keys()) + "\n"
        s += "(total = " + str(len(self.qnas)) + ")\n"
        s += "topics = " + str(self.topics.keys()) + "\n"
        s += "(total = " + str(len(self.topics.keys())) + ")"
        return s