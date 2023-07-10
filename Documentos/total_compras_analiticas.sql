--total dinero compras del dia actual [x]
SELECT sum(total_compra)
FROM compras_compra
WHERE fecha_compra >= CURRENT_DATE
  AND fecha_compra < CURRENT_DATE + INTERVAL '1 day'

--total dinero de compras de la semana actual [x]
SELECT sum(total_compra)
FROM compras_compra
WHERE fecha_compra >= date_trunc('week', CURRENT_DATE)
  AND fecha_compra < date_trunc('week', CURRENT_DATE) + INTERVAL '1 week'; 

--total dinero por dia de la semana actual (traducir los dias en el front o en el back) [x]
SELECT TO_CHAR(fecha_compra, 'Day') AS dia_semana, sum(cc.total_compra) AS total_compras
FROM compras_compra cc
WHERE fecha_compra >= date_trunc('week', CURRENT_DATE)
  AND fecha_compra < date_trunc('week', CURRENT_DATE) + INTERVAL '1 week'
GROUP BY dia_semana
ORDER BY dia_semana;

--total dinero compras por cada semana del año actual [x]
SELECT EXTRACT(WEEK FROM fecha_compra) AS semana, sum(cc.total_compra) AS total_compras
FROM compras_compra cc
WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
  AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY semana
ORDER BY semana;

--Cantidad de dinero de compras por cada semana del mes actual [x]
SELECT
  date_part('W', fecha_compra) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS semana_del_mes,
  EXTRACT(MONTH FROM fecha_compra) AS mes,
  sum(cc.total_compra) AS total_compras
FROM compras_compra cc
WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
  AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY mes, semana_del_mes
ORDER BY mes, semana_del_mes;

--Total compras por mes anual
SELECT EXTRACT(MONTH FROM fecha_compra)::INTEGER AS mes, sum(cc.total_compra) AS total_compras
  FROM compras_compra cc
  WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE)
      AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
  GROUP BY mes
  ORDER BY mes

--Cantidad de total dinero por cada semana del mes anterior
SELECT
  date_part('W', fecha_compra) - date_part('W', date_trunc('month', CURRENT_DATE)) + 1 AS semana_del_mes,
  EXTRACT(MONTH FROM fecha_compra) AS mes,
  sum(cc.total_compra) AS total_compras
FROM compras_compra cc
WHERE EXTRACT(MONTH FROM fecha_compra) = EXTRACT(MONTH FROM CURRENT_DATE - INTERVAL '1 month' )
  AND EXTRACT(YEAR FROM fecha_compra) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY mes, semana_del_mes
ORDER BY mes, semana_del_mes;