import wx
import sys
import ping3
from socket import *
from time import gmtime, strftime


def portScan(event):
    if portEnd.GetValue() < portStart.GetValue():
        dlg = wx.MessageDialog(mainWin, "Invalid Host Port Selection", "Confirm", wx.OK | wx.ICON_EXCLAMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
    return
