# FUN-TB

*`FUN-TB`* is a freely available open-source Python standalone tool designed for analyzing MTBSeq v.1.0 output files. It facilitates the comparison of the presence of Single Nucleotide Polymorphisms (SNPs) among phenotypically diverse sets of Mycobacterium tuberculosis samples through a Phenotypic centred networks structuration, making able to observe which altered genes and based on the node size and edge width in which proportion they are related to each phenotype. 

. FunTB is a command-line tool composed of three scripts: a) Variation dictionary creation, b) Phenotype-based samples lists generation, and c) Phenotype-centric and gene-surrounded networks structuration.

## Variation dictionary creation script
This script aims to create a Python dictionary object from an MTBSeq V.1.0 file. The dictionary summarizes the presence of SNPs, along with the position and frequency parameters of each altered gene per sample.
<p align="center">
  <img src="Images/Script_One.png" />
</p>

## Phenotype-based samples lists generation script
This second script aims to generate a series of lists containing sample IDs. These lists are constructed such that samples within the same list share common phenotypical features and clinical values.
<p align="center">
  <img src="Images/Script_Three.png"/>
</p>

## Phenotype-centric and gene-surrounded networks structuration script
The third script takes as input the files generated by the previous two scripts. It begins by extracting and summarizing gene information from samples within each specified list. Subsequently, it conducts comparisons among these groupings to identify positions that exhibit at least one alteration and are absent in the contrasting sets.

The script visualizes the results by representing variations in node size and their positions in the network. The contribution of each phenotype to node size is depicted through edge width. Node color serves as an indicator of group membership, and nodes present in more than one group are visually highlighted.

In summary, the script provides a comprehensive analysis of genetic variations, emphasizing their presence or absence in different phenotypic groups. The resulting network visualization offers insights into the relationships between genetic alterations and phenotypic characteristics.

<p align="center">
  <img src="Images/Script_Two.png" />
</p>

## Table of Contents

- [Features](#features)
- [Set Up](#Setup)
- [Usage](#usage)
- [Documentation](#documentation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Analyze genetic variations related to tuberculosis.
- Construct phenotype-centric networks based on genetic data.
- Visualize and hypothesize complex relationships between genes and phenotypes.

## Setup

Ensure you have these or similar versions installed on your system. 
- Python: 3.11.5
- Pandas: 2.0.2
- Numpy: 1.24.3
- Matplotlib: 3.7.1
- Networkx: 3.1
- Seaborn: 0.13.0
- Scipy: 1.11.1

## Usage

### Variation dictionary creation script

This first script takes as input three parameters: First, the MTBseq output file name and its direction. Second, Clinical data CSV file and finally, a string representing the name of the resulting file. To run this script, you have to execute the following-like command:

```bash
python FunTB_dictionary.py MTBseq_file.tab Clinical_Data.csv Dictionary_Output_File_name
```
And as output, we will get a TXT file, with all summarized information about each samples,. The output format looks like this:

- Sample 1
  - Gene 1
    - Total variations
      - integer representing number of alterations 
    - variation positions
      - variable position: frequency of variation
    - symbolic mutations
      - variation symbol: frequency of appearances

### Phenotype-based samples lists generation script

The second script takes as input one parameter: A Clinical data CSV file name, a string representing the name of the resulting file. To run this script, you have to execute the following-like command:

```bash
python Sample_Grouping__Creation.py Clinical_Data.csv
```
And as output, we will get a series of TXT files, which will contain the ids of samples that share common clinical values. The output format looks like this:

| sample id 1 |
|     :---:   |
| sample id 2 |
| sample id 3 |
|      .      |
|      .      |
|      .      |
| sample id n |
|             |

### Phenotype-centric and gene-surrounded networks structuration script

The third script requires a minimum of eight parameters as input. First, a string is needed to define the output file name for the network. Second, a TXT file is required to specify the variation dictionary file name. Third, an integer is needed to determine the percentage of conserved genes, ranging from 0 to 100. The fourth parameter is the alpha value, which determines the weight for ponderating the Alteration Density Score (ADS) contribution. The fifth parameter is the beta coefficient, responsible for regulating the contribution of the Dominant Altered Gene Score (DAGS). Following that, we have the gamma coefficient, which focuses on regulating the Cluster Diversity Score (CDAS). Each of these scores is then summed to calculate the Comprehensive Alteration Impact Score (CAIS), reflected in the node size. Finally, the last parameters are the names of files corresponding to lists of samples (at least two) from groups with contrasting phenotypical features. To run this script, you have to execute the following-like command:

```bash
python FuNTB.py Network_name Variation_dictionary_file Percentage_factor alpha_coefficient beta_coefficient gamma_coefficient Group_list_1 Group_list_2 ... Group_list_n
```

The output generated are three XML-Network file formats (GraphML, GEXF, GML) an input format for Cytoscape, a network software where we can visualize and edit our resulting genes' relationships. The output format could be summarized in a table like this:

| Source Node  |  Target Node   | CAIS Score | Edge Color | Node Size | Edge Width |
|    :---:     |     :---:      |  :---:     |    :---:   |   :---:   |    :---:   |
|     acee     |   Sensitive    |    7       |    blue    |     5     |     1.0    |
|     rpoc     |   Resistant    |    3       |    green   |     2     |     0.3    |

Once you import the output file in Cytoscape, you can map the different networks' parameters and get the editable format to set some extra settings like node position and distribution, node group based on desired or similar characteristics.  Finally, save your final network image.

## License

*`FUN-TB`* is available under MIT License. See License.txt for more details.
