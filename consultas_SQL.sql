--1. Todos los registros ordenados por fecha/hora
SELECT * FROM clima
ORDER BY time ASC;

--2. Temperatura máxima registrada
SELECT MAX(temp_celsius) AS temp_maxima FROM clima;

--3. Temperatura mínima registrada
SELECT MIN(temp_celsius) AS temp_minima FROM clima;

--4. Temperatura promedio general
SELECT AVG(temp_celsius) AS temp_promedio FROM clima;

--5. Temperatura promedio por día
SELECT DATE(time) AS dia, AVG(temp_celsius) AS temp_promedio
FROM clima
GROUP BY DATE(time)
ORDER BY dia;

--6. Temperatura máxima y mínima por día

SELECT DATE(time) AS dia,
       MAX(temp_celsius) AS temp_max,
       MIN(temp_celsius) AS temp_min
FROM clima
GROUP BY DATE(time)
ORDER BY dia;

--7. Registros con temperatura menor a 5 grados
SELECT * FROM clima
WHERE temp_celsius < 5
ORDER BY time;

--8. Conteo de registros por día
SELECT DATE(time) AS dia, COUNT(*) AS cantidad_registros
FROM clima
GROUP BY DATE(time)
ORDER BY dia;

--9. Temperatura promedio por hora del día agrupando por hora para ver patrones diarios
SELECT EXTRACT(HOUR FROM time) AS hora, AVG(temp_celsius) AS temp_promedio
FROM clima
GROUP BY hora
ORDER BY hora;

--10. Registro más reciente de temperatura
SELECT * FROM clima
ORDER BY time DESC
LIMIT 1;