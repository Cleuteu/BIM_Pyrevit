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


doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
options = __revit__.Application.Create.NewGeometryOptions()
SEBoptions = SpatialElementBoundaryOptions()


door_collector = FilteredElementCollector(doc)\
		  .OfCategory(BuiltInCategory.OST_Doors)\
		  .WhereElementIsNotElementType()\
		  .ToElements()

t = Transaction(doc, 'Fill door Ids')
t.Start()

for door in door_collector:
	
	print(door.Id.IntegerValue)
	door.LookupParameter('ID Revit').Set(door.Id.IntegerValue)
	
t.Commit()