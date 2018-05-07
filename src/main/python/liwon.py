"""
Main program for liwon, currently just a read-only view of questions, answers, topics, todos etc.
"""
import os
import qna
import qindex

LIWON_FOLDER = os.path.join(os.environ["HOME"], "Dropbox/liwon")


def scan_all_files(folder, qx):
    for f in os.listdir(folder):
        if f.endswith(".txt"):
            q = scan_file(os.path.join(folder, f))
            qx.index(q)
        print(f)


def scan_file(filename):
    f = open(filename)
    txt = f.readlines()
    f.close()
    q = qna.QnA(txt)
    return q


if __name__ == "__main__":
    qidx = qindex.QIndex()
    scan_all_files(LIWON_FOLDER + '/qna', qidx)
    print(qidx)

    print('Questions for the topic beetle are:')
    print([x.q for x in qidx.get_qnas_for_topic('beetle')])