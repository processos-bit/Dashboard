import app
from app import html, dcc
import pandas as pd
import plotly.graph_objects as go

df =pd.read_excel('ACOMPANHAMENTO DE CRONOGRAMA_ALTO PADRÃO.xlsx')

df[['RESPONSÁVEL','CHECKLIST_CEF','CHECKLIST_HABITE-SE']]=df[['RESPONSÁVEL','CHECKLIST_CEF','CHECKLIST_HABITE-SE']].fillna('-')

df.dtypes

# Agrupar por DISCIPLINA e calcular média das porcentagens
df_grouped = df.groupby('DISCIPLINA')[['%CONCLUÍDA', '%_PREVISTO']].mean().reset_index()

# Ordenar pelo valor de %CONCLUÍDA ou outro critério se desejar
df_grouped = df_grouped.sort_values(by='%CONCLUÍDA', ascending=False)

# Criar o gráfico de barras agrupadas
fig = go.Figure(data=[
    go.Bar(name='%CONCLUÍDA', x=df_grouped['DISCIPLINA'], y=df_grouped['%CONCLUÍDA'], marker_color='rgb(0,102,204)'),
    go.Bar(name='%PREVISTO', x=df_grouped['DISCIPLINA'], y=df_grouped['%_PREVISTO'], marker_color='rgb(255,204,0)')
])

fig.update_layout(
    barmode='group',
    title='Progresso das Disciplinas: Concluído vs Previsto',
    xaxis_title='Disciplina',
    yaxis_title='Percentual',
    xaxis_tickangle=-45,
    height=600
)

# Criar o app Dash
app = app.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Progresso"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)