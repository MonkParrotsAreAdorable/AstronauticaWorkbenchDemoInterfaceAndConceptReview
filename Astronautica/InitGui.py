import FreeCAD
import FreeCADGui
class AstronauticaWorkbench ( Workbench ):
    Icon = FreeCAD.getUserAppDataDir() + "Mod/Astronautica/Resources/icons/AstronauticaWorkbench.svg"
    MenuText = "Astronautica"
    ToolTip = "Astronautica workbench"
    def Initialize(self):
        import AstronauticaGui
        self.appendToolbar('Astronautica_FixedWing',['FixedWing_Draw_Aerofoil_Profile','FixedWing_Extrude_Wing_ribs_and_fem_simulation','FixedWing_Flight_Surfaces', 'FixedWing_CFd_Aerodynamic_Simulation', 'FixedWing_Fuselage_Draft', 'FixedWing_Fuselage_Blank_Spaces_Define', 'FixedWing_Fuselage_former_stringer_bulkhead', 'FixedWing_Fuselage_simulation_fem','FixedWing_Fuselage_simulation_cfd', 'FixedWing_Skinning', 'FixedWing_Riveting','FixedWing_Plumbing', 'FixedWing_Landing_Gear_Module' ,'FixedWing_Get_Mass'])
        self.appendToolbar('Astronautica_RotorCraft',['Separator','RotorCraft_Import_Or_Create_Fuselage','RotorCraft_Fuselage_String_And_Strut','RotorCraft_Skinning','RotorCraft_Riveting','RotorCraft_Plumbing','RotorCraft_Gearbox','RotorCraft_Rotor_Blade','RotorCraft_Swashplate','RotorCraft_Get_Mass','RotorCraft_FEM_Simulation','RotorCraft_CFD_Simulation'])
        self.appendMenu('Astronautica_FixedWing',['FixedWing_Draw_Aerofoil_Profile','FixedWing_Extrude_Wing_ribs_and_fem_simulation','FixedWing_Flight_Surfaces', 'FixedWing_CFd_Aerodynamic_Simulation' , 'FixedWing_Fuselage_Draft', 'FixedWing_Fuselage_Blank_Spaces_Define', 'FixedWing_Fuselage_former_stringer_bulkhead', 'FixedWing_Fuselage_simulation_fem','FixedWing_Fuselage_simulation_cfd', 'FixedWing_Skinning', 'FixedWing_Riveting','FixedWing_Plumbing', 'FixedWing_Landing_Gear_Module','FixedWing_Get_Mass'])
        self.appendMenu('Astronautica_RotorCraft',['Separator','RotorCraft_Import_Or_Create_Fuselage','RotorCraft_Fuselage_String_And_Strut','RotorCraft_Skinning','RotorCraft_Riveting','RotorCraft_Plumbing','RotorCraft_Gearbox','RotorCraft_Rotor_Blade','RotorCraft_Swashplate','RotorCraft_Get_Mass','RotorCraft_FEM_Simulation','RotorCraft_CFD_Simulation'])
    def GetClassName(self):
        return "Gui::PythonWorkbench"
FreeCADGui.addWorkbench(AstronauticaWorkbench())
