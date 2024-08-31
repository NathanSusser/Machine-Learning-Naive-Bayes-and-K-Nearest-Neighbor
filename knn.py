import pandas as pd 
import numpy as np 


def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def classify_nn(training_filename, testing_filename, k):
    training_data = pd.read_csv(training_filename)
    testing_data = pd.read_csv(testing_filename)
    
    training_features = training_data.iloc[:, :-1].values
    testing_features = testing_data.iloc[:, :-1].values
    training_labels = training_data.iloc[:, -1].values
    
    classifications = []
    for test_point in testing_features:
        print(test_point)
        print(training_features[0])
        distances = [euclidean_distance(test_point, train_point) for train_point in training_features]
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = training_labels[nearest_indices]

        unique_labels, label_counts = np.unique(nearest_labels, return_counts=True)
        majority_label = unique_labels[np.argmax(label_counts)]
        classifications.append(majority_label)
    
    return classifications

# Example usage:
training_filename = "/Users/nsusser/Desktop/COMP3308/Assignment 2/prima.csv"
testing_filename = "/Users/nsusser/Desktop/COMP3308/Assignment 2/testing_prima.csv"
k = 3
classifications = classify_nn(training_filename, testing_filename, k)
print(classifications)


