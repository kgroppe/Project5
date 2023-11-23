import email.headerregistry

import wx
import sys
import ping3
import socket

from time import gmtime, strftime

def pingScan(event):
    if hostEnd.GetValue():
        dlg = wx.MessageDialog(mainWin, "Invalid Local Host Selection",
                               "Confirm:", wx.OK | wx.ICON_EXCLAMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return

    mainWin.StatusBar.SetStatusText("Executing Ping Sweep .... Please Wait")

    utcStart = gmtime()
    utc = strftime("%a, %d %b %Y %X + 0000", utcStart)
    Results.AppendText("\n\nPing Sweep Started: "+utc+"\n\n")
    baseIP = str(ipaRange.GetValue())+"."+str(ipbRange.GetVaule())+"."+str(ipcRange.GetVaule())+"."

    ipRange = []

    for i in range(hostStart.GetVaule(), (hostEnd.GetValue()+1)):
        ipRange.append(baseIP+str(i))

    for ipAddress in ipRange:

        try:
            mainWin.StatusBar.SetStatusText("Pinging IP: "+ ipAddress)
            delay = ping3.ping(ipAddress, timeout=2)
            Results.AppendText(ipAddress+"\t")

            if delay != None:
                Results.AppendText("Response Success")
                Results.AppendText("Resonse Time:" +str(delay)+"Seconds")
                Results.AppendText("\n")
            else:
                Results.AppendText("Response Timeout")
                Results.AppendText("\n")
        except OSError as e:
            Results.AppendText(ipAddress)
            Results.AppendText("Response Failed: ")
            Results.AppendText(e.message)
            Results.AppendTest("\n")

    utcEnd = gmtime()
    utc = strftime("%a, %d %b %Y %X + 0000", utcEnd)
    Results.AppendText("\n\nPing Sweep Ended: " + utc + "\n\n")

    mainWin.StatusBar.SetStatusText("")

    return

def programExit(event):
    mainWin.Close()

app = wx.App()
mainWin = wx.Frame(None, title="Simple Ping (IMCP) Sweeper 1.0", size=(1000,600))
panelAction = wx.Panel(mainWin)

scanButton = wx.Button(panelAction, label="Scan")
scanButton.Bind(wx.EVT_BUTTON, pingScan)

exitButton = wx.Button(panelAction, label="Exit")
exitButton.Bind(wx.EVT_BUTTON, programExit)

Results = wx.TextCtrl(panelAction, style=wx.TE_MULTILINE | wx.HSCROLL)

ipaRange = wx.SpinCtrl(panelAction, -1,'')
ipaRange.SetRange(0,255)
ipaRange.SetValue(127)

ipbRange = wx.SpinCtrl(panelAction, -1,'')
ipbRange.SetRange(0,255)
ipbRange.SetValue(0)

ipcRange = wx.SpinCtrl(panelAction, -1,'')
ipcRange.SetRange(0,255)
ipcRange.SetValue(0)

ipLabel = wx.StaticText(panelAction, label="IP Base: ")

hostStart = wx.SpinCtrl(panelAction, -1, '')
hostStart.SetRange(0,255)
hostStart.SetValue(1)

hostEnd = wx.SpinCtrl(panelAction, -1, '')
hostEnd.SetRange(0,255)
hostEnd.SetValue(10)

HostStartLabel = wx.StaticText(panelAction, label="Host Start: ")
HostEndLabel = wx.StaticText(panelAction, label="Host End: ")

actionBox = wx.BoxSizer()
actionBox.Add(scanButton, proportion=1, flag=wx.LEFT, border=5)
actionBox.Add(exitButton, proportion=0, flag=wx.LEFT, border=5)

actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT, border=5)

actionBox.Add(ipaRange, proportion=0, flag=wx.LEFT, bordre=5)
actionBox.Add(ipbRange, proportion=0, flag=wx.LEFT, bordre=5)
actionBox.Add(ipcRange, proportion=0, flag=wx.LEFT, bordre=5)

actionBox.Add(HostStartLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)
actionBox.Add(hostStart, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(HostEndLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)
actionBox.Add(hostEnd, proportion=0, flag=wx.LEFT, border=5)

vertBox = wx.BoxSizer(wx.VERTICAL)
vertBox.Add(actionBox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
vertBox.Add(Results,proportion=1, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=5)

mainWin.CreateStatusBar()

panelAction.SetSizer(vertBox)
