
# ============================================================
# MICROBIAL WATER MONITOR
# Análisis de indicadores microbiológicos en masas de agua
# de España
#
# Para ejecutar la aplicación:
# python -m streamlit run app.py
# ============================================================


# PASO 1. IMPORTACIONES Y CONFIGURACIÓN

import streamlit as st  # Interfaz de la aplicación
import pandas as pd  # Manipulación y análisis de datos
import plotly.express as px  # Gráficos y mapas interactivos


st.set_page_config(
    page_title="Microbial Water Monitor",  # Nombre de la pestaña
    page_icon="💧💩",  # Icono de la aplicación
    layout="wide"  # Utiliza todo el ancho de la página
)

st.title("Microbial Water Monitor")  # Título principal

st.caption(
    "ANÁLISIS DE INDICADORES MICROBIOLÓGICOS EN MASAS DE AGUA DE ESPAÑA"
)  # Subtítulo

st.write(
    "Explora cómo se distribuyen los indicadores E. coli y Enterococci "
    "en las masas de agua de España, cómo evolucionan los registros a lo "
    "largo del tiempo y qué diferencias se observan entre los distintos "
    "tipos de agua."
)  # Introducción de la aplicación

st.divider()  # Separador visual


# Información general del proyecto

col1, col2, col3 = st.columns(3)  # Divide la página en tres columnas

with col1:
    st.markdown("**Indicadores**")
    st.write("E. coli y Enterococci")

with col2:
    st.markdown("**Ámbito geográfico**")
    st.write("España")

with col3:
    st.markdown("**Periodo de estudio**")
    st.write("2013–2015")


# PASO 2. CARGA DE LOS DATOS

@st.cache_data
def cargar_datos():
    aguas = pd.read_csv(
        "datos/datos_limpios.csv"
    )  # Lee el archivo CSV limpio

    aguas["fecha"] = pd.to_datetime(
        aguas["fecha"]
    )  # Convierte la columna fecha a formato datetime

    return aguas  # Devuelve el DataFrame preparado


aguas = cargar_datos()  # Ejecuta la función y guarda los datos


# Diccionario para traducir los tipos de agua

nombres_tipos_agua = {
    "other": "Otros",
    "river/stream": "Ríos y arroyos",
    "lake": "Lagos",
    "estuary": "Estuarios"
}


# PASO 3. FILTROS LATERALES

with st.sidebar:

    st.header("Filtros de consulta")

    # Selección de indicadores
    indicadores = st.multiselect(
        "Selecciona los indicadores",
        options=sorted(aguas["indicador"].unique()),
        default=sorted(aguas["indicador"].unique())
    )

    # Selección de tipos de agua
    tipos_agua = st.multiselect(
        "Selecciona los tipos de agua",
        options=list(nombres_tipos_agua.values()),
        default=list(nombres_tipos_agua.values())
    )

    # Selección del periodo de estudio
    fecha_minima = aguas["fecha"].min().date()
    fecha_maxima = aguas["fecha"].max().date()

    periodo = st.date_input(
        "Selecciona el periodo",
        value=(fecha_minima, fecha_maxima),
        min_value=fecha_minima,
        max_value=fecha_maxima
    )


# PASO 4. FILTRAR LOS DATOS

filtrados = aguas.copy()  # Crea una copia para no modificar los originales

# Convierte las etiquetas españolas a los valores originales del CSV
tipos_seleccionados = [
    tipo
    for tipo, nombre in nombres_tipos_agua.items()
    if nombre in tipos_agua
]

# Aplica el filtro de indicadores
filtrados = filtrados[
    filtrados["indicador"].isin(indicadores)
]

# Aplica el filtro de tipos de agua
filtrados = filtrados[
    filtrados["tipo_agua"].isin(tipos_seleccionados)
]

# Aplica el filtro de fechas cuando hay dos fechas seleccionadas
if isinstance(periodo, (tuple, list)) and len(periodo) == 2:

    fecha_inicio, fecha_fin = periodo

    filtrados = filtrados[
        (filtrados["fecha"].dt.date >= fecha_inicio)
        & (filtrados["fecha"].dt.date <= fecha_fin)
    ]


