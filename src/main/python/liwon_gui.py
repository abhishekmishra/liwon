"""
A simple UI for the liwon data
"""

import wx


class LiwonMainFrame(wx.Frame):
    """
    The top level window for the application.
    It will have a menubar, a toolbar, a statusbar and the main content
    area at the bottom
    """

    def __init__(self, title):
        super(LiwonMainFrame, self).__init__(None, title=title,
                                      size=(350, 250))


def main():
    app = wx.App()
    ex = LiwonMainFrame(title='liwon: Learning in Wonderland')
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()