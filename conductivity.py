# library
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def find_resistance(dataset):
    currents = dataset[0]
    voltages = dataset[1]
    resistance_sum = 0
    for i in range(0, len(currents)):
        resistance_sum = resistance_sum + (voltages[i]/currents[i])
    resistance = resistance_sum / len(currents)
    return resistance
#   ______________________________
#   |  a1   |  b1    | c1    | d1    |
#   |_____  |________|_______|_____  |  GLASS SAMPLE DIAGRAM
#   |  a2   |  b2    |  c2   |  d2   |
#   |____  _|________|_______|____  _|
##            I          V
glass_b1 = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000223, 0.000439, 0.000662, 0.000884, 0.001108]]
glass_a2 = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000246, 0.000467, 0.000759, 0.001097, 0.001288]]
glass_a1 = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000224, 0.000445, 0.000667, 0.000893, 0.001118]]
glass_b2 = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000222, 0.000442, 0.000664, 0.000889, 0.001111]]
glass_c2 = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000220, 0.000446, 0.000667, 0.000902, 0.001117]]
glass_d2 = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000224, 0.000446, 0.000674, 0.000900, 0.001127]]
glass_d1 = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000229, 0.000457, 0.000689, 0.000923, 0.001156]]
glass_c1 = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000222, 0.000442, 0.000666, 0.000892, 0.001118]]

resistance_glass_a1 = find_resistance(glass_a1)
resistance_glass_a2 = find_resistance(glass_a2)
resistance_glass_b1 = find_resistance(glass_b1)
resistance_glass_b2 = find_resistance(glass_b2)
resistance_glass_c1 = find_resistance(glass_c1)
resistance_glass_c2 = find_resistance(glass_c2)
resistance_glass_d1 = find_resistance(glass_d1)
resistance_glass_d2 = find_resistance(glass_d2)
"""
# Create a dataset
df = pd.DataFrame({'A': [resistance_glass_a1, resistance_glass_a2], 'B': [resistance_glass_b1, resistance_glass_b2], 'C': [resistance_glass_c1, resistance_glass_c2], 'D': [resistance_glass_d1, resistance_glass_d2],})
print(df)
# Default heatmap
sns.heatmap(df, annot=True, fmt='f', annot_kws={"size": 7}, cmap = 'winter', vmin=1.9, vmax=2.6, linewidths=0.25)
#plt.show()
"""

silicon_1_vdp_1234 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.000506, 0.000993, 0.001474, 0.001953, 0.002442]]
silicon_1_vdp_4321 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.000681, 0.001243, 0.001952, 0.002607, 0.003278]]
silicon_2_vdp_1234 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.000235, 0.000426, 0.000614, 0.000801, 0.000961]]
silicon_2_vdp_4321 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.001350, 0.002677, 0.004812, 0.005354, 0.006692]]

resistance_silicon_1_1234 = find_resistance(silicon_1_vdp_1234)
resistance_silicon_1_4321 = find_resistance(silicon_1_vdp_4321)
resistance_silicon_2_1234 = find_resistance(silicon_2_vdp_1234)
resistance_silicon_2_4321 = find_resistance(silicon_2_vdp_4321)

print("Resistance silicon 1 1234: " + str(resistance_silicon_1_1234))
print("Resistance silicon 1 4321: " + str(resistance_silicon_1_4321))
print("Resistance silicon 2 1234: " + str(resistance_silicon_2_1234))
print("Resistance silicon 2 4321: " + str(resistance_silicon_2_4321)) ## too high.

#### graphite sample

graphite_a1 = [[0.1, 0.2, 0.3, 0.4, 0.5], [0.000196, 0.000389, 0.000577, 0.000771, 0.000964]]
graphite_a4 = [[0.1, 0.2, 0.3, 0.4, 0.5], [0.000, 0.000, 0.000572, 0.000765, 0.000985]]
graphite_d1 = [[0.1, 0.2, 0.3, 0.4, 0.5], [0.000188, 0.000369, 0.000555, 0.000745, 0.000931]]
graphite_d4 = [[0.1, 0.2, 0.3, 0.4, 0.5], [0.000207, 0.000406, 0.000610, 0.000814, 0.001020]]
graphite_center = [[0.1, 0.2, 0.3, 0.4, 0.5], [0.000188, 0.000368, 0.000553, 0.000738, 0.000924]]