# PASO 5. COMPROBAR SI QUEDAN DATOS

if filtrados.empty:

    st.warning(
        "No hay registros que coincidan con los filtros seleccionados."
    )

    st.stop()  # Detiene la aplicación si no hay resultados


# PASO 6. MÉTRICAS PRINCIPALES

st.subheader("Resumen de la selección")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Registros analizados",
        f"{len(filtrados):,}".replace(",", ".")
    )  # Cuenta los registros seleccionados

with col2:

    st.metric(
        "Indicadores presentes",
        filtrados["indicador"].nunique()
    )  # Cuenta los indicadores diferentes

with col3:

    # Comprueba cuántas unidades de medida existen
    unidades = filtrados["unidad"].dropna().unique()

    if len(unidades) == 1:

        mediana = filtrados["valor"].median()

        st.metric(
            "Mediana de los valores",
            f"{mediana:.2f}"
        )  # Calcula la mediana si existe una sola unidad

    else:

        st.metric(
            "Unidades de medida",
            len(unidades)
        )  # Evita mezclar valores de distintas unidades

st.caption(
    "Las estadísticas son descriptivas. No constituyen una evaluación "
    "sanitaria de la calidad del agua."
)


# PASO 7. CREAR LAS PESTAÑAS

tab1, tab2, tab3, tab4 = st.tabs([
    "Panorama general",
    "Análisis comparativo",
    "Distribución geográfica",
    "Explorador de datos"
])


# ------------------------------------------------------------
# PESTAÑA 1. PANORAMA GENERAL
# ------------------------------------------------------------

with tab1:

    st.subheader("Evolución de los registros")

    # Agrupa los registros por año y cuenta las observaciones
    registros_anuales = (
        filtrados.assign(año=filtrados["fecha"].dt.year)
        .groupby("año")
        .size()
        .reset_index(name="registros")
    )

    # Muestra el gráfico de evolución anual
    st.bar_chart(
        registros_anuales,
        x="año",
        y="registros"
    )

    # Muestra la tabla anual
    st.dataframe(
        registros_anuales,
        hide_index=True,
        use_container_width=True
    )

    st.divider()

    st.subheader("Distribución de los indicadores")

    # Cuenta los registros de cada indicador
    registros_indicador = (
        filtrados.groupby("indicador")
        .size()
        .reset_index(name="registros")
    )

    # Representa la frecuencia de los indicadores
    st.bar_chart(
        registros_indicador,
        x="indicador",
        y="registros"
    )

    # Muestra la tabla de frecuencias
    st.dataframe(
        registros_indicador,
        hide_index=True,
        use_container_width=True
    )


# ------------------------------------------------------------
# PESTAÑA 2. ANÁLISIS COMPARATIVO
# ------------------------------------------------------------

