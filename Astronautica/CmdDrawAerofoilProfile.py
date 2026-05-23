import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class DrawAerofoilProfile:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/AerofoilSelectionTool.svg","MenuText": "Draw Aerofoil","ToolTip": "Allows User to sketch out an Aerofoil"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Draw Aerofoil function", "Allows user to draw an Aerofoil sketch")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
#FreeCADGui.addCommand('Draw_Aerofoil_Profile', DrawAerofoilProfile())