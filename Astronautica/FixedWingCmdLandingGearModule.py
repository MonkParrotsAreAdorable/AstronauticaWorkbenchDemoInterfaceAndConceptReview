import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FixedWing_LandingGearModule:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FixedWingLandingGear.svg","MenuText": "Landing Gear Module","ToolTip": "Open Source modular landing gears for a variety of loads"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Landing gear module", "Open Source modular landing gears for a variety of loads")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
