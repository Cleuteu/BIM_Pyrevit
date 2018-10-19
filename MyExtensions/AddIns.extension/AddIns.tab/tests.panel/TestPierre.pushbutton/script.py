
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

type_list = []
for i in groupmember:
	subel = doc.GetElement(i)
	subeltype = subel.GetType()
	if str(subeltype.ToString()) not in type_list:
			type_list.append(str(subeltype.ToString()))

# t = Transaction(doc, 'Ungroup/Regroup group')
# t.Start()

# status = ""
# try:
# 	Ungroup(group)
# 	status = "Group ungrouped"
# except:
# 	status = "Ungrouping fail"

# if status == "Group ungrouped":
# 	try:
# 		Regroup(groupname,groupmember)
# 		status = status + " and regrouped without failiure"
# 	except:
# 		status = status + " but regrouping failed"
		
# print(status + "\n")

# t.Commit()

t = Transaction(doc, 'Ungroup/Regroup group')
t.Start()

status = ""
try:
	Ungroup(group)
	Regroup(groupname,groupmember)
	status = "Yeah!"
except:
	status = "Fuck!"
		
print(status + "\n")

t.Commit()

for j in type_list:
		print(j)