# IMPORT 
import rpw
from rpw import revit, db, ui, DB, UI
from rpw.ui.forms import *


# INSERT LINK
#User select a revit file in folders
filepath = select_file('Revit Model (*.rvt)|*.rvt')
#start transaction
with db.Transaction('insert link'):
  for path in filepath:
    linkpath = DB.ModelPathUtils.ConvertUserVisiblePathToModelPath(filepath)   
  linkoptions = DB.RevitLinkOptions(relative=True)
  linkloadresult = DB.RevitLinkType.Create(revit.doc, linkpath, linkoptions)
  DB.RevitLinkInstance.Create(revit.doc, linkloadresult.ElementId)



# MAQUETTE
level_category = db.Collector(of_category='Levels', is_not_type=True)
level_elements = level_category.get_elements()
level_name = [levels.LookupParameter("Nom").AsString() for levels in level_elements]
level_elevation = [levels.Elevation for levels in level_elements]
level_id = [levels.Id for levels in level_elements]

grid_category = db.Collector(of_category='OST_Grids', is_not_type=True)
grid_elements = grid_category.get_elements()

# COLLECT LEVELS LINK
collector_maq = DB.FilteredElementCollector(revit.doc)
linkInstances = collector_maq.OfClass(DB.RevitLinkInstance)
linkDoc = [links.GetLinkDocument() for links in linkInstances]
collector_link = DB.FilteredElementCollector(linkDoc[0])

level_elements_link = collector_link.OfClass(DB.Level).ToElements()
level_name_link = [levels.LookupParameter("Nom").AsString() for levels in level_elements_link]
level_elevation_link = [levels.Elevation for levels in level_elements_link]

# COLLECT GRIDS LINK
collector_maq = DB.FilteredElementCollector(revit.doc)
linkInstances = collector_maq.OfClass(DB.RevitLinkInstance)
linkDoc = [links.GetLinkDocument() for links in linkInstances]   
collector_link = DB.FilteredElementCollector(linkDoc[0])

grid_elements_link = collector_link.OfClass(DB.Grid).ToElements()
grid_name_link = [grids.Name for grids in grid_elements_link]
grid_length_link = [grids.Curve.Length for grids in grid_elements_link]
grid_origin_link = [grids.Curve.Origin for grids in grid_elements_link]
grid_direction_link = [grids.Curve.Direction for grids in grid_elements_link]

# ACQUIRE COORDINATES
collector_maq = DB.FilteredElementCollector(revit.doc)
linkInstances = collector_maq.OfClass(DB.RevitLinkInstance)
linkDoc = [links.GetLinkDocument() for links in linkInstances]   
collector_link = DB.FilteredElementCollector(linkDoc[0])
coord = DB.Document.AcquireCoordinates(linkInstances)

# # CREATE LEVELS
# with db.Transaction('create levels'):
#   for k in range(len(level_elements_link)):
#     NewLevel = DB.Level.Create(document = revit.doc, elevation = 0)
#     NewLevel.Name = level_name_link[k]
#     NewLevel.Elevation = level_elevation_link[k]

# # DELETE LEVELS 
# with db.Transaction('delete levels'):
#   for levels in level_id:
#     DB.Document.Delete(revit.doc, levels)

# # CREATE GRIDS
# with db.Transaction('create grids'):
#   for k in range(len(grid_elements_link)):
#     start = db.XYZ(0,0,0)
#     end = db.XYZ(0,0,0)
#     BaseLine = db.Line.new([0,0],[1,1])
#     NewGrid = DB.Grid.Create(document = revit.doc, line = BaseLine)
#     NewGrid.Name = grid_name_link[k]
#     NewGrid.Curve.Origin = grid_origin_link[k]
#     NewGrid.Curve.Length = grid_length_link[k]
#     NewGrid.Curve.Direction = grid_direction_link[k]




# OUT

print grid_origin_link, grid_length_link, grid_direction_link

  