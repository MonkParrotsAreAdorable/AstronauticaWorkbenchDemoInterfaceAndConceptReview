import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FixedWing_FuselageSimulationCfd:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FixedWingFuselageCFD.svg","MenuText": "Fuselage CFD Simulation","ToolTip": "Allows a user to run a CFD simulation on the fuselage"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Fuselage CFD Simulation", "Allows the user to run a CFD simulation on the fuselage")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