with tab2:

    st.subheader("Comparación entre E. coli y Enterococci")

    st.write(
        "Comparamos la frecuencia y la distribución de los valores "
        "registrados para ambos indicadores."
    )

    # Cuenta los registros y calcula estadísticas por indicador y unidad
    comparacion_indicadores = (
        filtrados.groupby(["indicador", "unidad"])["valor"]
        .agg(
            registros="count",
            media="mean",
            mediana="median",
            minimo="min",
            maximo="max"
        )
        .reset_index()
        .round(2)
    )

    st.markdown("**Estadísticas por indicador**")

    # Muestra las estadísticas descriptivas
    st.dataframe(
        comparacion_indicadores,
        hide_index=True,
        use_container_width=True
    )

    st.divider()

    st.markdown("**Comparación de las medianas**")

    # Calcula la mediana de cada indicador y unidad
    medianas_indicadores = (
        filtrados.groupby(["indicador", "unidad"])["valor"]
        .median()
        .reset_index(name="mediana")
    )

    # Comprueba si hay una o varias unidades
    if medianas_indicadores["unidad"].nunique() > 1:

        figura_medianas = px.bar(
            medianas_indicadores,
            x="indicador",
            y="mediana",
            color="indicador",
            facet_col="unidad",
            title="Mediana de los valores por indicador y unidad"
        )

    else:

        figura_medianas = px.bar(
            medianas_indicadores,
            x="indicador",
            y="mediana",
            color="indicador",
            title="Mediana de los valores por indicador"
        )

    figura_medianas.update_layout(
        showlegend=False,
        xaxis_title="Indicador",
        yaxis_title="Mediana del valor"
    )

    st.plotly_chart(
        figura_medianas,
        use_container_width=True
    )

    st.divider()

    st.markdown("**Distribución de los valores por indicador**")

    # Comprueba si los indicadores comparten unidad
    if filtrados["unidad"].nunique() > 1:

        figura_box_indicadores = px.box(
            filtrados,
            x="indicador",
            y="valor",
            color="indicador",
            facet_col="unidad",
            points="outliers",
            title="Distribución de los valores por indicador y unidad"
        )

    else:

        figura_box_indicadores = px.box(
            filtrados,
            x="indicador",
            y="valor",
            color="indicador",
            points="outliers",
            title="Distribución de los valores por indicador"
        )

    figura_box_indicadores.update_layout(
        xaxis_title="Indicador",
        yaxis_title="Valor registrado",
        showlegend=False
    )

    st.plotly_chart(
        figura_box_indicadores,
        use_container_width=True
    )

    st.caption(
        "Los diagramas de caja permiten comparar medianas, dispersión "
        "y valores extremos. Los valores extremos no se consideran "
        "automáticamente errores."
    )

    st.divider()

    st.subheader("Comparación entre tipos de agua")

    st.write(
        "Analizamos si los valores registrados presentan diferencias "
        "entre las distintas categorías de masas de agua."
    )

    # Traduce los nombres de los tipos de agua para mostrarlos
    comparacion_agua = filtrados.copy()

    comparacion_agua["tipo_agua_es"] = (
        comparacion_agua["tipo_agua"]
        .map(nombres_tipos_agua)
    )

    # Calcula estadísticas por tipo de agua y unidad
    estadisticas_agua = (
        comparacion_agua.groupby(["tipo_agua_es", "unidad"])["valor"]
        .agg(
            registros="count",
            media="mean",
            mediana="median",
            minimo="min",
            maximo="max"
        )
        .reset_index()
        .round(2)
    )

    st.markdown("**Estadísticas por tipo de agua**")

    st.dataframe(
        estadisticas_agua,
        hide_index=True,
        use_container_width=True
    )

    st.divider()

    st.markdown("**Comparación de las medianas por tipo de agua**")

    # Calcula las medianas por tipo de agua y unidad
    medianas_agua = (
        comparacion_agua.groupby(["tipo_agua_es", "unidad"])["valor"]
        .median()
        .reset_index(name="mediana")
    )

    # Separa el gráfico si hay varias unidades
    if medianas_agua["unidad"].nunique() > 1:

        figura_medianas_agua = px.bar(
            medianas_agua,
            x="tipo_agua_es",
            y="mediana",
            color="tipo_agua_es",
            facet_col="unidad",
            title="Mediana por tipo de agua y unidad"
        )

    else:

        figura_medianas_agua = px.bar(
            medianas_agua,
            x="tipo_agua_es",
            y="mediana",
            color="tipo_agua_es",
            title="Mediana por tipo de agua"
        )

    figura_medianas_agua.update_layout(
        showlegend=False,
        xaxis_title="Tipo de agua",
        yaxis_title="Mediana del valor"
    )

    st.plotly_chart(
        figura_medianas_agua,
        use_container_width=True
    )

    st.divider()

    st.markdown("**Distribución de los valores por tipo de agua**")

    # Compara la distribución de los valores entre categorías
    if comparacion_agua["unidad"].nunique() > 1:

        figura_box_agua = px.box(
            comparacion_agua,
            x="tipo_agua_es",
            y="valor",
            color="tipo_agua_es",
            facet_col="unidad",
            points="outliers",
            title="Distribución de los valores por tipo de agua y unidad"
        )

    else:

        figura_box_agua = px.box(
            comparacion_agua,
            x="tipo_agua_es",
            y="valor",
            color="tipo_agua_es",
            points="outliers",
            title="Distribución de los valores por tipo de agua"
        )

    figura_box_agua.update_layout(
        showlegend=False,
        xaxis_title="Tipo de agua",
        yaxis_title="Valor registrado"
    )

    st.plotly_chart(
        figura_box_agua,
        use_container_width=True
    )

    st.caption(
        "Las comparaciones describen los registros disponibles. "
        "Las diferencias observadas no demuestran por sí solas "
        "diferencias en la calidad sanitaria de las masas de agua."
    )


