# _Api Mutantes_

## Descripción
El proposito de la aplicacion es verificar si un ADN de Base Nitrogenada corresponde a un Muntante o un Humano. Mediante la API puede guardar los ADN para luego consultar las estadisticas. 

## Caracteristicas

- Verifica si un ADN corresponde a un Mutante o un Humano. 
- Puede realizar un guardado de ADN.
- Segun los ADN recopilados se puede obtener la cantidad de Mutantes o Humanos que se encuentran en la base de datos.

## Rutas

- /mutant/ - Verifica si el DNA ingresado corresponde a un Mutante o un Humano.
- /stats - Obtiene la cantidad de Mutantes, Humanos y ratio de los ADN ingresados en la base de datos.
- /save - Guarda el ADN con BaseNitrogenada en la base de datos.

## Tecnologias

- Python
- Flask 
- ORM SQLAlchemy
- Mysql

## Instrucciones para el despliege
> -------------------------------

