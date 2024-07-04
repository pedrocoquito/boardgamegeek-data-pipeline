# boardgamegeek-data-pipeline
Pipeline de dados na nuvem para analisar tendências e padrões nos jogos de tabuleiro do BoardGameGeek

## Coleta de Dados

A coleta de dados foi realizada por meio do download direto do arquivo disponível no seguinte link: [BoardGameGeek Dataset](https://ieee-dataport.org/open-access/boardgamegeek-dataset-board-games). Este dataset contém as seguintes informações:

O dataset contém informações sobre diversos jogos de tabuleiro. Abaixo está uma tabela que descreve cada campo disponível no arquivo baixado:

| Nome do Campo em Inglês                | Descrição em Português                                                 | Tipo de Dado      |
|----------------------------------------|------------------------------------------------------------------------|-------------------|
| **Name**                               | Nome do jogo                                                             | string             |
| **Year published**                     | Ano de publicação do jogo                                                | number |
| **Minimum number of players recommended** | Número mínimo de jogadores                                 | number    |
| **Maximum number of players recommended** | Número máximo de jogadores                                 | number    |
| **Playing time**                       | Estimativa do tempo de jogo em minutos                                                 | number   |
| **Recommended minimum age of players** | Idade mínima recomendada dos jogadores                                  | number   |
| **Number of users that rated the game**| Número de usuários que avaliaram o jogo                                 | number   |
| **Average rating received by the game**| Avaliação média recebida pelo jogo                                      | number    |
| **BGG rank**                           | Classificação do jogo no BoardGameGeek                                  | number    |
| **Average complexity value of the game** | Valor médio de complexidade do jogo                                     | number    |
| **Number of BGG registered owners of the game** | Número de proprietários registrados no BoardGameGeek                    | number    |
| **Mechanics used by the game**        | Mecânicas usadas pelo jogo                                               | string             |
| **Board game domains that the game belongs to** | Domínios dos jogos de tabuleiro aos quais o jogo pertence               | string             |

**Evidências da Coleta:**
- O arquivo baixado foi armazenado na pasta `data/raw/` com o nome `BGG_Data_Set.xlsx`.
