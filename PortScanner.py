import socket

import wx
from socket import *

from time import gmtime, strftime

def portScan(event):
    if portEnd.GetValue() < portStart.GetValue():
        dlg = wx.MessageDialog(mainWin,"Invalid Host Port Selection", "Confirm", wx.OK|wx.ICON_EXCLAMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return

    mainWin.StatusBar.SetStatusText('Executing Port Scan ... Please Wait')

    utcStart = gmtime()
    utc = strftime("%a, %d %b %Y %X", utcStart)
    results.AppendText("\n\nPort Scan Started: "+utc+"\n\n")
    baseIP = str(ipaRange.GetValue())+'.'+str(ipbRange.GetValue())+'.'+str(ipcRange.GetValue())+'.'+str(ipdRange.GetValue())
    for port in range(portStart.GetValue(), portEnd.GetValue()+1):
        try:
            mainWin.StatusBar.SetStatusText("Scanning:" + baseIP + "Port: " +str(port))
            reqSocket = socket(AF_INET, SOCK_STREAM)
            response = reqSocket.connect_ex((baseIP, port))

            if response == 0:
                results.AppendText(baseIP + "\t"+str(port)+'\t')
                results.AppendText('Open')
                results.AppendText('\n')
            else:
                if displayAll.GetValue() == True:
                    results.AppendText(baseIP+'\t'+str(port)+'\t')
                    results.AppendText('Closed')
                    results.AppendText('\n')
            reqSocket.close()
        except OSError as e:
            results.AppendText(baseIP+'\t'+str(port)+'\t')
            results.AppendText('Failed: ')
            results.AppendText(e)
            results.AppendText('\n')
        utcEnd = gmtime()
        utc = strftime("%a, %d %b %Y %X", utcEnd)
        results.AppendText('\nPort Scan Ended: '+utc+ '\n\n')
        mainWin.StatusBar.SetStatusText('')


def programExit(event):
    mainWin.Close()

app = wx.App()
mainWin = wx.Frame(None, title="Simple Port Scanner", size=(1200,600))

panelAction= wx.Panel(mainWin)

displayAll = wx.CheckBox(panelAction, -1, 'Display All', (10,10))
displayAll.SetValue(True)

scanButton = wx.Button(panelAction, label='Scan')
scanButton.Bind(wx.EVT_BUTTON, portScan)

exitButton = wx.Button(panelAction, label='Exit')
exitButton.Bind(wx.EVT_BUTTON, programExit)

results = wx.TextCtrl(panelAction, style=wx.TE_MULTILINE|wx.HSCROLL)

ipaRange = wx.SpinCtrl(panelAction, -1, '')
ipaRange.SetRange(0,255)
ipaRange.SetValue(127)

ipbRange = wx.SpinCtrl(panelAction, -1, '')
ipbRange.SetRange(0,255)
ipbRange.SetValue(0)

ipcRange = wx.SpinCtrl(panelAction, -1, '')
ipcRange.SetRange(0,255)
ipcRange.SetValue(0)

ipdRange = wx.SpinCtrl(panelAction, -1, '')
ipdRange.SetRange(0,255)
ipdRange.SetValue(1)

ipLabel= wx.StaticText(panelAction, -1, '')

portStart = wx.SpinCtrl(panelAction, -1,'')
portStart.SetRange(1, 1025)
portStart.SetValue(1)

portEnd = wx.SpinCtrl(panelAction, -1, '')
portEnd.SetRange(1, 1025)
portEnd.SetValue(5)

PortStartLabel = wx.StaticText(panelAction, label="Port Start: ")
PortEndLabel = wx.StaticText(panelAction, label="Port End: ")

actionBox = wx.BoxSizer()

actionBox.Add(displayAll, proportion=0, flag=wx.Left|wx.CENTER, border=5)
actionBox.Add(scanButton, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(exitButton, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)

actionBox.Add(ipaRange, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipbRange, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipcRange, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipdRange, proportion=0, flag=wx.LEFT, border=5)

actionBox.Add(PortStartLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)
actionBox.Add(portStart, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(PortEndLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)
actionBox.Add(portEnd, proportion=0, flag=wx.LEFT, border=5)

vertBox = wx.BoxSizer(wx.VERTICAL)
vertBox.Add(actionBox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
vertBox.Add(results, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=5)

mainWin.CreateStatusBar()
panelAction.SetSizer(vertBox)


mainWin.Show()
app.MainLoop()
