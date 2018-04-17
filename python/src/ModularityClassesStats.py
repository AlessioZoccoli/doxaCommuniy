from python.modularity.ModularityClassesAnalysis import modularityClassesAverageMetrics
from pymongo import MongoClient
from pprint import pprint
import config, os
import pandas as pd


def modularityClasses2attributes(path2file):
    client = MongoClient(config.db_clientUsers)
    collection = client[config.db_users][config.db_collectionUsersSVO]

    #path2file = os.path.join(os.getcwd(), '../../gephiFbCambridge/similarity08/fbCambridge_sim08_res098_classes.csv')
    df = pd.read_csv(path2file)
    users2modClass = dict(zip(df['Id'].values, df['modularity_class'].values))

    classesAVGvalues = modularityClassesAverageMetrics(collection=collection, user2modularity=users2modClass)
    return classesAVGvalues


#pprint(modularityClasses2attributes())