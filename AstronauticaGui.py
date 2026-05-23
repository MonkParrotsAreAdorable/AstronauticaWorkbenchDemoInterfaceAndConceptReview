import FreeCAD
import FreeCADGui
from CmdCFdAerodynamicSimulation import CFdAerodynamicSimulation
from CmdDrawAerofoilProfile import DrawAerofoilProfile
from CmdExtrudeWingRibsAndFEMSimulation import ExtrudeWingRibsAndFEMSimulation
from CmdFlightSurfaces import FlightSurfaces
from CmdFuselageBlankSpacesDefine import FuselageBlankSpacesDefine
from CmdFuselageDraft import FuselageDraft
from CmdFuselageFormerStringerBulkhead import FuselageFormerStringerBulkhead
from CmdFuselageSimulationCfd import FuselageSimulationCfd
from CmdFuselageSimulationFem import FuselageSimulationFem
from CmdGetMass import GetMass
from CmdLandingGearModule import LandingGearModule
from CmdPlumbing import PlumbingFunc
from CmdRiveting import RivetingFunc
from CmdSkinning import SkinningFunc
FreeCADGui.addCommand('Draw_Aerofoil_Profile', DrawAerofoilProfile())
FreeCADGui.addCommand('Extrude_Wing_ribs_and_fem_simulation', ExtrudeWingRibsAndFEMSimulation())
FreeCADGui.addCommand('Flight_Surfaces', FlightSurfaces())
FreeCADGui.addCommand('CFd_Aerodynamic_Simulation', CFdAerodynamicSimulation())
FreeCADGui.addCommand('Get_Mass',GetMass())
FreeCADGui.addCommand('Fuselage_Draft', FuselageDraft())
FreeCADGui.addCommand('Fuselage_Blank_Spaces_Define', FuselageBlankSpacesDefine())
FreeCADGui.addCommand('Fuselage_former_stringer_bulkhead', FuselageFormerStringerBulkhead())
FreeCADGui.addCommand('Fuselage_simulation_fem', FuselageSimulationFem())
FreeCADGui.addCommand('Fuselage_simulation_cfd', FuselageSimulationCfd())
FreeCADGui.addCommand('Skinning', SkinningFunc())
FreeCADGui.addCommand('Riveting', RivetingFunc())
FreeCADGui.addCommand('Plumbing', PlumbingFunc())
FreeCADGui.addCommand('Landing_Gear_Module', LandingGearModule())
