import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FixedWing_GetMass:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FixedWingGetMass.svg","MenuText": "Get Mass","ToolTip": "Get the all-up mass of the aircraft at take off"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Get Mass", "Get the all-up mass of the aircraft at take off")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
