# boardgamegeek-data-pipeline
Cloud data pipeline to analyze trends and patterns in BoardGameGeek board games.

## Objective of the Project

**Problem to be Solved:**
Explore trends and patterns in board games to identify which factors contribute to a game's success and popularity on BoardGameGeek.

**Business Questions:**

1) What are the most popular and highly rated board games on BoardGameGeek?
2) Is there any correlation between game duration and its popularity or rating?
3) Which designers and publishers have the highest-rated games?
4) How have the popularity and ratings of games changed over the years?
5) Which game categories are the most popular and which have the best ratings?

## Data Collection

The data was collected by directly downloading the file available at the following link: [BoardGameGeek Dataset](https://ieee-dataport.org/open-access/boardgamegeek-dataset-board-games). This dataset contains the following information:

The dataset contains information about various board games. Below is a table describing each available field:


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

**Collection Evidence:**
- The file is stored in the `data/raw/` folder with the name `bgg_dataset.csv`.
