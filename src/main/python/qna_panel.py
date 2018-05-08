"""
A panel to display the components of a Q&A
"""

import wx


class QnAPanel(wx.ScrolledWindow):
    """
    A panel to display the components of a Q&A
    """

    def __init__(self, parent, qna):
        super(QnAPanel, self).__init__(parent)
        self.qna = qna
        self.font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        self.SetSize(50, 50)
        self.SetFont(self.font)
        self.InitUI()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        q_lbl = wx.StaticText(self, label='Question')
        q_lbl.SetForegroundColour('#0000ff')
        q_txt = wx.StaticText(self, label=self.qna.q)
        q_txt.SetForegroundColour('#000000')
        hbox1.Add(q_lbl, flag=wx.RIGHT, border=8)
        hbox1.Add(q_txt, flag=wx.RIGHT, border=8)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        a_lbl = wx.StaticText(self, label='Answer')
        a_lbl.SetForegroundColour('#0000ff')
        a_txt = wx.StaticText(self, label=self.qna.a)
        a_txt.SetForegroundColour('#000000')
        hbox2.Add(a_lbl, flag=wx.RIGHT, border=8)
        hbox2.Add(a_txt, flag=wx.RIGHT, border=8)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.SetSizer(vbox)
