
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

nstart = 0
type_list = []
for i in groupmember:
	nstart = nstart + 1
	subel = doc.GetElement(i)
	subeltype = subel.GetType()
	if str(subeltype.ToString()) not in type_list:
			type_list.append(str(subeltype.ToString()))

print(str(nstart) + " elements in group in the beginning")

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
host_list = []
try:
	# t = Transaction(doc, 'Ungroup/Regroup group')
	# t.Start()
	# Ungroup(group)
	nend = 0
	for k in groupmember:
		nend = nend + 1
		subel = doc.GetElement(k)
		print(subel.Id)
		# print(subel.GroupId)
		# print(subel.GetType())
		try:
			# Get the subel host id
			param = subel.get_Parameter(BuiltInParameter.HOST_ID_PARAM).AsValueString()
			print(subel.Id)
			print(param)
			if param != "-1":
				host_list.append(param)
			# param = subel.get_Parameter(BuiltInParameter.HOST_ID_PARAM).AsElementId()
			# if param.IntegerValue == -1:
			# 	print(subel.Id)

			# param = str(subel.LookupParameter("H"+u"\u00F4"+"te").AsString())
			# if "non associ" in param:
			# 	print(param)
			# 	print(subel.Id)
		except:
			"no"
	# Regroup(groupname,groupmember)
	print(str(nend) + " elements in group in the end")
	# Regroup(groupname,groupmember)
	status = "Yeah!"

except:
	status = "Fuck!"
	# continue
		
print(status + "\n")

print(host_list)

n = 0
for i in groupmember:
	if str(i.IntegerValue) in host_list:
		n = n + 1

print(str(n) + " host in group")

t.Commit()

# for j in type_list:
# 	print(j)

for i in dir(group):
		print(i)

x = group.IsExternalFileReference()
print(x)
print(dir(x))