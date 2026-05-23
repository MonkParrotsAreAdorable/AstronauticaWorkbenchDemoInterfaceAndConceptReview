import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RivetingFunc:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/Riveting.svg","MenuText": "Riveting","ToolTip": "Allows users to rivet the generated aircraft skin to the monocoque fuselage"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Riveting", "Allows users to add rivets through  the skin to the generated fuselage and monocoque body")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
#FreeCADGui.addCommand('Riveting',RivetingFunc())