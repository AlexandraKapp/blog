library(sf)
library(emdist)
library(geosphere)

example <- read_sf("data/example.gpkg")
scenario1 <- read_sf("data/example_similar.gpkg")
scenario2 <- read_sf("data/example_different.gpkg")


## Option 1 ##

# as we have the same centroids for all three scenarios, 
# you could actually also only compute `centroids_orig` and use them for all cases

signature_opt1 <- function(df_sf, crs) {
  centroids <- df_sf %>%
    st_transform(crs) %>%
    st_centroid() %>%
    st_coordinates()
  
  sig <- matrix(
    data = c(df_sf$example_data / sum(df_sf$example_data), centroids[, 1], centroids[, 2]),
    nrow = nrow(df_sf)
  )
    
  return (sig)
}

# create signatures (value, x_coordinate, y_coordinate) as input matrices for the emd function
sig_original <- signature_opt1(example, 3035)
sig_scenario1 <- signature_opt1(scenario1, 3035)
sig_scenario2 <- signature_opt1(scenario2, 3035)

emd_scen_1 <- emd(sig_original,
  sig_scenario1,
  dist = "euclidean"
)

emd_scen_2 <- emd(sig_original,
  sig_scenario2,
  dist = "euclidean"
)

print(paste("EMD for scenario 1:", round(emd_scen_1), "meters"))
print(paste("EMD for scenario 2:", round(emd_scen_2), "meters"))


## Option 2 ##

signature_opt2 <- function(df_sf){
  centroids <- example %>%
    st_transform(3395) %>%
    st_centroid() %>%
    st_transform(4326) %>%
    st_coordinates()
  
  sig <- matrix(
    data = c(df_sf$example_data / sum(df_sf$example_data), centroids[, 1], centroids[, 2]),
    nrow = nrow(df_sf), ncol = 3
  )
  return (sig)
}

# create signatures (value, x_coordinate, y_coordinate) as input matrices for the emd function
sig_original <- signature_opt2(example)
sig_scenario1 <- signature_opt2(scenario1)
sig_scenario2 <- signature_opt2(scenario2)

haversine <- function(x, y) {
  distHaversine(c(x[1], x[2]), c(y[1], y[2]))
}

# compute the earth  movers distance with geographical coordinates and the haversine distance
emd_scen_1 <- emd(
  sig_original,
  sig_scenario1,
  dist = haversine
)
emd_scen_2 <- emd(
  sig_original,
  sig_scenario2,
  dist = haversine
)

print(paste("EMD for scenario 1:", round(emd_scen_1), "meters"))
print(paste("EMD for scenario 2:", round(emd_scen_2), "meters"))
