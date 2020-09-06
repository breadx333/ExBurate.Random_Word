import wx
import random

class TestWindow(wx.Frame):

    def chBtnClick(self, event):
        f = open("Words.txt", "r")
        random_word = random.choice(f.read().split("\n"))
        self.chText.SetLabel(random_word)
        f.close()
        self.panel.Layout()

    def AddWordEnter(self, event):
        f1 = open("Words.txt", "a")
        n = self.AddBox.GetValue()
        
        if n == "" or len(n.replace(" ", "")) == 0:
            f1.close()
        else:
            f1.write("\n" + n)
            f1.close()
            self.AddBox.SetValue("")
        
    def __init__(self, parent, title):
        wx.Panel.__init__(self, None, title=title)

        self.panel = wx.Panel(self, wx.ID_ANY)

        #self.status_bar = self.CreateStatusBar(style=0)

        VSizer = wx.BoxSizer(wx.VERTICAL)
        HSizer = wx.BoxSizer(wx.HORIZONTAL)
        H2Sizer = wx.BoxSizer(wx.HORIZONTAL)

        static_line1 = wx.StaticLine(self.panel)
        HSizer.Add(static_line1, 1, wx.ALIGN_CENTER|wx.ALL, 5)
        VSizer.Add(HSizer, 1, wx.EXPAND, 5)

        #self.png = wx.StaticBitmap(self, -1, wx.Bitmap("Background.png", wx.BITMAP_TYPE_ANY))
        #VSizer.Add(self.png, 0, wx.ALL, 5)

        self.NameText = wx.StaticText(self.panel, wx.ID_ANY, label="Welcome to ExBurate ver.0.2!")
        VSizer.Add(self.NameText, 1, wx.CENTER|wx.ALL, 5)

        self.AddBox = wx.TextCtrl(self.panel, wx.ID_ANY, style=wx.TE_PROCESS_ENTER|wx.TE_CENTER)
        VSizer.Add(self.AddBox, 1, wx.CENTER|wx.ALL, 5)

        self.chText = wx.StaticText(self.panel, wx.ID_ANY, label="Click Random")
        self.chText.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        VSizer.Add(self.chText, 1, wx.CENTER|wx.ALL, 5)
        
        self.chBtn = wx.Button(self.panel, wx.ID_ANY, label="Random!")
        VSizer.Add(self.chBtn, 1, wx.CENTER|wx.ALL, 5)

        static_line1 = wx.StaticLine(self.panel)
        H2Sizer.Add(static_line1, 1, wx.ALIGN_CENTER|wx.ALL, 5)
        VSizer.Add(H2Sizer, 1, wx.EXPAND, 5)

        self.AddBox.Bind(wx.EVT_TEXT_ENTER, self.AddWordEnter)
        self.chBtn.Bind(wx.EVT_BUTTON, self.chBtnClick)

        self.panel.SetSizer(VSizer)
        self.Centre()
        self.Show()

if __name__ == "__main__":
    try:
        Rf = open("Words.txt", "r")
        Rf.close()
    except FileNotFoundError:
        xf = open("Words.txt", "x")
        xf.close()
        z = open("Words.txt", "a")
        z.write("Click Random")
        z.close()
   
    app = wx.App()
    frame = TestWindow(None, "ExBurate ver.0.2")
    app.MainLoop()
