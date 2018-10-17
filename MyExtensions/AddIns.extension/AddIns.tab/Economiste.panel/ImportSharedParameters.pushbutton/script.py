"""Importe les parametres partages"""

__title__ = 'Import Shared Parameters'

__doc__ = 'Ce programme importe les parametres partages dans un projet'


import clr
import System
import math
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from System.Collections.Generic import List
from pyrevit import forms

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
options = __revit__.Application.Create.NewGeometryOptions()
SEBoptions = SpatialElementBoundaryOptions()
roomcalculator = SpatialElementGeometryCalculator(doc)

app = doc.Application

#SharedParametersFile openning
spfile = app.OpenSharedParameterFile()

#Traduction of SharedParametersFile
spGroups = spfile.Groups
spGroupsDef = [g.Definitions for g in spGroups]
spParametersDef = [x for l in spGroupsDef for x in l]
#Names of groups
spGroupsName = [x.Name for x in spGroups]
#Names of SharedParameters
spParametersName = [x.Name for x in spParametersDef]

categoriesDef = [i for i in doc.Settings.Categories]
categoriesName = [i.Name for i in doc.Settings.Categories]

#Forms preparation
class CheckBoxOption:
    def __init__(self, name, default_state=False):
        self.name = name
        self.state = default_state

	# define the __nonzero__ method so you can use your objects in an 
	# if statement. e.g. if checkbox_option:
    def __nonzero__(self):
        return self.state

	# __bool__ is same as __nonzero__ but is for python 3 compatibility
    def __bool__(self):
        return self.state

def checkbox(itemsDef, itemsName):
	options = []
	for i in itemsName:
		options.append(CheckBoxOption(i))

	all_checkboxes = forms.SelectFromCheckBoxes.show(options)

	# now you can check the state of checkboxes in your program
	i = 0
	index = []
	for checkbox in all_checkboxes:
		if checkbox:
			index.append(i)
		i += 1

	itemsChoosed = []
	for i in index:
		itemsChoosed.append(itemsDef[i])
		#print itemsDef[i].Name
	return itemsChoosed

#Save the choices of the user
spParametersChoosed = checkbox(spParametersDef, spParametersName)
categoriesChoosed = checkbox(categoriesDef, categoriesName)

#creating category set
catset = app.Create.NewCategorySet()
[catset.Insert(j) for j in categoriesChoosed]

#Import in the field TEXT of the concerned elements
group = BuiltInParameterGroup.PG_TEXT

#Instances parameters
bind = app.Create.NewInstanceBinding(catset)

t = Transaction(doc, 'Fill door Ids')
t.Start()

bindmap = doc.ParameterBindings
for p in spParametersChoosed:
	try:
		bindmap.Insert(p, bind, group)
	except:
		continue
	
t.Commit()