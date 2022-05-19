# Asa Hayes
# GEOG-392

# Lab 4: Starting with ArcGIS/Python Scripting

import os
import arcpy

#create set work directory and create a shortcut to provided gdb
workDir = r"C:\Users\A\Desktop\GEOG-392\GEOG-392\Lab4"
arcpy.env.workspace = workDir
campusLoc = workDir + "/Campus.gdb"

#note: many operations in filewill fail if existing copies of any 
#      objects are detected. Runs properly on the first run,
#      throws "already exists" errors after if not deleted

#create gdb and shortcut to it
arcpy.CreateFileGDB_management(workDir, "Lab4.gdb")
labLoc = workDir + "/Lab4.gdb"

#input csv to create point layer
sheetIn = arcpy.MakeXYEventLayer_management("garages.csv", "X", "Y", "garagePoints")

#create other shortcuts
garage = labLoc + "/garagePoints"
buildings = labLoc + "/Structures"
garageBuffered = labLoc + "/GaragePoints_buffered"

#move garage points and building layers into created gdb
arcpy.FeatureClassToGeodatabase_conversion(sheetIn, labLoc)
arcpy.Copy_management(campusLoc + "\Structures", buildings)

#reproject garage points to buiding geo-coord system
#note: reprojected points saved as different layer, Project_management()
#      does not allow for same input/output source layer.
gcSys = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage, garage + "_projected", gcSys)

#create buffer around garages, intersect with buildings
bufferPts = arcpy.Buffer_analysis(garage  + "_projected", garageBuffered, 150)
arcpy.Intersect_analysis([buildings, bufferPts], labLoc + "/bufferIntersect", 'ALL')

#export buildings within 150m of garages to csv
arcpy.TableToTable_conversion(labLoc + "/bufferIntersect", workDir, "intersect_output.csv")
