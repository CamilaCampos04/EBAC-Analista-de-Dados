import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output, callback

df = pd.read_csv('ecommerce_estatistica.csv')
lista_generos = df['Gênero'].unique()
options = [{'label':nivel, 'value':nivel} for nivel in lista_generos]

def cria_graficos(selecao_genero):
    filtro_df = df[df['Gênero'].isin(selecao_genero)]

    # Gráfico de Histograma
    fig1 = px.histogram(df, x="Preço", nbins=25)
    fig1.update_layout(
        bargap=0.2,
        title='Distribuição dos Preços',
        xaxis_title='Preço',
        yaxis_title='Quantidade'
    )

    #Gráfico de Dispersão
    fig2 = px.scatter(df, x="Preço", y="Desconto", color="Gênero", size='Material_Freq', hover_data=['Temporada'])
    fig2.update_layout(
        title='Idade vc Salário por Nível de Educação',
        xaxis_title='Idade',
        yaxis_title='Salário'
    )

    # Mapa de calor
    fig3 = px.imshow(df[['Preço', 'Nota', 'Marca_Cod', 'Qtd_Vendidos_Cod']].corr(), text_auto=True)
    fig3.update_layout(
        title='Mapa de calor da correlação entre variáveis'
    )

    #Gráfico de Barras
    fig4 = px.bar(df, x="Qtd_Vendidos", color="Gênero")
    fig4.update_layout(
        title="Vendas por Gênero",
        xaxis_title="Quantidade de Vendas",
        yaxis_title="Quantidade de Clientes"
    )

    #Gráfico de pizza
    fig5 = px.pie(df, names='Gênero', hole=.2)
    fig5.update_layout(title='Porcentagem das Vendas por Gênero')
    fig5.update_traces(textposition='inside', textinfo='percent+label')

    #Gráfico de Violino
    fig6 = px.violin(df, y="Nota", color="Gênero",
                     violinmode='overlay',
                     hover_data=df.columns)
    fig6.update_layout(
        title='Densidade das Notas',
        yaxis_title='Notas'
    )

    fig7 = px.scatter(df, x="Temporada_Cod", y="Qtd_Vendidos_Cod", trendline="ols")
    fig7.update_layout(
        title='Regressão de Quantidade de Vendas por Temporada',
        xaxis_title='Temporada',
        yaxis_title='Quantidade de Vendas'
    )
    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

def cria_app(df):
    #Criar App
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Gráficos do Exercício do Módulo 23'),
        html.Div('''Interatividade entre os Dados'''),
        html.Br(),
        dcc.Checklist(
            id='id_selecao_genero',
            options=options,
            value=[lista_generos[0]],
        ),
        dcc.Graph(id='id_grafico_histograma'),
        dcc.Graph(id='id_grafico_dispersao'),
        dcc.Graph(id='id_grafico_mapa_calor'),
        dcc.Graph(id='id_grafico_barras'),
        dcc.Graph(id='id_grafico_pizza'),
        dcc.Graph(id='id_grafico_violino'),
        dcc.Graph(id='id_grafico_regressao')
    ])
    return app

#Executa App
if __name__ == '__main__':
    app = cria_app(df)

    @app.callback(
        [
            Output('id_grafico_histograma','figure'),
            Output('id_grafico_dispersao', 'figure'),
            Output('id_grafico_mapa_calor', 'figure'),
            Output('id_grafico_barras', 'figure'),
            Output('id_grafico_pizza', 'figure'),
            Output('id_grafico_violino', 'figure'),
            Output('id_grafico_regressao', 'figure'),
        ],
        [Input('id_selecao_genero', 'value')]
    )
    def atualiza_grafico(selecao_genero):
        fig1, fig2, fig3, fig4, fig5, fig6, fig7 = cria_graficos(selecao_genero)
        return [fig1, fig2, fig3, fig4, fig5, fig6, fig7]
    app.run_server(debug=True, port=8050) #Default 8050