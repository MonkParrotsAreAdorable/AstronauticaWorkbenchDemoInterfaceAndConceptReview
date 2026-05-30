import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdSwashplateParametric():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftSwashPlateParametric.svg","MenuText": "RotorCraft Swashplate development","ToolTip": "Import a parametric swashplate or design your own"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Rotorcraft Swashplate development", "Import a parametric swashplate or design your own")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
