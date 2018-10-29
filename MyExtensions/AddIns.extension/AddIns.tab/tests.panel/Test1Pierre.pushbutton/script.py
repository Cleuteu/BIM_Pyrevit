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

class FailureHandler(IFailuresPreprocessor):
  def __init__(self):
    self.ErrorMessage = ""
    self.ErrorSeverity = ""
  def PreprocessFailures(self, failuresAccessor):
  	# failuresAccessor.DeleteAllWarning()
  	# return FailureProcessingResult.Continue
  	failures = failuresAccessor.GetFailureMessages()
  	rslt = ""
  	for f in failures:
  		fseverity = failuresAccessor.GetSeverity()
  		if fseverity == FailureSeverity.Warning:
  			failuresAccessor.DeleteWarning(f)
  		elif fseverity == FailureSeverity.Error:
  			rslt = "Error"
  			failuresAccessor.ResolveFailure(f)
  	if rslt == "Error":
  		return FailureProcessingResult.ProceedWithCommit
  		# return FailureProcessingResult.ProceedWithRollBack
  	else:
  		return FailureProcessingResult.Continue

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

def Ungroup(group):
	group.UngroupMembers()
	
def Regroup(groupname,groupmember):
	newgroup = doc.Create.NewGroup(groupmember)
	newgroup.GroupType.Name = str(groupname)
	
# group = get_selected_elements(doc)[0]

# print(group.Id)
# print(group.GetType())
# print(group.GroupId)

# groupname = group.Name
# groupmember = group.GetMemberIds()

# IdsInLine = ""
# for i in groupmember:
# 	IdsInLine = IdsInLine + str(i.IntegerValue) + ", "

# IdsInLine = IdsInLine[:len(IdsInLine)-3]

# print(IdsInLine)

# status = ""
# t1 = Transaction(doc, 'Ungroup group')
# t1.Start()
# Ungroup(group)
# print("Group ungrouped")
# t1.Commit()
# try:
# 	t2 = Transaction(doc, 'Regroup group')
# 	t2.Start()

# 	failureHandlingOptions = t2.GetFailureHandlingOptions()
# 	failureHandler = FailureHandler()
# 	failureHandlingOptions.SetFailuresPreprocessor(failureHandler)
# 	failureHandlingOptions.SetClearAfterRollback(True)
# 	t2.SetFailureHandlingOptions(failureHandlingOptions)

# 	Regroup(groupname,groupmember)
# 	print("Group regrouped")
# 	status = "Yeah!"
# 	t2.Commit()

# except:
# 	t2.RollBack()
# 	print("Regrouping fail")
# 	status = "Fuck!"

# print(status + "\n")
# print(t2.GetStatus())





# tg = TransactionGroup(doc, 'Ungroup/regroup all groups')
# tg.Start()

for group in group_collector:
	print(group.Id)
	print(group.GroupId)

	groupname = group.Name
	print("Group name : " + groupname)
	groupmember = group.GetMemberIds()

	t1 = Transaction(doc, 'Ungroup group')
	t1.Start()
	Ungroup(group)
	print("Group ungrouped")
	t1.Commit()
	try:
		t2 = Transaction(doc, 'Regroup group')
		t2.Start()

		failureHandlingOptions = t2.GetFailureHandlingOptions()
		failureHandler = FailureHandler()
		failureHandlingOptions.SetFailuresPreprocessor(failureHandler)
		failureHandlingOptions.SetClearAfterRollback(True)
		t2.SetFailureHandlingOptions(failureHandlingOptions)

		Regroup(groupname,groupmember)
		print("Group regrouped")
		t2.Commit()

	except:
		t2.RollBack()
		print("Regrouping fail")
		IdsInLine = ""
		for i in groupmember:
			IdsInLine = IdsInLine + str(i.IntegerValue) + ", "

		IdsInLine = IdsInLine[:len(IdsInLine)-3]

		print("Grouped element ids was : " + IdsInLine)

print("Done")

# tg.Assimilate()