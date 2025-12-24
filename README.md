# **ADAPTIVE RELATIONSHIPS BETWEEN AVIAN MORPHOLOGY AND CLIMATE**

## **1. INTRODUCTION**

Adaptation simply refers to the evolutionary process by which populations change traits to better survive and reproduce in a specific environment. These adaptations are typically behavioral, physiological, or morphological. While behavioral traits describe how individuals act and physiological traits explain how internal systems function, morphological traits refer to the body structure. Morphological variation involves changes in the size, color, or shape of the body and limbs, which directly affect the organism’s survival. 

Driven by a research interest in evolutionary biology and a personal fascination with birds, this project is designed to explore how avian morphology adapts to different environmental conditions. Combining a global avian trait dataset (AVONET) with world climate records (WorldClim), the project aims to reveal possible correlations between morphological traits and climatic conditions. 

The project is expected to identify an inverse relationship between body size and temperature, as suggested by Bergmann’s rule. This is because larger body sizes help preserve internal body temperature due to a lower surface area to volume ratio. Similarly, shorter limbs help minimize heat loss. Therefore, an inverse relationship between limb size and temperature is expected. In addition, since precipitation determines the food and habitat resources available, it is expected to influence body and limb proportions. Temperature seasonality is also examined, since annual fluctuations in climate force organisms to adapt to both extremes or temporarily migrate to more favorable habitats. 

Furthermore, since selection pressures are not limited to climate, the project also investigates physiological and behavioral variables. Factors such as habitat, migratory behavior, diet, and lifestyle are expected to have an effect on morphology. For example, habitat and lifestyle could act on limb proportions, migratory behavior could specifically affect wing size and shape, and diet could specifically influence beak size.

## **2. METHODOLOGY**

### **2.1. Data Structure**

#### **2.1.1. AVONET**

AVONET is a publicly available database released with the publication titled “AVONET: morphological, ecological and geographical data for all birds” by Tobias et al. (2022). The database is a compilation of functional trait data for all birds, including morphological measurements, ecological variables, and geographic location. It includes measurements from 90020 individuals of 11009 bird species around the world and summarizes the data as species averages in different taxonomic formats. For this project, the BirdLife format is used, given in CSV format. 

The morphological traits measured are beak dimensions, wing dimensions, tail length, tarsus length, and body mass. The ecological variables recorded include habitat, migration, trophic level, and primary lifestyle. Information on geographic location is given as the minimum and maximum latitude, midpoint latitude and longitude, as well as range size.

#### **2.1.2 WorldClim**

WorldClim is an open-access database of high-resolution global climate data. The data are derived from measurements from weather stations across the world and are summarized as standard monthly variables and also bioclimatic variables that are most relevant to biological processes. There are 19 bioclimatic variables regarding the temperature and precipitation. The data are given in different spatial resolutions, and for this project, selected bioclimatic variables with 10-minute resolution are used. The database is Raster Data, given in GeoTIFF format, in which every pixel of the digital image corresponds to a climate value. 

### **2.2. Data Preparation**

First, the AVONET dataset is filtered to eliminate the unused variables. The following columns are kept:

- Morphological Traits: 
    - Mass
    - Beak Length
    - Tarsus Length
    - Tail Length
    - Wing Length
    - Hand-Wing Index
- Ecological Variables: 
    - Habitat
    - Trophic Level
    - Trophic Niche
    - Primary Lifestyle
    - Migration
- Geographical Information (for adding the climate data):
    - Centroid Longitude
    - Centroid Latitude 

Next, the rasterio library is used to extract the selected bioclimatic variables corresponding to the centroid longitude and latitude of each species. The following bioclimatic variables are added to the filtered AVONET dataset:

- BIO1: Annual Mean Temperature
- BIO4: Temperature Seasonality (Standard Deviation × 100)
- BIO5: Maximum Temperature of the Hottest Month
- BIO6: Minimum Temperature of the Coldest Month
- BIO12: Annual Mean Precipitation


### **2.3. Exploratory Data Analysis**

#### **2.3.1. Data Distribution**

The distribution of each variable is evaluated for normality based on skewness and kurtosis, since the Shapiro-Wilk test is overly sensitive with large sample sizes. While skewness is used as a measure of the symmetry of the distribution, kurtosis is used to measure the sharpness of the peak. For this project, the criteria for normal distribution are defined as both skewness and kurtosis values falling between -1 and 1. 

The morphological data are highly right-skewed for all six traits. For mass, tail length, wing length, and hand-wing index, log-transformation is applied to approach a normal distribution. However, for tarsus length and beak length, the assumption of normal distribution is rejected due to high kurtosis even after log-transformation. The morphological data are also evaluated for normality when grouped based on the ecological variables, for example, the distribution of mass within each habitat group. As a result, among all traits, only tail length consistently shows a normal distribution across ecological groups after log-transformation.

For minimum, maximum, and mean temperature, the data are highly left-skewed. However, normalization is intentionally not applied to these variables. This is because temperature does not follow multiplicative scaling; for example, 20 °C is not twice as hot as 10 °C. Therefore, applying logarithmic or exponential transformations could distort the physical and biological relevance. Consequently, the assumption of normal distribution is rejected for these variables. For precipitation, square root transformation is applied to approach a normal distribution. 

#### **2.3.2. Traits and Climatic Variables**

All the morphological traits are tested against minimum, maximum, and mean temperature to assess correlations, using Spearman's rank correlation coefficient. Mass is additionally tested against precipitation, using the Pearson correlation coefficient, given the normal distributions.

#### **2.3.3. Traits and Ecological Variables**

All the morphological traits are firstly grouped based on habitat groups (open, closed, aquatic), migratory behaviors (sedentary, partial, migratory), and trophic levels (herbivore, omnivore, carnivore). The traits, except for tail length, are first tested using the Kruskal–Wallis test to assess the differences in distributions across groups, followed by Dunn’s test to determine the groups that differ. For tail length, one-way ANOVA and Tukey’s HSD test are used for the same purpose, given the normal distributions. 

### **2.4. Machine Learning**

#### **2.4.1. Random Forest Regression**



#### **2.4.2. Principal Component Analysis (PCA)**



## **3. RESULTS**

### **3.1. Morphology and Climate**



### **3.2. Morphology and Ecology**



## **4. DISCUSSION** 



