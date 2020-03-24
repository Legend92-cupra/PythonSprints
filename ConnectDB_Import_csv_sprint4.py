try:
    import pymongo
    from pymongo import MongoClient
    import pandas as pd
    import json
except Exception as e:
    print("Some Modules are missing...")

uri = "mongodb://Eathan:Legend92@eathaninterncluster-2rxbj.mongodb.net/test?retryWrites=true&w=majority"
class MongoDB(object):

    def __init__(self, dBName=None, collectionName=None):

        self.dBName = dBName
        self.collectionName = collectionName

        self.client = MongoClient("localhost", 27017, maxPoolSize=50)

        self.DB = self.client[self.dBName]
        self.collection = self.DB[self.collectionName]

    def InsertData(self, path=None):
        """

        :param path: Path os csv file
        :return: None
        """

        df = pd.read_csv(path)
        data = df.to_dict('records')

        self.collection.insert_many(data, ordered=False)
        print("All the data has been exported to Mongo Db server ...")

if __name__ == "__main__":
    mongodb = MongoDB(dBName='Data_Tracker', collectionName='Chips')
    mongodb.InsertData(path='data_1.csv')

    mongodb1 = MongoDB(dBName='Data_Tracker', collectionName='Cooldrink')
    mongodb1.InsertData(path='data_2.csv')

    mongodb2 = MongoDB(dBName='Data_Tracker', collectionName='Chocolates')
    mongodb2.InsertData(path='data_3.csv')