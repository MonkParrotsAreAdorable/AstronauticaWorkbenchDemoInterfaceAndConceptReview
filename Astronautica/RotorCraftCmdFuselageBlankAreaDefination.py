import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdFuselageBlankAreaDefination():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftFuselageBlankSpaceDefination.svg","MenuText": "RotorCraft Fuselage Blank Area Defination","ToolTip": "Define the blank spaces for the rotorcraft to be excluded"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft Fuselage Blank section defination", "Press this to define the blank sections of the fuselage for cargo , pilot cockpit or other")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