resistance_graphite_a1 = find_resistance(graphite_a1)
resistance_graphite_a4 = find_resistance(graphite_a4)
resistance_graphite_d1 = find_resistance(graphite_d1)
resistance_graphite_d4 = find_resistance(graphite_d4)
resistance_graphite_center = find_resistance(graphite_center)

"""

df = pd.DataFrame({'A': [resistance_graphite_a1, 0, resistance_graphite_a4], 'B': [0, resistance_graphite_center, 0], 'D': [resistance_graphite_d1, 0, resistance_graphite_d4]})
print(df)
# Default heatmap
sns.heatmap(df, annot=True, fmt='f', annot_kws={"size": 7}, cmap = 'BuPu', vmin=0, vmax=0.005, linewidths=0.25)
plt.show()

"""

### Begin temperature stuff

silicon_241 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.005082, 0.010147, 0.015225, 0.020293, 0.025543]]
silicon_296 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.004927, 0.009891, 0.014884, 0.019873, 0.024944]]
silicon_435 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.003993, 0.008132, 0.012285, 0.016532, 0.021072]]
silicon_589 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.003357, 0.006904, 0.010437, 0.014025, 0.017523]]
silicon_717 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.002713, 0.005773, 0.008784, 0.011879, 0.015068]]
silicon_972 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.002785, 0.005931, 0.009270, 0.012516, 0.015811]]
silicon_1100 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.002498, 0.005551, 0.008541, 0.011707, 0.014756]]
silicon_747_cooling = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.003711, 0.007398, 0.011402, 0.015302, 0.019231]]

resistance_silicon_241 = find_resistance(silicon_241)
resistance_silicon_296 = find_resistance(silicon_296)
resistance_silicon_435 = find_resistance(silicon_435)
resistance_silicon_589 = find_resistance(silicon_589)
resistance_silicon_717 = find_resistance(silicon_717)
resistance_silicon_972 = find_resistance(silicon_972)
resistance_silicon_1100 = find_resistance(silicon_1100)
resistance_silicon_747_cooling = find_resistance(silicon_747_cooling)

temp_analysis = [[24.1, 29.6, 43.5, 58.9, 71.7, 97.2, 110, 74.7], [resistance_silicon_241, resistance_silicon_296, resistance_silicon_435, resistance_silicon_589, resistance_silicon_717, resistance_silicon_972, resistance_silicon_1100, resistance_silicon_747_cooling]]

plt.scatter(temp_analysis[0], temp_analysis[1])
plt.xlabel("Temperate (C)")
plt.ylabel("Observed Resistance (Ohms)")
plt.title("Observed resistance of Silicon sample with temp change")
plt.show()

cf_1234 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.0002, 0.000402, 0.000609, 0.000802, 0.001007]]
cf_4321 = [[0.01, 0.02, 0.03, 0.04, 0.05], [0.000297, 0.000587, 0.000884, 0.001177, 0.001473]]

resistance_cf_1234 = find_resistance(cf_1234)
resistance_cf_4321 = find_resistance(cf_4321)

print("Resistance of cf1: " + str(resistance_cf_1234))
print("Resistance of cf2: "  +str(resistance_cf_4321))
resistance_cf = (resistance_cf_4321 + resistance_cf_1234)/2

strand = [[0.0001, 0.0002, 0.0003, 0.0004, 0.0005], [0.000945, 0.001877, 0.002812, 0.003747, 0.004671]]
resistance_strand = find_resistance(strand)
strand_length = 0.053 #m
print("Resistance of strand: " + str(resistance_strand))

