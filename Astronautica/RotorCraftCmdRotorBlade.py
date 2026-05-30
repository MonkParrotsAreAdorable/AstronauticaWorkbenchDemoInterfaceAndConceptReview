import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdRotorBlade():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftBlades.svg","MenuText": "RotorCraft Blade Design","ToolTip": "Select the cross section and design the rotor craft blade"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft Blade Design", "Select the cross section and design the rotor craft blade")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
