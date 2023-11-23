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
    results.AppendText("\n\nPing Sweep Started: "+utc+"\n\n")
    baseIP = str(ipaRange.GetValue())+"."+str(ipbRange.GetVaule())+"."+str(ipcRange.GetVaule())+"."

    ipRange = []

    for i in range(hostStart.GetVaule(), (hostEnd.GetValue()+1)):
        ipRange.append(baseIP+str(i))

    for ipAddress in ipRange:

        try:
            mainWin.StatusBar.SetStatusText("Pinging IP: "+ ipAddress)
            delay = ping3.ping(ipAddress, timeout=2)
            results.AppendText(ipAddress+"\t")

            if delay != None:
                results.AppendText("Response Success")
                results.AppendText("Resonse Time:" +str(delay)+"Seconds")
                results.AppendText("\n")
            else:
                results.AppendText("Response Timeout")
                results.AppendText("\n")
        except OSError as e:
            results.AppendText(ipAddress)
            results.AppendText("Response Failed: ")
            results.AppendText(e.message)
            results.AppendTest("\n")

    utcEnd = gmtime()
    utc = strftime("%a, %d %b %Y %X + 0000", utcEnd)
    results.AppendText("\n\nPing Sweep Ended: " + utc + "\n\n")

    mainWin.StatusBar.SetStatusText("")

    return

def programExit(event):
    mainWin.Close()

app = wx.App()
mainWin = wx.Frame(None, title="Simple Ping (IMCP) Sweeper 1.0", size=(1000,600))
panelAction = wx.Panel(mainWin)

scanButton = wx.Button(panelAction, label="Scan")
scanButton.Bind(wx.EVT_BUTTON, pingScan())

exitButton = wx.Button(panelAction, label="Exit")
exitButton.Bind(wx.EVT_BUTTON, programExit())

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

hostStartLabel = wx.StaticText(panelAction, label="Host Start: ")
hostEndLabel = wx.StaticText(panelAction, label="Host End: ")

actionBox = wx.BoxSizer()
actionBox.Add(scanButton, proportion=1, flag=wx.LEFT, border=5)
actionBox.Add(exitButton, proportion=0, flag=wx.LEFT, border=5)
