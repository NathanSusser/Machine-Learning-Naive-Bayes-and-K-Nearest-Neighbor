import numpy as np
import pandas as pd
import heapq

def classify_nb(training_filename, testing_filename):
  training_data = pd.read_csv(training_filename, header=None)
  testing_data = pd.read_csv(testing_filename, header=None)
  outcomes = training_data.iloc[:,-1]
  training_yes = training_data[training_data.iloc[:, -1] == "yes"]
  training_no = training_data[training_data.iloc[:, -1] == "no"]
  training_data = training_data.drop(training_data.columns[-1], axis=1)
  ls = []
  means_yes = training_yes.mean()
  means_no = training_no.mean()
  sds_yes = training_yes.std()
  sds_no = training_no.std()
  
  total_samples = len(training_data)
  yes_samples = len(training_yes)
  no_samples = len(training_no)
    
  yes_p = yes_samples / total_samples
  no_p = no_samples / total_samples
  
  for i in range(len(testing_data)): #len(testing_data)
    prob = calc_log(testing_data.iloc[i], means_yes, means_no, sds_yes, sds_no, yes_p, no_p)
    if prob >= 0:
      ls.append("yes")
    else:
      ls.append("no")    
  return ls


def calc_log(testing, mean_yes, mean_no, sds_yes, sds_no, yes_p, no_p):
    log_prob_yes = np.log(yes_p)
    log_prob_no = np.log(no_p)
    for i in range(len(testing)):
        log_prob_yes += np.log(upd(testing[i], mean_yes[i], sds_yes[i]))
        log_prob_no += np.log(upd(testing[i], mean_no[i], sds_no[i]))
    return log_prob_yes - log_prob_no

def upd(x, mean, std):
  return (np.e**(-1*((x-mean)**2)/(2*(std**2))))/(std * np.sqrt(2*np.pi))



# Example usage:
training_filename = "/Users/nsusser/Desktop/COMP3308/Assignment 2/prima.csv"
testing_filename = "/Users/nsusser/Desktop/COMP3308/Assignment 2/testing_prima.csv"
classifications = classify_nb(training_filename, testing_filename)
print(classifications)
