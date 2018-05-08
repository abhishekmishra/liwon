"""
A simple UI for the liwon data
"""

import wx
import liwon
import qindex
import qna_panel


class LiwonMainFrame(wx.Frame):
    """
    The top level window for the application.
    It will have a menubar, a toolbar, a statusbar and the main content
    area at the bottom
    """

    def __init__(self, qindex, title):
        super(LiwonMainFrame, self).__init__(None,
                                             title=title,
                                             size=(1024, 768))
        self.qindex = qindex
        self.topics = []
        self.questions = []
        self.set_state()

        self.init_ui()
        self.Center()

    def init_ui(self):
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Question?')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        topics_list_box = wx.ListBox(panel, -1, choices=self.topics)
        hbox2.Add(topics_list_box, 1, flag=wx.EXPAND | wx.ALL, border=8)
        vbox.Add(hbox2, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.add_questions(panel, hbox3)
        vbox.Add(hbox3, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, border=10)

        # vbox.Add((-1, 10))
        panel.SetSizer(vbox)

    def add_questions(self, panel, hbox3):
        for qna in self.qindex.qnas:
            question_panel = qna_panel.QnAPanel(panel, qna)
            hbox3.Add(question_panel, 1, flag=0, border=8)

    def set_state(self):
        self.topics.extend(self.qindex.topics.keys())


def main():
    qidx = qindex.QIndex()
    liwon.scan_all_files(liwon.LIWON_FOLDER + '/qna', qidx)
    print(qidx)

    print('Questions for the topic beetle are:')
    print([x.q for x in qidx.get_qnas_for_topic('beetle')])

    app = wx.App()
    ex = LiwonMainFrame(qindex=qidx, title='liwon: Learning in Wonderland')
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()