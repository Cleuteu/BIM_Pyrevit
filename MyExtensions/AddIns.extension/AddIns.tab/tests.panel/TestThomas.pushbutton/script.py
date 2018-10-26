# IMPORT 
import clr
import System
import math
import Autodesk
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from pyrevit import DB, UI 
from System.Collections.Generic import List
from pyrevit import forms
from rpw.ui.forms import TextInput
from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox, Separator, Button)

# VARIABLES UTILES
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
options = __revit__.Application.Create.NewGeometryOptions()
SEBoptions = SpatialElementBoundaryOptions()
roomcalculator = SpatialElementGeometryCalculator(doc)

collector = Autodesk.Revit.DB.FilteredElementCollector(doc)


# TEST RECUPERATION NIVEAUX
# collector = FilteredElementCollector(doc)
# levelElements = collector.OfClass(Level).ToElements()

# levelElevation = []
# for lev in levelElements:
#   levelElevation.append(lev.ProjectElevation)
# levelName = []
# for lev in levelElements:
#   levelName.append(lev.LookupParameter("Nom").AsString())



# collector = Autodesk.Revit.DB.FilteredElementCollector(doc)
# linkInstances = collector.OfClass(Autodesk.Revit.DB.RevitLinkInstance)
# linkDoc = []
# for links in linkInstances:
#   linkDoc.append(links.GetLinkDocument())
    
# collector = FilteredElementCollector(linkDoc[0])
# levelElementsLink = collector.OfClass(Level).ToElements()

# levelElevationLink = []
# for lev in levelElementsLink:
#   levelElevationLink.append(lev.ProjectElevation)
# levelNameLink = []
# for lev in levelElementsLink:
#   levelNameLink.append(lev.LookupParameter("Nom").AsString())

# print(levelNameLink)


def take_links(doc=doc):
  linkInstances = collector.OfClass(Autodesk.Revit.DB.RevitLinkInstance)
  print linkInstances
  linkDoc = []
  for links in linkInstances:
    linkDoc.append(links.GetLinkDocument())
  return linkDoc

def collector_link(doc=doc):
  return FilteredElementCollector(linkDoc[0])

def take_levels_link(doc=linkDoc):
  levelElementsLink = collector.OfClass(Level).ToElements()
  levelElevationLink = []
  for lev in levelElementsLink:
    levelElevationLink.append(lev.ProjectElevation)
  levelNameLink = []
  for lev in levelElementsLink:
    levelNameLink.append(lev.LookupParameter("Nom").AsString())
  