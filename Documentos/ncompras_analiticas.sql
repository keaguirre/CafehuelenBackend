--Compras por dia de la semana actual (traducir los dias en el front o en el back) [x]
SELECT TO_CHAR(fecha_compra, 'Day') AS dia_semana, COUNT(id_compra) AS total_compras
FROM compras_compra
WHERE fecha_compra >= date_trunc('week', CURRENT_DATE)
  AND fecha_compra < date_trunc('week', CURRENT_DATE) + INTERVAL '1 week'
GROUP BY dia_semana
ORDER BY dia_semana;

--Fecha de inicio y cierre de la semana actual
SELECT
  TO_CHAR(date_trunc('week', CURRENT_DATE), 'DD') || '/' ||
  TO_CHAR(date_trunc('week', CURRENT_DATE), 'MM') AS dia_inicio_semana,
  TO_CHAR(date_trunc('week', CURRENT_DATE) + INTERVAL '6 days', 'DD') || '/' ||
  TO_CHAR(date_trunc('week', CURRENT_DATE) + INTERVAL '6 days', 'MM') AS dia_fin_semana;

--Cantidad de compras al dia de la consulta, del mes actual
SELECT
  COUNT(cc.id_compra) AS total_compras
FROM compras_compra cc
WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
  AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE);

--Cantidad de compras por cada semana del mes actual [x]
SELECT
  date_part('W', fecha_compra) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS semana_del_mes,
  EXTRACT(MONTH FROM fecha_compra) AS mes,
  COUNT(cc.id_compra) AS total_compras
FROM compras_compra cc
WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
  AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY mes, semana_del_mes
ORDER BY mes, semana_del_mes;

-- Cantidad de pedidos por cada semana del mes anterior [x]
SELECT
  date_part('W', fecha_compra) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS semana_del_mes,
  EXTRACT(MONTH FROM fecha_compra) AS mes,
  COUNT(cc.id_compra) AS total_compras
FROM compras_compra cc
WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE - INTERVAL '1 month' )
  AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY mes, semana_del_mes
ORDER BY mes, semana_del_mes;

--Compras por mes del año actual [x]
SELECT EXTRACT(MONTH FROM fecha_compra)::INTEGER AS mes, COUNT(cc.id_compra) AS total_compras
  FROM compras_compra cc
  WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
      AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
  GROUP BY mes
  ORDER BY mes

--Compras por semana del año actual [x]
SELECT EXTRACT(WEEK FROM fecha_compra) AS semana, COUNT(cc.id_compra) AS total_compras
FROM compras_compra cc
WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
  AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY semana
ORDER BY semana;

--Obtiene la semana actual del mes
SELECT date_part('W', CURRENT_DATE) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS semana_actual;



