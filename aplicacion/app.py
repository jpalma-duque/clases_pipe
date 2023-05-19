import streamlit as st
import plotly.graph_objects as go



def main():
    st.title('Resultados interesantisimos')

    boton = st.button('Botoncito')

    st.write(boton)

    option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', option)
    
    # Plot the figure
    fig = plot_data()
    st.plotly_chart(fig)




def plot_data():
    # Sample data
    timestamps = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
    values = [10, 15, 7, 12, 9]

    # Create a trace
    trace = go.Scatter(
        x=timestamps,
        y=values,
        mode='lines',
        name='Time Series Data'
    )

    # Create data array with the trace
    data = [trace]

    # Create layout
    layout = go.Layout(
        title='Time Series Plot',
        xaxis=dict(title='Timestamp'),
        yaxis=dict(title='Values')
    )

    # Create figure
    fig = go.Figure(data=data, layout=layout)

    return fig


main()