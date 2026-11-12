# Water Quality Lab

## 1. Descripción del proyecto

**Water Quality Lab** es un proyecto de análisis de datos centrado en la calidad microbiológica del agua en España.

A partir de datos recopilados por [Open Water Quality](https://openwaterquality.org/), se explorarán diferentes indicadores microbiológicos para conocer su distribución, evolución temporal y presencia en distintos tipos de masas de agua.

El proyecto se desarrolla con Python y forma parte de mi aprendizaje práctico en análisis de datos y visualización.

## 2. Objetivos del proyecto

- Explorar y comprender un conjunto de datos reales.
- Aprender a limpiar, transformar y analizar datos con Python.
- Estudiar la distribución de diferentes indicadores microbiológicos.
- Identificar patrones geográficos y temporales.
- Comparar los resultados entre indicadores y tipos de masas de agua.
- Representar los resultados mediante gráficos y mapas interactivos.
- Crear un dashboard con Streamlit para consultar los datos de forma sencilla.
- Publicarlo en Streamlit Cloud Community.

## 3. Datos utilizados

**Fuente:** [Open Water Quality](https://openwaterquality.org/)

**Ámbito geográfico:** España.

**Periodo disponible:** 18/02/2013 – 20/07/2015.

**Número de registros:** 100.000.

**Indicadores microbiológicos:**
- E. coli.
- Enterococci.

**Tipos de masas de agua presentes en la descarga:**

- **Ríos y arroyos (river/stream):** cursos naturales de agua en movimiento.
- **Estuarios (estuary):** zonas de transición donde el agua dulce de los ríos se mezcla con el agua del mar.
- **Lagos (lake):** masas de agua continentales rodeadas de tierra.
- **Otros (other):** registros clasificados bajo esta categoría en la fuente original.

Los datos se han descargado en dos formatos:

- **CSV:** para el análisis y la manipulación de los datos.
- **GeoJSON:** para trabajar con la información geográfica y crear mapas interactivos.

**Nota sobre los datos:** la exportación está limitada a 100.000 registros (`capped: true`). Por tanto, el conjunto descargado puede no contener todas las observaciones disponibles en Open Water Quality. El análisis se realizará exclusivamente sobre los registros incluidos en los archivos descargados.

## 4. Preguntas que se han investigado

**1. ¿Qué indicadores microbiológicos aparecen con mayor frecuencia?**

Los dos indicadores tienen una representación prácticamente equilibrada. E. coli cuenta con 50.325 registros (50,33 %), mientras que Enterococci tiene 49.675 (49,68 %). La diferencia es de solo 650 muestras.

**2. ¿Cómo se distribuyen geográficamente las muestras?**

La representación de una muestra aleatoria de 10.000 registros muestra que existen mediciones en la península ibérica y en los archipiélagos. Sin embargo, la distribución geográfica no es uniforme: se observan zonas con mayor concentración de muestras y otras con menor presencia de registros.

**3. ¿Cómo han evolucionado los registros a lo largo del tiempo?**

En 2013 se registraron 39.746 muestras (39,75 %), y en 2014, 40.464 (40,46 %). En 2015 la cifra desciende a 19.790 (19,79 %). Esta diferencia debe interpretarse teniendo en cuenta que los datos de 2015 solo llegan hasta el 20 de julio.

**4. ¿Existen diferencias entre los distintos tipos de masas de agua?**

La categoría `other` concentra 87.207 muestras (87,21 %). Las demás categorías tienen una representación mucho menor: `river/stream` cuenta con 4.785 (4,79 %), `estuary` con 4.633 (4,63 %) y `lake` con 3.375 (3,38 %). Esta distribución desigual debe tenerse en cuenta al comparar los grupos.

**5. ¿Qué diferencias existen entre los niveles registrados de E. coli y Enterococci?**

La mediana de E. coli es de 6 CFU/100mL, mientras que la de Enterococci es de 5 CFU/100mL. La diferencia es pequeña, por lo que los valores centrales de ambos indicadores son similares.

**6. ¿Qué diferencias se observan entre las regiones de España en los resultados de los análisis microbiológicos?**

No ha sido posible realizar esta comparación porque la columna `region` contiene únicamente el valor Spain en los 100.000 registros. Por tanto, el conjunto de datos no permite distinguir entre regiones españolas.

## 5. Herramientas

- **Python:** lenguaje de programación.
- **Pandas:** manipulación y análisis de datos.
- **NumPy:** operaciones numéricas.
- **Matplotlib y Seaborn:** visualización de datos.
- **Streamlit:** desarrollo de un dashboard interactivo.
- **Git y GitHub:** control de versiones y publicación del proyecto.

## 6. Desarrollo del proyecto

El proyecto se organizará en las siguientes fases:

1. **Exploración:** conocer la estructura, las variables y las características del conjunto de datos.
2. **Limpieza:** revisar valores ausentes, duplicados, formatos y posibles inconsistencias.
3. **Análisis:** estudiar frecuencias, distribuciones, estadísticas y evolución temporal.
4. **Visualización:** crear gráficos que ayuden a interpretar los resultados.
5. **Dashboard:** desarrollar una aplicación interactiva con Streamlit.
6. **Mapa:** representar geográficamente las muestras disponibles y permitir su consulta mediante filtros.

## 7. Dashboard interactivo

La aplicación permitirá explorar los resultados mediante gráficos, filtros y un mapa de las muestras.

Además, incluirá una sección llamada **«Tu consulta de laboratorio»**, en la que el usuario podrá seleccionar:

- Un indicador microbiológico.
- Un tipo de masa de agua.
- Una región geográfica.

A partir de esa selección, se mostrarán los registros correspondientes, incluyendo el número de muestras, sus valores, su evolución temporal y su distribución geográfica.

## 8. Limitaciones

- El conjunto de datos descargado contiene registros correspondientes al periodo comprendido entre 2013 y 2015.
- La exportación está limitada a 100.000 registros, por lo que puede no representar la totalidad de los datos disponibles en la fuente.
- La cobertura geográfica y temporal puede ser desigual.
- La distribución de los registros entre indicadores y tipos de masas de agua puede limitar algunas comparaciones.
- Los resultados dependen de la calidad y de los métodos utilizados por las distintas fuentes.
- La presencia de valores elevados no permite, por sí sola, establecer conclusiones sobre la seguridad sanitaria del agua.
- Este proyecto tiene una finalidad educativa y de aprendizaje. No constituye una evaluación sanitaria oficial ni sustituye los controles de las autoridades competentes.

## 9. Autor

**Erika Pinel Ortega** 👽

- GitHub: [@eripinor](https://github.com/eripinor)
- LinkedIn: [erika-pinel](https://www.linkedin.com/in/erika-pinel/)

## 10. Estado del proyecto

⚠️PROYECTO EN DESARROLLO⚠️
1. EDA terminado.
2. Aplicación de Streamlit en proceso.