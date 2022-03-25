# FUN-TB

FUN-TB is a computational tool developed in Python, which objective is to compare several Mycobacterium Tuberculosis sequences against a reference. This tool contrasts the presence of variations at the gene level to find candidate genes and positions for first or second-line antibiotic resistance signatures.

This tool takes as input three parameters. First, an MTBseq output tab file. Second, a list of samples in txt format that you want to compare and, finally, an integer number that represents the number of top genes you want to compare against the interest groups. This tool can be run by executing the following command:


'''
FUN-TB.py MTBseq_file.tab samples.txt 1000
'''

And as output, we get a CSV file, an input format for Cytoscape a network software where we can visualize and edit our resulting relationships.  The output format looks like this:

