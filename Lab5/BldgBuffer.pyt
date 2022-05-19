# -*- coding: utf-8 -*-

import arcpy
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [BldgBuffer]


class BldgBuffer(object):
    #desc Tool for show in ArcGIS
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Building Buffer"
        self.description = "Uses a buffer to find buildings within a user-defined range of a chosen building on campus"
        self.canRunInBackground = False
        self.Catergory = "Building Tools"

    #require the 2 inputs as done in Pt. 1
    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Building Number",
            name="buildingNumber",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param1 = arcpy.Parameter(
            displayName="Buffer radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1]
        return params

    #unused, does not rely on extensions
    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    #unused, user inputs are basic and need no processing before execution in this case
    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    #unused, errors already defined in main code
    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    #script is verbatim from Pt. 1, only changed to fit parameters
    def execute(self, parameters, messages):
        #create set work directory and create a shortcut to provided gdb
        workDir = r"C:\Users\A\Desktop\GEOG-392\GEOG-392\Lab5"
        arcpy.env.workspace = workDir
        campusLoc = workDir + "/Campus.gdb"

        #Prompt user for a building number on campus, and a distance in meters to buffer around it
        bldgNumIn = parameters[0].valueAsText
        bufSzIn = int(parameters[1].value)

        # Check if building with input number exists on campus
        structures = campusLoc + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause = "Bldg = '%s'"  % bldgNumIn)
        shouldProceed = False

        #check for building in Structures, cursor iterates until bldg is found or end
        #break statement added to reduce runtime, otherwise iterates thru entire table everytime
        for row in cursor:
            if row.getValue("Bldg") == bldgNumIn:
                shouldProceed = True
                break

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

        return
