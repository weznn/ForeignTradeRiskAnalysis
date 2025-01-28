pip install pandas numpy matplotlib seaborn requests beautifulsoup4 scikit-learn dash plotly

pip install dash plotly dash-bootstrap-components

import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

# Ticaret verilerini oluşturma
data = {
    'year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029],
    'product_code': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'export_value': [150000, 180000, 200000, 220000, 250000, 270000, 290000, 310000, 330000, 350000],
    'import_value': [120000, 160000, 250000, 210000, 240000, 260000, 300000, 330000, 320000, 340000],
    'risk_level': ['low', 'medium', 'high', 'medium', 'low', 'low', 'high', 'high', 'medium', 'medium']
}

df = pd.DataFrame(data)

# Dash uygulaması başlatma
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


# Grafikler için görselleştirmeler
def ticaret_veri_analizi(df):
    # İhracat ve ithalat değerlerinin yıllara göre çizilmesi
    export_trace = go.Scatter(x=df['year'], y=df['export_value'], mode='lines+markers', name='İhracat Değeri')
    import_trace = go.Scatter(x=df['year'], y=df['import_value'], mode='lines+markers', name='İthalat Değeri')

    # Grafik düzenlemeleri
    layout = go.Layout(
        title='İhracat ve İthalat Değerleri',
        xaxis=dict(title='Yıl'),
        yaxis=dict(title='Değer (₺)'),
        template='plotly_dark'
    )

    # Grafik çizme
    return {
        'data': [export_trace, import_trace],
        'layout': layout
    }


# Dash layout kısmı
app.layout = html.Div([
    html.H1('Ticaret Verisi Analizi', style={'text-align': 'center'}),

    # Ticaret verisi grafik
    dcc.Graph(
        id='ticaret-analizi',
        figure=ticaret_veri_analizi(df)
    ),

    # Ticaret verileri tablosu
    html.Div([
        html.H3('Ticaret Verileri Tablosu', style={'text-align': 'center'}),
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    ])
])

# Uygulamayı çalıştırma
if __name__ == "__main__":
    app.run_server(debug=True)
