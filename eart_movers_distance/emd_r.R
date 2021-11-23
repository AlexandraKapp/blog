library(sf)
library(emdist)
library(geosphere)

example <- read_sf("data/example.gpkg")
scenario1 <- read_sf("data/example_similar.gpkg")
scenario2 <- read_sf("data/example_different.gpkg")


## Option 1 ##

# as we have the same centroids for all three scenarios, 
# you could actually also only compute `centroids_orig` and use them for all cases
centroids_orig <- example %>%
  st_transform(3035) %>%
  st_centroid() %>%
  st_coordinates()
centroids_scen1 <- scenario1 %>%
  st_transform(3035) %>%
  st_centroid() %>%
  st_coordinates()
centroids_scen2 <- scenario2 %>%
  st_transform(3035) %>%
  st_centroid() %>%
  st_coordinates()

# create signatures (value, x_coordinate, y_coordinate) as input matrices for the emd function
sig_original <- matrix(
  data = c(example$example_data / sum(example$example_data), centroids_orig[, 1], centroids_orig[, 2]),
  nrow = nrow(example), ncol = 3
)
sig_scenario1 <- matrix(
  data = c(scenario1$example_data / sum(scenario1$example_data), centroids_scen1[, 1], centroids_scen1[, 2]),
  nrow = nrow(example), ncol = 3
)
sig_scenario2 <- matrix(
  data = c(scenario2$example_data / sum(scenario2$example_data), centroids_scen2[, 1], centroids_scen2[, 2]),
  nrow = nrow(example), ncol = 3
)

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

# as we have the same centroids for all three scenarios, 
# you could actually also only compute `centroids_orig` and use them for all cases
centroids_orig <- example %>%
  st_transform(3035) %>%
  st_centroid() %>%
  st_transform(4326) %>%
  st_coordinates()
centroids_scen1 <- scenario1 %>%
  st_transform(3035) %>%
  st_centroid() %>%
  st_transform(4326) %>%
  st_coordinates()
centroids_scen2 <- scenario2 %>%
  st_transform(3035) %>%
  st_centroid() %>%
  st_transform(4326) %>%
  st_coordinates()

# create signatures (value, x_coordinate, y_coordinate) as input matrices for the emd function
sig_original <- matrix(
  data = c(example$example_data / sum(example$example_data), centroids_orig[, 1], centroids_orig[, 2]),
  nrow = nrow(example), ncol = 3
)
sig_scenario1 <- matrix(
  data = c(scenario1$example_data / sum(scenario1$example_data), centroids_scen1[, 1], centroids_scen1[, 2]),
  nrow = nrow(example), ncol = 3
)
sig_scenario2 <- matrix(
  data = c(scenario2$example_data / sum(scenario2$example_data), centroids_scen2[, 1], centroids_scen2[, 2]),
  nrow = nrow(example), ncol = 3
)

haversine <- function(x, y) {
  distHaversine(c(x[1], x[2]), c(y[1], y[2]))
}

# compute the earth  movers distance with geographical coordinates and the haversine distance
emd_scen_1 <- emd(sig_original,
  sig_scenario1,
  dist = haversine
)
emd_scen_2 <- emd(sig_original,
  sig_scenario2,
  dist = haversine
)

print(paste("EMD for scenario 1:", round(emd_scen_1), "meters"))
print(paste("EMD for scenario 2:", round(emd_scen_2), "meters"))
