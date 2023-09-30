# Projeto1_CDADOS
O Projeto 1 da matéria de Ciência dos Dados cursado na graduação de Engenharia de Computação no [Insper][insper] é um classificador de textos utilizando o Naive Bayes.

### ETAPAS DO PROJETO

1. Coleta dos exemplos
Usando o notebook fornecido como exemplo, baixe a base de dados de reviews de livros da
Amazon

2. Definindo a variável Target
Com base nas mensagens, será necessário criar uma variável Target. A variável Target
representa o que se deseja aprender a partir dos dados. Em um cenário de negócios, a
variável Target viria da necessidade apontada por alguma área cliente da empresa,
entretanto, neste projeto ela deverá ser definida pelo grupo. No caso deste trabalho, a
variável Target poderia ser a classificação dos reviews como ACIONÁVEL ou NÃOACIONÁVEL, por exemplo.

3. Classificando as mensagens na coragem
Agora você deve abrir o arquivo Excel dados_treino.xlsx com as mensagens
capturadas e classificar cada uma conforme a definição utilizada pelo grupo para a variável
Target. Guarde essa classificação na coluna Target (crie essa coluna ao lado da coluna
Mensagem), considerando ao rótulo ou número inteiro para identificar as classes definidas
pelo grupo.
Faça o mesmo no arquivo Excel dados_teste.xlsx que contém as mensagens do Teste.
Um ponto de atenção nesta etapa é evitar que cada membro do grupo classifique as
mensagens com critérios diferentes. Conversem e garantam que o critério que define a
variável Target esteja bem definido entre os membros do grupo. Também é recomendado
que todos os membros do grupo atuem tanto na classificação do treino quanto do teste e
revisem a classificação dos colegas para diminuir a incidência de viés.

4. Montando o classificador Naive-Bayes
Use o arquivo Projeto1 Template.ipynb disponibilizado no Blackboard como template para
construir o projeto 1 conforme demanda abaixo.
Considerando apenas as mensagens classificadas armazenadas no arquivo
dados_treino.xlsx, o objetivo aqui é ensinar o seu classificador quais são as palavras mais
comuns (frequentes) nas mensagens de cada categoria.

5. Verificando a performance
Considerando agora apenas as mensagens classificadas armazenadas no arquivo
dados_teste.xlsx, seu objetivo aqui é testar a qualidade do seu classificador.
Para tanto, você deve extrair as seguintes contagens:
✔Porcentagem de verdadeiros positivos (Ex: mensagens relevantes e que são
classificadas como relevantes)
✔Porcentagem de falsos positivos (Ex: mensagens irrelevantes e que são classificadas
como relevantes)
✔Porcentagem de verdadeiros negativos (Ex: mensagens irrelevantes e que são
classificadas como irrelevantes)
✔Porcentagem de falsos negativos (Ex: mensagens relevantes e que são classificadas
como irrelevantes)
✔Acurácia (mensagens corretamente classificadas, independente da categoria)

6. Qualidade do Classificador a partir de novas separações das notícias entre
Treinamento e Teste
Um importante passo no aprendizado de máquina é trabalhar com uma boa base de dados
para o treinamento e teste do seu classificador. Entretanto, é razoável pensar que a divisão
de dados utilizada no seu Classificador representa uma entre muitas possíveis combinações
em dividir o total de notícias em 300 para treinamento e 200 para teste.
Assim sendo, aqui o objetivo é avaliar como as notícias contidas na base de dados de
treinamento podem interferir numa melhor ou não tão boa classificação das mensagens
contidas na base de teste.
Nesse caso, faça:
✔Junte todas as mensagens do Treinamento e do Teste em único dataframe (vamos
supor que sejam 500) e separe, de forma aleatória, 300 mensagens para ficar na base
de dados treinamento e 200 na base de dados teste. Obs.: Apenas aqui sua dupla
poderá usar alguma biblioteca que possua um comando já pronto que realiza essa
separação na base de dados (procure no google ''split em train e test");
✔Para cada base separada, faça os itens de 4 a 5 descritos no tópico Etapas do
projeto e guarde os percentuais de acertos (= % de positivos verdadeiros + % de
negativos verdadeiros);
✔Repita os dois passos acima 100 vezes.
Construa um histograma com esses percentuais de acertos e discuta o resultado do
histograma refletindo sobre possíveis vantagens ou desvantagens sobre construir um
Classificador considerando uma única vez a divisão da base de dados em treinamento e em
teste. 



## Alunos
- [Enzo Junqueira][enzo]
- [Thomas Rudge][thomas]

[enzo]: https://github.com/enzojunq
[thomas]: https://github.com/thomasrudge
[insper]: https://www.insper.edu.br/
