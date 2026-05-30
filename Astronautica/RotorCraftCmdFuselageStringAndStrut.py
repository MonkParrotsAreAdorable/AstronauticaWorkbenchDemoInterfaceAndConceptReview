import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdFuselageStringAndStrut():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftStringAndStrut.svg","MenuText": "RotorCraft Fuselage string and strut generation","ToolTip": "Begin Rotorcraft String and strut generation"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft fuselage string and strut creation", "Press to begin the entire rotorcraft string and strut procudure with an FEM simulation loop")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
