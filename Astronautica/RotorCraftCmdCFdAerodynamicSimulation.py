import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdCFdAerodynamicSimulation():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftCFDSimulation.svg","MenuText": "RotorCraft Aerodynamic Simulation","ToolTip": "Begin Rotorcraft Aerodynamic Simulation"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft Cfd Simulation", "Press to begin the Aerodynamic Simulation of the rotorcraft body")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