# ------------------------------------------------------------
# PESTAÑA 3. DISTRIBUCIÓN GEOGRÁFICA
# ------------------------------------------------------------

with tab3:

    st.subheader("Distribución geográfica de los registros")

    st.write(
        "Explora dónde se localizan las muestras, sus valores "
        "microbiológicos y los tipos de masas de agua analizados."
    )

    # Elimina las filas sin coordenadas
    mapa = filtrados.dropna(
        subset=["latitud", "longitud"]
    ).copy()

    if mapa.empty:

        st.warning(
            "No hay coordenadas disponibles para esta selección."
        )

    else:

        # Limita los puntos representados para facilitar la visualización
        if len(mapa) > 10000:

            mapa = mapa.sample(
                n=10000,
                random_state=42
            )

        # ----------------------------------------------------
        # MAPA 1. VALORES MICROBIOLÓGICOS
        # ----------------------------------------------------

        st.subheader("1. Distribución de los valores microbiológicos")

        st.write(
            "Los colores representan el valor registrado en cada muestra."
        )

        # Calcula el percentil 95 para ajustar la escala de color
        limite_color = mapa["valor"].quantile(0.95)

        # Crea el mapa coloreado según los valores
        figura_valores = px.scatter_map(
            mapa,
            lat="latitud",
            lon="longitud",
            color="valor",
            color_continuous_scale="Viridis",
            range_color=(0, limite_color),
            hover_name="indicador",
            hover_data={
                "fecha": True,
                "valor": True,
                "unidad": True,
                "tipo_agua": True,
                "latitud": False,
                "longitud": False
            },
            zoom=4,
            height=600
        )

        # Configura el aspecto del mapa
        figura_valores.update_layout(
            map_style="open-street-map",
            margin={"r": 0, "t": 20, "l": 0, "b": 0}
        )

        # Muestra el primer mapa
        st.plotly_chart(
            figura_valores,
            use_container_width=True
        )

        st.caption(
            f"Se representan {len(mapa):,} muestras. "
            "La escala de color utiliza el percentil 95 como límite superior."
            .replace(",", ".")
        )

        st.divider()

        # ----------------------------------------------------
        # MAPA 2. TIPOS DE AGUA
        # ----------------------------------------------------

        st.subheader("2. Distribución por tipo de agua")

        st.write(
            "Cada color identifica una categoría de masa de agua."
        )

        # Traduce los tipos de agua al español
        mapa["tipo_agua_es"] = (
            mapa["tipo_agua"].map(nombres_tipos_agua)
        )

        # Crea el mapa con colores diferenciados por categoría
        figura_tipos = px.scatter_map(
            mapa,
            lat="latitud",
            lon="longitud",
            color="tipo_agua_es",
            color_discrete_map={
                "Otros": "#4477AA",
                "Ríos y arroyos": "#EE6677",
                "Lagos": "#228833",
                "Estuarios": "#CCBB44"
            },
            hover_name="tipo_agua_es",
            hover_data={
                "fecha": True,
                "indicador": True,
                "valor": True,
                "unidad": True,
                "latitud": False,
                "longitud": False
            },
            zoom=4,
            height=600
        )

        # Configura el aspecto del segundo mapa
        figura_tipos.update_layout(
            map_style="open-street-map",
            margin={"r": 0, "t": 20, "l": 0, "b": 0},
            legend_title_text="Tipo de agua"
        )

        # Muestra el segundo mapa
        st.plotly_chart(
            figura_tipos,
            use_container_width=True
        )

        # Cuenta las muestras representadas por tipo de agua
        resumen_tipos = (
            mapa.groupby("tipo_agua_es")
            .size()
            .reset_index(name="registros")
        )

        st.dataframe(
            resumen_tipos,
            hide_index=True,
            use_container_width=True
        )


