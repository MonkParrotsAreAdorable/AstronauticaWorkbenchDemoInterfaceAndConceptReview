import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdAnimation():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftAnimation.svg","MenuText": "RotorCraft Animation","ToolTip": "Begin rotorcraft assembly animations"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft animation", "Animate diffrent assemblies of the rotorcraft")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
