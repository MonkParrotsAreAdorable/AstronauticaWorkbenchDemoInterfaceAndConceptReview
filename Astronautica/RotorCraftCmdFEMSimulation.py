import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class RotorCraft_CmdFEMSimulation():
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/RotorCraftFEMSimulation.svg","MenuText": "RotorCraft FEM Simulation","ToolTip": "Begin Rotorcraft FEM Simulation"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "RotorCraft FEM Simulation", "Press to begin the FEM Simulation of the rotorcraft body")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
