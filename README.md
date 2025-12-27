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

The morphological traits measured are beak dimensions, wing dimensions, tarsus length, and body mass. The ecological variables recorded include habitat, migration, trophic level, and primary lifestyle. Information on geographic location is given as the minimum and maximum latitude, midpoint latitude and longitude, as well as range size.

#### **2.1.2 WorldClim**

WorldClim is an open-access database of high-resolution global climate data. The data are derived from measurements from weather stations across the world and are summarized as standard monthly variables and also bioclimatic variables that are most relevant to biological processes. There are 19 bioclimatic variables regarding the temperature and precipitation. The data are given in different spatial resolutions, and for this project, selected bioclimatic variables with 10-minute resolution are used. The database is Raster Data, given in GeoTIFF format, in which every pixel of the digital image corresponds to a climate value. 

### **2.2. Data Preparation**

First, the AVONET dataset is filtered to eliminate the unused variables. The following columns are kept:

- Morphological Traits: 
    - Mass
    - Beak Length
    - Tarsus Length
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

The morphological data are highly right-skewed for all five traits. For mass, wing length, and hand-wing index, log-transformation is applied to approach a normal distribution. However, for tarsus length and beak length, the assumption of normal distribution is rejected due to high kurtosis even after log-transformation. The morphological data are also evaluated for normality when grouped based on the ecological variables, for example, the distribution of mass within each habitat group. However, none of the traits are normally distributed across ecological groups.

For minimum, maximum, and mean temperature, the data are highly left-skewed. However, normalization is intentionally not applied to these variables. This is because temperature does not follow multiplicative scaling; for example, 20 °C is not twice as hot as 10 °C. Therefore, applying logarithmic or exponential transformations could distort the physical and biological relevance. Consequently, the assumption of normal distribution is rejected for these variables. For precipitation, square root transformation is applied to approach a normal distribution. 

#### **2.3.2. Climatic Variables**

All the morphological traits are tested against minimum, maximum, and mean temperature to assess correlations, using Spearman's rank correlation coefficient. Mass is additionally tested against precipitation, using the Pearson correlation coefficient, given the normal distributions.

#### **2.3.3. Ecological Variables**

All morphological traits are first grouped based on habitat types (Open, Closed, Aquatic), migratory behaviors (Sedentary, Partial, Migratory), and trophic levels (Herbivore, Omnivore, Carnivore). All the selected traits are first tested using the Kruskal–Wallis test to assess the differences in distributions, followed by Dunn’s test to determine the groups that differ.

### **2.4. Machine Learning**

#### **2.4.1. Random Forest Regression**

A random forest regression model is built for each morphological trait, combining the climatic and ecological variables. To improve the predictive power, both variable sets are expanded. In addition to the previously used temperature and precipitation, temperature seasonality is included as a climatic variable. The trophic level is replaced by the trophic niche, with 10 distinct dietary specializations. Instead of grouping the habitats into broad categories, 11 specific habitat types are used to preserve the variance. The primary lifestyle is added as a new feature, with five categories of locomotory niches: Aerial (flying), Insessorial (perching), Terrestrial (walking), Aquatic (swimming), and Generalist (not specialized).

The ecological variables are converted into numerical variables via one-hot encoding. The data is split into training (80%) and testing (20%) sets to build the model. To prevent overfitting, several thresholds are applied to the model; the number of trees is limited to 100, with a maximum of 10 branches and a minimum of 5 samples in each leaf. Feature importance is used to quantify the predictive power of each variable on a certain morphological trait. Based on the proportion of variance explained by each variable, it is concluded which factors are more controlling in avian morphology. 

#### **2.4.2. Principal Component Analysis (PCA)**

PCA is performed to reduce the morphological traits into a few dimensions. The data is first standardized for each trait, including tail length, to equally contribute to the analysis. Initially, a full PCA is run to determine the number of principal components to explain a sufficient amount of variance. The result demonstrated that the first two principal components, PC1 and PC2, account for nearly 85% of the total variance (Figure 1). PC1 represents the overall body size, accounting for all the size measures almost equally. PC2 represents the wing shape, heavily based on the Hand-Wing Index (Figure 2). Based on these two components, a two-dimensional morphospace is visualized for all the birds. The clusters are identified to conclude how climatic and ecological variables relate to the overall morphology. 

## **3. RESULTS**

### **3.1. Morphology and Climate**



### **3.2. Morphology and Ecology**



## **4. DISCUSSION** 



