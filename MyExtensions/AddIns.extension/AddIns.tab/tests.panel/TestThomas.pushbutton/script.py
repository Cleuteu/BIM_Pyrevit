# IMPORT 

import rpw
from rpw import revit, db, ui, DB, UI
from rpw.ui.forms import *

# MAQUETTE
level_category = db.Collector(of_category='Levels', is_not_type=True)
level_elements = level_category.get_elements()
level_name = [levels.LookupParameter("Nom").AsString() for levels in level_elements]
level_elevation = [levels.ProjectElevation for levels in level_elements]

base_point_category = db.Collector(of_category='OST_ProjectBasePoint')
base_point_elements = base_point_category.get_elements()
base_point_elevation = [pdb.LookupParameter("Elév.").AsValueString() for pdb in base_point_elements]

# LINK
collector_maq = DB.FilteredElementCollector(revit.doc)
linkInstances = collector_maq.OfClass(DB.RevitLinkInstance)
linkDoc = [links.GetLinkDocument() for links in linkInstances]
collector_link = DB.FilteredElementCollector(linkDoc[0])

level_elements_link = collector_link.OfClass(DB.Level).ToElements()
level_name_link = [levels.LookupParameter("Nom").AsString() for levels in level_elements_link]
level_elevation_link = [levels.ProjectElevation for levels in level_elements_link]

print base_point_elevation

# OUT


  