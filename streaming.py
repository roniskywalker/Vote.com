from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Initialize SparkSession
    spark = (SparkSession.builder
             .appName("ElectionAnalysis")
             .master("local[*]")  # Use local Spark execution with all available cores
             .config("spark.jars.packages",
                     "org.apache.spark:spark-sql-kafka-0-10_2.13:3.5.1")  # Spark-Kafka integration
             .config("spark.jars",
                     "/media/ankan/AnkanHazra/Personal/Data projects/Real-Time-Voting-System/postgresql-42.7.3.jar")  # PostgreSQL driver
             .config("spark.sql.adaptive.enabled", "false")  # Disable adaptive query execution
             .getOrCreate())
