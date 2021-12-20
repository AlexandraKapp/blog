# Human Mobility Data Use Case Collection

Collection of use cases that human mobility data in needed for in the urban setting, as described in [this]() blog article.

## Urban and Traffic Planning

<style>
table th:first-of-type {
    width: 10%;
}
table th:nth-of-type(2) {
    width: 40%;
}
table th:nth-of-type(3) {
    width: 50%;
}
</style>

| Topic | Use Case | Example |
|---|---|---|
| traffic simulation | Traffic model to simulate the  influence of different scenarios on traffic situations. E.g., the opening of  a new shopping mall or adding a new bus line. | <ul><li>Four-step traffic demand model that uses origin-destination marices (e.g., [Visum PTV](https://www.ptvgroup.com/de/loesungenprodukte/ptv-visum/))</li> <li>[MatSim](https://www.matsim.org/): agent-based model that uses day plans </li> <li>[BikeSim](https://www.bmvi.de/SharedDocs/DE/Artikel/DG/mfund-projekte/bikeSim.html):  bike simulation that uses cyclist trajectories</li>|
| bike infrastructure | Optimize the bike  infrastructure: detect shortcomings through analysis of street attributes  based on GPS trajectories and sensor data (e.g., bumpyness, high chance of  accidents, low bike speed). | <ul><li>[SimRa](https://www.digital-future.berlin/forschung/projekte/simra/) tracks  GPS trajectories of cyclists and identifies almost accidents based on  smartphone sensors</li><li>The [OpenBikeSensor](https://www.openbikesensor.org/en/) tracks GPS trajectories of cylclists and measures the distances of passing cars.</li><li>[Paper](https://www.sciencedirect.com/science/article/abs/pii/S0966692318300875)  on difference between actual paths and shortest paths of bike GPS trajectories.</li><li>[Movebis](https://www.movebis.org/das-projekt/): provides ridership  volumes and speed of bicycles for city administrations based on bike GPS  trajectories</li><li>use of smartphone sensors to identify bumpy roads (e.g., see [this survey  paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6263868/), this  [Hackathon  project](https://hackaday.com/2015/08/17/hackaday-prize-entry-project-dekoboko-%E5%87%B8%E5%87%B9-maps-bumpy-roads-on-a-bike/),  [this  project](https://www.esentri.com/combining-machine-learning-iot-and-cycling-for-low-cost-infrastructure-monitoring/),  this ["Sensorbike"  project](https://nationaler-radverkehrsplan.de/de/aktuell/nachrichten/sensorbike-fahrrad-zur-erforschung-des))</li></ul> |
| bike infrastructure | Determine high demand  origin-destination connections to optimize the bike infrastructure for those  routes. | [Propensity to Cycle  Tool](https://journals.sagepub.com/doi/abs/10.3141/2339-10) uses  origin-destination matrices to visualize cycling demand and thereby povide a  bike infrastructure planning tool. |
| bike infrastructure | Determine the count of bikes for  reporting, monitoring, funding and as a decision basis. | <ul><li>[OpenTrafficCount](https://www.technologiestiftung-berlin.de/en/projects/open-traffic-count/):  Project for a cost-efficient bicycle counter.</li><li>[Interactive map of bicycle  counters](https://data.eco-counter.com/ParcPublic/?id=4586)</li> <li>[Article](https://journals.sagepub.com/doi/abs/10.3141/2339-10) about funds,  based on reported bicycle use and safety reports.</li>   <li>In Germany, such counts can be used for a rededication of a street to a bicylce street.</li> |
| bike infrastructure | Identify locations to place bike  counters for a representative sample of bicyle ridership within a city. | [Article](https://findingspress.org/article/10828-where-to-put-bike-counters-stratifying-bicycling-patterns-in-the-city-using-crowdsourced-data)  how to aggregate GPS trajectories to average hourly activity count for  street-segments to determine traffic volumes and thereby suitable bike counter locations. |
| public transport | Demand-driven short- and  longterm public transport offer. Based on historic and real-time data, public  transport can be optimized to fit daily routines, to account for special  events (e.g., soccer game), or to satisfy real-time demands. | <ul><li>[Funding Project Mobile Data Fusion](https://www.bmvi.de/SharedDocs/DE/Artikel/DG/mfund-projekte/mobiledatafusion.html) that explores the combination of different data sources to derive public transport demand data<li>[Study](https://arxiv.org/pdf/2106.05359.pdf) that analyses public transport  usage during events to evaluate system performance.</li>  <li>[ProTrain](https://www.telefonica.de/analytics/anonymisierte-daten/projekt-pro-train-in-berlin-brandenburg-gestartet.html):  Project to optimize regional public transport offer based on cellular network  data.</li>   <li>[EFA  Analytics](https://vm.baden-wuerttemberg.de/de/politik-zukunft/zukunftskonzepte/digitale-mobilitaet/mobidata-bw-hackathon/projekt-efa-analytics/):  Project on analysis of public transport routing queries for public transport  load predictions.</li> <li>[Publication](https://www.researchgate.net/profile/Zhichao-Cao/publication/336915749_Real-time_schedule_adjustments_for_autonomous_public_transport_vehicles/links/5dba840d299bf1a47b0273e3/Real-time-schedule-adjustments-for-autonomous-public-transport-vehicles.pdf)  on real-time schedule adjustments. </li><ul>|
| shared mobility | Integrate new on-demand and  shared-mobility offers, such as bike, e-scooter, car-sharing and offers into  the cityscape and public transport network:   Provision of demand-based positioning of docking stations and parking  spots. | <ul><li>[Study](https://ideas.repec.org/a/eee/transa/v82y2015icp216-227.html) on  demand-based positioning of docking stations.</li>   <li>[Study](https://www.sciencedirect.com/science/article/abs/pii/S1361920921003795)  on machine learning approach to determine optimal e-scooter parking  locations.</li></ul>|
| shared mobility |   Redistribution of shared vehicles (e-scooter & bike-sharing) and  positioning of ride-hailing (e.g., Uber) and ride-sharing (e.g., Moia)  vehicles based on historic demands. | [Study](https://www.researchgate.net/publication/344503514_Effective_Heuristics_for_Distributing_Vehicles_in_Free-floating_Micromobility_Systems)  on effective redistribution of vehicles. |
| shared mobility | City administrations use  reportings on usage behavior and analysis tools to evaluate the use of  micro-mobility in their cities. The mobility data specification has been  established as a standard that more and more mobility service providers start  to use and offer their data accordingly. The specification goes beyond human  mobility data (e.g., charging status of vehicles or definition of prohibited  parking zones, see [this  article](https://www.openmobilityfoundation.org/whats-possible-with-mds/) and  [this MDS use case  gallery](https://airtable.com/shrPf4QvORkjZmHIs/tblzFfU6fxQm5Sdhm)) but also  includes start end end locations of rentals. | Service providers that combine  data from multiple providers and offer analysis platforms to cities. E.g.,  [Vianova](https://de.vianova.io/) [Remix](https://de.remix.com/),  [Populus](https://www.populus.ai/). |


## Traffic Management and Routing

| Topic | Use Case | Example |
|---|---|---|
|  |  |  |
|  |  |  |

## Other Use Cases

| Topic | Use Case | Example |
|---|---|---|
|  |  |  |
|  |  |  |