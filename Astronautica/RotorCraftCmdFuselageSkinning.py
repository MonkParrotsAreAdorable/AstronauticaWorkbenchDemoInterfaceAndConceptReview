import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdFuselageSkinning():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftFuselageSkinning.svg","MenuText": "RotorCraft Skinning process","ToolTip": "Begin Rotorcraft skinning process"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft fuselage Skinning", "Press to begin the Skinning process of the rotorcraft body")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
