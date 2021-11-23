import numpy as np
import geopandas as gpd
import cv2
from haversine import haversine, Unit


example = gpd.read_file("data/example.gpkg")
scenario1 = gpd.read_file("data/example_similar.gpkg")
scenario2 = gpd.read_file("data/example_different.gpkg")

#### Option 1: use projected coordinates ####
# using the EPSG:3035 projection ETRS89-extended / LAEA Europe

example["centroid_3035"] = example.geometry.to_crs(3035).centroid
scenario1["centroid_3035"] = scenario1.geometry.to_crs(3035).centroid
scenario2["centroid_3035"] = scenario2.geometry.to_crs(3035).centroid

sig_original = np.empty((len(example), 3), dtype=np.float32) # float32 needed as input for cv2.emd!
# we need to normalize the data in case the total n of the two compared distributions are not equal
sig_original[:,0] = example.example_data / example.example_data.sum()
sig_original[:,1] = example.centroid_3035.x
sig_original[:,2] = example.centroid_3035.y

sig_scen1 = np.empty((len(scenario1), 3), dtype=np.float32) # float32 needed as input for cv2.emd!
# we need to normalize the data in case the total n of the two compared distributions are not equal
sig_scen1[:,0] = scenario1.example_data / scenario1.example_data.sum()
sig_scen1[:,1] = scenario1.centroid_3035.x
sig_scen1[:,2] = scenario1.centroid_3035.y


sig_scen2 = np.empty((len(scenario2), 3), dtype=np.float32) # float32 needed as input for cv2.emd!
# we need to normalize the data in case the total n of the two compared distributions are not equal
sig_scen2[:,0] = scenario2.example_data / scenario2.example_data.sum()
sig_scen2[:,1] = scenario2.centroid_3035.x
sig_scen2[:,2] = scenario2.centroid_3035.y

emd_scen1, _ , _ = cv2.EMD(sig_original, sig_scen1, distType = cv2.DIST_L2)
emd_scen2, _ , _ = cv2.EMD(sig_original, sig_scen2, distType = cv2.DIST_L2)

print("Option 1:")
print("Earth movers distance scenario 1 (CRS: EGSG:3035): " + str(round(emd_scen1)) + " meters")
print("Earth movers distance scenario 2 (CRS: EGSG:3035): " + str(round(emd_scen2)) + " meters")


#### Option 2: construct a custom cost_matrix with the haversine distance ####

example["centroid_4326"] = example.geometry.to_crs(3395).centroid.to_crs(4326)
scenario1["centroid_4326"] = scenario1.geometry.to_crs(3395).centroid.to_crs(4326)
scenario2["centroid_4326"] = scenario2.geometry.to_crs(3395).centroid.to_crs(4326)

def get_cost_matrix(coords_sig1, coords_sig2):
    #get all potential combinations between all points from sig1 and sig2
    grid = np.meshgrid(range(0, len(coords_sig1)), 
                        range(0, len(coords_sig2)))
    tile_combinations = np.array([grid[0].flatten(), grid[1].flatten()])
    
    # create an empty cost matrix with the length of all possible combinations
    cost_matrix = np.empty(tile_combinations.shape[1], dtype = np.float32) # float32 needed as input for cv2.emd!

    # compute haversine distance for all possible combinations
    for column in range(0, tile_combinations.shape[1]):
        tile_1 = tile_combinations[0, column]
        tile_2 = tile_combinations[1, column]
        cost_matrix[column]  = haversine(coords_sig1[tile_1], coords_sig2[tile_2], unit = Unit.METERS)
    
    # reshape array to matrix
    return np.reshape(cost_matrix, (len(coords_sig1),len(coords_sig2)))

# as the coordinates in both scenarios are the same, 
# the cost matrix can be used for both scenarios
coords_sig1 = list(zip(example.centroid_4326.y, example.centroid_4326.x))
coords_sig2 = list(zip(scenario1.centroid_4326.y, scenario1.centroid_4326.x))

cost_matrix = get_cost_matrix(coords_sig1, coords_sig2)

emd_scen1, _ , _ = cv2.EMD(sig_original, sig_scen1, distType = cv2.DIST_USER, cost = cost_matrix)
emd_scen2, _ , _ = cv2.EMD(sig_original, sig_scen2, distType = cv2.DIST_USER, cost = cost_matrix)

print("Option 2:")
print("Earth movers distance scenario 1: " + str(round(emd_scen1)) + " meters")
print("Earth movers distance scenario 2: " + str(round(emd_scen2)) + " meters")
