
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

# Collect all groups in active view, Alex please erase second attribute if you want to filter in the whole doc 
group_collector = FilteredElementCollector(doc,doc.ActiveView.Id)\
	  .OfClass(Group)

def get_selected_elements(doc):
    try:
        # Revit 2016
        return [doc.GetElement(id)
                for id in __revit__.ActiveUIDocument.Selection.GetElementIds()]
    except:
        # old method
        return list(__revit__.ActiveUIDocument.Selection.Elements)

# Ungroup function 
def Ungroup(group):
	group.UngroupMembers()
	
# Regroup function 
def Regroup(groupname,groupmember):
	newgroup = doc.Create.NewGroup(groupmember)
	newgroup.GroupType.Name = str(groupname)
	
group = get_selected_elements(doc)[0]
print(group.Id)
print(group.GetType())
print(group.GroupId)

groupname = group.Name
groupmember = group.GetMemberIds()

for i in groupmember:
	subel = doc.GetElement(i)
	print(subel.GetType())
	print(subel.GroupId)