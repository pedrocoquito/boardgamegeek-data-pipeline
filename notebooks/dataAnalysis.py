from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import count, when, isnull # type: ignore

# Spark session starter
spark = SparkSession.builder.appName("Data Quality Analysis").getOrCreate()

# Load data
df_games = spark.table('games_dimension')
df_mechanics = spark.table('mechanics_dimension')
df_domains = spark.table('domains_dimension')
df_facts = spark.table('facts_table')

#  Verify null values
df_games.select([count(when(isnull(c), c)).alias(c) for c in df_games.columns]).show()
df_mechanics.select([count(when(isnull(c), c)).alias(c) for c in df_mechanics.columns]).show()
df_domains.select([count(when(isnull(c), c)).alias(c) for c in df_domains.columns]).show()
df_facts.select([count(when(isnull(c), c)).alias(c) for c in df_facts.columns]).show()

# Verify duplicated values
df_games.groupBy(df_games.columns).count().filter("count > 1").show()
df_mechanics.groupBy(df_mechanics.columns).count().filter("count > 1").show()
df_domains.groupBy(df_domains.columns).count().filter("count > 1").show()
df_facts.groupBy(df_facts.columns).count().filter("count > 1").show()

# Statistical analysis of numerical attributes
df_games.describe(['year_published', 'min_players', 'max_players', 'play_time', 'min_age']).show()
df_facts.describe(['users_rated', 'rating_average', 'bgg_rank', 'complexity_average', 'owned_users']).show()

# Mechanic and Domain analysis
df_mechanics.groupBy('mechanic_name').count().orderBy('count', ascending=False).show()
df_domains.groupBy('domain_name').count().orderBy('count', ascending=False).show()
