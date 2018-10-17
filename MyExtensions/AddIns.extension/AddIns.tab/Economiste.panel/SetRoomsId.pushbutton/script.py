"""Remplit les IDs des pieces"""

__title__ = 'Set room\n IDs'

__doc__ = 'Ce programme remplit les IDs des pieces'

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

room_collector = FilteredElementCollector(doc)\
		  .OfCategory(BuiltInCategory.OST_Rooms)\
		  .WhereElementIsNotElementType()\
		  .ToElements()

t = Transaction(doc, 'Fill room Ids')
t.Start()
#test
for room in room_collector:

	print(room.Id.IntegerValue)
	room.LookupParameter('SP_ID_REVIT').Set(room.Id.IntegerValue)

t.Commit()
