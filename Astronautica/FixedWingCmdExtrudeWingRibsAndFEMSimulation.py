import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FixedWing_ExtrudeWingRibsAndFEMSimulation:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FixedWingWingDefinationFunction.svg","MenuText": "Wing Generation with Spurs and simulation","ToolTip": "Allows a user to generate a wing with spars in a semi-automated fashion"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Extrude wing and ribs as well as FEM simulation", "This function allows the user to generate a wing and add wing spurs in a semi-automated fashion with a simulation loop providing guidance")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
