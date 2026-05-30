import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdGetMass():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftGetMass.svg","MenuText": "RotorCraft All Up Mass","ToolTip": "View the entire mass of the rotorcraft"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft Get Mass", "View the entire rotorcraft mass")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
