import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FuselageBlankSpacesDefine:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FuselageBlankSpaces.svg","MenuText": "Assign blank spaces to a fuselage","ToolTip": "Allows a user to define a blank space in a fuselage"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Assign Blank spaces", "Allows a user to define blank spaces in a fuselage , for things like a Cargo hold perhaps.")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
#FreeCADGui.addCommand('Fuselage_Blank_Spaces_Define', FuselageBlankSpacesDefine())