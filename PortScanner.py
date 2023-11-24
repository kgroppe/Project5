import wx
import sys
import ping3
from socket import *

from time import gmtime, strftime

def protScan(event):
    if portEnd.GetValue() < portStart.GetVaule():
        dlg = wx.MessageDialog(mainWin,"Invalid Host Port Selection", "Confirm", wx.OK|wx.ICON_EXCLAMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return

    mainWin.StatusBar.SetStatus9'Executing Port Scan ... Please Wait')

    

