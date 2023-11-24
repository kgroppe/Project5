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



mainWin.Show()
app.MainLoop()
