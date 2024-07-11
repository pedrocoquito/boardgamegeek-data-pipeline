# boardgamegeek-data-pipeline
Cloud data pipeline to analyze trends and patterns in BoardGameGeek board games.
- The files `cluster.png` and `cluster.JSON` in the `docs/` folder contains information and evidence about the cluster configured in Databricks to the achievement of the project.

## Objective of the Project

**Problem to be Solved:**
Explore trends and patterns in board games to identify which factors contribute to a game's success and popularity on BoardGameGeek from 2001 to 2021.

**Business Questions:**

1. **What are the most popular and highly rated board games on BoardGameGeek?**

2. **Is there a correlation between game duration and its popularity or rating?**

3. **Is there a correlation between the recommended minimum age and a game's popularity?**

4. **What is the complexity of the most popular games?**

5. **How have the popularity and ratings of games changed over the years?**

6. **Which game Mechanics and Domains are the most popular and which have the best ratings?**

7. **Is there a correlation between popularity and a game's rating?**

8. **What is the relationship between the recommended number of players and a game’s popularity?**

## Data Collection

The data was collected by directly downloading the file available at the following link: [BoardGameGeek Dataset](https://www.kaggle.com/datasets/melissamonfared/board-games). This dataset contains the following information:

| **Column**                                             | **Description**                                                                                   | **Data Type**    |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------------|
| `ID`                                                   | Game identification code                                                                          | Integer          |
| `Name`                                                 | Name of the board game                                                                            | String           |
| `Year Published`                                       | Year when the board game was published                                                            | Integer          |
| `Min Players`                                          | Minimum number of players recommended for the game                                                | Integer          |
| `Max Players`                                          | Maximum number of players recommended for the game                                                | Integer          |
| `Play Time`                                            | Duration of the game in minutes                                                                   | Integer          |
| `Min Age`                                              | Minimum recommended age for players                                                               | Integer          |
| `Users Rated`                                          | Number of users who have rated the game                                                           | Integer          |
| `Rating Average`                                       | Average rating given to the game                                                                  | Float            |
| `BGG Rank`                                             | Rank of the game on BoardGameGeek                                                                 | Integer          |
| `Complexity Average`                                   | Average complexity rating of the game                                                             | Float            |
| `Owned Users`                                          | Number of registered owners on BoardGameGeek                                                      | Integer          |
| `Mechanics`                                            | Mechanics that are used in the game                                                               | String           |
| `Domains`                                              | Domains or categories that the game belongs to                                                    | String           |

- The file is stored in the `data/raw/` folder with the name `BGG_Data_Set.csv`.
- The script `processDataset.py`, located in the `scripts/` folder, was used to consider only games published between the years 2001 and 2021. The file `dataset.csv` in the `data/processed/` folder was created with this script.

## Data Model Choice

The star schema was used, where we have a fact table and dimension tables.

### Facts Table (facts)

| Column           | Description                | Data Type           | Data Values           |
|------------------|----------------------------|---------------------|-----------------------|
| `game_id`          | Game identification code (foreign key)             | Integer | 
| `users_rated`      | Number of users who rated the game                 | Integer | minimum: 0, maximum: - (incremental value)
| `rating_average`   | Average user ratings                               | Float | minimum: 0, maximum: 10
| `complexity_average` | Average complexity rating of the game            | Float | minimum: 0, maximum: 5
| `owned_users`      | Number of users who own the game                   | Integer | minimum: 0, maximum: - (incremental value)

### Dimension Tables

#### Games Dimension (games_dimension)

| Column           | Description                | Data Type           | Data Values           |
|------------------|----------------------------|---------------------|-----------------------|
| `game_id`        | Game identification code            |  Integer | 
| `name`           | Name of the game                    | String |
| `year_published` | Year the game was published         | Integer | minimum: 2001, maximum: 2021
| `min_players`    | Minimum number of players           | Integer | minimum: 1, maximum: 999 (For games without min players)
| `max_players`    | Maximum number of players           | Integer | minimum: 1, maximum: 999 (For games without max players)
| `play_time`      | Duration of the game in minutes     | Integer | minimum: 1, maximum: 999 (For games with campaign)
| `min_age`        | Minimum recommended age for players | Integer | minimum: 1, maximum: 21

#### Mechanics Dimension (mechanics_dimension)

| Column           | Description                | Data Type           | Data Values           |
|------------------|----------------------------|---------------------|-----------------------|
| `mechanic_id`    | Mechanic identification code |  Integer | 
| `mechanics`      | Mechanics on the game       | String | Cooperative Game, Deck Construction, Hand Management, Role Playing ...
| `game_id`        | Game identification code   |  Integer | 

#### Domains Dimension (domains_dimension)

| Column           | Description                | Data Type           | Data Values           |
|------------------|----------------------------|---------------------|-----------------------|
| `domain_id`      | Domain identification code |  Integer | 
| `domains`        | Domains of the game         | String | Children's Games, Family Games, Party Games ...
| `game_id`        | Game identification code   |  Integer | 

- **Data Source:** The data was downloaded from the kaggle website.
- **Collection Technique:** Direct download of the CSV file.
- **Transformations:** The data was transformed to fit the Star Schema model, creating fact and dimension tables as described. 
- **Code:** The code for creation is in the file `modelingAndLoading.py` on the `notebooks/` folder and its execution on Databricks can be found at the link [Modeling and Loading Data](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784750/3650020472583597/latest.html) or the screenshot showing the execution on the platform in the folder in the file `modelingAndLoading.png` on the `docs/` folder. 

## Data Analysis and Normalization

### Data Quality Analysis

- The data analysis is used to perform checks and transformations on the dataset to ensure its quality.
- The file `dataAnalysis.py` on the `notebooks/` folder and its execution on Databricks can be found at the link [Data Analysis](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784756/3650020472583597/latest.html) or the screenshot showing the execution on the platform in the folder in the file `dataAnalysis.png` on the `docs/` folder.

The script performed the following steps:

1. Check for null values:
    - No null values were found in the tables

2. Check for duplicate values:
    - No duplicate rows were found in the tables.

3. Perform a statistical analysis on numerical attributes to identify the minimum and maximum values:
    - `games_dimension` table:
        - `year_published` ranges from 2001 to 2021.
        - `min_players` ranges from 0 to 10.
        - `max_players` ranges from 1 to 999.
        - `play_time` ranges from 0 to 2250 minutes.
        - `min_age` ranges from 0 to 25 years.
    - `facts_table`:
        - `users_rated` ranges from 30 to 182214.
        - `rating_average` ranges from 1.1 to 97.0.
        - `complexity_average` ranges from 0.0 to 49.0.
        - `owned_users` ranges from 3 to 155312.

4. Group the mechanics and domains by their names and counts, ordering them by the count in descending order:
    - The most frequent mechanics and domains are listed, indicating the popularity of certain game mechanics and domains among the games.

### Data Normalization

- The file `dataNormalization.py` on the `notebooks/` folder and its execution on Databricks can be found at the link [Data Normalization](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784762/3650020472583597/latest.html) or the screenshot showing the execution on the platform in the folder in the file `dataNormalization.png` on the `docs/` folder.

The script performed the following steps:

1. Remove duplicates: Duplicate entries in the dataset are removed, keeping only the first occurrence.

2. Fix zero or negative values: For specific columns, values of 0 or less are replaced with a specified default value:
   - The columns `min_players`, `max_players`, and `complexity_average`: Set to 1 if the value is 0 or less.

3. Set Maximum Values: For specific columns, values exceeding a certain value are fixed:
   - `max_players` and `play_time`: Limited in 999.
   - `min_age`: Limited in 21.

4. Imput Missing Values: Values in the `min_age` and `play_time` columns are imputed with the median value of the column for games with similar complexity.
 
5. Standardizing floating numbers: Rounded to 2 decimal places and formatted to avoid leading zeros and using `.` as the decimal separator.
 
6. The corrected data has been saved in new tables (`games_dimension_normalized` and `facts_normalized`).

## Problem solving

- The file `questionsQueries.sql` in the `scripts/` folder and its execution on Databricks can be found at the link [Questions Queries](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784768/3650020472583597/latest.html). These are the queries that show the results for the questions in the Business Questions section:

#### 1. What are the most popular and highly rated board games on BoardGameGeek?

- The screenshot showing the execution on the platform is in the file `q1.png` in the `docs/` folder.

The results show that the game Pandemic has significantly more users than the others by a wide margin. However, among all these games, the user ratings are quite close to each other. It can be said that they have similar ratings, although not necessarily the highest ratings on the platform.

#### 2. Is there a correlation between game duration and its popularity or rating?

- The screenshot showing the execution on the platform is in the file `q2.png` in the `docs/` folder.

The results indicate that there is virtually no correlation between game duration and popularity, nor between game duration and game rating, as both correlations are around 0.02.

#### 3. Is there a correlation between the recommended minimum age and a game's popularity?

- The screenshot showing the execution on the platform is in the file `q3.png` in the `docs/` folder.

In this result, it was possible to notice the impact of the recommended minimum age on the number of people who own the game. With a correlation of 0.09, it shows that minimum age can be an important criterion in game sales.

#### 4. What is the complexity of the most popular games?

- The screenshot showing the execution on the platform is in the file `q4.png` in the `docs/` folder.

The results here are not sufficient to determine the importance of a game's difficulty on its sales quantity. It only indicates that a game does not necessarily need to be the simplest level, and more complex games are not the best sellers.

#### 5. How have the popularity and ratings of games changed over the years?

- The screenshot showing the execution on the platform is in the file `q5.png` in the `docs/` folder.

The results show that the period between 2012 and 2018 had the highest number of users owning the games, while games in 2020 and 2021 had higher average ratings.

#### 6. Which game Mechanics and Domains are the most popular and which have the best ratings?

- The screenshot showing the execution on the platform is in the file `q6-Domains.png` and `q6-Mechanics.png` in the `docs/` folder.

The result shows that the "Hand Management" mechanic has the highest number of users and by a considerable margin. While the "Solo" mechanic has the highest scores on the platform.
In terms of domains, "Strategy Games" has a higher number of players than second place ("Family Games") and although the scores are closer, the "Thematic Games" domain took first place.

#### 7. Is there a correlation between popularity and a game's rating?

- The screenshot showing the execution on the platform is in the file `q7.png` in the `docs/` folder.

The query shows that there is no relationship between the number of game owners and the average rating of the games.

#### 8. What is the relationship between the recommended number of players and a game’s popularity?

- The screenshot showing the execution on the platform is in the file `q8.png` in the `docs/` folder.

With this result, it is not possible to determine whether there is any relationship between the minimum age to play and the number of players who own the games.

## Conclusion

With the data obtained it would be possible to determine some guidelines in the development of board games, the most determining being: Hand Management Mechanics and in the Thematic Games domain, in addition the game should not have a high complexity and guarantee a low recommended minimum age. 
