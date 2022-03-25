# FUN-TB

FUN-TB is a computational tool developed in Python, which objective is to compare several Mycobacterium Tuberculosis sequences against a reference. This tool contrasts the presence of variations at the gene level to find candidate genes and positions for first or second-line antibiotic resistance signatures.

This tool takes as input three parameters. First, an MTBseq output tab file. Second, a list of samples in txt format that you want to compare and, finally, an integer number representing the number of top genes you want to get from the interest groups. To run this tool, you have to execute the following-like command:

```
FUN-TB.py MTBseq_file.tab samples.txt 1000
```

And as output, we will get a CSV file, an input format for Cytoscape, a network software where we can visualize and edit our resulting genes' relationships. The output format looks like this:

| Source Node  |  Target Node   | Fitness Score | Edge Color | Node Size |
|    :---:     |     :---:      |     :---:     |    :---:   |   :---:   |
|     acee     |   Sensitive    |       7       |    blue    |     5     |
|     rpoc     |   Resistant    |       3       |    green   |     2     |

Once you import the output file in Cytoscape, you can map the different networks' parameters and get the editable format to set some extra settings like node position and distribution, node group based on desired or similar characteristics.  Finally, save your final network image.

At the moment, you can find a [Beta version](https://colab.research.google.com/drive/1bttbnmZs682GMH_eq-J7EWxsvm6UBFRW?usp=sharing) implemented in Google Colab, where we have already pre-loaded some Mexican available sequences data and their corresponding metadata information (Geographical, Age, Sex, Comorbidities, Acquisition year, and Drug Resistance status). You can select from a list of options, the characteristics desired for each of the two groups you can compare.


![alt text](https://github.com/ind-genomics/FUN-TB/blob/main/Images/Network2.png?raw=true)
