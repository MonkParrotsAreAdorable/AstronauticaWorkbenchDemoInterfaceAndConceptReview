import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class LandingGearModule:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/LandingGear.svg","MenuText": "Landing Gear Module","ToolTip": "Open Source modular landing gears for a variety of loads"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Landing gear module", "Open Source modular landing gears for a variety of loads")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
#FreeCADGui.addCommand('Landing_Gear_Module', LandingGearModule())