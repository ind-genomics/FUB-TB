At the moment, you can find a [Beta version](https://colab.research.google.com/drive/1bttbnmZs682GMH_eq-J7EWxsvm6UBFRW?usp=sharing) implemented in Google Colab, where we have already pre-loaded some Mexican available sequences data and their corresponding metadata information (Geographical, Age, Sex, Comorbidities, Acquisition year, and Drug Resistance status). You can select from a list of options, the characteristics desired for each of the two groups you can compare and get a preliminary network image corresponding to the two groups of interest.

To run this beta, you need, first, to execute the code section; this group of cells contains all the necessary functions to load and process the data to generate the final network.

Then, within the FUN-TB section, you have to choose the characteristics for each of the two groups you want to compare. Once you select those features, run both cells.

Finally, you need to set a total of the top genes (Integer number) you want to consider in the network structure, then run the cell of network construction and, that's it, you will have a preliminary image of your network.

<p align="center">
  <img src="https://github.com/ind-genomics/FUN-TB/blob/main/Images/Network2.png?raw=true" />
</p>
