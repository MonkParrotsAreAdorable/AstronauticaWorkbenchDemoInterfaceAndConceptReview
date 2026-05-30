import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FixedWing_FuselageSimulationFem:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FixedWingFuselageFEM.svg","MenuText": "FEM Fuselage Simulation","ToolTip": "Allows a user to run an FEM simulation on a fuselage"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "FEM Fuselage Simulation", "Allows a user to run an FEM simulation on a fuselage")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
