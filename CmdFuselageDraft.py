import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FuselageDraft:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FuselageDraftModule.svg","MenuText": "Fuselage_Draft","ToolTip": "Fuselage draft , allows a user to draft the fuselage ."}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Fuselage Draft", "A user will use a sketcher like workbench to run a fuselage draft here , or maybe add a CPACS file import ")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
#FreeCADGui.addCommand('Fuselage_Draft', FuselageDraft())