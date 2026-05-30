import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdImportOrCreateFuselage():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftImportOrCreateFuselage.svg","MenuText": "RotorCraft Fuselage Import/Create","ToolTip": "Create or import a rotorcraft fuselage"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft Fuselage Import / Draft", "Draft a fuselage or Import a fuselage file")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
