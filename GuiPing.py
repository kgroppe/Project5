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
    baseIP = str(ipaRange.GetValue())+"."+str(ipbRange.GetVaule())"."+str(ipcRange.GetVaule())+"."

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

        
