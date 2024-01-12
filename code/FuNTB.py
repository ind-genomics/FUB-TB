# Libraries imports

import ast
import csv
import itertools
import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import operator
import os
import pandas as pd
import random
import requests
import seaborn as sns
import sys
import statistics

from itertools import permutations
from networkx.classes.function import edges
from  random import sample
from scipy import stats

from collections import Counter
from itertools import permutations
from matplotlib.pyplot import figure
from matplotlib.legend import Legend

from NetworkDataGeneration import *
from NetworkStructureGeneration import *
from ParetoFrontExtraction import *

# Input parameters
Network_name = sys.argv[1] # Name to sav the file
Variations_dictionary_file = sys.argv[2] # Variation dictionary File (.txt)
Parteto_frontiers = sys.argv[3] # Select top genes to show up within the network representation (integer)
alpha = sys.argv[4] # Ponderation factor float -> [0-1]
beta = sys.argv[5] # Ponderation factor float -> [0-1]
gamma = sys.argv[6] # Ponderation factor float -> [0-1]
Group_Lists = sys.argv[7:] # Groups list files (.txt)
FunTB_dir = os.getcwd() # Current work directory

# Loading input files
non_synonym_variation_data = open(os.path.join(FunTB_dir, os.path.join('Variations_dictionaries',Variations_dictionary_file)), "r")
contents = non_synonym_variation_data.read()
non_synonym_variation_data_dictionary = ast.literal_eval(contents) # Pyton dictionary file that contains all alterations genes information.

## Samples Ids extraction
groups = [] # Total samples list
for group_file in Group_Lists:
  with open(os.path.join(FunTB_dir, os.path.join('Samples_lists_files',group_file)),  "r") as file:
    file_content = file.read()
  
  group_data = ast.literal_eval(file_content)
  groups.append(group_data)

## Extracting groups names
groups_names = []
for group_file in Group_Lists:
  groups_names.append(group_file.split('.')[0])

## Get combinations of indexes for groups comparisons - Unique genes and common positions removal
groups_comparisons = generate_groups_permutations(groups)

## Extract genes' information (variations and their relative frequency)
Groups_genes_data = []
for i,group_samples in enumerate(groups):
  Groups_genes_data.append(GenesData(group_samples, non_synonym_variation_data_dictionary))

## Perform group comparisons to remove common variable positions
relevant_genes_data = []
for group_comparison in groups_comparisons:
  relevant_genes_data.append(relevant_genes(uncommon_positions(Groups_genes_data[group_comparison[0]],
                                                               Groups_genes_data[group_comparison[1]])))

# Network Struture
## Get network components (Gene nodes, Group nodes and edges)
Variations_network, Groups_genes_network = GetNetwork(groups_names, relevant_genes_data)

## Set size of group nodes, 1000 by default
for group_name in groups_names:
  Variations_network.nodes[group_name]['size'] = 1000

## Setting network attributes (Node size --> Fitness score, Node color --> Degree or Group link, Edge weigth --> pvs contribution)
Group_genes_information = GetGroupsGenesInformation(groups_names, Groups_genes_network, relevant_genes_data)

# Update genes alteration information
Score_genes_info = {}

for group, genes in Group_genes_information.items():
  for gene in genes:
    if gene not in Score_genes_info:
      Score_genes_info[gene] = Group_genes_information[group][gene]
    else:
      Score_genes_info[gene] = update_positions(Score_genes_info[gene], Group_genes_information[group][gene])

# Metrics calculation
gene_scores = {}

for gene, positions in Score_genes_info.items():
  if gene in Variations_network.nodes():
    gene_scores[gene] = {}
    Alteraton_Density_Score = AlterationDensityScore(sum(Score_genes_info[gene].values()), len(Score_genes_info[gene]))
    gene_scores[gene]['ADS'] = Alteraton_Density_Score

    Dominant_Altered_Gene_Score = DominantAlteredGeneScore(max(Score_genes_info[gene].values()), len(Score_genes_info[gene]))
    gene_scores[gene]['DAGS'] = Dominant_Altered_Gene_Score

    number_of_neighbours = GetTotalGroupGenes(gene, Variations_network)
    Cluster_Diversity_Alteration_Score = ClusterDiversityAlterationScore(len(Score_genes_info[gene]), number_of_neighbours)
    gene_scores[gene]['CDAS'] = Cluster_Diversity_Alteration_Score

