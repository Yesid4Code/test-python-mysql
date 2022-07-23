# Generar scripts que realicen las siguientes consultas

-------* Consultar los items que pertenezcan a la compañia (utilizando INNER JOIN) con ID #3 *-------

SELECT * FROM items INNER JOIN companies ON items.companyId = companies.id WHERE companies.id = 3;

-------* Mostrar los últimos 10 items *-------
SELECT * FROM items ORDER BY id DESC LIMIT 10;

-------* Mostrar los items que en el nombre terminen con la letra A *-------
SELECT * FROM items ORDER BY id DESC LIMIT 10;

-------* Mostrar los items que tengan relacionado el color Rojo *-------
SELECT * FROM items INNER JOIN colors ON items.colorid = colors.id WHERE colors.name = "ROJO";
