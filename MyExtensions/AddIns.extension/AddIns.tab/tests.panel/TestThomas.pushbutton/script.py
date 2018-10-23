import clr
import System
import math
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from System.Collections.Generic import List
from pyrevit import forms
from rpw.ui.forms import TextInput
from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox, Separator, Button)


doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
options = __revit__.Application.Create.NewGeometryOptions()
SEBoptions = SpatialElementBoundaryOptions()
roomcalculator = SpatialElementGeometryCalculator(doc)

forms.select_views(title='Select Views', button_name='Select', width=1000, multiple=True, filterfunc=None, doc=None)


# collector = FilteredElementCollector(doc)
# siteElement = collector.OfClass(SiteLocation).ToElements()
# siteElemMaq = UnwrapElement(siteElement)
# latitude = []
# longitude = []
# placeNameTest = []
# placeName = []
# indice2 = 0
# for i in range(len(siteElemMaq)):
#   placeNameTest.append(siteElemMaq[i].PlaceName)
#   if placeNameTest[i]:
#     indice2 = i
# for i in range(len(siteElemMaq)):
#   if i == indice2:
#     latitude.append(siteElemMaq[i].Latitude)
#     longitude.append(siteElemMaq[i].Longitude)
#     placeName.append(siteElemMaq[i].PlaceName)
  
# #SITE LOCATION LINK /////////////////////////////////////////////////////////////
# collector = Autodesk.Revit.DB.FilteredElementCollector(doc)
# linkInstances = collector.OfClass(Autodesk.Revit.DB.RevitLinkInstance)
# linkDoc = []
# for i in linkInstances:
#   linkDoc.append(i.GetLinkDocument())
    
# collector = FilteredElementCollector(linkDoc[0])
# siteElementLink = collector.OfClass(SiteLocation).ToElements()
# siteElemLink = UnwrapElement(siteElementLink)
# latLink = []
# longLink = []
# placeNameTestLink = []
# placeNameLink = []
  
# for i in range(len(siteElemLink)):
#   placeNameTestLink.append(siteElemLink[i].PlaceName)
#   if placeNameTestLink[i]:
#     indice2 = i
# for i in range(len(siteElemLink)):
#   if i == indice2:
#     latLink.append(siteElemLink[i].Latitude)
#     longLink.append(siteElemLink[i].Longitude)
#     placeNameLink.append(siteElemLink[i].PlaceName)

# #OPERATIONS SUR LINK ET MAQUETTE SITE LOCATION /////////////////////////////////////////////////////
# pourcentSiteLocation = 0
# textSiteLocation = ""
# if abs(latitude[0] - latLink[0]) < 0.001:
#   pourcentSiteLocation = pourcentSiteLocation + 0.33333333333333333
#   if abs(longitude[0] - longLink[0]) < 0.001:
#     pourcentSiteLocation = pourcentSiteLocation + 0.33333333333333333
#     if placeName in placeNameLink :
#       pourcentSiteLocation = pourcentSiteLocation + 0.33333333333333333
#       textSiteLocation = "Les coordonnées du site partagé sont les mêmes que le QNP"
#     else:
#       textSiteLocation = "Les coordonnées sont OK mais le nom de l'emplacement du site partagé est différent du QNP"
#   else: 
#     textSiteLocation = "Les coordonnées du site partagé ne sont pas les mêmes que le QNP"
# else :
#   textSiteLocation = "Les coordonnées du site partagé ne sont pas les mêmes que le QNP"


