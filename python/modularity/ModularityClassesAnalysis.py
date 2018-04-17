from collections import defaultdict
import config
from statistics import mean
from copy import deepcopy
from pprint import pprint


def modularityClassesAverageMetrics(collection, user2modularity):
    """

    :param collection: mongo collection. Users and their Sentiment, objectivity and volume
    :param user2modularity: users to their respective modularity
    :return: dictionary associating each modularity class to its average S, V and O
    """

    metricsAVG = defaultdict(lambda: defaultdict(list))

    alpha = config.ALPHA
    beta = config.BETA
    gamma = config.GAMMA

    for user in collection.find():
        userEntry = metricsAVG[user2modularity[user['_id']]]
        userEntry['sentiment'].append(alpha * user['sentiment'])
        userEntry['volume'].append(beta * user['volume'])
        userEntry['objectivity'].append(gamma * user['objectivity'])

    # average values
    for classMetric in metricsAVG:
        metricsAVG[classMetric]['sentiment'] = mean(metricsAVG[classMetric]['sentiment'])
        metricsAVG[classMetric]['volume'] = mean(metricsAVG[classMetric]['volume'])
        metricsAVG[classMetric]['objectivity'] = mean(metricsAVG[classMetric]['objectivity'])

    return metricsAVG