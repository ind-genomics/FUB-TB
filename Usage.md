# FunTB: Functional Network of variants in TB genomes pipeline v.1.0.1

**Last updated: Feb 4, 2024**

*`FUN-TB`* is a freely available open-source Python standalone tool designed for analyzing MTBSeq v.1.0 output files. It facilitates the comparison of the presence of Single Nucleotide Polymorphisms (SNPs) among phenotypically diverse sets of Mycobacterium tuberculosis samples through a Phenotypic centred networks structuration, making able to observe which altered genes and based on the node size and edge width in which proportion they are related to each phenotype.

# Usage of FunTB

* [1. Prerequisites](#prerequisites)
* [2. Preparing clinical data table](#predb)
* [3. Running FunTB scripts](#runningfuntb)
* [4. FunTB output](#output)
* [5. After FunTB](#afterfuntb)

<a name="prerequisites"></a>
## 1. Prerequisites

To run FunTB, users need two main files.
- MTBSeq v.1.0.1 output file (tab)
- Clinical data file (csv)

<a name="predb"></a>
## 2. Preparing clinical data table
FunTB requires `Clinical data table` in CSV format file. We recommended to structure it in the following manner:

Samples iDs   | Clinical variable 1 | Clinical variable 2 |
------------- | ------------------- | ------------------- |
Sample iD 1   |     cv1 value 1     |     cv2 value 1     |
Sample iD 2   |     cv1 value 2     |     cv2 value 2     |
Sample iD 3   |     cv1 value 3     |     cv2 value 3     |
   $\.$       |         $\.$        |         $\.$        |
   $\.$       |         $\.$        |         $\.$        |
   $\.$       |         $\.$        |         $\.$        |
Sample iD n   |     cv1 value n     |     cv2 value n     |


<a name="runningfuntb"></a>
## 3. Running FunTB scripts
Once within FunTB directory, where you could see the following content:

#### Directory content
- Seven subdirectories
  - MTBSeq_files
  - Metadata_files (Clinical data tables)
  - Networks_files
  - Pareto_Front_Data
  - Sample_lists_files
  - Pareto_Front_Data
- Six Python scripts
  - FunTB.py (main script tool)
  - FunTB_dictionary.py
  - Sample_Grouping_Creation.py
  - NetworkDataGeneration.py
  - NetworkStructureGeneration.py
  - ParetoFrontExtraction.py

The first script to be executed is the `FunTB_dactionary.py` which takes for input the MTBSeq file. Running the follwing command:

```
python $FunTB_DIR/FunTB_dictionary.py \
  --MTBSeq_file <MTBSeq_file_name> \
  --Clinical_data_file <Clinical_data_file_name> \
  --Dictionary_file_name <Output_file_name>
```

The second script in the pipeline is to execute the `Sample_Grouping_Creation.py` which takes as input a CSV file that contains clinical data separated in columns.

```
python $FunTB_DIR/Sample_Grouping__Creation.py  Clinical_Data.csv \
  --Clinical_data_file <Clinical_data_file_name> \
```

Finally, the third script is to generate series of XML-network format files, 

```
python $FunTB_DIR/FuNTB.py  Clinical_Data.csv \
  --Network_name <Output_file_name> \
  --Variation_dictionary_file <Alteration_dictionary_file> \
  --Percentage_factor_integer <Remaining_genes_factor> \
  --alpha_coefficient <Coefficient_to_pondered_sum> \
  --beta_coefficient <Coefficient_to_pondered_sum> \
  --gamma_coefficient <Coefficient_to_pondered_sum> \
  --Group_list_1 <Samples_Ids_List_TXT_file> \
  --Group_list_1 <Samples_Ids_List_TXT_file> \
   .
   .
   .
  --Group_list_n <Samples_Ids_List_TXT_file>
```
<a name="output"></a>
## 4. FunTB output

Final output will be located in `Networks_files` directory.

- Network_name.graphml
- Network_name.gml
- Network_name.gexf

<a name="afterfuntb"></a>
## 5. After FunTB

The output files are post-processed in Cytoscape, to get a final network visualization like the following one:
