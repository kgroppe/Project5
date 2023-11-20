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
    baseIP = str(ipaRange.GetValue())+"."+str(ipbRange.GetVaule())"."+str(ipcRange.GetVaule())+"."

    ipRange = []

    for i in range(hostStart.GetVaule(), (hostEnd.GetValue()+1)):
        ipRange.append(baseIP+str(i))
    