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

td_button = TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.Cancel | TaskDialogCommonButtons.No

res = TaskDialog.Show("Importation from Excel","Le fichier Excel est-il ouvert sur le bon onglet? Les ids des elements doivent etre en colonne 1 et les noms de parametres partages en ligne 1",td_button)

if res == TaskDialogResult.Yes:
               
               # Ungroup function 
               def Ungroup(group):
                              group.UngroupMembers()
                              
               # Regroup function 
               def Regroup(groupname,groupmember):
                              newgroup = doc.Create.NewGroup(groupmember)
                              newgroup.GroupType.Name = str(groupname)
               
               def convertStr(s):
                   """Convert string to either int or float."""
                   try:
                       ret = int(s)
                   except ValueError:
                       ret = 0
                   return ret
                              
               #Open a form and choose the worksheet number
               ops = ['1', '2', '3', '4','5']
               worksheet = forms.CommandSwitchWindow.show(ops, message='Select the number of the worksheet in Excel')
               worksheet = convertStr(worksheet)

               t = Transaction(doc, 'Read Excel spreadsheet.') 
               t.Start()
               
               #Accessing the Excel applications.
               xlApp = System.Runtime.InteropServices.Marshal.GetActiveObject('Excel.Application')
               
               #Worksheet, Row, and Column parameters
               # worksheet = 2
               rowStart = 1
               rowEnd = 900
               column_id = 1
               colStart = 2
               colEnd = 3
               
               #Using a loop to read a range of values and print them to the console.
               array = []
               param_names_excel = []
               data = {}
               for r in range(rowStart, rowEnd):
                              data_id = xlApp.Worksheets(worksheet).Cells(r, column_id).Text
                              data_id_int = convertStr(data_id)
                              if data_id_int != 0:
                                            data = {'id': data_id_int}
                                            for c in range(colStart, colEnd):
                                                           data_param_value = xlApp.Worksheets(worksheet).Cells(r, c).Text
                                                           data_param_name = xlApp.Worksheets(worksheet).Cells(1, c).Text
                                                           if data_param_name != '':
                                                                          param_names_excel.append(data_param_name)
                                                                          if data_param_value != '':
                                                                                         data[data_param_name] = data_param_value
                                            array.append(data)
               
                              
               t.Commit()
               
               #Recuperation des portes
               doors = FilteredElementCollector(doc)\
                                              .OfCategory(BuiltInCategory.OST_Doors)\
                                              .WhereElementIsNotElementType()\
                                              .ToElements()
               
               #Get parameters in the model
               params_door_set = doors[0].Parameters
               params_door_name = []
               for param_door in params_door_set:
                              params_door_name.append(param_door.Definition.Name)
                              
               unfounddoors = []
               
               t = Transaction(doc, 'Feed doors')
               t.Start()

               for hash in array:
                              idInt = int(hash['id'])
                              try :
                                            door_id = ElementId(idInt)
                                            door = doc.GetElement(door_id)
                                            groupId = door.GroupId
                                            if str(groupId) != "-1":
                                                           group = doc.GetElement(groupId)
                                                           groupname = group.Name
                                                           groupmember = group.GetMemberIds()
                                                           Ungroup(group)
                                                           
                                            for param in param_names_excel:
                                                           if (param in params_door_name) and (param in hash):
                                                                          door.LookupParameter(param).Set(hash[param])
                                                                          
                                            if str(groupId) != "-1":
                                                           Regroup(groupname,groupmember)
                                                           # if "(membre exclu)" in group.GroupType.Name:
                                                                          # group.GroupType.Name = groupname
                                            print("Door " + str(idInt) + " : OK")

                              except:
                                            print(str(idInt) + " not in REVIT doc")
                                            unfounddoors.append(idInt)
                                            
               print("Job done!")
               
               t.Commit()

               if len(unfounddoors) != 0:
                              print(str(len(unfounddoors)) + " doors not found : ")
                              print(unfounddoors)

else:
               "A plus tard!"