# ------------------------------------------------------------
# PESTAÑA 4. EXPLORADOR DE DATOS
# ------------------------------------------------------------

with tab4:

    st.subheader("Explorador de datos")

    st.write(
        "Consulta los registros que cumplen los filtros seleccionados "
        "y explora sus principales características."
    )

    # Permite elegir las columnas que se quieren visualizar
    columnas = st.multiselect(
        "Selecciona las columnas que quieres visualizar",
        options=list(filtrados.columns),
        default=[
            "fecha",
            "indicador",
            "valor",
            "unidad",
            "tipo_agua",
            "latitud",
            "longitud"
        ]
    )

    # Muestra la tabla con las columnas seleccionadas
    if columnas:

        st.dataframe(
            filtrados[columnas],
            hide_index=True,
            use_container_width=True
        )

    else:

        st.warning(
            "Selecciona al menos una columna para mostrar."
        )

    st.divider()

    st.subheader("Tu consulta de agua")

    # Permite seleccionar un indicador
    indicador_consulta = st.selectbox(
        "Selecciona un indicador",
        options=sorted(filtrados["indicador"].unique())
    )

    # Permite seleccionar un tipo de agua
    tipo_consulta = st.selectbox(
        "Selecciona un tipo de agua",
        options=sorted(filtrados["tipo_agua"].unique()),
        format_func=lambda tipo: nombres_tipos_agua.get(tipo, tipo)
    )

    # Filtra los registros según las dos selecciones
    consulta = filtrados[
        (filtrados["indicador"] == indicador_consulta)
        & (filtrados["tipo_agua"] == tipo_consulta)
    ]

    if consulta.empty:

        st.warning(
            "No hay registros para esta combinación."
        )

    else:

        # Calcula las métricas de la consulta
        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Registros encontrados",
                f"{len(consulta):,}".replace(",", ".")
            )

        with col2:

            st.metric(
                "Mediana",
                f"{consulta['valor'].median():.2f}"
            )

        with col3:

            st.metric(
                "Media",
                f"{consulta['valor'].mean():.2f}"
            )

        # Muestra la evolución temporal de la consulta
        st.write("Evolución temporal de la selección")

        evolucion_consulta = (
            consulta.assign(año=consulta["fecha"].dt.year)
            .groupby("año")
            .size()
            .reset_index(name="registros")
        )

        st.bar_chart(
            evolucion_consulta,
            x="año",
            y="registros"
        )

        st.caption(
            "Los resultados son descriptivos y no constituyen "
            "una evaluación sanitaria de la calidad del agua."
        )

# --------------------------------------------------
# 5. FUENTE DE DATOS Y METODOLOGÍA
# --------------------------------------------------

# Línea divisoria para separar este apartado del resto de la aplicación
st.divider()

# Título del apartado
st.subheader("Fuente de datos y metodología")

# Explicación del origen de los datos
st.write(
    "Los datos utilizados en este proyecto proceden de "
    "[Open Water Quality](https://openwaterquality.org/), "
    "una plataforma de recopilación y consulta de datos "
    "sobre calidad del agua."
)

# Información general del conjunto de datos
st.markdown("""
- **Fuente:** [Open Water Quality](https://openwaterquality.org/)
- **Ámbito geográfico:** España.
- **Periodo solicitado:** 1995–2025.
- **Periodo disponible en los datos descargados:** 18/02/2013 – 20/07/2015.
- **Indicadores analizados:** E. coli y Enterococci.
- **Número de registros:** 100.000.
""")

# Advertencia sobre las limitaciones de los datos
st.info(
    "La descarga está limitada a 100.000 registros, por lo que "
    "los datos disponibles no representan necesariamente la "
    "totalidad de las mediciones realizadas durante el periodo "
    "solicitado. Los resultados de esta aplicación tienen carácter "
    "descriptivo y están condicionados por la cobertura y "
    "disponibilidad de los datos originales."
)