from pyspark.sql import sparkSession
spark=sparkSession.builder.appName("local").getOrCreate()
df=spark.read.format("parquet").load()
df.show()