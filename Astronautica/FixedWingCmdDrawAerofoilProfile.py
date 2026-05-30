import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FixedWing_DrawAerofoilProfile:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FixedWingAerofoilSelectionTool.svg","MenuText": "Draw Aerofoil","ToolTip": "Allows User to sketch out an Aerofoil"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Draw Aerofoil function", "Allows user to draw an Aerofoil sketch")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
