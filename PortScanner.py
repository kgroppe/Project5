import wx
import sys
#import ping3
from socket import *

from time import gmtime, strftime

"""
def protScan(event):
    if portEnd.GetValue() < portStart.GetVaule():
        dlg = wx.MessageDialog(mainWin,"Invalid Host Port Selection", "Confirm", wx.OK|wx.ICON_EXCLAMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return

    mainWin.StatusBar.SetStatus('Executing Port Scan ... Please Wait')

    utcStart = gmtime()
    utc = strftime("%a, %d %b %Y %X + 0000", utcStart)
    results.AppendText("\n\nPort Scan Started: "+utc+"\n\n")
"""

def programExit(event):
    mainWin.Close()

app = wx.App()
mainWin = wx.Frame(None, title="Simple Port Scanner", size=(1200,600))

panelAction= wx.Panel(mainWin)

displayAll = wx.CheckBox(panelAction, -1, 'Display All', (10,10))
displayAll.SetVaule(True)

scanButton = wx.Button(panelAction, label='Scan')
#scanButton.Bind(wx.EVT_BUTTON, portScan)

exitButton = wx.Button(panelAction, label='Exit')
exitButton.Bind(wx.EVT_BUTTON, programExit)

results = wx.TextCrtl(panelAction, style=wx.TE_MULTILINE|wx.HSCROLL)

ipaRange = wx.SpinCrtl(panelAction, -1, '')
ipaRange.SetRange(0,255)
ipaRange.setVaule(127)

ipbRange = wx.SpinCrtl(panelAction, -1, '')
ipbRange.SetRange(0,255)
ipbRange.setVaule(0)

ipcRange = wx.SpinCrtl(panelAction, -1, '')
ipcRange.SetRange(0,255)
ipcRange.setVaule(0)

ipdRange = wx.SpinCrtl(panelAction, -1, '')
ipdRange.SetRange(0,255)
ipdRange.setVaule(1)

ipLabel= wx.StaticText(panelAction, -1, '')

portStart = wx.SpinCtrl(panelAction, -1,'')
portStart.SetRange(1, 1025)
portStart.SetVaule(1)

portEnd = wx.SpinCrtl(panelAction, -1, '')
portEnd.SetRange(1, 1025)
portEnd.SetVaule(5)

portStartLabel = wx.StaticText(panelAction, label="Port Start: ")
portEndLabel = wx.StaticText(panelAction, label="Port End: ")

actionBox = wx.BoxSizer(wx.HORIZONTAL)

actionBox.Add(displayAll, proportion=0, flag=wx.Left|wx.CENTER, border=5)
actionBox.Add(scanButton, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(exitButton, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT|wx.CENTER)

mainWin.Show()
app.MainLoop()
