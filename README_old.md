# **Desafio - Data Engineer**

Este repositório contém um teste prático projetado para avaliar suas habilidades nas seguintes áreas:

* **SQL e Python** : Manipulação de dados, consultas e operações programáticas.
* **Extração, Transformação e Carga de Dados (ETL/ELT)** : Aplicação de conceitos para extrair, transformar e carregar dados de fontes diversas.
* **Análise e Limpeza de Dados** : Identificação de inconsistências, tratamento de dados faltantes e organização para análise.

O teste inclui um conjunto de dados sobre alunos e escolas da cidade de São Paulo no ano de 2023, fornecendo uma oportunidade de aplicar seus conhecimentos em um cenário realista. Estude cuidadosamente cada aspecto dos dados e demonstre sua capacidade de resolver problemas complexos de dados com eficiência.

## **Dados Disponíveis:**

Este teste oferece acesso a um conjunto de dados relacionados à educação pública na cidade de São Paulo. Os dados incluem:

* **Matrículas** : Mais de 10.000 alunos matriculados em escolas públicas municipais.

### Links Úteis:

* **Matrículas 2023** : Informações sobre matrículas nas escolas públicas em São Paulo. [QEdu](https://qedu.org.br/municipio/3550308-sao-paulo)
* **Valores dos Benefícios 2023** : Detalhes sobre os créditos liberados para compra de materiais e uniformes escolares. [Prefeitura de São Paulo](https://capital.sp.gov.br/w/noticia/prefeitura-libera-creditos-para-compra-de-material-e-uniforme-escolar-para-mais-de-28-6-mil-novos-estudantes-matriculados-na-rede-municipal)
* **Concorrência com Escolas Privadas** : Portal com informações sobre o fornecimento de uniformes. [Portal de Uniformes](https://portaldeuniformes.sme.prefeitura.sp.gov.br/)

ℹ️ **Test.md** - Arquivo contendo as questões do teste.
ℹ️ **README.md** - Arquivo com as instruções gerais.

## **Instruções:**

Seu objetivo será desenvolver um pipeline de dados usando Python/SQL para realizar a extração, tratamento e armazenamento das informações provenientes dos links indicados. Após essa etapa, será necessário criar datasets estruturados para análise posterior. O desafio é composto por questões obrigatórias que devem ser resolvidas com foco em precisão e performance.

### **Tarefas Principais** :

* **Extração de Dados** : Utilize técnicas de extração de dados como **Web Scraping** (usando bibliotecas como `BeautifulSoup` ou  **Selenium** ) ou APIs, conforme aplicável, para coletar as informações dos links fornecidos.
* **Tratamento e Armazenamento** : Realize o tratamento adequado dos dados e armazene-os em um banco de dados utilizando uma arquitetura eficiente, como  **Medallion** ,  **Data Lakehouse** , **SSOT (Single Source of Truth)** ou  **OLAP** , conforme sua escolha e justificativa.
* **Transformação de Dados** : Aplique as transformações necessárias para garantir que os dados estejam prontos para análise, incluindo a limpeza e normalização.
* **Criação de Tabelas** : Desenvolva um script Python que faça o upload dos dados em um banco de dados  **SQLite** . Garanta que a tipagem de dados e os nomes de colunas estejam corretamente definidos conforme o arquivo de descrição fornecido.
* **Consultas SQL** : Escreva consultas SQL para responder às perguntas do teste, utilizando os dados armazenados no banco.

### **Arquitetura do Banco de Dados**

Recomenda-se o uso de uma arquitetura avançada para a criação e organização do banco de dados:

* **Medallion Architecture** : Organize os dados em camadas (bronze, silver, gold) para garantir uma transformação incremental e fácil manutenção.
* **Data Lakehouse** : Combine a flexibilidade de um data lake com as estruturas transacionais de um data warehouse para um pipeline de dados unificado.
* **SSOT (Single Source of Truth)** : Crie um repositório centralizado e consistente que sirva como fonte única e confiável de todos os dados.
* **OLAP (Online Analytical Processing)** : Utilize OLAP para otimizar a análise multidimensional de grandes volumes de dados.

### **Objetivos do Teste** :

* [ ] Extração dos dados para um banco SQLite utilizando Web Scraping ou API.
* [ ] Aplicação da arquitetura escolhida (Medallion, Lakehouse, SSOT ou OLAP) no desenvolvimento do banco de dados.
* [ ] Respeitar a tipagem de dados e os nomes das colunas ao criar as tabelas.
* [ ] Desenvolver consultas SQL para responder às perguntas do teste com precisão.
* [ ] Organizar o código em pastas separadas, respeitando a estrutura fornecida.
* [ ] Documentar a solução com comentários e arquivos README, explicando sua estratégia.
* [ ] Realizar os commits em branchs separados seguindo o padrão: nome + sobrenome.

### **Resultado Final** :

Além de concluir o pipeline de extração, tratamento e armazenamento, você deverá criar datasets específicos para responder às perguntas de análise de negócios fornecidas. As soluções finais serão submetidas via solicitação de pull (PR) neste repositório.

Este teste não só avalia suas habilidades em programação aplicada à engenharia de dados, especialmente em extração, transformação e armazenamento de dados. Buscamos identificar a capacidade de estruturar bem um pipeline de dados, com foco em ELT/ETL, além de um código limpo e organizado. Um código bem documentado, seguindo as boas práticas do PEP8, será considerado um diferencial na avaliação.

Além disso, o teste tem como objetivo gerar insights estratégicos sobre o mercado em 2023, com base nos dados extraídos dos links fornecidos. A análise deve focar no tamanho do mercado, valores gerados e a divisão de participação de mercado entre os concorrentes, permitindo à diretoria avaliar se o desempenho realizado pela empresa foi equivalente ao potencial do mercado. A empresa que solicitou este teste é uma das concorrentes, por isso, a criação desses datasets deve fornecer uma visão clara e fundamentada sobre a fatia de mercado de cada competidor, ajudando na tomada de decisões estratégicas.

## **Envio da Solução:**

Para submeter sua solução, siga os passos abaixo:

1. **Fork do Repositório** : Crie um fork deste repositório para a sua conta pessoal.
2. **Criação de Branch** : Crie um branch usando o seguinte padrão de nomeação: `nome-sobrenome`.
3. **Organização do Código** : Certifique-se de que os scripts e o código estejam organizados em pastas adequadas, mantendo a estrutura original fornecida no repositório.
4. **Documentação** : Documente claramente sua solução, explicando cada etapa do processo, desde a extração até a transformação dos dados. Use comentários no código e, se necessário, crie arquivos README adicionais para descrever as decisões e justificativas da sua abordagem.
5. **Commits** : Realize commits frequentes e bem documentados durante o desenvolvimento. Lembre-se de seguir o padrão de nomeação nos commits.
6. **Pull Request (PR)** : Após finalizar sua solução, abra uma **pull request (PR)** com o branch que você criou para este repositório.

### **Checklist de Verificação**

Antes de submeter a PR, confira:

* [ ] Todos os requisitos foram implementados.
* [ ] O código está organizado de maneira clara e documentada.
* [ ] A arquitetura escolhida está aplicada corretamente.
* [ ] As consultas SQL e scripts Python foram devidamente testados.
* [ ] Os commits seguem o padrão nome + sobrenome.
* [ ] O README está claro e explica sua abordagem.

Estamos ansiosos para revisar sua solução e entender sua abordagem para resolver este desafio!
