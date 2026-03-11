"""
Módulo de visualizações gráficas para as Sefirot
MANTIDO - Sem alterações necessárias
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, List

def criar_radar_sefirot(avaliacoes: Dict[str, int]) -> go.Figure:
    ordem_sefirot = ['Chessed', 'Gevurah', 'Tiferet', 'Netzach', 'Hod', 'Yesod', 'Malchut']
    valores = [avaliacoes.get(s, 5) for s in ordem_sefirot]
    
    valores_completos = valores + [valores[0]]
    sefirot_completas = ordem_sefirot + [ordem_sefirot[0]]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=valores_completos,
        theta=sefirot_completas,
        fill='toself',
        name='Avaliação Atual',
        line=dict(color='#6B5B95', width=3),
        fillcolor='rgba(107, 91, 149, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=[5] * 8,
        theta=sefirot_completas,
        fill='toself',
        name='Equilíbrio Ideal',
        line=dict(color='#888888', width=2, dash='dash'),
        fillcolor='rgba(136, 136, 136, 0.1)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickmode='linear',
                tick0=0,
                dtick=2
            )
        ),
        showlegend=True,
        height=500,
        title=dict(
            text='🌳 Mapa das Sefirot Emocionais',
            x=0.5,
            font=dict(size=18)
        )
    )
    
    return fig


def criar_grafico_barras_equilibrio(pares_equilibrio: Dict) -> go.Figure:
    df_data = []
    for nome_par, dados in pares_equilibrio.items():
        df_data.append({
            'Par': nome_par,
            dados['sefirah1']: dados['valor1'],
            dados['sefirah2']: dados['valor2'],
            'Diferença': dados['diferenca']
        })
    
    df = pd.DataFrame(df_data)
    
    fig = go.Figure()
    
    for col in df.columns:
        if col not in ['Par', 'Diferença']:
            fig.add_trace(go.Bar(
                name=col,
                x=df['Par'],
                y=df[col],
                marker_color='#6B5B95' if 'Chessed' in col or 'Netzach' in col or 'Yesod' in col else '#FF6961'
            ))
    
    fig.update_layout(
        barmode='group',
        height=400,
        title=dict(
            text='⚖️ Equilíbrio entre Pares de Sefirot',
            x=0.5
        ),
        yaxis=dict(range=[0, 10]),
        showlegend=True
    )
    
    return fig


def criar_timeline_progresso(historico_sessoes: List[Dict]) -> go.Figure:
    if not historico_sessoes:
        return go.Figure().add_annotation(text="Sem dados históricos", xref="paper", yref="paper")
    
    df_data = []
    for sessao in historico_sessoes:
        data = sessao.get('data_inicio', '')[:10]
        avaliacoes = sessao.get('avaliacoes_sefirot', {})
        
        for sefirah in ['Chessed', 'Gevurah', 'Tiferet', 'Netzach', 'Hod', 'Yesod', 'Malchut']:
            df_data.append({
                'Data': data,
                'Sefirah': sefirah,
                'Valor': avaliacoes.get(sefirah, 5)
            })
    
    df = pd.DataFrame(df_data)
    
    fig = px.line(
        df, 
        x='Data', 
        y='Valor', 
        color='Sefirah',
        markers=True,
        title='📈 Evolução das Sefirot ao Longo do Tempo',
        labels={'Valor': 'Score (0-10)', 'Data': 'Data da Sessão'}
    )
    
    fig.update_layout(
        height=500,
        yaxis=dict(range=[0, 10]),
        hovermode='x unified'
    )
    
    return fig


def criar_arvore_sefirot() -> go.Figure:
    posicoes = {
        'Keter': (0.5, 1.0),
        'Chochmah': (0.3, 0.85),
        'Binah': (0.7, 0.85),
        'Daat': (0.5, 0.75),
        'Chessed': (0.3, 0.6),
        'Gevurah': (0.7, 0.6),
        'Tiferet': (0.5, 0.5),
        'Netzach': (0.3, 0.35),
        'Hod': (0.7, 0.35),
        'Yesod': (0.5, 0.2),
        'Malchut': (0.5, 0.05)
    }
    
    conexoes = [
        ('Keter', 'Chochmah'), ('Keter', 'Binah'),
        ('Chochmah', 'Daat'), ('Binah', 'Daat'),
        ('Daat', 'Chessed'), ('Daat', 'Gevurah'),
        ('Chessed', 'Tiferet'), ('Gevurah', 'Tiferet'),
        ('Tiferet', 'Netzach'), ('Tiferet', 'Hod'),
        ('Netzach', 'Yesod'), ('Hod', 'Yesod'),
        ('Yesod', 'Malchut')
    ]
    
    x_nodes = [pos[0] for pos in posicoes.values()]
    y_nodes = [pos[1] for pos in posicoes.values()]
    node_names = list(posicoes.keys())
    
    x_edges = []
    y_edges = []
    
    for conexao in conexoes:
        x0, y0 = posicoes[conexao[0]]
        x1, y1 = posicoes[conexao[1]]
        x_edges.extend([x0, x1, None])
        y_edges.extend([y0, y1, None])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x_edges, y=y_edges,
        line=dict(width=2, color='#6B5B95'),
        hoverinfo='none',
        mode='lines'
    ))
    
    fig.add_trace(go.Scatter(
        x=x_nodes, y=y_nodes,
        mode='markers+text',
        marker=dict(size=20, color='#FFB347', line=dict(width=2, color='#333333')),
        text=node_names,
        textposition='middle center',
        textfont=dict(size=10, color='#333333'),
        hoverinfo='text'
    ))
    
    fig.update_layout(
        showlegend=False,
        height=600,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1.1]),
        plot_bgcolor='white',
        title=dict(text='🌳 Árvore da Vida - Estrutura das Sefirot', x=0.5)
    )
    
    return fig


def criar_gauge_proposito(score: int) -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "🎯 Nível de Propósito", 'font': {'size': 24}},
        gauge={
            'axis': {'range': [None, 10]},
            'bar': {'color': "#6B5B95"},
            'steps': [
                {'range': [0, 4], 'color': "#FF6961"},
                {'range': [4, 7], 'color': "#FFB347"},
                {'range': [7, 10], 'color': "#77DD77"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    
    fig.update_layout(height=400)
    return fig