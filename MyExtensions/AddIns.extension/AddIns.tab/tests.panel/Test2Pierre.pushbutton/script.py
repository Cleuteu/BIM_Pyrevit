
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
roomcalculator = SpatialElementGeometryCalculator(doc)

# def get_selected_elements(doc):
#     try:
#         # Revit 2016
#         return [doc.GetElement(id)
#                 for id in __revit__.ActiveUIDocument.Selection.GetElementIds()]
#     except:
#         # old method
#         return list(__revit__.ActiveUIDocument.Selection.Elements)
	
# el = get_selected_elements(doc)[0]
# print(el.Id)
# print(el.GroupId)

# t = Transaction(doc, 'Set Param')
# t.Start()

# el.LookupParameter('ECO_lot').Set("God no")

# t.Commit()



cat_list = [BuiltInCategory.OST_PipeCurves, BuiltInCategory.OST_DuctCurves,\
			BuiltInCategory.OST_CableTray]

cat = BuiltInCategory.OST_CableTray 

element_collector = FilteredElementCollector(doc)\
	.OfCategory(cat)\
	.WhereElementIsNotElementType()\
	.ToElements()

icollection = List[ElementId]()

param = "Niveau de r"+"\xe9"+"f"+"\xe9"+"rence"

for element in element_collector:
	# print(element.LookupParameter(param).AsValueString()+" !")
	if element.LookupParameter(param).AsValueString() == "RDC-OLD":
		icollection.Add(element.Id)
	
uidoc.Selection.SetElementIds(icollection)

