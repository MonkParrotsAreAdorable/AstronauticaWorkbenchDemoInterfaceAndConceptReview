import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FlightSurfaces:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FlightSurfaces.svg","MenuText": "Flight Surfaces","ToolTip": "Allows user to generate diffrent types of flight surfaces."}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Flight Surfaces", "Allows user to generate all flight surfaces")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
#FreeCADGui.addCommand('Flight_Surfaces',FlightSurfaces())