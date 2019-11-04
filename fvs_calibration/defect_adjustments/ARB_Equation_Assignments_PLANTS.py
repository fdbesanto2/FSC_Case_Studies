
# coding: utf-8

# In[1]:

from ARB_Volume_Equations import *


# In[2]:

# Dictionary of ARB volume equations to be used for each species in Oregon, Washington, and California
# Uses USDA PLANTS Symbols as dictionary keys

VolumeEq_Dict_PLANTS = {
    '2TREE': {'common_name': 'Unknown tree', 'type': 'HW', 'WOR': Eq_26, 'WWA': Eq_26, 'EOR': Eq_26, 'EWA': Eq_26, 'CA': Eq_41},
    
    # Softwoods
    '2TN': {'common_name': 'Unknown conifer', 'type': 'SW', 'WOR': Eq_17, 'WWA': Eq_17, 'EOR': Eq_17, 'EWA': Eq_17, 'CA': Eq_17},
    'ABAM': {'common_name': 'Pacific silver fir', 'type': 'SW', 'WOR': Eq_11, 'WWA': Eq_11, 'EOR': Eq_10, 'EWA': Eq_10, 'CA': Eq_None},
    'ABBR': {'common_name': 'Bristlecone fir', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_18},
    'ABCO': {'common_name': 'White fir', 'type': 'SW', 'WOR': Eq_23, 'WWA': Eq_None, 'EOR': Eq_10, 'EWA': Eq_None, 'CA': Eq_23},
    'ABLO': {'common_name': 'Sierra white fir', 'type': 'SW', 'WOR': Eq_23, 'WWA': Eq_None, 'EOR': Eq_10, 'EWA': Eq_None, 'CA': Eq_23},
    'ABGR': {'common_name': 'Grand fir', 'type': 'SW', 'WOR': Eq_11, 'WWA': Eq_11, 'EOR': Eq_10, 'EWA': Eq_10, 'CA': Eq_23},
    'ABLA': {'common_name': 'Subalpine fir', 'type': 'SW', 'WOR': Eq_11, 'WWA': Eq_11, 'EOR': Eq_10, 'EWA': Eq_10, 'CA': Eq_18},
    'ABLAL': {'common_name': 'Subalpine fir', 'type': 'SW', 'WOR': Eq_11, 'WWA': Eq_11, 'EOR': Eq_10, 'EWA': Eq_10, 'CA': Eq_18},
    'ABMA': {'common_name': 'Red fir', 'type': 'SW', 'WOR': Eq_18, 'WWA': Eq_18, 'EOR': Eq_18, 'EWA': Eq_18, 'CA': Eq_18},
    'ABMAM': {'common_name': 'California red fir', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_18},
    'ABMAS': {'common_name': 'Shasta red fir', 'type': 'SW', 'WOR': Eq_18, 'WWA': Eq_18, 'EOR': Eq_18, 'EWA': Eq_18, 'CA': Eq_18},
    'ABPR': {'common_name': 'Noble fir', 'type': 'SW', 'WOR': Eq_11, 'WWA': Eq_11, 'EOR': Eq_10, 'EWA': Eq_10, 'CA': Eq_18},
    'CHLA': {'common_name': 'Port Orford cedar', 'type': 'SW', 'WOR': Eq_19, 'WWA': Eq_19, 'EOR': Eq_19, 'EWA': Eq_19, 'CA': Eq_8},
    'CANO9': {'common_name': 'Alaska cedar', 'type': 'SW', 'WOR': Eq_9, 'WWA': Eq_9, 'EOR': Eq_8, 'EWA': Eq_8, 'CA': Eq_8},
    'CHNO': {'common_name': 'Alaska cedar', 'type': 'SW', 'WOR': Eq_9, 'WWA': Eq_9, 'EOR': Eq_8, 'EWA': Eq_8, 'CA': Eq_8},
    'CUPRE': {'common_name': 'Cypress', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_19},
    'HEAR22': {'common_name': 'Arizona cypress', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_19},
    'HEMA21': {'common_name': 'McNabb cypress', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_19},
    'JUCA7': {'common_name': 'California juniper', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_21},
    'JUGR7': {'common_name': 'Western juniper', 'type': 'SW', 'WOR': Eq_21, 'WWA': Eq_21, 'EOR': Eq_21, 'EWA': Eq_21, 'CA': Eq_21},
    'JUOC': {'common_name': 'Western juniper', 'type': 'SW', 'WOR': Eq_21, 'WWA': Eq_21, 'EOR': Eq_21, 'EWA': Eq_21, 'CA': Eq_21},
    'JUOS': {'common_name': 'Utah juniper', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_21},
    'LALY': {'common_name': 'Subalpine larch', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_22, 'EOR': Eq_None, 'EWA': Eq_22, 'CA': Eq_None},
    'LAOC': {'common_name': 'Western larch', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_22, 'EOR': Eq_22, 'EWA': Eq_22, 'CA': Eq_None},
    'CALOC2': {'common_name': 'Incense cedar', 'type': 'SW', 'WOR': Eq_19, 'WWA': Eq_19, 'EOR': Eq_19, 'EWA': Eq_19, 'CA': Eq_19},
    'CADE27': {'common_name': 'Incense cedar', 'type': 'SW', 'WOR': Eq_19, 'WWA': Eq_19, 'EOR': Eq_19, 'EWA': Eq_19, 'CA': Eq_19},
    'PIBR': {'common_name': 'Brewer spruce', 'type': 'SW', 'WOR': Eq_13, 'WWA': Eq_None, 'EOR': Eq_13, 'EWA': Eq_None, 'CA': Eq_12},
    'PIEN': {'common_name': 'Engelmann spruce', 'type': 'SW', 'WOR': Eq_13, 'WWA': Eq_13, 'EOR': Eq_12, 'EWA': Eq_12, 'CA': Eq_12},
    'PIENE': {'common_name': 'Engelmann spruce', 'type': 'SW', 'WOR': Eq_13, 'WWA': Eq_13, 'EOR': Eq_12, 'EWA': Eq_12, 'CA': Eq_12},
    'PIENM2': {'common_name': 'Engelmann spruce', 'type': 'SW', 'WOR': Eq_13, 'WWA': Eq_13, 'EOR': Eq_12, 'EWA': Eq_12, 'CA': Eq_12},
    'PISI': {'common_name': 'Sitka spruce', 'type': 'SW', 'WOR': Eq_13, 'WWA': Eq_13, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_12},
    'PIAL': {'common_name': 'Whitebark pine', 'type': 'SW', 'WOR': Eq_15, 'WWA': Eq_15, 'EOR': Eq_15, 'EWA': Eq_15, 'CA': Eq_20},
    'PIAR': {'common_name': 'Bristlecone pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_16},
    'PIAT': {'common_name': 'Knobcone pine', 'type': 'SW', 'WOR': Eq_15, 'WWA': Eq_None, 'EOR': Eq_15, 'EWA': Eq_None, 'CA': Eq_16},
    'PIBA': {'common_name': 'Foxtail pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_16},
    'PIBAA': {'common_name': 'Foxtail pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_16},
    'PIBAB': {'common_name': 'Foxtail pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_16},
    'PICO': {'common_name': 'Lodgepole pine', 'type': 'SW', 'WOR': Eq_15, 'WWA': Eq_15, 'EOR': Eq_15, 'EWA': Eq_15, 'CA': Eq_16},
    'PICOL': {'common_name': 'Lodgepole pine', 'type': 'SW', 'WOR': Eq_15, 'WWA': Eq_15, 'EOR': Eq_15, 'EWA': Eq_15, 'CA': Eq_16},
    'PICOM': {'common_name': 'Sierra lodgepole pine', 'type': 'SW', 'WOR': Eq_15, 'WWA': Eq_15, 'EOR': Eq_15, 'EWA': Eq_15, 'CA': Eq_16},
    'PICO3': {'common_name': 'Coulter pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_5},
    'PIFL2': {'common_name': 'Limber pine', 'type': 'SW', 'WOR': Eq_15, 'WWA': Eq_None, 'EOR': Eq_15, 'EWA': Eq_None, 'CA': Eq_16},
    'PIJE': {'common_name': 'Jeffrey pine', 'type': 'SW', 'WOR': Eq_5, 'WWA': Eq_None, 'EOR': Eq_4, 'EWA': Eq_None, 'CA': Eq_5},
    'PILA': {'common_name': 'Sugar pine', 'type': 'SW', 'WOR': Eq_20, 'WWA': Eq_20, 'EOR': Eq_20, 'EWA': Eq_20, 'CA': Eq_20},
    'PIMO3': {'common_name': 'Western white pine', 'type': 'SW', 'WOR': Eq_15, 'WWA': Eq_15, 'EOR': Eq_15, 'EWA': Eq_15, 'CA': Eq_20},
    'PIMU': {'common_name': 'Bishop pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_16},
    # Ponderosa pine >=5" dbh
    'PIPO': {'common_name': 'Ponderosa pine', 'type': 'SW', 'WOR': Eq_5, 'WWA': Eq_4, 'EOR': Eq_4, 'EWA': Eq_4, 'CA': Eq_5},
    'PIPOB2': {'common_name': 'Ponderosa pine', 'type': 'SW', 'WOR': Eq_5, 'WWA': Eq_4, 'EOR': Eq_4, 'EWA': Eq_4, 'CA': Eq_5},
    'PIPOB3': {'common_name': 'Ponderosa pine', 'type': 'SW', 'WOR': Eq_5, 'WWA': Eq_4, 'EOR': Eq_4, 'EWA': Eq_4, 'CA': Eq_5},
    'PIPOP': {'common_name': 'Ponderosa pine', 'type': 'SW', 'WOR': Eq_5, 'WWA': Eq_4, 'EOR': Eq_4, 'EWA': Eq_4, 'CA': Eq_5},
    'PIPOS': {'common_name': 'Ponderosa pine', 'type': 'SW', 'WOR': Eq_5, 'WWA': Eq_4, 'EOR': Eq_4, 'EWA': Eq_4, 'CA': Eq_5},
#    # Ponderosa pine <5" dbh
#    'PIPO': {'common_name': 'Ponderosa pine', 'WOR': Eq_5, 'WWA': Eq_5, 'EOR': Eq_5, 'EWA': Eq_5, 'CA': Eq_5},
#    'PIPOB2': {'common_name': 'Ponderosa pine', 'WOR': Eq_5, 'WWA': Eq_5, 'EOR': Eq_5, 'EWA': Eq_5, 'CA': Eq_5},
#    'PIPOB3': {'common_name': 'Ponderosa pine', 'WOR': Eq_5, 'WWA': Eq_5, 'EOR': Eq_5, 'EWA': Eq_5, 'CA': Eq_5},
#    'PIPOP': {'common_name': 'Ponderosa pine', 'WOR': Eq_5, 'WWA': Eq_5, 'EOR': Eq_5, 'EWA': Eq_5, 'CA': Eq_5},
#    'PIPOS': {'common_name': 'Ponderosa pine', 'WOR': Eq_5, 'WWA': Eq_5, 'EOR': Eq_5, 'EWA': Eq_5, 'CA': Eq_5},
    'PIRA': {'common_name': 'Monterey pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_16}, 
    'PIRA2': {'common_name': 'Monterey pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_16}, 
    'PISA2': {'common_name': 'Gray pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_5}, 
    'PISY': {'common_name': 'Scots pine', 'type': 'SW', 'WOR': Eq_17, 'WWA': Eq_17, 'EOR': Eq_17, 'EWA': Eq_17, 'CA': Eq_17},
    'PIMO': {'common_name': 'Singleleaf pinyon', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_21},
    'PIPOW2': {'common_name': 'Washoe pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_5},
    'PIWA': {'common_name': 'Washoe pine', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_5},
    'PSMA': {'common_name': 'Bigcone Douglas-fir', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_3},
    'PSME': {'common_name': 'Douglas-fir', 'type': 'SW', 'WOR': Eq_1, 'WWA': Eq_1, 'EOR': Eq_2, 'EWA': Eq_2, 'CA': Eq_3},
    'SEQUO': {'common_name': 'Redwood', 'type': 'SW', 'WOR': Eq_24, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_24},
    'SESE3': {'common_name': 'Redwood', 'type': 'SW', 'WOR': Eq_24, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_24},
    'SEQUO2': {'common_name': 'Giant sequoia', 'type': 'SW', 'WOR': Eq_24, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_24},
    'SEGI2': {'common_name': 'Giant sequoia', 'type': 'SW', 'WOR': Eq_24, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_24},
    'TABR2': {'common_name': 'Pacific yew', 'type': 'SW', 'WOR': Eq_9, 'WWA': Eq_9, 'EOR': Eq_8, 'EWA': Eq_8, 'CA': Eq_8},
    'THPL': {'common_name': 'Western redcedar', 'type': 'SW', 'WOR': Eq_9, 'WWA': Eq_9, 'EOR': Eq_8, 'EWA': Eq_8, 'CA': Eq_8},
    'TOCA': {'common_name': 'California nutmeg', 'type': 'SW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_8},
    'TSHE': {'common_name': 'Western hemlock', 'type': 'SW', 'WOR': Eq_6, 'WWA': Eq_6, 'EOR': Eq_6, 'EWA': Eq_6, 'CA': Eq_6},
    'TSME': {'common_name': 'Mountain hemlock', 'type': 'SW', 'WOR': Eq_17, 'WWA': Eq_17, 'EOR': Eq_17, 'EWA': Eq_17, 'CA': Eq_17},
    
    # Hardwoods
    '2TB': {'common_name': 'Unknown hardwood', 'type': 'HW', 'WOR': Eq_26, 'WWA': Eq_26, 'EOR': Eq_26, 'EWA': Eq_26, 'CA': Eq_41},
    'ACMA3': {'common_name': 'Bigleaf maple', 'type': 'HW', 'WOR': Eq_37, 'WWA': Eq_26, 'EOR': Eq_37, 'EWA': Eq_26, 'CA': Eq_37},
    'ACNE2': {'common_name': 'Boxelder', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_38},
    'ACGL': {'common_name': 'Rocky Mountain maple', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'ACGR3': {'common_name': 'Bigtooth maple', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'ACGRG': {'common_name': 'Bigtooth maple', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'AECA': {'common_name': 'California buckeye', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_43},
    'AESCU': {'common_name': 'Buckeye', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_43},
    'AIAL': {'common_name': 'Tree of heaven', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_26},
    'ALRH2': {'common_name': 'White alder', 'type': 'HW', 'WOR': Eq_26, 'WWA': Eq_None, 'EOR': Eq_26, 'EWA': Eq_None, 'CA': Eq_26},
    'ALRU2': {'common_name': 'Red alder', 'type': 'HW', 'WOR': Eq_26, 'WWA': Eq_26, 'EOR': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'ARME': {'common_name': 'Pacific madrone', 'type': 'HW', 'WOR': Eq_40, 'EOR': Eq_26, 'WWA': Eq_40, 'EWA': Eq_26, 'CA': Eq_40},
    'BEOC2': {'common_name': 'Water birch', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_26},
    'BEPA': {'common_name': 'Paper birch', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'BEPAP': {'common_name': 'Paper birch', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'BEPAC': {'common_name': 'Western paper birch', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_26, 'EOR': Eq_None, 'EWA': Eq_26, 'CA': Eq_None},
    'CHCH7': {'common_name': 'Golden chinkapin', 'type': 'HW', 'WOR': Eq_32, 'EOR': Eq_26, 'WWA': Eq_None, 'EWA': Eq_26, 'CA': Eq_32},
    'CHCHC4': {'common_name': 'Golden chinkapin', 'type': 'HW', 'WOR': Eq_32, 'EOR': Eq_26, 'WWA': Eq_None, 'EWA': Eq_26, 'CA': Eq_32},
    'CHCHM': {'common_name': 'Golden chinkapin', 'type': 'HW', 'WOR': Eq_32, 'EOR': Eq_26, 'WWA': Eq_None, 'EWA': Eq_26, 'CA': Eq_32},
    'CELE3': {'common_name': 'Curl-leaf mountain mahogany', 'type': 'HW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_45, 'EWA': Eq_None, 'CA': Eq_45},
    'CELEI': {'common_name': 'Curl-leaf mountain mahogany', 'type': 'HW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_45, 'EWA': Eq_None, 'CA': Eq_45},
    'CELEL': {'common_name': 'Curl-leaf mountain mahogany', 'type': 'HW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_45, 'EWA': Eq_None, 'CA': Eq_45},
    'CONU4': {'common_name': 'Pacific dogwood', 'type': 'HW', 'WOR': Eq_None, 'EOR': Eq_26, 'WWA': Eq_None, 'EWA': Eq_26, 'CA': Eq_26},
    'CRATA': {'common_name': 'Hawthorn', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'EUCAL': {'common_name': 'Eucalyptus', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_31},
    'FRLA': {'common_name': 'Oregon ash', 'type': 'HW', 'WOR': Eq_38, 'EOR': Eq_26, 'WWA': Eq_38, 'EWA': Eq_26, 'CA': Eq_38},
    'ILEX': {'common_name': 'Holly', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'ILOP': {'common_name': 'American holly', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'ILOPA': {'common_name': 'American holly', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'ILOPO': {'common_name': 'American holly', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'JUGLA': {'common_name': 'Walnut', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_None, 'CA': Eq_38},
    'NOTHO9': {'common_name': 'Tanoak', 'type': 'HW', 'WOR': Eq_34, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_34},
    'NODE3': {'common_name': 'Tanoak', 'type': 'HW', 'WOR': Eq_34, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_34},
    'NODED': {'common_name': 'Tanoak', 'type': 'HW', 'WOR': Eq_34, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_34},
    'NODEE': {'common_name': 'Tanoak', 'type': 'HW', 'WOR': Eq_34, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_34},          
    'NODEA': {'common_name': 'Tanoak', 'type': 'HW', 'WOR': Eq_34, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_34},
    'LIDE3': {'common_name': 'Tanoak', 'type': 'HW', 'WOR': Eq_34, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_34},
    'MALUS': {'common_name': 'Apple', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_42},
    'PLRA': {'common_name': 'California sycamore', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_42},
    'POPUL': {'common_name': 'Cottonwood and Poplar', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'POBE2': {'common_name': 'Cottonwood', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'POHE5': {'common_name': 'Cottonwood', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'POIN23': {'common_name': 'Cottonwood', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},        
    'POSM2': {'common_name': 'Cottonwood', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'POBA2': {'common_name': 'Balsam poplar', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'POBAB2': {'common_name': 'Balsam poplar', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'PODE3': {'common_name': 'Eastern cottonwood', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'PODED': {'common_name': 'Eastern cottonwood', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'PODEM': {'common_name': 'Eastern cottonwood', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'POTR5': {'common_name': 'Quaking aspen', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_28},
    'POBAT': {'common_name': 'Black cottonwood', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_27},          
    'POFR2': {'common_name': 'Fremont poplar', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_27},
    'POFRF3': {'common_name': 'Fremont poplar', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_27},
    'POFRM': {'common_name': 'Fremont poplar', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_27},
    'PROSO': {'common_name': 'Mesquite', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},
    'PRUNU': {'common_name': 'Prunus spp.', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'PRVI': {'common_name': 'Chokecherry', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'PRAV': {'common_name': 'Sweet cherry', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'PREM': {'common_name': 'Bitter cherry', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'PREME': {'common_name': 'Bitter cherry', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'PREMM': {'common_name': 'Bitter cherry', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'PRAV': {'common_name': 'Bitter cherry', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'QUERC': {'common_name': 'Oak-deciduous', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_43},
    'QUAG': {'common_name': 'California live oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_43},
    'QUAGA': {'common_name': 'California live oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_43},
    'QUCH2': {'common_name': 'Canyon live oak', 'type': 'HW', 'WOR': Eq_42, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_42},
    'QUCHC': {'common_name': 'Canyon live oak', 'type': 'HW', 'WOR': Eq_42, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_42},
    'QUCHN': {'common_name': 'Canyon live oak', 'type': 'HW', 'WOR': Eq_42, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_42},
    'QUDO': {'common_name': 'Blue oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_39},
    'QUEM': {'common_name': 'Emory oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_None},         
    'QUEN': {'common_name': 'Engelmann oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_36},
    'QUGA4': {'common_name': 'Oregon white oak', 'type': 'HW', 'WOR': Eq_41, 'EOR': Eq_26, 'WWA': Eq_41, 'EWA': Eq_26, 'CA': Eq_41},
    'QUGAF': {'common_name': 'Oregon white oak', 'type': 'HW', 'WOR': Eq_41, 'EOR': Eq_26, 'WWA': Eq_41, 'EWA': Eq_26, 'CA': Eq_41},
    'QUGAG2': {'common_name': 'Oregon white oak', 'type': 'HW', 'WOR': Eq_41, 'EOR': Eq_26, 'WWA': Eq_41, 'EWA': Eq_26, 'CA': Eq_41},
    'QUGAS': {'common_name': 'Oregon white oak', 'type': 'HW', 'WOR': Eq_41, 'EOR': Eq_26, 'WWA': Eq_41, 'EWA': Eq_26, 'CA': Eq_41},
    'QUKE': {'common_name': 'California black oak', 'type': 'HW', 'WOR': Eq_38, 'EOR': Eq_None, 'WWA': Eq_38, 'EWA': Eq_26, 'CA': Eq_38},
    'QULO': {'common_name': 'California white (valley) oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_35},
    'QUWI2': {'common_name': 'Interior live oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_44},
    'QUWIF': {'common_name': 'Interior live oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_44},
    'QUWIW': {'common_name': 'Interior live oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_44},
    'ROPS': {'common_name': 'Black locust', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_41},
    'SALIX': {'common_name': 'Willow', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_40},
    'SAAL2': {'common_name': 'White willow', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_40},
    'SALUL': {'common_name': 'Pacific willow', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_40},
    'SANI': {'common_name': 'Black willow', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_40},
    'SAPY': {'common_name': 'Balsam willow', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_40},
    'SASC': {'common_name': "Scouler's willow", 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_40},
    'UMBEL': {'common_name': 'California laurel', 'type': 'HW', 'WOR': Eq_33, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_33},
    'UMCA': {'common_name': 'California laurel', 'type': 'HW', 'WOR': Eq_33, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_33},
    'UMCAC': {'common_name': 'California laurel', 'type': 'HW', 'WOR': Eq_33, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_33},
    'UMCAF': {'common_name': 'California laurel', 'type': 'HW', 'WOR': Eq_33, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_33},
              
    # in GNN, but not in CAR/ARB species list
    
    # ABGRC used in GNN for "White and Grand firs" -- borrowed equations from ABGR (Grand fir)
    'ABGRC': {'common_name': 'White and Grand fir', 'type': 'SW', 'WOR': Eq_11, 'WWA': Eq_11, 'EOR': Eq_10, 'EWA': Eq_10, 'CA': Eq_23},
    
    # ABPRSH used in GNN to refer to "Noble, California red, and Shasta red firs" -- borrowed equations from ABPR (Noble fir)
    'ABPRSH': {'common_name': 'Noble and Red firs', 'type': 'SW', 'WOR': Eq_11, 'WWA': Eq_11, 'EOR': Eq_10, 'EWA': Eq_10, 'CA': Eq_18},
    
    # Borrowing from PRUNU (Prunus spp.) because FVS uses same equations for these species
    'ACCI': {'common_name': 'Vine maple', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    'ACGLD4': {'common_name': 'Douglas maple', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},
    
    # Borrowing from from CUPRE (Cypress)
    'CUBA': {'common_name': 'Modoc cypress', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_19},
    'CUMA': {'common_name': 'McNabb cypress', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_19},
    'CUMA2': {'common_name': 'Monterey cypress', 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_19},
    'CUSA3': {'common_name': "Sargent's cypress", 'type': 'SW', 'WOR': Eq_None, 'EOR': Eq_None, 'WWA': Eq_None, 'EWA': Eq_None, 'CA': Eq_19},

    # FRAXI borrwed from FRLA (Oregon ash)
    'FRAXI': {'common_name': 'Ash', 'type': 'HW', 'WOR': Eq_38, 'EOR': Eq_26, 'WWA': Eq_38, 'EWA': Eq_26, 'CA': Eq_38},

    # FRPU7 borrowed from PRUNU (Prunus spp.) because FVS uses same equations for these species
    'FRPU7': {'common_name': 'Cascara buckthorn', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_26},

    # JUHI borrowed from JUGLA (Walnut)
    'JUHI': {'common_name': 'Northern California walnut', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_None, 'CA': Eq_38},

    # JUSC2 borrowed from JUOC (Western juniper)
    'JUSC2': {'common_name': 'Rocky Mountain juniper', 'type': 'SW', 'WOR': Eq_21, 'WWA': Eq_21, 'EOR': Eq_21, 'EWA': Eq_21, 'CA': Eq_21},

    # Borrowed from MALUS (Apple)
    'MAFU': {'common_name': 'Oregon crap apple', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_42},
    'PYCO': {'common_name': 'Common pear', 'type': 'HW', 'WOR': Eq_26, 'EOR': Eq_26, 'WWA': Eq_26, 'EWA': Eq_26, 'CA': Eq_42},

    # Borrowed from QUERC (Oak-deciduous)
    'QUMU': {'common_name': 'Chinkapin oak', 'type': 'HW', 'WOR': Eq_None, 'WWA': Eq_None, 'EOR': Eq_None, 'EWA': Eq_None, 'CA': Eq_43},
}
