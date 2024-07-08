# boardgamegeek-data-pipeline
Cloud data pipeline to analyze trends and patterns in BoardGameGeek board games.

## Objective of the Project

**Problem to be Solved:**
Explore trends and patterns in board games to identify which factors contribute to a game's success and popularity on BoardGameGeek.

**Business Questions:**

- What are the most popular and highly rated board games on BoardGameGeek?
- Is there any correlation between game duration and its popularity or rating?
- Which designers and publishers have the highest-rated games?
- How have the popularity and ratings of games changed over the years?
- Which game categories are the most popular and which have the best ratings?

## Data Collection

The data was collected by directly downloading the file available at the following link: [BoardGameGeek Dataset](https://ieee-dataport.org/open-access/boardgamegeek-dataset-board-games). This dataset contains the following information:

The dataset contains information about various board games. Below is a table describing each available field:


| **Column**                                             | **Description**                                                                                   | **Data Type**     |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------------|
| `id`                                                   | Game identification code                                                                          | Integer           |
| `name`                                                 | Name of the board game                                                                            | String           |
| `year_published`                                       | Year when the board game was published                                                            | Integer          |
| `minimum_age`                                          | Minimum number of players recommended for the game                                                | Integer          |
| `maximum_players`                                      | Maximum number of players recommended for the game                                                | Integer          |
| `playing_time`                                         | Duration of the game in minutes                                                                   | Integer          |
| `minimum_age`                                          | Minimum recommended age for players                                                               | Integer          |
| `users_rated`                                          | Number of users who have rated the game                                                           | Integer          |
| `rating_average`                                       | Average rating given to the game                                                                  | Float            |
| `bgg_rank`                                             | Rank of the game on BoardGameGeek                                                                 | Integer          |
| `complexity_average`                                   | Average complexity rating of the game                                                             | Float            |
| `owned_users`                                          | Number of registered owners on BoardGameGeek                                                      | Integer          |
| `mechanics`                                            | Mechanics that are used in the game                                                               | String           |
| `domains`                                              | Domains or categories that the game belongs to                                                    | String           |

**Collection Evidence:**
- The file is stored in the `data/raw/` folder with the name `bgg_dataset.csv`.
