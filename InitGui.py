import FreeCAD
import FreeCADGui
class AstronauticaWorkbench ( Workbench ):
    Icon = FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/AstronauticaWorkbench.svg"
    MenuText = "Astronautica"
    ToolTip = "Astronautica workbench"
    def Initialize(self):
        import AstronauticaGui
        self.appendToolbar('Astronautica',['Draw_Aerofoil_Profile'])
        self.appendToolbar('Astronautica',['Extrude_Wing_ribs_and_fem_simulation','Flight_Surfaces', 'CFd_Aerodynamic_Simulation' ,'Get_Mass', 'Fuselage_Draft', 'Fuselage_Blank_Spaces_Define', 'Fuselage_former_stringer_bulkhead', 'Fuselage_simulation_fem','Fuselage_simulation_cfd', 'Skinning', 'Riveting','Plumbing', 'Landing_Gear_Module'])
        self.appendMenu('Astronautica',['Draw_Aerofoil_Profile'])
        self.appendMenu('Astronautica',['Extrude_Wing_ribs_and_fem_simulation','Flight_Surfaces', 'CFd_Aerodynamic_Simulation' ,'Get_Mass', 'Fuselage_Draft', 'Fuselage_Blank_Spaces_Define', 'Fuselage_former_stringer_bulkhead', 'Fuselage_simulation_fem','Fuselage_simulation_cfd', 'Skinning', 'Riveting','Plumbing', 'Landing_Gear_Module'])
    def GetClassName(self):
        return "Gui::PythonWorkbench"
FreeCADGui.addWorkbench(AstronauticaWorkbench())
