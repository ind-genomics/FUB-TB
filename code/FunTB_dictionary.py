import pandas as pd
import numpy as np
import os
import sys
import time

# python VariationsDictionary MTBseq_file.csv Metadata_file.csv
url_MTBseqFile = sys.argv[1] # File MTBseq format (.tab)
url_Samples_data = sys.argv[2] # Metadata File (.csv)
dict_name= sys.argv[1][:-4]
save_dir = os.getcwd()
MTBseq_file = pd.read_csv(url_MTBseqFile, sep='\t', skiprows = (1))
Metadata_file = pd.read_csv(url_Samples_data)
ReferencSequence = MTBseq_file['Ref'].values
GeneNames = MTBseq_file['GeneName'].values


# Aminoacid dictionary from three symbol notation to one symbol notation
amino_acid_dict = {'ala':'A', 'arg':'R', 'asn':'N', 'asp':'D', 'cys':'C','glu':'E', 'gln':'Q', 'gly':'G', 'his':'H', 'ile':'I','leu':'L', 'lys':'K', 'met':'M', 'phe':'F', 'pro':'P','ser':'S', 'thr':'T', 'trp':'W', 'tyr':'Y', 'val':'V'}

# Functions
def GetVariationsParameters(variation):
  
  '''Get variation parameters function to identify which symbolic variation is present, the position related and their frequency.

    Parameters:
    variation (str): String that represents the variation present in 

    Returns:
    2-tuple: Returns the position and the traduction of the variations
  '''

  if variation[0] == variation[-1] == '_': # No variation at all
    pass
  elif variation[0] == '_': # '_' From no codification to one codification
    position = variation[1:-3]
    traduction = '_' + variation[1:-3] + amino_acid_dict[variation[-3:]]
    return (position, traduction)
  elif variation[-1] == '_': # From one codificationto no codification
    position = variation[3:-1]
    traduction = amino_acid_dict[variation[:3]] + variation[3:-1] + '_'
    return (position, traduction)
  elif variation[0:3] != variation[-3:]: # From codify an amino acid to codify a different amino acid
    position = variation[3:-3]
    traduction = amino_acid_dict[variation[:3]] + variation[3:-3] + amino_acid_dict[variation[-3:]]
    return (position, traduction)
  else:
    pass

def GetRelevantData(variations, genes=GeneNames):

  '''Eliminate those rows where the variation has no gene name's relationship

    Parameters:
    variations (str or numeric): Data representing the variations
    genes (list): list of gene names from samples that may present some variations

    Returns:
    2-tuple: Returns the position and the translation of the variations
  '''

  # Convert variations to a numpy array to handle different data types
  variations = np.array(variations)

  # Filter out non-string values (e.g., NaN, numeric values)
  indxs = np.where((variations != '-') & (variations != ' ') & pd.notnull(variations) & (variations.astype(str) != 'nan'))

  # Retrieve relevant variations and genes
  variations = variations[indxs]
  genes = GeneNames[indxs]

  return variations, genes

def CreateDictionary(MTBseq_file = MTBseq_file):

  '''Elaborates a variation dictionary, aiming to more efficient look up process to network generation

    Parameters:
    variations (str): String that represents the variation present in 
    genes (list): list of gene names from samples that may present some variations

    Returns:
    dictionary: Returns the position and the traduction of the variations
  '''

  varitations_dictionary = {}

  for sample in MTBseq_file.columns[-len(Metadata_file.index):]:
    sample_name = sample.split('.')[0]
    varitations_dictionary[sample_name] = {}
    mutations, genes = GetRelevantData(MTBseq_file[sample].values)
    for gene,mutation in zip(genes, mutations):
      # Get variation and position of the variation
      variation = mutation.split(' ')[0].lower()
      variation_parameters = GetVariationsParameters(variation)

      if gene != '-' and variation_parameters != None:
        # Add gene within the dictionary
        if gene not in varitations_dictionary[sample_name]:
          varitations_dictionary[sample_name][gene] = {}
          varitations_dictionary[sample_name][gene]['total_variations'] = 1
          varitations_dictionary[sample_name][gene]['variation_positions'] = {}
          varitations_dictionary[sample_name][gene]['symbolic_mutations'] = {}
        
          # Add position within the dictionary
          if variation_parameters[0] not in varitations_dictionary[sample_name][gene]['variation_positions']:
            varitations_dictionary[sample_name][gene]['variation_positions'][variation_parameters[0]] = 1
          else:
            varitations_dictionary[sample_name][gene]['variation_positions'][variation_parameters[0]] += 1

          # Add symbolic variation within the dctionary
          if variation_parameters[1] not in varitations_dictionary[sample_name][gene]['symbolic_mutations']:
            varitations_dictionary[sample_name][gene]['symbolic_mutations'][variation_parameters[1]] = 1
          else:
            varitations_dictionary[sample_name][gene]['symbolic_mutations'][variation_parameters[1]] += 1
          # Add variation within the dictionary
          #print(position, variation)
        else:
          varitations_dictionary[sample_name][gene]['total_variations'] += 1
          # Add position within the dictionary
          if variation_parameters[0] not in varitations_dictionary[sample_name][gene]['variation_positions']:
            varitations_dictionary[sample_name][gene]['variation_positions'][variation_parameters[0]] = 1
          else:
            varitations_dictionary[sample_name][gene]['variation_positions'][variation_parameters[0]] += 1

          # Add symbolic variation within the dctionary
          if variation_parameters[1] not in varitations_dictionary[sample_name][gene]['symbolic_mutations']:
            varitations_dictionary[sample_name][gene]['symbolic_mutations'][variation_parameters[1]] = 1
          else:
            varitations_dictionary[sample_name][gene]['symbolic_mutations'][variation_parameters[1]] += 1

  return varitations_dictionary

def SaveDictionaryFile(Variation_dictionary, dict_name = dict_name, save_dir = save_dir):
  
  ''''Saves into the system the created variation dictionary

    Parameters:
    Variation_dictionary (dict): String that represents the variation present in 
    dict_name (str): String with the name of the saving file
    save_dir (str): String that contains saving direction folder
    Returns:
    dictionary: Returns the position and the traduction of the variations
  '''
  # open file for writing
  with open(dict_name + '_test_file.txt', 'w') as file:
    # write file
    file.write(str(Variation_dictionary))
    # close file
    file.close()
    
# Creating variation dictionary
varitations_dictionary = CreateDictionary(MTBseq_file)
SaveDictionaryFile(varitations_dictionary)