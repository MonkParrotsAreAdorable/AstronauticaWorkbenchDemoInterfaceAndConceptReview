import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdGearboxDefination():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftGearbox.svg","MenuText": "RotorCraft gearbox command","ToolTip": "Begin development of the gearbox of the rotorcraft"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft Gearbox command", "Press to begin the rotorcraft gearbox generation procedure , enter reduction ratios , etc.")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
