import os
import config
from collections import defaultdict
import pandas as pd
from itertools import product


def tanimotoSimilarity(v1, v2):
    """
    TS =             (v1 dot v2)
            __________________________________
            ||v1||^2 + ||v2||^2 - (v1 dot v2)}

    :param v1: list, Vector 1
    :param v2: list, Vector 2
    :return: float. Tanimoto similarity between v1 and v2

    """
    sumXX, sumXY, sumYY = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumXX += x * x
        sumYY += y * y
        sumXY += x * y
    return sumXY / (sumXX + sumYY - sumXY)


def svoGraph(collection):
    """

    :param collection: mongo collection with users and SVO attributes
    :return: pandas.DataFrame as adjacence matrix
    """
    usersSVO = defaultdict(float)
    graph = defaultdict(list)

    for el in collection.find():
        usersSVO[el['_id']] = config.ALPHA * el['sentiment'] + config.BETA * el['volume'] + \
                              config.GAMMA * el['objectivity']

    for user1, user2 in product(usersSVO.keys(), usersSVO.keys()):
        if user1 == user2 or tanimotoSimilarity([usersSVO[user1]], [usersSVO[user2]]) < config.similarityThreshold:
            graph[user1].append(0)
        elif tanimotoSimilarity([usersSVO[user1]], [usersSVO[user2]]) >= config.similarityThreshold:
            graph[user1].append(1)

    df = pd.DataFrame(graph, columns=usersSVO.keys(), index=usersSVO.keys())

    return df


def svoGraphCSV(collection, filename):
    """
    :param collection: mongo collection with users and SVO attributes
    :param filename: output filename (csv). it will be stored in ROOT FOLDER
    :return: None
    """
    dataframe = svoGraph(collection)
    directory = os.path.join(os.getcwd(), '../..') # see filename parameter in docs

    if os.path.isdir(directory):
        dataframe.to_csv(os.path.join(os.getcwd(), '../../csv', filename), sep=',')
    else:
        print(directory, " NOT FOUND\n")
        raise Exception


