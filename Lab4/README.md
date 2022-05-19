# Lab 4
### Asa Hayes

This lab is an introduction to actually using Python to script actions within ArcGIS Pro. While the actions are fairly simple at first glance, starting the process of automating them allows for complex actions to be done much more accurately and efficiently.

Basic premise is to find all buildings within 150m of any of the parking garages on campus

The main tasks of this lab are to: 
> 1. Read in garage location X/Y coords from the provided .csv
> 2. Create a geodatabase and add in the input layers
> 3. Buffer the garage points
> 4. Intersect the buildings layer with the buffered garage points
> 5. Output the resulting table to a .csv
