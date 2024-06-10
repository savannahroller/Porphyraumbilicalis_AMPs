#import needed modules 
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt


#create a file path leading to the tsv file to turn into a data fram 
amPEP_filepath = "/scratch/rollers/week10FINALPROJECT/PorphyraUmbilicalis/PorphUmbamPEPOUT.tsv"

#create a file path leading to the squeaked sequences 
protein_seqs_filepath = "/scratch/rollers/week10FINALPROJECT/PorphyraUmbilicalis/PorphyaUmbilicalisOUT/Pumbilicalis_456_v1.5.protein_primaryTranscriptOnly_squeak.fa"

#create a file handle for the sequences 
protein_seqs_handle = open(protein_seqs_filepath, "r")

#turn the amPEP tsv file into a data frame 
amPEP_dataframe = pd.read_csv(amPEP_filepath, delimiter = "\t")

###create a dictionary of the protein sequences:
#make a dictionary of the test sequence, using the ID as the key, and the sequence as the value 
#make an empty dictionary 
protein_seqs_dict = {}

#Loop through the line in the file
for line in protein_seqs_handle:
    if line.startswith(">"):
        id_temp = line.strip() #Removes "\n"
        id_clean = id_temp.replace(">", "") #Removes ">" by replacing with nothing.
        
        #Add the item to the dictionary
        protein_seqs_dict[id_clean]="" # id_clean is the key, the value is an empty string (for now)
    else:
        seq_line = line.strip() #Removes "\n"
        
        #append this line to the dictionary value, using the key (which is still "id_clean" from the previous line)
        protein_seqs_dict[id_clean] += seq_line

#create a data frame from the dictionary
df_seqs = pd.DataFrame(list(protein_seqs_dict.items()), columns=['SequenceID', 'sequence']) 

#concatenate the two data frames (sequences and amPEP info)
fulldataframe = pd.concat([amPEP_dataframe, df_seqs], axis = 1)

#use a for loop to create a list of the lengths of each sequence in the dictionary from earlier 
sequence_lengths = []
for sequence in protein_seqs_dict:
    sequence_lengths.append(len(protein_seqs_dict[sequence]))

#add the list of sequence lengths to the full data frame 
fulldataframe['SequenceLengths'] = sequence_lengths


#after verifying the sequence id from amPEP and the Squeaked file are the same, we can remove the repeated column of sequence ID's 
fulldataframe = fulldataframe.drop(columns = ["SequenceID"])

#create a tsv file of the data frame 
fulldataframe.to_csv('/scratch/rollers/week10FINALPROJECT/PorphyraUmbilicalis/Porphyraumbilicalis_AMPs/CompleteDataFrame.tsv', sep= '\t' , index=False, header = True)

