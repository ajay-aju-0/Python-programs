# printout all colors from color list 1 not contained in color list 2

color_list_1=["rose","black","green","yellow","silver","orange"]
color_list_2=["blue","white","silver","gold","grey","pink"]
print([i for i in color_list_1 if i not in color_list_2])