from itertools import islice

from pyspark import SparkContext
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
import pyspark
from pyspark.sql import SparkSession

if __name__ == '__main__':
    #sc = SparkContext(appName='PDD')
    #data = sc.textFile('hdfs://nodemaster:9000/data.txt')
    #header = data.first()
    #data = data.filter(lambda x: x != header)

    #r = data.map(lambda l: l.split(',')) \
#            .map(lambda l: l + [len(l)])

    #training, testing = data.randomSplit([0.7, 0.3], 17)

    #c2
    spark = SparkSession.builder.appName('PDD2').getOrCreate()
    df = spark.read.csv('hdfs://nodemaster:9000/data.txt', header=True, inferSchema=True)
    df.printSchema()

    import pandas as pd

    pd.DataFrame(df.take(5), columns=df.columns).transpose()



    #print(data.take(10))
    #print(r.take(10))
