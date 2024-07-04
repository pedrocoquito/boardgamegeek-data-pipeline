# boardgamegeek-data-pipeline
Pipeline de dados na nuvem para analisar tendências e padrões nos jogos de tabuleiro do BoardGameGeek

## Objetivo do Trabalho

**Problema a ser Resolvido:**
Explorar as tendências e padrões nos jogos de tabuleiro para identificar quais fatores contribuem para o sucesso e popularidade de um jogo no BoardGameGeek.

**Perguntas de Negócio:**

Quais são os jogos de tabuleiro mais populares e bem avaliados no BoardGameGeek?
Existe alguma correlação entre a duração do jogo e sua popularidade ou avaliação?
Quais designers e publicadoras têm os jogos mais bem avaliados?
Como a popularidade e as avaliações de jogos mudaram ao longo dos anos?
Quais categorias de jogos são mais populares e quais têm as melhores avaliações?

## Coleta de Dados

A coleta de dados foi realizada por meio do download direto do arquivo disponível no seguinte link: [BoardGameGeek Dataset](https://ieee-dataport.org/open-access/boardgamegeek-dataset-board-games). Este dataset contém as seguintes informações:

O dataset contém informações sobre diversos jogos de tabuleiro. Abaixo está uma tabela que descreve cada campo disponível no arquivo baixado:

| **Column**                                             | **Description**                                                                                   | **Data Type**     |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------------|
| `Name`                                                 | Name of the board game                                                                           | String           |
| `Year published`                                      | Year when the board game was published                                                           | Integer          |
| `Minimum number of players recommended`              | Minimum number of players recommended for the game                                             | Integer          |
| `Maximum number of players recommended`              | Maximum number of players recommended for the game                                             | Integer          |
| `Playing time`                                        | Duration of the game in minutes                                                                   | Integer          |
| `Recommended minimum age of players`                  | Minimum recommended age for players                                                              | Integer          |
| `Number of users that rated the game`                 | Number of users who have rated the game                                                           | Integer          |
| `Average rating received by the game`                 | Average rating given to the game                                                                 | Float            |
| `BGG rank`                                             | Rank of the game on BoardGameGeek                                                                 | Integer          |
| `Average complexity value of the game`                | Average complexity rating of the game                                                             | Float            |
| `Number of BGG registered owners of the game`         | Number of registered owners on BoardGameGeek                                                     | Integer          |
| `Mechanics used by the game`                           | Mechanics that are used in the game                                                                | String           |
| `Board game domains that the game belongs to`         | Domains or categories that the game belongs to                                                   | String           |

**Evidências da Coleta:**
- O arquivo baixado foi armazenado na pasta `data/raw/` com o nome `BGG_Data_Set.xlsx`.
