# Asa Hayes
# GEOG-392

# Lab 6: Color Map, Toolboxes, Progressors

import os
import arcpy

# set directory for project
# use of input() is implied, mainly shown in the toolbox form, see further mentions below
projIn = r"C:\Users\A\Documents\ArcGIS\Projects\GEOG-392_Lab6"
project = arcpy.mp.ArcGISProject(projIn + r"\\GEOG-392_Lab6.aprx")

#note: for inputs handled by terminal, here's an example of taking in the name of the layer to be re-symbolized
#input() statements left out to streamline demo script, but are applied to toolbox
#lyrName = input("Please enter name of layer to re-symbolize")


# Select primary map in proj, iterate thru applied layers
campus = project.listMaps('Map')[0]

for layer in campus.listLayers():
    if layer.isFeatureLayer:
        symbology = layer.symbology
        if hasattr(symbology, 'renderer'):
            if layer.name == "GarageParking":
                print("GarageParking Found")
                # Update the copy's renderer to be 'GraduatedColorsRenderer'
                symbology.updateRenderer('GraduatedColorsRenderer')
                print(symbology.renderer)
                # Tell arcpy which field we want to base our choropleth off of
                #THIS FIELD UP TO INPUT
                symbology.renderer.classificationField = "Shape_Area"
                # Set how many classes we'll have
                #THIS FIELD UP TO INPUT
                symbology.renderer.breakCount = 5
                # Set the color ramp
                #would set color ramp as a possible input, but deemed beyond scope to try and index all options in tool
                symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
                layer.symbology = symbology # Very important step
            else:
                print("NOT GarageParking")

project.saveACopy(projIn + r"\\GEOG-392_Lab6_color.aprx")