# Define a function to perform Min-Max scaling normalization
def min_max_scaling(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

# Find the minimum and maximum values for each variable (ADS, DAGS, CDAS)
min_ads = min([gene_scores[gene]['ADS'] for gene in gene_scores])
max_ads = max([gene_scores[gene]['ADS'] for gene in gene_scores])

min_dags = min([gene_scores[gene]['DAGS'] for gene in gene_scores])
max_dags = max([gene_scores[gene]['DAGS'] for gene in gene_scores])

min_cdas = min([gene_scores[gene]['CDAS'] for gene in gene_scores])
max_cdas = max([gene_scores[gene]['CDAS'] for gene in gene_scores])

# Apply Min-Max scaling to each variable
for gene in gene_scores:
    gene_scores[gene]['ADS'] = round(min_max_scaling(gene_scores[gene]['ADS'], min_ads, max_ads), 4)
    gene_scores[gene]['DAGS'] = round(min_max_scaling(gene_scores[gene]['DAGS'], min_dags, max_dags), 4)
    gene_scores[gene]['CDAS'] = round(min_max_scaling(gene_scores[gene]['CDAS'], min_cdas, max_cdas), 4)

# Comprenhensive Alteration Impact Scores
for gene, scores in gene_scores.items():
  gene_scores[gene]['CAIS'] = CAIS(scores['ADS'], scores['DAGS'], scores['CDAS'], alpha, beta, gamma)

# Remove genes under certain treshold

df = pd.DataFrame(gene_scores).T.reset_index()
df = pd.melt(df, id_vars='index')

df = df[df['variable'] == 'CAIS'].sort_values(by='value', ascending=False)

# Calculate the number of rows to retrieve based on the percentage
num_rows = int(len(df) * int(Parteto_frontiers) / 100)

# Get the values from a specific column (e.g., 'Column1') for the first n percent
remove_nodes = df['index'].iloc[num_rows:]

Variations_network.remove_nodes_from(list(remove_nodes))

## Add extra nodes attributes (Node colors and Edge weitgth)
colors = get_colors(len(groups))
colors

color_dictionary = {}

for group_name, color in zip(groups_names, colors): # This for cycle assing color to group names nodes
  color_dictionary[group_name] = color
  Variations_network.nodes[group_name]['color'] = color

for i in range(2, len(groups) + 1):
  color_dictionary[i] = get_colors(1)[0]

for node in Variations_network.nodes:
  degree = Variations_network.degree[node]
  if degree > len(groups):
    pass
  elif degree > 1 and degree <= len(groups):
    Variations_network.nodes[node]['color'] = color_dictionary[degree]
  else:
    for i,group in enumerate(Group_genes_information.keys()):
      if node in Group_genes_information[group]:
        Variations_network.nodes[node]['color'] = colors[i]
      else:
        pass

for node in Variations_network.nodes:
  if node not in groups_names:
    # Set size to gene nodes
    size_value = df[df['index'] == node]['value'].values[0] * 8000
    Variations_network.nodes[node]['size'] = np.round(size_value, 2)
  else:
    # Set size of group nodes, 1000 by default
    Variations_network.nodes[node]['size'] = 10000.00

# Assigning edges width

for node in Variations_network.nodes:
  for i,group in zip(range(len(Group_Lists)), Group_Lists):
    if node in Score_genes_info.keys():
      if node in Groups_genes_data[i]:
        # Check edge
        if (group, node) in Variations_network.edges:
          # Positions in common
          common_positions = set(Score_genes_info[node].keys()) & set(Groups_genes_data[i][node].keys())
          # Assign edge width
          Variations_network.edges[(group, node)]['width'] = len(common_positions)/len(Score_genes_info[node])
    else:
      pass

# Variation network removal
Variations_network.remove_nodes_from(list(remove_nodes))
save_dir = os.path.join(FunTB_dir, 'Networks_files')

# Saving networks files
nx.write_graphml(Variations_network, os.path.join(save_dir, Network_name) + "_Graph.graphml")
nx.write_gexf(Variations_network, os.path.join(save_dir, Network_name) + "_Graph.gexf")
nx.write_gml(Variations_network, os.path.join(save_dir, Network_name) + "_Graph.gml")