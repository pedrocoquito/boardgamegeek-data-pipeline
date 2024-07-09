# boardgamegeek-data-pipeline
Cloud data pipeline to analyze trends and patterns in BoardGameGeek board games.

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


## Data Lineage
- **Data Source:** The data was downloaded from the kaggle website.
- **Collection Technique:** Direct download of the CSV file.
- **Transformations:** The data will be transformed to fit the Star Schema model, creating fact and dimension tables as described.


ADD Databrick links: 

[Modeling and Loading Data](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784750/3650020472583597/latest.html)

[Data Analysis](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784756/3650020472583597/latest.html)

[Data Normalization](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784762/3650020472583597/latest.html)

[Questions Queries](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2574631733088421/3142486001784768/3650020472583597/latest.html)
