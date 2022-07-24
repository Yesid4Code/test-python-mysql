# Generar scripts para las siguientes solicitudes

-------* Eliminar los datos de la tabla colors *-------
Eliminar la referencia de la tabla item a la tabla colors: 'ON DELETE CASCADE'
DELETE FROM colors;

-------* Agregar un campo llamado Description en la tabla items, que permita ser NULL, y que tenga un máximo de 200 caracteres *-------
ALTER TABLE items ADD Description VARCHAR(200);
