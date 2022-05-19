# Asa Hayes
# GEOG-392

# Lab 5: Creating Tools in ArcGIS

import os
import arcpy

#create set work directory and create a shortcut to provided gdb
workDir = r"C:\Users\A\Desktop\GEOG-392\GEOG-392\Lab5"
arcpy.env.workspace = workDir
campusLoc = workDir + "/Campus.gdb"

#Prompt user for a building number on campus, and a distance in meters to buffer around it
bldgNumIn = input("Please enter a building number: ")
bufSzIn = int(input("Please enter a buffer size (meters): "))

# Check if building with input number exists on campus
structures = campusLoc + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause = "Bldg = '%s'"  % bldgNumIn)
shouldProceed = False

#check for building in Structures, cursor iterates
for row in cursor:
    if row.getValue("Bldg") == bldgNumIn:
        shouldProceed = True

#if doesn't exist, leave with an error, code continues in main block if does exist
if shouldProceed:
    # Generate the name for our output buffer layer & get reference to building
    bldgBuf = "/building_%s_buffed_%s" % (bldgNumIn, bufSzIn)
    bldgFeat = arcpy.Select_analysis(structures, campusLoc + "/building_%s" % (bldgNumIn), "Bldg = '%s'"  % bldgNumIn)

    # Buffer the selected building, clip the structures to our buffered feature, cleanup
    arcpy.Buffer_analysis(bldgFeat, campusLoc + bldgBuf, bufSzIn)
    arcpy.Clip_analysis(structures, campusLoc + bldgBuf, campusLoc + "/clip_%s" % (bldgNumIn))
    arcpy.Delete_management(campusLoc + "/building_%s" % (bldgNumIn))
else:
    arcpy.AddError("No building with input number found")


