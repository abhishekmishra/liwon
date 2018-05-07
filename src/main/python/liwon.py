"""
Main program for liwon, currently just a read-only view of questions, answers, topics, todos etc.
"""
import os


LIWON_FOLDER = os.path.join(os.environ["HOME"], "Dropbox/liwon")


def scan_all_files(folder):
    for f in os.listdir(folder):
        if f.endswith(".txt"):
            scan_file(os.path.join(folder, f))
        print(f)


def scan_file(fname):
    f = open(fname)
    txt = f.readlines()
    f.close()
    #print(txt)
    break_it_up(txt)


def break_it_up(txt):
    q, count = get_question(txt)
    print(q)
    related = get_related(txt)
    print(related)


def get_question(txt):
    q = ""
    count = 0
    for l in txt:
        count += 1
        if l.isspace():
            break
        q += l + '\n'

    return q, count


def get_related(txt):
    relatedstr = ""
    inrel = False
    for l in txt:
        if inrel:
            if l.isspace():
                break
            relatedstr += l
        if l.startswith('Related:'):
            inrel = True

    related = relatedstr.split(',')
    related = [x.strip() for x in related]
    return related


def get_trigger(txt):
    trigger = ""
    in_trigger = False
    for l in txt:
        if in_trigger:
            if l.isspace():
                break
            trigger += l
        if l.startswith('Trigger:'):
            in_trigger = True

    return trigger


def get_answer(txt):
    answer = ""
    in_answer = False
    for l in txt:
        if in_answer:
            if l.isspace():
                break
            answer += l
        if l.startswith('Answer:'):
            in_answer = True

    return answer


if __name__ == "__main__":
    scan_all_files(LIWON_FOLDER + '/qna')