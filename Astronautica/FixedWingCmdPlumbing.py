import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FixedWing_PlumbingFunc:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FixedWingPlumbing.svg","MenuText": "Plumbing","ToolTip": "Allows a user to setup up fuel systems and electrical system"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Plumbing", "Allows a user to setup up fuel systems and electrical systems")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
