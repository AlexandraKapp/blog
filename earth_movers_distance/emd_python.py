import numpy as np
import geopandas as gpd
import cv2
from haversine import haversine, Unit


example = gpd.read_file("data/example.gpkg")
scenario1 = gpd.read_file("data/example_similar.gpkg")
scenario2 = gpd.read_file("data/example_different.gpkg")

#### Option 1: use projected coordinates ####
# using the EPSG:3035 projection ETRS89-extended / LAEA Europe

def signature_opt1(gdf, crs):
    centroids = gdf.geometry.to_crs(crs).centroid

    sig = np.empty((len(gdf), 3), dtype=np.float32) # float32 needed as input for cv2.emd!
    # we need to normalize the data in case the total n of the two compared distributions are not equal
    sig[:,0] = gdf.example_data / gdf.example_data.sum()
    sig[:,1] = centroids.x
    sig[:,2] = centroids.y
    return sig

sig_original = signature_opt1(example, 3035)
sig_scen1 = signature_opt1(scenario1, 3035)
sig_scen2 = signature_opt1(scenario2, 3035)


emd_scen1, _ , _ = cv2.EMD(sig_original, sig_scen1, distType = cv2.DIST_L2)
emd_scen2, _ , _ = cv2.EMD(sig_original, sig_scen2, distType = cv2.DIST_L2)

print("Option 1:")
print("Earth movers distance scenario 1 (CRS: EGSG:3035): " + str(round(emd_scen1)) + " meters")
print("Earth movers distance scenario 2 (CRS: EGSG:3035): " + str(round(emd_scen2)) + " meters")


#### Option 2: construct a custom cost_matrix with the haversine distance ####

def get_cost_matrix(gdf1, gdf2):
    gdf1_centroids = gdf1.to_crs(3395).centroid.to_crs(4326)
    gdf2_centroids = gdf2.to_crs(3395).centroid.to_crs(4326)
    coords_sig1 = list(zip(gdf1_centroids.y, gdf1_centroids.x))
    coords_sig2 = list(zip(gdf2_centroids.y, gdf2_centroids.x))
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

# as the coordinates are the same in both scenarios 
# you could use the same cost matrix for both scenarios
cost_matrix1 = get_cost_matrix(example, scenario1)
cost_matrix2 = get_cost_matrix(example, scenario2)

emd_scen1, _ , _ = cv2.EMD(sig_original, sig_scen1, distType = cv2.DIST_USER, cost = cost_matrix1)
emd_scen2, _ , _ = cv2.EMD(sig_original, sig_scen2, distType = cv2.DIST_USER, cost = cost_matrix2)

print("Option 2:")
print("Earth movers distance scenario 1: " + str(round(emd_scen1)) + " meters")
print("Earth movers distance scenario 2: " + str(round(emd_scen2)) + " meters")
