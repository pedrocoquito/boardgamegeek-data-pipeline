from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import count, when, isnull, min, max # type: ignore

# Spark session starter
spark = SparkSession.builder.appName("Data Analysis").getOrCreate()

# Load data
df_games = spark.table('games_dimension')
df_mechanics = spark.table('mechanics_dimension')
df_domains = spark.table('domains_dimension')
df_facts = spark.table('facts')

# Verify null values
df_games.select([count(when(isnull(c), c)).alias(c) for c in df_games.columns]).show()
df_mechanics.select([count(when(isnull(c), c)).alias(c) for c in df_mechanics.columns]).show()
df_domains.select([count(when(isnull(c), c)).alias(c) for c in df_domains.columns]).show()
df_facts.select([count(when(isnull(c), c)).alias(c) for c in df_facts.columns]).show()

# Verify duplicated values
df_games.groupBy(df_games.columns).count().filter("count > 1").show()
df_mechanics.groupBy(df_mechanics.columns).count().filter("count > 1").show()
df_domains.groupBy(df_domains.columns).count().filter("count > 1").show()
df_facts.groupBy(df_facts.columns).count().filter("count > 1").show()

# Verify minimum and maximum values in non-string columns
numerical_columns_games = ['year_published', 'min_players', 'max_players', 'play_time', 'min_age']
numerical_columns_facts = ['users_rated', 'rating_average', 'complexity_average', 'owned_users']

# Min and Max on games_dimension
df_games.select([min(c).alias(f"min_{c}") for c in numerical_columns_games] + [max(c).alias(f"max_{c}") for c in numerical_columns_games]).show()

# Min and Max on facts_table
df_facts.select([min(c).alias(f"min_{c}") for c in numerical_columns_facts] + [max(c).alias(f"max_{c}") for c in numerical_columns_facts]).show()
