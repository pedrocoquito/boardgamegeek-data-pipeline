# boardgamegeek-data-pipeline
Pipeline de dados na nuvem para analisar tendências e padrões nos jogos de tabuleiro do BoardGameGeek

## Objetivo do Trabalho

**Problema a ser Resolvido:**
Explorar as tendências e padrões nos jogos de tabuleiro para identificar quais fatores contribuem para o sucesso e popularidade de um jogo no BoardGameGeek.

**Perguntas de Negócio:**

- Quais são os jogos de tabuleiro mais populares e bem avaliados no BoardGameGeek?
- Existe alguma correlação entre a duração do jogo e sua popularidade ou avaliação?
- Quais designers e publicadoras têm os jogos mais bem avaliados?
- Como a popularidade e as avaliações de jogos mudaram ao longo dos anos?
- Quais categorias de jogos são mais populares e quais têm as melhores avaliações?

## Coleta de Dados

A coleta de dados foi realizada por meio do download direto do arquivo disponível no seguinte link: [BoardGameGeek Dataset](https://ieee-dataport.org/open-access/boardgamegeek-dataset-board-games). Este dataset contém as seguintes informações:

O dataset contém informações sobre diversos jogos de tabuleiro. Abaixo está uma tabela que descreve cada campo disponível:

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

**Evidências da Coleta:**
- O arquivo baixado foi armazenado na pasta `data/raw/` com o nome `bgg_dataset.csv`.
