# IMPORT
import clr
import System 
import rpw
from rpw import revit, db, ui, DB, UI
from rpw.ui.forms import *
from System import Array
from System.Runtime.InteropServices import Marshal


# CHECK POUR BOUYGUE IMMO 
# category type or name from maquette
liste_cat = []
# Surface
surface_category = db.Collector(of_category='Areas', is_not_type=True)
surface_element = surface_category.get_elements()
surface_name = [surface.LookupParameter('Nom').AsString() for surface in surface_element]
liste_cat.append(surface_name)
# piece
room_category = db.Collector(of_category='Rooms', is_not_type=True)
room_element = room_category.get_elements()
room_name = [room.LookupParameter('Nom').AsString() for room in room_element]
liste_cat.append(room_name)
# zone

# Mur
wall_category = db.Collector(of_category='Walls', is_not_type=True)
wall_element = wall_category.get_elements()
wall_type = [wall.LookupParameter('Type').AsValueString() for wall in wall_element]
liste_cat.append(wall_type)
# poteau
column_category = db.Collector(of_category='Columns', is_not_type=True)
column_element = column_category.get_elements()
column_type = [column.LookupParameter('Type').AsValueString() for column in column_element]
liste_cat.append(column_type)
# poutre
# beam_category = db.Collector(of_category='Beams', is_not_type=True)
# beam_element = beam_category.get_elements()
# beam_type = [beam.LookupParameter('Type').AsValueString() for beam in beam_element]
# liste_cat.append(beam_type)
# sol
floor_category = db.Collector(of_category='Floors', is_not_type=True)
floor_element = floor_category.get_elements()
floor_type = [floor.LookupParameter('Type').AsValueString() for floor in floor_element]
liste_cat.append(floor_type)
# toiture
roof_category = db.Collector(of_category='Roofs', is_not_type=True)
roof_element = roof_category.get_elements()
roof_type = [roof.LookupParameter('Type').AsValueString() for roof in roof_element]
liste_cat.append(roof_type)
# fenetre
window_category = db.Collector(of_category='windows', is_not_type=True)
window_element = window_category.get_elements()
window_type = [window.LookupParameter('Type').AsValueString() for window in window_element]
liste_cat.append(window_type)
# mur-rideau

# escalier
stair_category = db.Collector(of_category='stairs', is_not_type=True)
stair_element = stair_category.get_elements()
stair_type = [stair.LookupParameter('Type').AsValueString() for stair in stair_element]
liste_cat.append(stair_type)
# cloison

# plafond
ceiling_category = db.Collector(of_category='ceilings', is_not_type=True)
ceiling_element = ceiling_category.get_elements()
ceiling_type = [ceiling.LookupParameter('Type').AsValueString() for ceiling in ceiling_element]
liste_cat.append(ceiling_type)
# Porte
door_category = db.Collector(of_category='doors', is_not_type=True)
door_element = door_category.get_elements()
door_type = [door.LookupParameter('Type').AsValueString() for door in door_element]
liste_cat.append(door_type)
# brise soleil
# store
# garde-coprs
# appareil elevateur
# parking
# topographie
# voirie




