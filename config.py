#######################
#                     #
#       Topics        #
#       Here          #
#                     #
# hashtagify.com      #
# hashtags.org        #
#######################

"""



    Oscars - 2018



"""


# DB
client_mongo_uri_oscars2018 = 'mongodb://localhost:27017'
db_name_oscars2018 = 'oscars2018'
db_collection_oscars2018 = 'tweets'


"""



    Facebook and Cambridge Analytica - March 2018



"""


client_mongo_uri_fbCA = 'mongodb://localhost:27017'
db_name_fbCA = 'fbCambridgeanalytica'
db_collection_fbCA2 = 'tweets'

#############################################################################
#                                                                           #
#       Users  who tweetted about Facebook and Cambridge Analytica          #
#                                                                           #
#############################################################################

client_mongo_uri_UsersFbCA = client_mongo_uri_fbCA
db_usersTweetFbCa = db_name_fbCA
db_collection_UsersFbCaTweets = 'users100Tweets'  # tweets from 100 selected users
db_collection_usersFbCaSVO = 'users100SVO'  # these 100 users and SVO attributes

#######################
#                     #
#       Edit          #
#       Settings      #
#                     #
#######################

db_clientTopic = client_mongo_uri_fbCA
db_topic = db_name_fbCA
db_collection_topic = db_collection_fbCA2


db_clientUsers = client_mongo_uri_UsersFbCA
db_users = db_usersTweetFbCa
db_collectionUsersTweets = db_collection_UsersFbCaTweets
db_collectionUsersSVO = db_collection_usersFbCaSVO

####################
# csv graph path   #
####################

ALPHA = 0.3
BETA = 0.6
GAMMA = 0.1

#similarityThreshold = 0.6
similarityThreshold = 0.8

#svoGraphFilename = 'svoGraph06FbCambridge.csv'
svoGraphFilename = 'svoGraph08FbCambridge.csv'

nodes2modularityClassCSV = ''
