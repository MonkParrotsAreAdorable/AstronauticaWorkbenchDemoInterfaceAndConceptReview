import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdPlumbing():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftPlumbing.svg","MenuText": "RotorCraft Plumbing","ToolTip": "Define the plumbing and fuel systems of the rotorcraft"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft Plumbing Command", "Define the fuel systems , tanks and storage locations of the rotorcraft")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
