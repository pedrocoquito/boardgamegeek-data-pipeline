from pyspark.sql.functions import explode, split, monotonically_increasing_id # type: ignore

# Load CSV data
file_location = "/FileStore/tables/BGG_Data_Set-1.csv"
df = spark.read.csv(file_location, header=True, inferSchema=True) # type: ignore

# Rename collumns
df = df.withColumnRenamed('ID', 'id') \
       .withColumnRenamed('Name', 'name') \
       .withColumnRenamed('Year Published', 'year_published') \
       .withColumnRenamed('Min Players', 'min_players') \
       .withColumnRenamed('Max Players', 'max_players') \
       .withColumnRenamed('Play Time', 'play_time') \
       .withColumnRenamed('Min Age', 'min_age') \
       .withColumnRenamed('Users Rated', 'users_rated') \
       .withColumnRenamed('Rating Average', 'rating_average') \
       .withColumnRenamed('BGG Rank', 'bgg_rank') \
       .withColumnRenamed('Complexity Average', 'complexity_average') \
       .withColumnRenamed('Owned Users', 'owned_users') \
       .withColumnRenamed('Mechanics', 'mechanics') \
       .withColumnRenamed('Domains', 'domains')

# Create tables

# games dimension table
df_games = df.select('id', 'name', 'year_published', 'min_players', 'max_players', 'play_time', 'min_age').distinct()
df_games.write.mode('overwrite').saveAsTable('games_dimension')

# mechanics dimension table
from pyspark.sql.functions import explode, split # type: ignore
df_mechanics = df.select('id', explode(split('mechanics', ', ')).alias('mechanic_name')).distinct()
df_mechanics = df_mechanics.withColumn('mechanic_id', monotonically_increasing_id())
df_mechanics.write.mode('overwrite').saveAsTable('mechanics_dimension')

# domains dimension table
df_domains = df.select('id', explode(split('domains', ', ')).alias('domain_name')).distinct()
df_domains = df_domains.withColumn('domain_id', monotonically_increasing_id())
df_domains.write.mode('overwrite').saveAsTable('domains_dimension')

# fact table
df_facts = df.select('id', 'users_rated', 'rating_average', 'bgg_rank', 'complexity_average', 'owned_users')
df_facts.write.mode('overwrite').saveAsTable('facts_table')

# Show created tables
spark.sql("SHOW TABLES").show() # type: ignore
