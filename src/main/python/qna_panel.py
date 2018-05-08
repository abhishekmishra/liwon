"""
A panel to display the components of a Q&A
"""

import wx


class QnAPanel(wx.Panel):
    """
    A panel to display the components of a Q&A
    """

    def __init__(self, parent, qna):
        super(QnAPanel, self).__init__(parent)
        self.qna = qna
        self.font1 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, True, 'Verdana')
        self.font2 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Verdana')

        self.SetFont(self.font2)
        self.SetForegroundColour('#0000ff')
        self.InitUI()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Question?')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.SetSizer(vbox)
