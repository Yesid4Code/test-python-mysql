# Generar scripts para las siguientes solicitudes

-------* Eliminar los datos de la tabla colors *-------
ALTER TABLE items DROP FOREIGN KEY items_ibfk_1;
-- items_lbfk_1 is the CONSTRAINT for the FOREIGN KEY (`colorId`)
DELETE FROM colors;

-------* Agregar un campo llamado Description en la tabla items, que permita ser NULL, y que tenga un máximo de 200 caracteres *-------
ALTER TABLE items ADD Description VARCHAR(200);