# EXCEL
clr.AddReferenceByName('Microsoft.office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel
ex = Excel.ApplicationClass()
ex.Visible = True
ex.DisplayAlerts = False
xlApp = Marshal.GetActiveObject("Excel.Application")

fileData = ['C:\Users\ThomasFaguet\Documents\PROJETS\PUISARD Lyon\Cahier_des_charges_Codification.xlsx']
fileVisa = ['C:\Users\ThomasFaguet\Documents\PROJETS\PUISARD Lyon\DonneesBrutesCodification.xlsx']

wb_data = ex.Workbooks.Open(fileData[0])
ws_data = wb_data.Worksheets[1]

corresp={0:"A",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z",27:"AA",28:"AB",29:"AC",30:"AD",31:"AE",32:"AF",33:"AG",34:"AH",35:"AI",36:"AJ",37:"AK",38:"AL",39:"AM",40:"AN",41:"AO",42:"AP",43:"AQ",44:"AR",45:"AS",46:"AT",47:"AV",48:"AW",49:"AX",50:"AY",51:"AZ"}
xlrange={}
for i in range(1,51):
  for j in range(1,100):
    xlrange[i,j] = corresp[i]+str(j) 


#tableau data
obj = [[] for k in range(100)]
for i in range(2,51):
  if ws_data.Range[xlrange[i,1]].text != "":
    for j in range(2,100):
      if ws_data.Range[xlrange[i,j]].text != "":
        obj[i-2].append(ws_data.Range[xlrange[i,j]].text)


#tableau visa
wb_visa = ex.Workbooks.Open(fileVisa[0])
ws_visa = wb_visa.Worksheets[2]

#operations
for j in range(1,10):
  res1 = len(liste_cat[j])
  n = float(0)
  for typ in liste_cat[j]:
    for data in obj[j]:
      if data == typ:
        n = n + 1
        pourcent = n/res1
        cell = ws_visa.Range[xlrange[1,j]]
        cell.Value2 = res1
        cell2 = ws_visa.Range[xlrange[2,j]]
        cell2.Value2 = n
        cell3 = ws_visa.Range[xlrange[3,j]]
        cell3.Value2 = pourcent


# cell = ws_visa.Range["A1"]
# cell.Value2 = res1
# cell2 = ws_visa.Range["B1"]
# cell2.Value2 = n
# cell3 = ws_visa.Range["C1"]
# cell3.Value2 = pourcent

#fermeture excel
Marshal.ReleaseComObject(ws_data)
Marshal.ReleaseComObject(ws_visa)
Marshal.ReleaseComObject(wb_data)
Marshal.ReleaseComObject(wb_visa)
Marshal.ReleaseComObject(xlApp)




# # # USERFORM BIM CHECKER
# # components = [Label('Check a choisir'),
# #               CheckBox('checkbox1', 'Verifier le nom de la maquette'),
# #               CheckBox('checkbox2', 'Verifier si la maquette est centrale ou local'),
# #               CheckBox('checkbox3', 'Verifier le nombre de groupe dans la maquette' ),
# #               CheckBox('checkbox4', 'Verifier emplacement partage'),
# #               CheckBox('checkbox5', 'Verifier le point de base'),
# #               CheckBox('checkbox6', 'Verifier les niveaux'),
# #               CheckBox('checkbox7', 'Verifier les quadrillages'),
# #               CheckBox('checkbox8', 'Verifier les avertissements'),
# #               CheckBox('checkbox9', 'Verifier si chaque vue est utilisee pour une vue en plan'),
# #               CheckBox('checkbox10', 'Verifier le poids de la maquette'),
# #               CheckBox('checkbox11', 'Verifier la version Revit'),
# #               Label('Version Revit'),
# #               ComboBox('combobox1', {'2015':2015, '2016':2016, '2017':2017, '2018':2018, '2019':2019}),
# #               Label('Nom maquette exacte'),
# #               TextBox('textbox1', Text="EXEMPLE_MAQUETTE.rvt"),
# #               Label('Poids maximum maquette'),
# #               ComboBox('combobox2', {'150':150, '200':200, '250':250, '300':300, '350':350, '400':400, '450':450}),
# #               Label('choisir maquette QNP'),
# #               Button(button_text='QNP'),             
# #               Label('choisir visa Excel'),
# #               Button(button_text='VISA BIM'),
# #               Separator(), 
# #               Button('OK GO')]
# # form = FlexForm('BIM CHECKER DU FUTUR', components)
# # form.show()




# # # INSERT LINK
# # #User select a revit file in folders
# # filepath = select_file('Revit Model (*.rvt)|*.rvt')
# # #start transaction
# # with db.Transaction('insert link'):
# #   for path in filepath:
# #     linkpath = DB.ModelPathUtils.ConvertUserVisiblePathToModelPath(filepath)   
# #   linkoptions = DB.RevitLinkOptions(relative=True)
# #   linkloadresult = DB.RevitLinkType.Create(revit.doc, linkpath, linkoptions)
# #   DB.RevitLinkInstance.Create(revit.doc, linkloadresult.ElementId)

# # # ACQUIRE COORDINATES
# # # collector_maq = DB.FilteredElementCollector(revit.doc)
# # # linkInstances = collector_maq.OfClass(DB.RevitLinkInstance).AsElementId()

# # # DB.Document.AcquireCoordinates(linkInstances)

# # # GET SITE LOCATION LINK
# # collector_maq = DB.FilteredElementCollector(revit.doc)
# # linkInstances = collector_maq.OfClass(DB.RevitLinkInstance)
# # linkDoc = [links.GetLinkDocument() for links in linkInstances]
# # collector_link = DB.FilteredElementCollector(linkDoc[0])

# # siteloc_elements_link = collector_link.OfClass(DB.ProjectLocation).ToElements()
# # projectloc_name_link = [proj.Name for proj in siteloc_elements_link]
# # for proj in siteloc_elements_link:
# #   if proj.Name != "Projet" and proj.Name != "Interne":
# #     siteloc_longitude_link = proj.SiteLocation.Longitude
# #     siteloc_latitude_link = proj.SiteLocation.Latitude
# #     siteloc_elevation_link = proj.SiteLocation.Elevation
# #     siteloc_placename_link = proj.SiteLocation.PlaceName


# # # COLLECT LEVELS MAQUETTE
# # level_category = db.Collector(of_category='Levels', is_not_type=True)
# # level_elements = level_category.get_elements()
# # level_name = [levels.LookupParameter("Nom").AsString() for levels in level_elements]
# # level_elevation = [levels.Elevation for levels in level_elements]
# # level_id = [levels.Id for levels in level_elements]

# # # COLLECT GRIDS MAQUETTE
# # grid_category = db.Collector(of_category='OST_Grids', is_not_type=True)
# # grid_elements = grid_category.get_elements()

# # # COLLECT LEVELS LINK
# # collector_maq = DB.FilteredElementCollector(revit.doc)
# # linkInstances = collector_maq.OfClass(DB.RevitLinkInstance)
# # linkDoc = [links.GetLinkDocument() for links in linkInstances]
# # collector_link = DB.FilteredElementCollector(linkDoc[0])

# # level_elements_link = collector_link.OfClass(DB.Level).ToElements()
# # level_name_link = [levels.LookupParameter("Nom").AsString() for levels in level_elements_link]
# # level_elevation_link = [levels.Elevation for levels in level_elements_link]

# # # COLLECT GRIDS LINK
# # collector_maq = DB.FilteredElementCollector(revit.doc)
# # linkInstances = collector_maq.OfClass(DB.RevitLinkInstance)
# # linkDoc = [links.GetLinkDocument() for links in linkInstances]   
# # collector_link = DB.FilteredElementCollector(linkDoc[0])

# # grid_elements_link = collector_link.OfClass(DB.Grid).ToElements()
# # grid_name_link = [grids.Name for grids in grid_elements_link]
# # grid_length_link = [grids.Curve.Length for grids in grid_elements_link]
# # grid_origin_link = [grids.Curve.Origin for grids in grid_elements_link]
# # grid_direction_link = [grids.Curve.Direction for grids in grid_elements_link]


# # # # CREATE LEVELS
# # # with db.Transaction('create levels'):
# # #   for k in range(len(level_elements_link)):
# # #     NewLevel = DB.Level.Create(document = revit.doc, elevation = 0)
# # #     NewLevel.Name = level_name_link[k]
# # #     NewLevel.Elevation = level_elevation_link[k]

# # # # DELETE LEVELS 
# # # with db.Transaction('delete levels'):
# # #   for levels in level_id:
# # #     DB.Document.Delete(revit.doc, levels)

# # # # CREATE GRIDS
# # # with db.Transaction('create grids'):
# # #   for k in range(len(grid_elements_link)):
# # #     start = db.XYZ(0,0,0)
# # #     end = db.XYZ(0,0,0)
# # #     BaseLine = db.Line.new([0,0],[1,1])
# # #     NewGrid = DB.Grid.Create(document = revit.doc, line = BaseLine)
# # #     NewGrid.Name = grid_name_link[k]
# # #     NewGrid.Curve.Origin = grid_origin_link[k]
# # #     NewGrid.Curve.Length = grid_length_link[k]
# # #     NewGrid.Curve.Direction = grid_direction_link[k]




# # # OUT

# # print siteloc_elements_link, siteloc_elevation_link, siteloc_latitude_link, siteloc_longitude_link, siteloc_placename_link


#   