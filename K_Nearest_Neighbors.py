import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def knn(data, test):

    k = 3
    distances = dict()

    for x in range(len(data.x)):

        distances[x] = euclidean_distance(test, df.iloc[[x], [0, 1]])



    sorted_dict = sorted(distances.items(), key=lambda x:x[1])

    classes = []


    for x in range(k):

        classes.append(data.iloc[sorted_dict[x][0]].c)

    counter = dict()


    for x in range(len(classes)):
        if classes[x] not in counter:
            counter.update({classes[x] : 1})
        else:
            counter[classes[x]] += 1

    
    sorted_counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)

    print("The predicted class is " + sorted_counter[0][0])



def euclidean_distance(p1, p2):

    return np.sqrt(((float(p1.x) - float(p2.x)) ** 2) + ((float(p1.y) - float(p2.y)) ** 2))



data = {'x': [1, 2, 4, 3, 3, 5, 5], 'y': [1, 2, 3, 3, 5, 6, 4], 'c':['A', 'A', 'B', 'A', 'B', 'B', 'B']}

df = pd.DataFrame(data)




input1 = input("enter a x value to predict the classification: ")
input2 = input("enter a y value to predict the classification: ")

test_point = pd.DataFrame({'x': [float(input1)], 'y': [float(input2)]})

knn(df, test_point)
