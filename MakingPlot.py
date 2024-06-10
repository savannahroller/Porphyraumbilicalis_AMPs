#import needed modules 
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt

#create a file handle to access the previously made data fram 
dataframe_filepath = '/scratch/rollers/week10FINALPROJECT/PorphyraUmbilicalis/Porphyra-umbilicalis-AMPs/CompleteDataFrame.tsv'

#open the data frame as an actual data frame, instead of tsv
dataframe_dataframe = pd.read_csv(dataframe_filepath, delimiter = "\t")

#create the plot
plt.figure(figsize=(18, 10))
plt.scatter(dataframe_dataframe['SequenceLengths'], dataframe_dataframe['probability_AMP'], c = "navy")

#add titles and labels
plt.title('Porphyra umbilicalis Protein Sequence Length and AMP probability')
plt.xlabel('Protein Sequence Length')
plt.ylabel('Probability of being an AMP')
plt.grid(True)

#export the created plot into a png file 
plt.savefig('scatter_plot.png', dpi=300)

