import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "class_0", 1: "class_1", 2: "class_2"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format


def process_data(data):
    processed = [
        {
            'alcohol': d.alcohol,
            'malic_acid': d.malic_acid,
            'ash': d.ash,
            'alcalinity_of_ash': d.alcalinity_of_ash,
            'magnesium': d.magnesium,
            'total_phenols': d.total_phenols,
            'flavanoids': d.flavanoids,
            'nonflavanoid_phenols': d.nonflavanoid_phenols,
            'proanthocyanins': d.proanthocyanins,
            'color_intensity': d.color_intensity,
            'hue': d.hue,
            'od280': d.od280,
            'proline': d.proline,
            'wine_class': d.wine_class
        }
        for d in data
    ]

    return processed
