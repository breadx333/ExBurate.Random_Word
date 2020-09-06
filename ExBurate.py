import wx
import random

class TestWindow(wx.Frame):

    def chBtnClick(self, event):
        f = open("Words.txt", "r")
        random_word = random.choice(f.read().split("\n"))
        self.chText.SetLabel(random_word)
        self.panel.Layout()

    def AddWordEnter(self, event):
        f1 = open("Words.txt", "a")
        n = self.AddBox.GetValue()
        f1.write(n + "\n")
        self.AddBox.SetValue("")
        
    def __init__(self, parent, title):
        wx.Frame.__init__(self, None, title=title, )

        self.panel = wx.Panel(self, wx.ID_ANY)

        VSizer = wx.BoxSizer(wx.VERTICAL)

        static_line1 = wx.StaticLine(self.panel)
        VSizer.Add(static_line1, 0, wx.EXPAND|wx.ALL, 5)

        #self.png = wx.StaticBitmap(self, -1, wx.Bitmap("Background.png", wx.BITMAP_TYPE_ANY))
        #VSizer.Add(self.png, 0, wx.ALL, 5)

        self.NameText = wx.StaticText(self.panel, wx.ID_ANY, label="ExBurate ver.0.1")
        VSizer.Add(self.NameText, 0, wx.CENTER|wx.ALL, 5)

        self.AddBox = wx.TextCtrl(self.panel, wx.ID_ANY, style=wx.TE_PROCESS_ENTER|wx.TE_CENTER)
        VSizer.Add(self.AddBox, 0, wx.CENTER|wx.ALL, 5)

        self.chText = wx.StaticText(self.panel, wx.ID_ANY, label="Click Random")
        self.chText.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        VSizer.Add(self.chText, 0, wx.CENTER|wx.ALL, 5)
        
        self.chBtn = wx.Button(self.panel, wx.ID_ANY, label="Random!")
        VSizer.Add(self.chBtn, 0, wx.CENTER|wx.ALL, 5)

        static_line1 = wx.StaticLine(self.panel)
        VSizer.Add(static_line1, 0, wx.EXPAND|wx.ALL, 5)

        self.AddBox.Bind(wx.EVT_TEXT_ENTER, self.AddWordEnter)
        self.chBtn.Bind(wx.EVT_BUTTON, self.chBtnClick)

        self.panel.SetSizer(VSizer)
        self.Centre()
        self.Show()

if __name__ == "__main__":
    try:
        open("Words.txt", "r")
    except FileNotFoundError:
        open("Words.txt", "x")
   
    app = wx.App()
    frame = TestWindow(None, "ExBurate ver.0.1")
    app.MainLoop()
