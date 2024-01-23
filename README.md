# FUN-TB

*`FUN-TB`* is a freely available open-source Python standalone tool designed for analyzing MTBSeq v.1.0 output files. It facilitates the comparison of the presence of Single Nucleotide Polymorphisms (SNPs) among phenotypically diverse sets of Mycobacterium tuberculosis samples. FunTB is a command-line tool composed of three scripts: a) Variation dictionary creation, b) Phenotype-based samples lists generation, and c) Phenotype-centric and gene-surrounded networks structuration.

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

<p align="center">
  <img src="Images/Script_Two.png" />
</p>

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)



## Features

- Analyze genetic variations related to tuberculosis.
- Construct phenotype-centric networks based on genetic data.
- Visualize and interpret complex relationships between genes and phenotypes.

## Installation

Ensure you have Python 3.x installed on your system. Install MyTool using pip:

bash
pip install mytool

## Usage

This tool takes as input three parameters. First, an MTBseq output tab file. Second, a list of samples in txt format that you want to compare and, finally, an integer number representing the number of top genes you want to get from the interest groups. To run this tool, you have to execute the following-like command:

FUN-TB.py MTBseq_file.tab samples.txt 1000


And as output, we will get a CSV file, an input format for Cytoscape, a network software where we can visualize and edit our resulting genes' relationships. The output format looks like this:

| Source Node  |  Target Node   | Fitness Score | Edge Color | Node Size |
|    :---:     |     :---:      |     :---:     |    :---:   |   :---:   |
|     acee     |   Sensitive    |       7       |    blue    |     5     |
|     rpoc     |   Resistant    |       3       |    green   |     2     |

Once you import the output file in Cytoscape, you can map the different networks' parameters and get the editable format to set some extra settings like node position and distribution, node group based on desired or similar characteristics.  Finally, save your final network image. The workflow of the data processing is as follows:



At the moment, you can find a [Beta version](https://colab.research.google.com/drive/1bttbnmZs682GMH_eq-J7EWxsvm6UBFRW?usp=sharing) implemented in Google Colab, where we have already pre-loaded some Mexican available sequences data and their corresponding metadata information (Geographical, Age, Sex, Comorbidities, Acquisition year, and Drug Resistance status). You can select from a list of options, the characteristics desired for each of the two groups you can compare and get a preliminary network image corresponding to the two groups of interest.

To run this beta, you need, first, to execute the code section; this group of cells contains all the necessary functions to load and process the data to generate the final network.

Then, within the FUN-TB section, you have to choose the characteristics for each of the two groups you want to compare. Once you select those features, run both cells.

Finally, you need to set a total of the top genes (Integer number) you want to consider in the network structure, then run the cell of network construction and, that's it, you will have a preliminary image of your network.

<p align="center">
  <img src="https://github.com/ind-genomics/FUN-TB/blob/main/Images/Network2.png?raw=true" />
</p>

## License

*`FUN-TB`* is available under MIT License. See License.txt for more details.
