-- todas as matrículas de escolas públicas

SELECT Categoria, Total_Matriculas
FROM matriculas 
WHERE tipo_escola = 'Pública';

-- categorias com mais de 100.000 matrículas em escolas privadas
SELECT Categoria, Total_Matriculas
FROM matriculas
WHERE tipo_escola = 'Privada'
AND Total_Matriculas > 100000;

--Listar todas as categorias de escolas públicas, ordenadas pelo número de matrículas (decrescente)
SELECT Categoria, Total_Matriculas
FROM matriculas
WHERE tipo_escola = 'Pública'
ORDER BY Total_Matriculas DESC;


--Soma total de matrículas em escolas públicas e privadas
SELECT tipo_escola, SUM(Total_Matriculas) AS Total_Geral
FROM matriculas
GROUP BY tipo_escola;

-- Selecionar categorias de escolas públicas que possuem mais matrículas do que a média de matrículas em escolas privadas
SELECT Categoria, Total_Matriculas
FROM matriculas
WHERE tipo_escola = 'Pública'
AND Total_Matriculas > (
    SELECT AVG(Total_Matriculas)
    FROM matriculas
    WHERE tipo_escola = 'Privada'
);


--Selecionar todas as categorias com valor acima de 100
SELECT categoria, valor
FROM beneficio
WHERE valor > 100;

--Calcular o valor total de todas as categorias e o valor médio
SELECT 
    SUM(valor) AS valor_total, 
    AVG(valor) AS valor_medio
FROM beneficio;

--Selecionar as categorias cujo valor está acima da média de todos os valores
SELECT categoria, valor
FROM beneficio
WHERE valor > (
    SELECT AVG(valor)
    FROM beneficio
);





