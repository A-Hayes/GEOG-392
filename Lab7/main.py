# Asa Hayes
# GEOG-392
# Lab 7

import arcpy

# Create composite from Landsat bands
# Note: change directories to data location, images too large to be kept in project folder
# Band order is B, G, R, NIR
dataPath = r"C:\Users\A\Desktop\Lab7_data"
b1 = arcpy.sa.Raster(dataPath + r"\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF") 
b2 = arcpy.sa.Raster(dataPath + r"\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF") 
b3 = arcpy.sa.Raster(dataPath + r"\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF") 
b4 = arcpy.sa.Raster(dataPath + r"\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF") 
compBands = arcpy.CompositeBands_management([b1, b2, b3, b4], dataPath + "\BandComposite.tif")

# Draw Hillshade
pathDEM = r"C:\Users\A\Desktop\Lab7_data\n30_w097_1arc_v3.tif"
# azimuth = 315, altitude = 45, z-factor = 1
# [:-4] removes last 4 chars (ie the ".tif") from pathDEM so that hillshade name can be appended
arcpy.ddd.HillShade(pathDEM, pathDEM[:-4] + "_hillshade.tif", 315, 45, "NO_SHADOWS", 1)

# Draw Slope iamge
output_measure = "DEGREE" # z-factor still 1
arcpy.ddd.Slope(pathDEM, pathDEM[:-4] + "_slopes.tif", output_measure, 1)