from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkDataFrameExample") \
    .config("spark.hadoop.security.authentication", "simple") \
    .config("spark.hadoop.security.authorization", "false") \
    .config("spark.sql.warehouse.dir", "file:///C:/tmp") \
    .getOrCreate()
