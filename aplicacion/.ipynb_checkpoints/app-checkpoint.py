import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    
    st.title('Visualizar resultados API')
    
    df = leer_archivos()

    especies = df.species.unique()
    especie = st.selectbox('Selecciona una especie', ['Todas las especies'] + list(especies), index=1)
    
    mapa, datos = st.tabs(['Mapa', 'Base de datos'])
    
    if especie == 'Todas las especies':
        sub_df = df.copy()
    else:
        sub_df = df.query('species==@especie').copy()
    
    with datos:
        st.write(sub_df)
    
    with mapa:
        fig = graficar_especies(sub_df)
        st.plotly_chart(fig)
    
    
    
def graficar_especies(df):

    fig = px.scatter_mapbox(df, lat="decimalLatitude", lon="decimalLongitude", hover_data=["species"],
                            color="species", zoom=5, height=600, width=800)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(mapbox_center={"lat": -53.0, "lon": -70.0})

    return fig

    
    
@st.cache_data    
def leer_archivos():
    df = pd.read_parquet('aplicacion/datos_app/datos_consolidados_observaciones.parquet')
    return df


main()