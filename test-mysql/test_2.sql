# Generar scripts que realicen las siguientes modificaciones

-------* Colocarle el Precio a los items que lo tengan en NULL, tomando como referencia el valor del costo del item + 10.000 *-------

UPDATE items SET price = 10000 WHERE price = 0

-------* Incrementar el precio de los items en 10% *-------
UPDATE items SET price = (price + (price * 0.1));

-------* Anteponer la palabra Nuevo a los items que comiencen con C en el nombre *-------
UPDATE items SET name = CONCAT("Nuevo", " ", name) WHERE name LIKE 'C%';
