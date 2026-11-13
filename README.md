# Microbial Water Monitor

## 1. Descripción del proyecto

**Microbial Water Monitor** es un proyecto de análisis de datos centrado en la calidad microbiológica del agua en España.

A partir de datos recopilados por [Open Water Quality](https://openwaterquality.org/), se exploran dos indicadores microbiológicos —E. coli y Enterococci— para estudiar su frecuencia, distribución geográfica, evolución temporal y presencia en distintos tipos de masas de agua.

El proyecto se ha desarrollado con Python y combina un proceso de análisis exploratorio de datos (EDA) con una aplicación interactiva creada con Streamlit. Forma parte de un proceso de aprendizaje práctico en programación, análisis de datos y visualización.

## 2. Objetivos del proyecto

- Explorar y comprender un conjunto de datos reales.
- Aprender a limpiar, transformar y analizar datos con Python.
- Estudiar la distribución de los indicadores microbiológicos disponibles.
- Examinar los patrones geográficos y temporales de los registros.
- Comparar descriptivamente los valores entre indicadores y tipos de masas de agua.
- Representar los resultados mediante gráficos y mapas interactivos.
- Crear una aplicación con Streamlit que permita consultar los datos mediante filtros.
- Documentar el proceso de trabajo, los resultados y las limitaciones del conjunto de datos.

## 3. Datos utilizados

**Fuente:** [Open Water Quality](https://openwaterquality.org/)

**Ámbito geográfico:** España.

**Periodo solicitado inicialmente:** 1995–2025.

**Periodo realmente cubierto por los registros descargados:** 18/02/2013 – 20/07/2015.

**Número de registros descargados:** 100.000.

**Indicadores microbiológicos analizados:**
- E. coli.
- Enterococci.

**Tipos de masas de agua presentes en la descarga:**

- **Ríos y arroyos (`river/stream`):** cursos naturales de agua en movimiento.
- **Estuarios (`estuary`):** zonas de transición donde el agua dulce de los ríos se mezcla con el agua del mar.
- **Lagos (`lake`):** masas de agua continentales rodeadas de tierra.
- **Otros (`other`):** registros clasificados bajo esta categoría en la fuente original.

Los datos se descargaron en dos formatos:

- **CSV:** utilizado para el análisis y la manipulación de los datos.
- **GeoJSON:** utilizado para trabajar con la información geográfica y crear mapas interactivos.

La aplicación trabaja con el conjunto de datos limpio generado durante el análisis exploratorio, conservando los archivos originales.

**Nota sobre la descarga:** la exportación está limitada a 100.000 registros (`capped: true`). Por tanto, el conjunto descargado puede no contener todas las observaciones disponibles en Open Water Quality. Aunque el periodo solicitado inicialmente fue 1995–2025, los registros obtenidos solo abarcan del 18 de febrero de 2013 al 20 de julio de 2015. El análisis y la aplicación se limitan a los datos efectivamente descargados.

## 4. Preguntas investigadas y principales resultados

### 4.1. ¿Qué indicadores microbiológicos aparecen con mayor frecuencia?

Los dos indicadores tienen una representación prácticamente equilibrada:

- **E. coli:** 50.325 registros (50,33 %).
- **Enterococci:** 49.675 registros (49,68 %).

La diferencia es de 650 registros.

### 4.2. ¿Cómo se distribuyen geográficamente las muestras?

La representación de una muestra aleatoria de 10.000 registros muestra mediciones en la península ibérica y en los archipiélagos. La distribución geográfica no es uniforme: se observan zonas con mayor concentración de muestras y otras con menor presencia de registros.

La aplicación incluye mapas interactivos para explorar la distribución de las mediciones y visualizar los registros según su valor o el tipo de masa de agua.

### 4.3. ¿Cómo han evolucionado los registros a lo largo del tiempo?

La distribución de los registros por año es la siguiente:

- **2013:** 39.746 muestras (39,75 %).
- **2014:** 40.464 muestras (40,46 %).
- **2015:** 19.790 muestras (19,79 %).

La cifra de 2015 debe interpretarse teniendo en cuenta que los datos de ese año solo llegan hasta el 20 de julio. Por tanto, no es directamente comparable con los años completos.

### 4.4. ¿Existen diferencias entre los distintos tipos de masas de agua?

La distribución de los registros por tipo de agua es muy desigual:

- **Otros (`other`):** 87.207 muestras (87,21 %).
- **Ríos y arroyos (`river/stream`):** 4.785 muestras (4,79 %).
- **Estuarios (`estuary`):** 4.633 muestras (4,63 %).
- **Lagos (`lake`):** 3.375 muestras (3,38 %).

Esta diferencia en el tamaño de los grupos debe tenerse en cuenta al comparar sus valores.

### 4.5. ¿Qué diferencias existen entre los niveles registrados de E. coli y Enterococci?

La mediana de los valores registrados es:

- **E. coli:** 6 CFU/100mL.
- **Enterococci:** 5 CFU/100mL.

La diferencia entre ambas medianas es pequeña. La aplicación permite ampliar la comparación mediante estadísticas descriptivas y gráficos.

### 4.6. ¿Qué diferencias se observan entre las regiones de España?

No ha sido posible realizar esta comparación porque la columna `region` contiene únicamente el valor `Spain` en los 100.000 registros. Por tanto, el conjunto de datos no permite distinguir entre regiones españolas.

## 5. Herramientas y tecnologías

- **Python:** lenguaje de programación.
- **Pandas:** manipulación y análisis de datos.
- **NumPy:** operaciones numéricas.
- **Matplotlib y Seaborn:** visualización durante el análisis exploratorio.
- **Plotly:** creación de gráficos y mapas interactivos.
- **Streamlit:** desarrollo de la aplicación interactiva.
- **Jupyter Notebook:** desarrollo del análisis exploratorio.
- **Visual Studio Code:** entorno de desarrollo.
- **Git y GitHub:** control de versiones y alojamiento del código.

## 6. Desarrollo del proyecto

El trabajo se ha organizado en las siguientes fases:

1. **Exploración:** revisión de la estructura, las variables y las características del conjunto de datos.
2. **Limpieza:** revisión de valores ausentes, duplicados, formatos y posibles inconsistencias; preparación de un conjunto de datos limpio.
3. **Análisis exploratorio (EDA):** estudio de frecuencias, distribuciones, estadísticas descriptivas, valores extremos y evolución temporal.
4. **Visualización:** elaboración de gráficos para facilitar la interpretación de los resultados.
5. **Aplicación interactiva:** desarrollo de un dashboard con Streamlit para consultar los datos mediante filtros, gráficos y mapas.
6. **Documentación:** recopilación de los objetivos, el proceso, los resultados y las limitaciones del proyecto.

## 7. Aplicación interactiva

La aplicación **Microbial Water Monitor** está organizada en cuatro pestañas:

### 7.1. Panorama general

Presenta una visión global del conjunto de datos filtrado, con indicadores resumidos y gráficos sobre la distribución de los registros a lo largo del tiempo y por indicador microbiológico.

### 7.2. Análisis comparativo

Permite comparar descriptivamente los valores registrados para E. coli y Enterococci, así como explorar las diferencias entre los cuatro tipos de masas de agua mediante estadísticas y gráficos.

### 7.3. Distribución geográfica

Incluye dos mapas interactivos:

- Un mapa que representa las mediciones según su valor microbiológico.
- Un mapa que distingue los registros según el tipo de masa de agua.

Para facilitar la visualización, los mapas utilizan una muestra de hasta 10.000 registros.

### 7.4. Explorador de datos

Permite consultar los registros filtrados, seleccionar las columnas que se desean visualizar y explorar los resultados según el indicador y el tipo de masa de agua.

### Filtros disponibles

La aplicación dispone de filtros generales para seleccionar:

- Indicador microbiológico.
- Tipo de masa de agua.
- Periodo de fechas.

### Fuente y metodología

La aplicación incluye un apartado específico con el enlace a [Open Water Quality](https://openwaterquality.org/), la información básica de la descarga y una nota sobre sus limitaciones.

## 8. Presentación del proyecto

Junto con el código y la aplicación, se incluye una **presentación explicativa** en la que se exponen el proyecto, sus objetivos, las fases de trabajo, el análisis realizado, los principales resultados y las limitaciones encontradas.

La presentación complementa este README y permite conocer el desarrollo del proyecto de una forma más visual y resumida.

**Presentación:** [Ver presentación del proyecto](PEGAR_AQUÍ_EL_ENLACE_DE_LA_PRESENTACIÓN)

## 9. Limitaciones

- El conjunto descargado contiene registros del periodo comprendido entre el 18/02/2013 y el 20/07/2015, aunque el periodo solicitado inicialmente fue 1995–2025.
- La exportación está limitada a 100.000 registros, por lo que puede no representar la totalidad de los datos disponibles en la fuente.
- La cobertura geográfica y temporal puede ser desigual.
- La categoría `other` concentra la mayoría de los registros, lo que limita la comparabilidad entre tipos de masas de agua.
- La columna `region` solo contiene el valor `Spain`, por lo que no es posible realizar comparaciones entre comunidades autónomas o regiones.
- Los resultados dependen de la calidad, cobertura y metodología de los datos recopilados por las distintas fuentes.
- Las comparaciones de la aplicación son descriptivas; no permiten afirmar por sí solas que existan diferencias estadísticamente significativas.
- La presencia de valores elevados no permite, por sí sola, establecer conclusiones sobre la seguridad sanitaria del agua.

Este proyecto tiene una finalidad educativa y de aprendizaje. No constituye una evaluación sanitaria oficial ni sustituye los análisis ni los controles de las autoridades competentes.

## 10. Publicación en Streamlit Community Cloud

La aplicación **Microbial Water Monitor** está publicada en **Streamlit Community Cloud** y puede consultarse a través del siguiente enlace:

**Aplicación:** [Abrir Microbial Water Monitor](https://microbial-water-monitor.streamlit.app/)

La publicación permite acceder al dashboard interactivo y explorar los datos sin necesidad de instalar Python ni ejecutar el proyecto localmente.

## 11. Autoría

**Erika Pinel Ortega**

- GitHub: [@eripinor](https://github.com/eripinor)
- LinkedIn: [erika-pinel](https://www.linkedin.com/in/erika-pinel/)

## 12. Estado del proyecto

- **Análisis exploratorio (EDA):** terminado.
- **Aplicación Streamlit:** terminada y publicada.
- **Documentación del proyecto:** README completado.
- **Presentación explicativa:** terminada y publicada.

**Proyecto completado.**