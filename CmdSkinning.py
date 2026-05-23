import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class SkinningFunc:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/Skinning.svg","MenuText": "Skinning","ToolTip": "Allows a user to generate the aircraft skin parametrically"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Skinning", "Allows a user to generate the aircraft skin parametrically")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
#FreeCADGui.addCommand('Skinning', SkinningFunc())