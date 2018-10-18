"""Remplit les IDs des portes"""

__title__ = 'Set door\n IDs'

__doc__ = 'Ce programme remplit les IDs des portes'

import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from System.Collections.Generic import List
from rpw.ui.forms import TextInput
from pyrevit import forms


doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
options = __revit__.Application.Create.NewGeometryOptions()
SEBoptions = SpatialElementBoundaryOptions()

from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox,
		                  Separator, Button)
components = [Label('Pick a category:'),
              ComboBox('combobox1', {'Doors': 0, 'Rooms': 1}),
              Label('Enter the name of ID parameter:'),
              TextBox('textbox1', Text="ID Revit"),
              Separator(),
              Button('Select')]
form = FlexForm('Title', components)
form.show()
# User selects `Opt 1`, types 'Wood' in TextBox, and select Checkbox
print form.values

parameterName = form.values['combobox1']
category = form.values['combobox1']

if category == 0:
	collector = FilteredElementCollector(doc)\
		 		.OfCategory(BuiltInCategory.OST_Doors)\
		  		.WhereElementIsNotElementType()\
		  		.ToElements()
	print 'ici'
else:
	collector = FilteredElementCollector(doc)\
		 		.OfCategory(BuiltInCategory.OST_Rooms)\
		  		.WhereElementIsNotElementType()\
		  		.ToElements()
	print 'la!'

t = Transaction(doc, 'Fill Ids')
t.Start()

for i in collector:
	
	print(i.Id.IntegerValue)
	i.LookupParameter('ID Revit').Set(i.Id.IntegerValue)
	
t.Commit()