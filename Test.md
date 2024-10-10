Seu desafio consiste em **extrair dados diretamente** dos links fornecidos no README.md utilizando  **web scraping** ,  **API** , ou outras técnicas à sua escolha. Você pode utilizar ferramentas como  **Selenium** , **requests** ou **BeautifulSoup** para coletar os dados. Contudo, sinta-se à vontade para explorar outras abordagens ou bibliotecas que achar mais eficientes para a extração e processamento dos dados. **Boa sorte!**

### **Questão 1 - ETL (Python)**

O primeiro passo do desafio é **extrair os dados** fornecidos nos links do README.md utilizando  **Python** . Isso pode ser feito através de **web scraping** ou  **API** , a depender da natureza do site ou serviço. Após a extração dos dados:

* Realize o upload desses dados para um banco de dados  **SQLite** .
* Crie um schema chamado  **test_engineer** .
* Crie as tabelas com base nos dados extraídos, mantendo a estrutura, tipagem, e os nomes das colunas de acordo com as fontes originais.

#### Requisitos:

1. **Automatização do Processo de Extração** : Use bibliotecas como **Selenium** para interagir com páginas dinâmicas, **requests** para fazer requisições HTTP simples ou **BeautifulSoup** para parsear o HTML. Sinta-se à vontade para utilizar outras soluções criativas, caso julgue apropriado.
2. **Persistência de Dados** : Garanta que os dados extraídos sejam corretamente armazenados no banco de dados  **SQLite** , respeitando a integridade dos mesmos.
3. **Estrutura do Banco** : As tabelas devem refletir adequadamente os dados extraídos. Atente-se para a correta tipagem dos dados e consistência nos nomes das colunas.

 ***Dica*** : Para gerenciar a criação de tabelas e inserção de dados, você pode utilizar **SQLAlchemy** para facilitar a conexão e manipulação de dados no  **SQLite** .

### **Questão 2 - Estruture os Dados**

Utilizando uma das arquiteturas mencionadas no README.md (como Medallion, SSOT, Lakehouse ou OLAP), você deve estruturar os dados extraídos de forma a garantir uma organização eficiente e escalável.

* Crie as tabelas e suas relações, conforme necessário, para representar adequadamente as informações extraídas.
* Aplique as melhores práticas de modelagem de dados para assegurar que os dados sejam facilmente acessíveis e analisáveis.

### **Questão 3 - Utilize SQL e Python**

Realize uma análise exploratória dos dados, com foco na validação da qualidade das informações nos datasets. Utilize SQL e Python para tratar os dados, implementando técnicas de tratamento que garantam a segurança e a privacidade dos dados sensíveis nessa camada de armazenamento.

#### **Técnicas sugeridas:**

* **Anonimização:** Remova ou substitua dados identificáveis.
* **Normalização:** Ajuste as escalas dos dados para melhorar a comparabilidade.
* **Limpeza:** Elimine duplicatas, corrija erros de digitação e trate valores ausentes.

Use sua criatividade para explorar a base de dados, buscando inconsistências e outras "sujeiras". Além disso, considere a aplicação de bibliotecas como PySpark, pandas, ou Dask para manipulação e análise de grandes volumes de dados.

***Dica:*** Você pode utilizar Jupyter Notebook para compartilhar seu passo a passo e visualizações durante a análise.

### **Questão 4 - Utilize SQL**

O objetivo desta etapa é estruturar os dados na última camada, criando datasets que atendam especificamente às demandas da empresa, conforme descrito no Resultado Final do README.md. Isso pode incluir a implementação de uma arquitetura OLAP, onde cada dataset será projetado para responder a uma necessidade de negócio específica, facilitando a análise e a geração de insights.

Crie consultas SQL que estabeleçam relações significativas entre os dados, gerando mini datasets que forneçam informações relevantes e que sejam facilmente acessíveis para análises futuras. Pense em como cada um desses datasets pode ajudar a responder às perguntas de negócio e contribuir para uma visão estratégica do mercado.

***Dica:*** Use tabelas intermediárias para facilitar a construção dos datasets finais e considere a normalização dos dados para otimizar o desempenho das consultas.

### **Questão 5 - Documentação e Estrutura**

Documente os dados, a estrutura do banco e os passos do processo de ETL. Explique claramente como os dados foram extraídos, transformados e carregados, garantindo que qualquer parte interessada possa entender o fluxo de dados.

**Bônus 1:** Considere a implementação de ferramentas como  **PySpark** , **Apache Airflow** ou **Docker** para otimizar os serviços de extração e transformação. Isso não apenas melhora a eficiência, mas também a escalabilidade do seu pipeline de dados.

**Bônus 2:** Inclua uma explicação sobre como agendar a extração de dados para que ocorra diariamente ou em um período específico. Detalhe como garantir que os dados estejam sempre atualizados e disponíveis para análise, permitindo que sua equipe tome decisões informadas em tempo real.
