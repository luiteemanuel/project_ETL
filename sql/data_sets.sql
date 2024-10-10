-- categorias com maior número de matrículas por tipo de escola
CREATE TABLE top_categorias_por_tipo_escola (
    Categoria TEXT,
    tipo_escola TEXT,
    Total_Matriculas INTEGER
);
INSERT INTO top_categorias_por_tipo_escola (Categoria, tipo_escola, Total_Matriculas)

WITH Ranked_Categorias AS (
    SELECT 
        Categoria, 
        tipo_escola, 
        Total_Matriculas,
        ROW_NUMBER() OVER (PARTITION BY tipo_escola ORDER BY Total_Matriculas DESC) AS ranking
    FROM matriculas
)
SELECT 
    Categoria, 
    tipo_escola, 
    Total_Matriculas
FROM Ranked_Categorias
WHERE ranking <= 3;



-- Distribuição de matrículas por categoria e escola, com percentuais
CREATE TABLE percentual_matriculas (
    Categoria TEXT,
    tipo_escola TEXT,
    Total_Matriculas INTEGER,
    percentual REAL
);

INSERT INTO percentual_matriculas (Categoria, tipo_escola, Total_Matriculas, percentual)
WITH Total_Geral AS (
    SELECT SUM(Total_Matriculas) AS total_geral
    FROM matriculas
)
SELECT 
    Categoria, 
    tipo_escola, 
    Total_Matriculas,
    ROUND((Total_Matriculas / (SELECT total_geral FROM Total_Geral)) * 100, 2) AS percentual
FROM matriculas;

