# boardgamegeek-data-pipeline

Cloud data pipeline to analyze trends and patterns on BoardGameGeek website.
- The files `cluster.png` and `cluster.JSON` in the `docs/` folder contain information and evidence about the cluster configured in Databricks for achieving the project.

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

The data was collected by directly downloading the file from this link: [BoardGameGeek Dataset](https://www.kaggle.com/datasets/melissamonfared/board-games). The dataset includes:

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

- The file is stored in the `data/raw/` folder as `BGG_Data_Set.csv`.
- The script `processDataset.py` in the `scripts/` folder was used to filter games published between 2001 and 2021. The resulting file `dataset.csv` is in the `data/processed/` folder.

## Data Model Choice

The star schema was used, which includes a fact table and dimension tables.

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

- **Data Source:** Downloaded from Kaggle.
- **Collection Technique:** Direct CSV download.
- **Transformations:** Data was adjusted to fit the Star Schema model, creating fact and dimension tables. 
- **Code:** The `modelingAndLoading.py` file in the `notebooks/` folder and its execution on Databricks link [Modeling and Loading Data](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784750/3650020472583597/latest.html) or see the `modelingAndLoading.png` screenshot in the `docs/` folder. 

## Data Analysis and Normalization

### Data Quality Analysis

- The file `dataAnalysis.py` in the `notebooks/` folder and its execution on Databricks can be found here: [Data Analysis](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784756/3650020472583597/latest.html) or the screenshot on `dataAnalysis.png` file in the `docs/` folder.

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

- The file `dataNormalization.py` in the `notebooks/` folder and its execution on Databricks can be found at the link [Data Normalization](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784762/3650020472583597/latest.html) or the screenshot showing the execution on the platform in the file `dataNormalization.png` in the `docs/` folder.

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

- Check out the questionsQueries.sql file in the scripts/ folder and its execution on Databricks here: [Questions Queries](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784768/3650020472583597/latest.html). You can also see the `q1.png` through `q8.png` screenshots in the `docs/` folder.

## Results for Business Questions:

#### 1. What are the most popular and highly rated board games on BoardGameGeek?

- Screenshot `q1.png`.
- Pandemic is the most popular with 155312 owners and second place with 112410. User ratings fairly close among the top games (~7.6).

#### 2. Is there a correlation between game duration and its popularity or rating?

- Screenshot `q2.png`.
- Little to no correlation (0.02 result) between game duration and either popularity or rating.

#### 3. Is there a correlation between the recommended minimum age and a game's popularity?

- Screenshot `q3.png`.
- Minimum age has impact on game sales with a correlation of 0.09.

#### 4. What is the complexity of the most popular games?

- Screenshot `q4.png`.
- No strong correlation between a game's complexity and its sales values from 1.19 to 3.24.

#### 5. How have the popularity and ratings of games changed over the years?

- Screenshot `q5.png`.
- Popularity peaked between 2012 (1715345) and 2018 (1623136) with a peak in 2015 with 2198127 owners, while ratings were higher in 2020 (14.0) and 2021 (14.9).

#### 6. Which game Mechanics and Domains are the most popular and which have the best ratings?

- Screenshots `q6-Domains.png` and `q6-Mechanics.png`.
- "Hand Management" with 9163625 users is the most popular mechanic; While "Thematic Games" has the highest ratings with 13.5.

#### 7. Is there a correlation between popularity and a game's rating?

- Screenshot `q7.png`.
- No significant relationship (with 0.02) between the number of owners and game ratings.

#### 8. What is the relationship between the recommended number of players and a game’s popularity?

- Screenshot `q8.png`.
- No clear relationship between the recommended number of players and game popularity, since the minimum and maximum number of players varied a lot.

## Conclusion

The data shows that successful board games often have "Hand Management" mechanics and fit into the "Thematic Games" domain. They also tend to have low complexity and a low recommended minimum age.
