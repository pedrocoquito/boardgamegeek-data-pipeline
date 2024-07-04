# boardgamegeek-data-pipeline
Pipeline de dados na nuvem para analisar tendências e padrões nos jogos de tabuleiro do BoardGameGeek

## Coleta de Dados

A coleta de dados foi realizada por meio do download direto do arquivo disponível no seguinte link: [BoardGameGeek Dataset](https://ieee-dataport.org/open-access/boardgamegeek-dataset-board-games). Este dataset contém as seguintes informações:

Name
Year published
Miniminum number of players recommended
Maximum number of players recommended
Playing time
Recommended minimum age of players
Number of users that rated the game
Average rating received by the game
BGG rank
Average complexity value of the game
Number of BGG registered owners of the game
Mechanics used by the game
Board game domains that the game belongs to

**Evidências da Coleta:**
- O arquivo baixado foi armazenado na pasta `data/raw/` com o nome `BGG_Data_Set.xlsx`.

## Descrição dos Dados do Dataset

O dataset contém informações sobre diversos jogos de tabuleiro. Abaixo está uma tabela que descreve cada campo disponível no arquivo baixado:

| Nome do Campo em Inglês                | Descrição em Português                                                 | Tipo de Dado      |
|----------------------------------------|------------------------------------------------------------------------|-------------------|
| **Name**                               | Nome do jogo                                                             | Texto             |
| **Year published**                     | Ano de publicação do jogo                                                | Ano (Número Inteiro) |
| **Minimum number of players recommended** | Número mínimo de jogadores recomendados                                | Número Inteiro    |
| **Maximum number of players recommended** | Número máximo de jogadores recomendados                                | Número Inteiro    |
| **Playing time**                       | Tempo de jogo em minutos                                                 | Número Inteiro    |
| **Recommended minimum age of players** | Idade mínima recomendada dos jogadores                                  | Número Inteiro    |
| **Number of users that rated the game**| Número de usuários que avaliaram o jogo                                 | Número Inteiro    |
| **Average rating received by the game**| Avaliação média recebida pelo jogo                                      | Número Decimal    |
| **BGG rank**                           | Classificação do jogo no BoardGameGeek                                  | Número Inteiro    |
| **Average complexity value of the game** | Valor médio de complexidade do jogo                                     | Número Decimal    |
| **Number of BGG registered owners of the game** | Número de proprietários registrados no BoardGameGeek                    | Número Inteiro    |
| **Mechanics used by the game**        | Mecânicas usadas pelo jogo                                               | Texto             |
| **Board game domains that the game belongs to** | Domínios dos jogos de tabuleiro aos quais o jogo pertence               | Texto             |

### Exemplo de Dados

Aqui está um exemplo de como os dados podem ser representados:

| Name         | Year published | Minimum number of players recommended | Maximum number of players recommended | Playing time | Recommended minimum age of players | Number of users that rated the game | Average rating received by the game | BGG rank | Average complexity value of the game | Number of BGG registered owners of the game | Mechanics used by the game                                                                                                                                                                        | Board game domains that the game belongs to                             |
|--------------|----------------|---------------------------------------|---------------------------------------|--------------|------------------------------------|-------------------------------------|--------------------------------------|----------|-------------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Gloomhaven    | 2017           | 1                                     | 4                                     | 120          | 14                                 | 42055                               | 8.79                                 | 1        | 3.86                                | 68323                                     | Action Queue, Action Retrieval, Campaign / Battle Card Driven, Card Play Conflict Resolution, Communication Limits, Cooperative Game, Deck Construction, Deck Bag and Pool Building, Grid Movement, Hand Management, Hexagon Grid, Legacy Game, Modular Board, Once-Per-Game Abilities, Scenario / Mission / Campaign Game, Simultaneous Action Selection, Solo / Solitaire Game, Storytelling, Variable Player Powers | Strategy Games, Thematic Games |
