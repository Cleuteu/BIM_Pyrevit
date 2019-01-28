
"""Import a list of points in order to edit the shape of a slab"""

__title__ = 'Hauteur sous poutres'

__doc__ = 'Calcul et application d\'un filtre de hauteur sous poutres pour une maquette geometre d\'un batiment cure'

# -*- coding: utf-8 -*-
e_a = str("\xe9")
a_a = str("\xe0")

import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import * 
from pyrevit import forms
from rpw.ui.forms import (select_file, Alert, TextInput, FlexForm, Label, ComboBox, TextBox, TextBox, Separator, Button, CommandLink, TaskDialog)

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

options = __revit__.Application.Create.NewGeometryOptions()

beam_collector = FilteredElementCollector(doc,doc.ActiveView.Id)\
                .OfCategory(BuiltInCategory.OST_StructuralFraming)\
                .WhereElementIsNotElementType()\
                .ToElements()

level_collector = FilteredElementCollector(doc)\
            .OfCategory(BuiltInCategory.OST_Levels)\
            .WhereElementIsNotElementType()\
            .ToElements()
            
levels = {}
for level in level_collector:
  levels[level.Name] = level


components = [Label('Select the floor\'s level :'),
          ComboBox('floor_level', levels),
          Label('Enter the height required under the beams:'),
          TextBox('height_required', Text="2.80"),
          Separator(),
          Button('OK')]
form = FlexForm('Title', components)
form.show()

floor_level = round(form.values["floor_level"].Elevation/3.2808399,3)
height_required = float(form.values["height_required"])
# Alert('Pick a slab please (clicking on it)', title = "Select a slab", exit = False)
# # Pick an element
# sel = uidoc.Selection
# obType = Selection.ObjectType.Element
# ref = sel.PickObject(obType, "Select floor.")
# floor = doc.GetElement(ref.ElementId)

t = Transaction(doc, 'Tag beam')
t.Start()

for beam in beam_collector:
  z_max = (beam.get_Geometry(options).GetBoundingBox().Max.Z + beam.LookupParameter("Valeur de d"+e_a+"calage"+" Z").AsDouble())/3.2808399
  z_min = ((beam.get_Geometry(options).GetBoundingBox().Min).Z/3.2808399)
  heightBeam = round(z_max - z_min, 2)
  delta = z_min - floor_level - height_required
  try:	
  	beam.LookupParameter("HSP").Set(z_min - floor_level)
  except:
  	print("Not succeed for " + beam.Id)
    # beam.LookupParameter("HSP").Set(height_required + 0.01)



t.Commit()

