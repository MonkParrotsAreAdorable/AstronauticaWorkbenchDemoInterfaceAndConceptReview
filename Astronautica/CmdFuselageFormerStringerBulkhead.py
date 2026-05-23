import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
class FuselageFormerStringerBulkhead:
    def GetResources(self):
        return {"Pixmap": FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/FuselageFormerBulkhead.svg","MenuText": "Fuselage Stringer , Former and Bulkhead module","ToolTip": "Add formers , stringers and bulkheads to your fuselage"}
    def Activated(self):
        QtGui.QMessageBox.information(None, "Fuselage Former , Stringer and Bulkhead", "This feature allows a user to add formers , stringers and bulkheads into a fuselage created from the Fuselage draft function and fuselage blank spaces function")
    def IsActive(self):
       return FreeCAD.ActiveDocument is not None
#FreeCADGui.addCommand('Fuselage_former_stringer_bulkhead', FuselageFormerStringerBulkhead())