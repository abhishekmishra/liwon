class QnA:
    """
    A class which represents a question and answer object.

    It has the following:
    1. A question
    2. An optional category
    3. Related items
    4. Trigger
    5. Answer
    6. Follow-up questions
    7. To-do items
    """

    def __init__(self, text):
        self.text = text
        self.q = None
        self.category = None
        self.related = None
        self.trigger = None
        self.a = None
        self.followup = None
        self.todo = None

        self.break_it_up()

    def break_it_up(self):
        self.q, count = self.extract_question()
        self.category = self.extract_category()
        self.related = self.extract_related()
        self.trigger = self.extract_trigger()
        self.a = self.extract_answer()
        self.followup = self.extract_followup()
        self.todo = self.extract_todo()

    def extract_question(self):
        q = ""
        count = 0
        for l in self.text:
            count += 1
            if l.isspace():
                break
            q += l + '\n'

        return q.strip(), count

    def extract_category(self):
        category = ""
        in_category = False
        for l in self.text:
            if in_category:
                if l.isspace():
                    break
                category += l
            if l.startswith('Category:'):
                in_category = True

        return category

    def extract_related(self):
        relatedstr = ""
        inrel = False
        for l in self.text:
            if inrel:
                if l.isspace():
                    break
                relatedstr += l
            if l.startswith('Related:'):
                inrel = True

        related = relatedstr.split(',')
        related = [x.strip() for x in related]
        return related

    def extract_trigger(self):
        trigger = ""
        in_trigger = False
        for l in self.text:
            if in_trigger:
                if l.isspace():
                    break
                trigger += l
            if l.startswith('Trigger:'):
                in_trigger = True

        return trigger

    def extract_answer(self):
        answer = ""
        in_answer = False
        for l in self.text:
            if in_answer:
                if l.isspace():
                    break
                answer += l
            if l.startswith('Answer:'):
                in_answer = True

        return answer

    def extract_followup(self):
        followup_str = ""
        in_followup = False
        for l in self.text:
            if in_followup:
                if l.isspace():
                    break
                followup_str += l
            if l.startswith('Follow-up:'):
                in_followup = True

        followup = followup_str.splitlines()
        followup = [x.strip() for x in followup]
        return followup

    def extract_todo(self):
        todo_str = ""
        in_todo = False
        for l in self.text:
            if in_todo:
                if l.isspace():
                    break
                todo_str += l
            if l.startswith('Todo:'):
                in_todo = True

        todo = todo_str.splitlines()
        todo = [x.strip() for x in todo]
        return todo

    def __str__(self):
        s = "q=" + self.q + "\n"
        s += "category=" + self.category + "\n"
        s += "related=" + str(self.related) + "\n"
        s += "trigger=" + self.trigger + "\n"
        s += "a=" + self.a + "\n"
        s += "followup=" + str(self.followup) + "\n"
        s += "todo=" + str(self.todo) + "\n"
        return s