import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdFuselageRiveting():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftFuselageRiveting.svg","MenuText": "RotorCraft Riveting process","ToolTip": "Begin Rotorcraft Riveting process"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft Fuselage Riveting", "Press to begin the Riveting process of the rotorcraft body")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
