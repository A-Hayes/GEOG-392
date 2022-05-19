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
        self.tools = [ConvertToColorMap]


class ConvertToColorMap(object):
    #desc Tool for show in ArcGIS
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Convert to Color Map"
        self.description = "Converts symbology of input layer to a graduated color scale based on supplied field"
        self.canRunInBackground = False
        self.Catergory = "Symbology"

    #configure/require the inputs 
    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Target Project (.aprx)",
            name="projectIn",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        param0.filter.list = ['aprx']

        param1 = arcpy.Parameter(
            displayName="Target Layer Name",
            name="layerIn",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        param2 = arcpy.Parameter(
            displayName="Target Attribute for Color Scaling (default is Shape_Area)",
            name="attrIn",
            datatype="GPString",
            parameterType="Optional",
            direction="Input"
        )

        param3 = arcpy.Parameter(
            displayName="Number of Breaks on Scale",
            name="numBreaks",
            datatype="GPLong",
            parameterType="Optional",
            direction="Input"
        )

        param4 = arcpy.Parameter(
            displayName="Output File",
            name="projectOut",
            datatype="DEFile",
            parameterType="Required",
            direction="Output"
        )
        params = [param0, param1, param2, param3, param4]
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
        #set input project file as curretn working project
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)

        campus = project.listMaps('Map')[0]

        for layer in campus.listLayers():
            if layer.isFeatureLayer:
                symbology = layer.symbology
                if hasattr(symbology, 'renderer'):
                    if layer.name == parameters[1]:
                        # Update the copy's renderer to be 'GraduatedColorsRenderer'
                        symbology.updateRenderer('GraduatedColorsRenderer')
                        # Tell arcpy which field we want to base our choropleth off of, shape_area by defualt
                        if (parameters[2] != "Shape_Area") & (parameters[2] != "") :
                            symbology.renderer.classificationField = parameters[2]
                        else:
                            symbology.renderer.classificationField = "Shape_Area"
                        # Set how many classes we'll have
                        #THIS FIELD UP TO INPUT
                        if (parameters[3] != 5) & (parameters[3] != None) :
                            symbology.renderer.breakCount = parameters[3]
                        else:
                            symbology.renderer.breakCount = 5
                        # Set the color ramp
                        #would set color ramp as a possible input, but deemed beyond scope to try and index all options in tool
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
                        layer.symbology = symbology # Very important step
                    else:
                        print("NOT GarageParking")

        project.saveACopy(parameters[4])

        return
