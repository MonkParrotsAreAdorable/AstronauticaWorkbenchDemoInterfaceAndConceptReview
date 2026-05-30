import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FixedWing_CFdAerodynamicSimulation():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FixedWingAerodynamicSimulationWing.svg","MenuText": "Aerodynamic Simulation","ToolTip": "Begin wing Aerodynamic Simulation"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Wing Aerodynamic Simulation Function", "Press to begin the Aerodynamic Simulation of the wing")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
