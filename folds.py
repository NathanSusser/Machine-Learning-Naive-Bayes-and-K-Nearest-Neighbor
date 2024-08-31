import pandas as pd
import numpy as np
def ten_folds(data_filename):
    data = pd.read_csv(data_filename)
    training_yes = data[data.iloc[:, -1] == "yes"]
    training_no = data[data.iloc[:, -1] == "no"]
    ten_yes = np.array_split(training_yes, 10)
    ten_no = np.array_split(training_no, 10)
    folds = []
    for yes, no in zip(ten_yes, ten_no):
        folds.append(pd.concat([yes, no], ignore_index=True))
    return folds

def ten_folds_csv(data_filename, fold_filename):
    data = pd.read_csv(data_filename)
    training_yes = data[data.iloc[:, -1] == "yes"]
    training_no = data[data.iloc[:, -1] == "no"]
    ten_yes = np.array_split(training_yes, 10)
    ten_no = np.array_split(training_no, 10)
    folds = []
    for yes, no in zip(ten_yes, ten_no):
        merged_data = pd.concat([yes, no], ignore_index=True)
        folds.append(merged_data)
        
    
    for i in range(10):
        head = f"\nfold{i+1}\n"
        with open(fold_filename, 'a') as file:
            file.write(head)
        folds[i].to_csv(fold_filename, mode='a', header=False, index=False)

dat = "/Users/nsusser/Desktop/COMP3308/Assignment 2/prima.csv"
fol = "/Users/nsusser/Desktop/COMP3308/Assignment 2/prima_folds.csv"
ten_folds_csv(dat, fol)