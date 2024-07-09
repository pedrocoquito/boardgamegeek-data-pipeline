from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import count, when, isnull, min, max, col, round, lit, row_number # type: ignore
from pyspark.sql.window import Window # type: ignore
from pyspark.sql.types import FloatType # type: ignore

# Spark session starter
spark = SparkSession.builder.appName("Data Normalization").getOrCreate()

# Load data
df_games = spark.table('games_dimension')
df_facts = spark.table('facts')

# Step 1: Remove duplicate items
df_games = df_games.dropDuplicates()
df_facts = df_facts.dropDuplicates()

# Step 2: Apply default values for columns with 0 or less
df_games = df_games.withColumn('min_players', when(col('min_players') <= 0, 1).otherwise(col('min_players')))
df_games = df_games.withColumn('max_players', when(col('max_players') <= 0, 1).otherwise(col('max_players')))
df_facts = df_facts.withColumn('complexity_average', when(col('complexity_average') <= 0, 1).otherwise(col('complexity_average')))

# Step 3: Apply maximum limits for specific columns
df_games = df_games.withColumn('max_players', when(col('max_players') > 999, 999).otherwise(col('max_players')))
df_games = df_games.withColumn('play_time', when(col('play_time') > 999, 999).otherwise(col('play_time')))
df_games = df_games.withColumn('min_age', when(col('min_age') > 21, 21).otherwise(col('min_age')))

# Step 4: Apply median value for min_age and play_time when 0
def apply_median_for_zero_values(df, column, ref_column):
    if ref_column not in df.columns:
        return df
    windowSpec = Window.orderBy(col(ref_column))
    df_with_row_number = df.withColumn("row_num", row_number().over(windowSpec))
    
    median_windowSpec = Window.partitionBy().orderBy(col(ref_column))
    median_col = df_with_row_number.select(col(ref_column)).withColumn("row_num", row_number().over(median_windowSpec)).filter("row_num <= 20 or row_num >= 20")
    median_value = median_col.approxQuantile(ref_column, [0.5], 0.25)[0]
    
    return df.withColumn(column, when(col(column) == 0, lit(median_value)).otherwise(col(column)))

df_games = apply_median_for_zero_values(df_games, 'min_age', 'min_players')
df_games = apply_median_for_zero_values(df_games, 'play_time', 'min_players')

# Step 5: Standardize float values
df_facts = df_facts.withColumn('rating_average', round(col('rating_average'), 2).cast(FloatType()))
df_facts = df_facts.withColumn('complexity_average', round(col('complexity_average'), 2).cast(FloatType()))

# Save the normalized tables
df_games.write.mode("overwrite").saveAsTable("games_dimension_normalized")
df_facts.write.mode("overwrite").saveAsTable("facts_normalized")
