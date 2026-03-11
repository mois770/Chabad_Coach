"""
APLICAÇÃO STREAMLIT - COACHING SEFIRÓTICO COM ORIENTAÇÃO ATIVA
================================================================
Executar: streamlit run app.py

MUDANÇA FUNDAMENTAL:
- ANTES: Programa coletava dados, usuário decidia ações
- AGORA: Programa analisa e FORNECE orientação em cada etapa

VERSÃO: 3.0.1 - Correção: Métricas de Sucesso pré-preenchidas
"""

# ═══════════════════════════════════════════════════════════════
# IMPORTAÇÕES
# ═══════════════════════════════════════════════════════════════

import streamlit as st
import json
import os
from datetime import datetime
from uuid import uuid4
from pathlib import Path
from typing import Dict, List, Optional

from utils.sefirot_engine import SefirotEngine, CoachingSession
from utils.sefirot_semantic_analyzer import SemanticSefirotAnalyzer
from utils.sefirot_guidance import SefirotGuidanceEngine
from utils.visualizations import (
    criar_radar_sefirot,
    criar_grafico_barras_equilibrio,
    criar_timeline_progresso,
    criar_arvore_sefirot,
    criar_gauge_proposito
)

# Configuração da página
st.set_page_config(
    page_title="Coaching Sefirótico",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar engines
engine_numerico = SefirotEngine()
engine_semantico = SemanticSefirotAnalyzer()
engine_guidance = SefirotGuidanceEngine()

# Configurar diretório de dados
DATA_DIR = Path("data/sessions")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# FUNÇÕES DE SUPORTE
# ═══════════════════════════════════════════════════════════════

def salvar_sessao(sessao: CoachingSession):
    arquivo = DATA_DIR / f"sessao_{sessao.id}.json"
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(sessao.to_dict(), f, ensure_ascii=False, indent=2)

def carregar_sessoes() -> list:
    sessoes = []
    for arquivo in DATA_DIR.glob("sessao_*.json"):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                if dados.get('usuario_nome') and dados.get('topico'):
                    sessoes.append(CoachingSession.from_dict(dados))
        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️ Arquivo inválido ignorado: {arquivo.name} - {e}")
            continue
    return sorted(sessoes, key=lambda s: s.data_inicio, reverse=True)

def limpar_session_state():
    keys_to_clear = [
        'sessao_atual', 'etapa_atual', 'usuario_nome', 'topico',
        'area_vida', 'analise_intelectual', 'avaliacoes_sefirot',
        'analise_sistema', 'plano_acao', 'analise_semantica',
        'orientacao_completa', 'sugestoes_acao'
    ]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]

# ═══════════════════════════════════════════════════════════════
# INICIALIZAÇÃO DO SESSION STATE
# ═══════════════════════════════════════════════════════════════

if 'sessao_atual' not in st.session_state:
    st.session_state.sessao_atual = None
if 'etapa_atual' not in st.session_state:
    st.session_state.etapa_atual = 0
if 'avaliacoes_sefirot' not in st.session_state:
    st.session_state.avaliacoes_sefirot = {}
if 'analise_semantica' not in st.session_state:
    st.session_state.analise_semantica = None
if 'orientacao_completa' not in st.session_state:
    st.session_state.orientacao_completa = None
if 'sugestoes_acao' not in st.session_state:
    st.session_state.sugestoes_acao = {}

# ═══════════════════════════════════════════════════════════════
# INTERFACE PRINCIPAL
# ═══════════════════════════════════════════════════════════════

def main():
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/tree.png", width=80)
        st.title("🌳 Coaching Sefirótico")
        st.markdown("---")
        
        menu = st.radio(
            "Navegação",
            ["🏠 Início", "✨ Nova Sessão", "📊 Histórico", "📚 Casos de Estudo", "ℹ️ Sobre"],
            index=0,
            key="menu_navegacao"
        )
        
        st.markdown("---")
        st.info("**🔒 100% Local** - Zero alucinação, privacidade total")
        st.markdown("Baseada em Cabalá + Coaching + Análise Sistêmica")
    
    if menu == "🏠 Início":
        pagina_inicio()
    elif menu == "✨ Nova Sessão":
        nova_sessao()
    elif menu == "📊 Histórico":
        pagina_historico()
    elif menu == "📚 Casos de Estudo":
        pagina_casos_estudo()
    elif menu == "ℹ️ Sobre":
        pagina_sobre()

# ═══════════════════════════════════════════════════════════════
# PÁGINA INICIAL
# ═══════════════════════════════════════════════════════════════

def pagina_inicio():
    st.title("🌳 Bem-vindo ao Coaching Sefirótico")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sessões Realizadas", len(carregar_sessoes()))
    
    with col2:
        sessoes = carregar_sessoes()
        if sessoes:
            media_proposito = sum(
                s.avaliacoes_sefirot.get('Tiferet', 5) 
                for s in sessoes
            ) / len(sessoes)
            st.metric("Propósito Médio", f"{media_proposito:.1f}/10")
        else:
            st.metric("Propósito Médio", "N/A")
    
    with col3:
        st.metric("Análise", "Numérica + Semântica")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 O que é?")
        st.markdown("""
        Uma ferramenta de **autoconhecimento e desenvolvimento pessoal** que integra:
        
        - 📖 **Sabedoria das Sefirot** (Cabalá judaica)
        - 🎯 **Técnicas de Coaching** (questionamento poderoso)
        - 🌐 **Análise Sistêmica** (interconexões e padrões)
        - 🧠 **Análise Semântica Local** (zero alucinação, 100% privacidade)
        
        **DIFERENCIAL**: Orientação ativa em cada etapa, não apenas coleta de dados.
        """)
        
        if st.button("🚀 Começar Nova Sessão", use_container_width=True, key="btn_inicio_nova_sessao"):
            st.session_state.etapa_atual = 0
            st.rerun()
    
    with col2:
        st.subheader("📈 Últimas Sessões")
        sessoes = carregar_sessoes()[:3]
        
        if sessoes:
            for i, sessao in enumerate(sessoes):
                with st.expander(f"{sessao.topico[:50]}... - {sessao.data_inicio.strftime('%d/%m/%Y')}", key=f"exp_inicial_{i}"):
                    st.write(f"**Área**: {sessao.area_vida}")
                    st.write(f"**Status**: {'✅ Concluída' if sessao.concluida else '🔄 Em andamento'}")
        else:
            st.info("Nenhuma sessão registrada ainda. Comece uma nova sessão!")
    
    st.markdown("---")
    
    st.subheader("🌳 Árvore das Sefirot")
    st.plotly_chart(criar_arvore_sefirot(), use_container_width=True, key="arvore_sefirot_inicio")

# ═══════════════════════════════════════════════════════════════
# NOVA SESSÃO (FLUXO COMPLETO)
# ═══════════════════════════════════════════════════════════════

def nova_sessao():
    st.title("✨ Nova Sessão de Coaching")
    
    etapas = ["Dados", "ChaBaD + Análise", "Sefirot + Feedback", "Sistema + Insights", "Ação + Sugestões", "Relatório"]
    progresso = st.progress(st.session_state.etapa_atual / len(etapas))
    st.caption(f"Etapa {st.session_state.etapa_atual + 1} de {len(etapas)}: {etapas[st.session_state.etapa_atual]}")
    
    st.markdown("---")
    
    if st.session_state.etapa_atual == 0:
        etapa_dados_basicos()
    elif st.session_state.etapa_atual == 1:
        etapa_analise_intelectual_com_feedback()
    elif st.session_state.etapa_atual == 2:
        etapa_sefirot_com_feedback()
    elif st.session_state.etapa_atual == 3:
        etapa_analise_sistemica_com_insights()
    elif st.session_state.etapa_atual == 4:
        etapa_plano_acao_com_sugestoes()
    elif st.session_state.etapa_atual == 5:
        etapa_relatorio_final()

# ═══════════════════════════════════════════════════════════════
# ETAPA 1: DADOS BÁSICOS
# ═══════════════════════════════════════════════════════════════

def etapa_dados_basicos():
    st.subheader("📋 Dados Básicos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.session_state.usuario_nome = st.text_input(
            "Como posso lhe chamar?",
            value=st.session_state.get('usuario_nome', ''),
            placeholder="Seu nome ou 'Anônimo'",
            key="input_nome"
        )
    
    with col2:
        areas = ["Trabalho/Carreira", "Relacionamentos", "Saúde/Bem-estar", 
                 "Crescimento Pessoal", "Espiritualidade", "Outro"]
        st.session_state.area_vida = st.selectbox(
            "Área da vida para focar:",
            areas,
            index=areas.index(st.session_state.get('area_vida', areas[0])) 
            if st.session_state.get('area_vida') in areas else 0,
            key="select_area_vida"
        )
    
    st.session_state.topico = st.text_area(
        "Descreva brevemente a situação ou desafio:",
        value=st.session_state.get('topico', ''),
        placeholder="Ex: Sinto sobrecarga no trabalho e pouco tempo para família...",
        height=100,
        key="text_area_topico"
    )
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("➡️ Próxima Etapa", use_container_width=True, key="btn_dados_proxima"):
            if st.session_state.usuario_nome and st.session_state.topico:
                st.session_state.etapa_atual = 1
                st.rerun()
            else:
                st.warning("Por favor, preencha nome e descrição do tópico.")
    
    with col2:
        if st.button("🔄 Reiniciar", use_container_width=True, key="btn_dados_reiniciar"):
            limpar_session_state()
            st.rerun()

# ═══════════════════════════════════════════════════════════════
# ETAPA 2: CHABAD + FEEDBACK IMEDIATO
# ═══════════════════════════════════════════════════════════════

def etapa_analise_intelectual_com_feedback():
    st.subheader("🧠 Análise Intelectual (ChaBaD)")
    st.markdown("*Descreva sua situação. O sistema analisará e dará feedback imediato.*")
    
    if 'analise_intelectual' not in st.session_state:
        st.session_state.analise_intelectual = {}
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📖 Chochmah (Sabedoria/Visão)")
        st.session_state.analise_intelectual['chochmah'] = st.text_area(
            "Qual é a visão maior ou propósito por trás desta situação?",
            value=st.session_state.analise_intelectual.get('chochmah', ''),
            height=100,
            key="text_chochmah"
        )
    
    with col2:
        st.markdown("### 🔍 Binah (Entendimento/Análise)")
        st.session_state.analise_intelectual['binah'] = st.text_area(
            "Quais padrões e consequências você identifica?",
            value=st.session_state.analise_intelectual.get('binah', ''),
            height=100,
            key="text_binah"
        )
    
    st.markdown("### 💡 Da'at (Conhecimento/Conexão)")
    st.session_state.analise_intelectual['daat'] = st.text_area(
        "Isso ressoa com seus valores mais profundos? Como?",
        value=st.session_state.analise_intelectual.get('daat', ''),
        height=100,
        key="text_daat"
    )
    
    # ✅ NOVO: Botão para analisar e mostrar feedback
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        if st.button("🔍 Analisar Meu Texto", use_container_width=True, key="btn_analisar_chabad"):
            analise = engine_semantico.analisar_texto_usuario(st.session_state.analise_intelectual)
            st.session_state.analise_semantica = analise
            st.success("✅ Análise completa! Veja os insights abaixo.")
    
    # ✅ NOVO: Mostrar feedback se análise já foi feita
    if st.session_state.analise_semantica:
        st.markdown("---")
        st.markdown("### 🎯 Feedback da Sua Descrição")
        
        analise = st.session_state.analise_semantica
        
        if analise.get('sefirot_predominantes'):
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"""
                **📊 Padrões Detectados no Seu Texto:**
                
                {chr(10).join([f"- **{s['sefirah']}**: {s['similaridade']*100:.0f}% de similaridade" 
                               for s in analise['sefirot_predominantes']])}
                
                **Confiança:** {analise.get('confianca', 'média').upper()}
                """)
            
            with col2:
                st.warning(f"""
                **💡 Orientação Inicial:**
                
                Seu texto sugere foco em **{analise['sefirot_predominantes'][0]['sefirah']}**.
                
                Na próxima etapa, avalie cuidadosamente esta Sefirah.
                """)
                
                sefirah_principal = analise['sefirot_predominantes'][0]['sefirah']
                for item in analise['sefirot_predominantes']:
                    if item['sefirah'] == sefirah_principal:
                        st.write(f"**🔧 Prática Recomendada:** {item['conhecimento'].pratica_corretiva[:150]}...")
    
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        if st.button("➡️ Próxima Etapa", use_container_width=True, key="btn_chabad_proxima"):
            st.session_state.etapa_atual = 2
            st.rerun()
    with col2:
        if st.button("⬅️ Voltar", use_container_width=True, key="btn_chabad_voltar"):
            st.session_state.etapa_atual = 0
            st.rerun()
    with col3:
        if st.button("🔄 Reiniciar", use_container_width=True, key="btn_chabad_reiniciar"):
            limpar_session_state()
            st.rerun()

# ═══════════════════════════════════════════════════════════════
# ETAPA 3: SEFIROT + FEEDBACK
# ═══════════════════════════════════════════════════════════════

def etapa_sefirot_com_feedback():
    st.subheader("💚 Mapeamento das Sefirot Emocionais")
    st.markdown("*Avalie cada área. O sistema mostrará padrões e orientações em tempo real.*")
    
    if 'avaliacoes_sefirot' not in st.session_state:
        st.session_state.avaliacoes_sefirot = {}
    
    cols = st.columns(2)
    
    for i, (sefirah, dados) in enumerate(engine_numerico.sefirot_emocionais.items()):
        col = cols[i % 2]
        with col:
            with st.expander(f"{dados.nome} ({dados.hebraico}) - {dados.atributo}", expanded=False):
                st.write(f"📊 {dados.pergunta_diagnostico}")
                
                valor = st.slider(
                    "Sua avaliação (0-10):",
                    min_value=0,
                    max_value=10,
                    value=st.session_state.avaliacoes_sefirot.get(sefirah, 5),
                    key=f"slider_{sefirah}"
                )
                
                st.session_state.avaliacoes_sefirot[sefirah] = valor
                
                observacao = st.text_area(
                    "Observação específica:",
                    value="",
                    height=60,
                    key=f"obs_{sefirah}"
                )
    
    # ✅ NOVO: Feedback em tempo real baseado nas avaliações
    if len(st.session_state.avaliacoes_sefirot) >= 5:
        st.markdown("---")
        st.markdown("### 🎯 Feedback Parcial das Suas Avaliações")
        
        criticas = [(k, v) for k, v in st.session_state.avaliacoes_sefirot.items() if v <= 4 or v >= 8]
        criticas.sort(key=lambda x: x[1])
        
        if criticas:
            col1, col2 = st.columns(2)
            
            with col1:
                st.warning(f"""
                **⚠️ Áreas que Merecem Atenção:**
                
                {chr(10).join([f"- **{k}**: {v}/10" for k, v in criticas[:3]])}
                """)
            
            with col2:
                sefirah_critica = criticas[0][0]
                guidance = engine_guidance.guidance_db.get(sefirah_critica)
                if guidance:
                    st.info(f"""
                    **💡 Orientação para {sefirah_critica}:**
                    
                    {guidance.pratica_corretiva}
                    
                    **Meditação:** {guidance.meditacao_chabad[:100]}...
                    """)
        
        st.markdown("### 📊 Visualização em Tempo Real")
        fig_radar = criar_radar_sefirot(st.session_state.avaliacoes_sefirot)
        st.plotly_chart(fig_radar, use_container_width=True, key="radar_sefirot_sessao")
    
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        if st.button("➡️ Próxima Etapa", use_container_width=True, key="btn_sefirot_proxima"):
            st.session_state.etapa_atual = 3
            st.rerun()
    with col2:
        if st.button("⬅️ Voltar", use_container_width=True, key="btn_sefirot_voltar"):
            st.session_state.etapa_atual = 1
            st.rerun()
    with col3:
        if st.button("🔄 Reiniciar", use_container_width=True, key="btn_sefirot_reiniciar"):
            limpar_session_state()
            st.rerun()

# ═══════════════════════════════════════════════════════════════
# ETAPA 4: SISTEMA + INSIGHTS
# ═══════════════════════════════════════════════════════════════

def etapa_analise_sistemica_com_insights():
    st.subheader("🌐 Análise Sistêmica")
    st.markdown("*Descreva o sistema. O sistema sugerirá pontos de alavancagem.*")
    
    if 'analise_sistema' not in st.session_state:
        st.session_state.analise_sistema = {}
    
    st.session_state.analise_sistema['atores'] = st.text_area(
        "Quem ou o que está envolvido nesta situação? (separe por vírgulas)",
        value=st.session_state.analise_sistema.get('atores', ''),
        height=80,
        placeholder="Ex: Eu, minha equipe, minha família, meu chefe...",
        key="text_atores"
    )
    
    st.session_state.analise_sistema['dinamicas'] = st.text_area(
        "Como os elementos se relacionam? Há ciclos ou padrões?",
        value=st.session_state.analise_sistema.get('dinamicas', ''),
        height=100,
        placeholder="Ex: Trabalho muito → chego cansado em casa → família se distancia → trabalho mais...",
        key="text_dinamicas"
    )
    
    st.session_state.analise_sistema['alavancagem'] = st.text_area(
        "Onde uma pequena mudança poderia gerar grande impacto?",
        value=st.session_state.analise_sistema.get('alavancagem', ''),
        height=80,
        placeholder="Ex: Estabelecer limite de horário de trabalho...",
        key="text_alavancagem"
    )
    
    # ✅ NOVO: Sugestões de pontos de alavancagem
    if st.session_state.avaliacoes_sefirot:
        st.markdown("---")
        st.markdown("### 💡 Sugestões de Pontos de Alavancagem")
        
        mais_baixa = min(st.session_state.avaliacoes_sefirot.items(), key=lambda x: x[1])
        guidance = engine_guidance.guidance_db.get(mais_baixa[0])
        
        if guidance:
            st.success(f"""
            **🎯 Baseado na Sua Avaliação de {mais_baixa[0]} ({mais_baixa[1]}/10):**
            
            Um ponto de alavancagem provável é: **{guidance.pratica_corretiva.split('.')[0]}**.
            
            Exemplo concreto para sua situação:
            - Se é **Gevurah**: Estabelecer 1 limite claro de horário
            - Se é **Chessed**: Redirecionar 1 ato de generosidade por dia
            - Se é **Tiferet**: Escolher 1 decisão que equilibre trabalho e família
            - Se é **Yesod**: Alinhar 1 compromisso com seus valores
            - Se é **Malchut**: Completar 1 projeto parado esta semana
            """)
    
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        if st.button("➡️ Próxima Etapa", use_container_width=True, key="btn_sistema_proxima"):
            st.session_state.etapa_atual = 4
            st.rerun()
    with col2:
        if st.button("⬅️ Voltar", use_container_width=True, key="btn_sistema_voltar"):
            st.session_state.etapa_atual = 2
            st.rerun()
    with col3:
        if st.button("🔄 Reiniciar", use_container_width=True, key="btn_sistema_reiniciar"):
            limpar_session_state()
            st.rerun()

# ═══════════════════════════════════════════════════════════════
# ETAPA 5: PLANO DE AÇÃO + SUGESTÕES (CORRIGIDO!)
# ═══════════════════════════════════════════════════════════════

def etapa_plano_acao_com_sugestoes():
    st.subheader("📝 Plano de Ação")
    st.markdown("*O sistema SUGERE ações baseadas na análise. Você pode ajustar.*")
    
    if 'plano_acao' not in st.session_state:
        st.session_state.plano_acao = []
    
    # ✅ Gerar sugestões baseadas na análise
    if not st.session_state.sugestoes_acao and st.session_state.avaliacoes_sefirot:
        criticas = [(k, v) for k, v in st.session_state.avaliacoes_sefirot.items() if v <= 4]
        
        sugestoes = {}
        
        for sefirah, score in criticas[:3]:
            guidance = engine_guidance.guidance_db.get(sefirah)
            if guidance:
                sugestoes[sefirah] = {
                    '48h': f"Ação imediata relacionada a {sefirah}: {guidance.pratica_corretiva[:80]}",
                    '2sem': f"Consolidar prática de {sefirah} por 2 semanas",
                    '3mes': f"Transformação em {sefirah} em 3 meses",
                    'metricas': f"Registrar {sefirah} diariamente (0-10) + 1 evidência concreta"
                }
        
        if not sugestoes:
            mais_baixas = sorted(st.session_state.avaliacoes_sefirot.items(), key=lambda x: x[1])[:3]
            for sefirah, score in mais_baixas:
                guidance = engine_guidance.guidance_db.get(sefirah)
                if guidance:
                    sugestoes[sefirah] = {
                        '48h': f"Ação imediata relacionada a {sefirah}: {guidance.pratica_corretiva[:80]}",
                        '2sem': f"Consolidar prática de {sefirah} por 2 semanas",
                        '3mes': f"Transformação em {sefirah} em 3 meses",
                        'metricas': f"Registrar {sefirah} diariamente (0-10) + 1 evidência concreta"
                    }
        
        st.session_state.sugestoes_acao = sugestoes
    
    # ✅ Mostrar sugestões antes dos campos de entrada
    if st.session_state.sugestoes_acao:
        st.markdown("### 💡 Sugestões Baseadas na Sua Análise")
        
        for sefirah, acoes in st.session_state.sugestoes_acao.items():
            with st.expander(f"🎯 {sefirah} - Sugestões de Ação"):
                st.write(f"**⚡ 48 horas:** {acoes['48h']}")
                st.write(f"**📅 2 semanas:** {acoes['2sem']}")
                st.write(f"**🎯 3 meses:** {acoes['3mes']}")
                st.write(f"**📊 Métricas:** {acoes['metricas']}")
        
        st.info("💡 Você pode usar estas sugestões como base ou criar suas próprias ações abaixo.")
    
    st.markdown("---")
    st.markdown("### 📝 Seu Plano de Ação (Ajuste as Sugestões ou Crie Novas)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ⚡ Ação Imediata (48 horas)")
        
        sugestao_48h = ""
        if st.session_state.sugestoes_acao:
            primeira_sefirah = list(st.session_state.sugestoes_acao.keys())[0]
            sugestao_48h = st.session_state.sugestoes_acao[primeira_sefirah]['48h']
        
        acao_48h = st.text_area(
            "Qual passo concreto você pode dar nas próximas 48 horas?",
            value=sugestao_48h,
            height=80,
            key="text_acao_48h"
        )
        
        st.markdown("### 📅 Curto Prazo (2 semanas)")
        sugestao_2sem = list(st.session_state.sugestoes_acao.values())[0]['2sem'] if st.session_state.sugestoes_acao else ""
        acao_2sem = st.text_area(
            "O que você pode consolidar em 2 semanas?",
            value=sugestao_2sem,
            height=80,
            key="text_acao_2sem"
        )
    
    with col2:
        st.markdown("### 🎯 Longo Prazo (3 meses)")
        sugestao_3mes = list(st.session_state.sugestoes_acao.values())[0]['3mes'] if st.session_state.sugestoes_acao else ""
        acao_3mes = st.text_area(
            "Qual transformação você busca em 3 meses?",
            value=sugestao_3mes,
            height=80,
            key="text_acao_3mes"
        )
        
        st.markdown("### 📊 Métricas de Sucesso")
        
        # ✅ CORREÇÃO: Pré-preencher com sugestão de métricas
        sugestao_metricas = ""
        if st.session_state.sugestoes_acao:
            primeira_sefirah = list(st.session_state.sugestoes_acao.keys())[0]
            sugestao_metricas = st.session_state.sugestoes_acao[primeira_sefirah]['metricas']
        
        metricas = st.text_area(
            "Como você saberá que está progredindo?",
            value=sugestao_metricas,  # ✅ AGORA PRÉ-PREENCHIDO
            height=80,
            key="text_metricas",
            placeholder="Ex: Registrar score diário + 1 evidência concreta por semana"
        )
    
    st.session_state.plano_acao = [
        {'prazo': '48 horas', 'acao': acao_48h, 'sefirah': 'Malchut'},
        {'prazo': '2 semanas', 'acao': acao_2sem, 'sefirah': 'Yesod'},
        {'prazo': '3 meses', 'acao': acao_3mes, 'sefirah': 'Tiferet'},
        {'prazo': 'Contínuo', 'acao': f'Monitorar: {metricas}', 'sefirah': 'Hod'}
    ]
    
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        if st.button("➡️ Gerar Relatório", use_container_width=True, key="btn_acao_relatorio"):
            st.session_state.etapa_atual = 5
            st.rerun()
    with col2:
        if st.button("⬅️ Voltar", use_container_width=True, key="btn_acao_voltar"):
            st.session_state.etapa_atual = 3
            st.rerun()
    with col3:
        if st.button("🔄 Reiniciar", use_container_width=True, key="btn_acao_reiniciar"):
            limpar_session_state()
            st.rerun()

# ═══════════════════════════════════════════════════════════════
# 
# ═══════════════════════════════════════════════════════════════

def etapa_relatorio_final():
    st.subheader("📊 Relatório Final da Sessão")
    
    progresso_analise = st.progress(0)
    status_texto = st.empty()
    
    status_texto.text("🔄 Executando análise semântica do seu texto...")
    progresso_analise.progress(25)
    
    if not st.session_state.analise_semantica:
        analise_semantica = engine_semantico.analisar_texto_usuario(
            st.session_state.analise_intelectual
        )
        st.session_state.analise_semantica = analise_semantica
    else:
        analise_semantica = st.session_state.analise_semantica
    
    status_texto.text("🔄 Combinando análise semântica com avaliações numéricas...")
    progresso_analise.progress(50)
    
    status_texto.text("🔄 Gerando orientação baseada em Chabad-Chassidut...")
    progresso_analise.progress(75)
    
    orientacao_completa = engine_guidance.gerar_orientacao_completa(
        st.session_state.avaliacoes_sefirot,
        st.session_state.analise_intelectual,
        analise_semantica
    )
    st.session_state.orientacao_completa = orientacao_completa
    
    progresso_analise.progress(100)
    status_texto.text("✅ Análise completa!")
    
    sessao = CoachingSession(
        id=str(uuid4())[:8],
        usuario_nome=st.session_state.get('usuario_nome', 'Anônimo'),
        data_inicio=datetime.now(),
        topico=st.session_state.get('topico', ''),
        area_vida=st.session_state.get('area_vida', ''),
        analise_intelectual=st.session_state.get('analise_intelectual', {}),
        avaliacoes_sefirot=st.session_state.get('avaliacoes_sefirot', {}),
        analise_sistema=st.session_state.get('analise_sistema', {}),
        plano_acao=st.session_state.get('plano_acao', []),
        notas=json.dumps(analise_semantica, ensure_ascii=False, indent=2),
        concluida=True,
        data_conclusao=datetime.now()
    )
    
    salvar_sessao(sessao)
    st.success(f"✅ Sessão salva com ID: {sessao.id}")
    
    st.markdown("### 🎯 Orientação Prioritária")
    st.info(orientacao_completa['orientacao_prioritaria'], icon="🎯")
    
    st.markdown("### 🧠 Análise Semântica do Seu Texto")
    
    if analise_semantica.get('sefirot_predominantes'):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Sefirot Detectadas no Seu Texto:**")
            for item in analise_semantica['sefirot_predominantes']:
                st.write(f"- **{item['sefirah']}**: {item['similaridade']*100:.1f}% similaridade")
        
        with col2:
            st.markdown("**Confiança da Análise:**")
            confianca = analise_semantica.get('confianca', 'média')
            if confianca == 'alta':
                st.success(f"✅ {confianca.upper()}")
            elif confianca == 'média':
                st.warning(f"⚠️ {confianca.upper()}")
            else:
                st.info(f"ℹ️ {confianca.upper()}")
    else:
        st.info("Não foi possível detectar padrões semânticos claros. A orientação será baseada apenas nas avaliações numéricas.")
    
    if orientacao_completa.get('sefirot_criticas'):
        st.markdown("### ⚠️ Áreas que Merecem Atenção")
        
        for crit in orientacao_completa['sefirot_criticas']:
            with st.expander(f"{crit['sefirah']} ({crit['valor']}/10 - {crit['tipo']})"):
                g = crit['guidance']
                st.write(f"**📖 Significação:** {g.significacao_profunda}")
                st.write(f"**⚠️ Sinal:** {g.sinal_desequilibrio}")
                st.write(f"**🔧 Prática Corretiva:** {g.pratica_corretiva}")
                st.write(f"**🧘 Meditação:** {g.meditacao_chabad}")
                st.write(f"**💪 Afirmação:** _{g.afirmacao_transformadora}_")
                
                if analise_semantica.get('sefirot_predominantes'):
                    semantica_concorda = any(
                        s['sefirah'] == crit['sefirah'] 
                        for s in analise_semantica['sefirot_predominantes']
                    )
                    if semantica_concorda:
                        st.success("✅ Sua descrição textual confirma esta área como prioritária")
    
    st.markdown("### 📅 Plano Espiritual de 7 Dias")
    for dia in orientacao_completa['plano_espiritual']:
        with st.expander(f"{dia['dia']} - {dia['sefirah']}"):
            st.write(f"🛠️ **Prática:** {dia['pratica']}")
            st.write(f"🧘 **Meditação:** {dia['meditacao']}")
    
    st.markdown("### 📚 Sabedoria Chassídica")
    st.markdown(f"> {orientacao_completa['texto_chassidico']}")
    
    st.markdown("---")
    st.markdown("### 📊 Visualizações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌳 Mapa das Sefirot")
        fig_radar = criar_radar_sefirot(sessao.avaliacoes_sefirot)
        st.plotly_chart(fig_radar, use_container_width=True, key="radar_relatorio_final")
    
    with col2:
        st.markdown("### ⚖️ Equilíbrio entre Pares")
        pares = engine_numerico.calcular_equilibrio(sessao.avaliacoes_sefirot)
        fig_barras = criar_grafico_barras_equilibrio(pares)
        st.plotly_chart(fig_barras, use_container_width=True, key="barras_equilibrio_final")
    
    st.markdown("### 📝 Seu Plano de Ação")
    for i, item in enumerate(sessao.plano_acao, 1):
        st.markdown(f"**{i}. [{item['prazo']}]** {item['acao']} *(Sefirah: {item['sefirah']})*")
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        json_str = json.dumps(sessao.to_dict(), ensure_ascii=False, indent=2)
        st.download_button(
            label="📥 Baixar JSON",
            data=json_str,
            file_name=f"sessao_{sessao.id}.json",
            mime="application/json",
            use_container_width=True,
            key=f"download_json_{sessao.id}"
        )
    
    with col2:
        txt_content = gerar_relatorio_txt(sessao, orientacao_completa)
        st.download_button(
            label="📥 Baixar TXT",
            data=txt_content,
            file_name=f"sessao_{sessao.id}.txt",
            mime="text/plain",
            use_container_width=True,
            key=f"download_txt_{sessao.id}"
        )
    
    with col3:
        if st.button("🏠 Voltar ao Início", use_container_width=True, key="btn_relatorio_inicio"):
            limpar_session_state()
            st.rerun()

def gerar_relatorio_txt(sessao: CoachingSession, orientacao: Dict = None) -> str:
    relatorio = f"""
═══════════════════════════════════════════════════════════════
  RELATÓRIO DE COACHING SEFIRÓTICO
  🔒 100% Local - Zero Alucinação
═══════════════════════════════════════════════════════════════
  Usuário: {sessao.usuario_nome}
  Data: {sessao.data_inicio.strftime('%d/%m/%Y %H:%M')}
  Tópico: {sessao.topico}
  Área: {sessao.area_vida}

🧠 ANÁLISE INTELECTUAL (ChaBaD)
─────────────────────────────
• Chochmah: {sessao.analise_intelectual.get('chochmah', 'N/A')}
• Binah: {sessao.analise_intelectual.get('binah', 'N/A')}
• Da'at: {sessao.analise_intelectual.get('daat', 'N/A')}

💚 AVALIAÇÕES SEFIROT
────────────────────
""" + "\n".join([
    f"• {k}: {v}/10" for k, v in sessao.avaliacoes_sefirot.items()
]) + f"""

🌐 ANÁLISE SISTÊMICA
───────────────────
• Atores: {sessao.analise_sistema.get('atores', 'N/A')}
• Dinâmicas: {sessao.analise_sistema.get('dinamicas', 'N/A')}
• Alavancagem: {sessao.analise_sistema.get('alavancagem', 'N/A')}

📝 PLANO DE AÇÃO
────────────────
""" + "\n".join([
    f"{i+1}. [{p['prazo']}] {p['acao']} ({p['sefirah']})"
    for i, p in enumerate(sessao.plano_acao)
])
    
    if orientacao:
        relatorio += f"""

═══════════════════════════════════════════════════════════════
  ORIENTAÇÃO SEFIRÓTICA (BASE FECHADA)
═══════════════════════════════════════════════════════════════

{orientacao['orientacao_prioritaria']}
"""
    
    return relatorio

# ═══════════════════════════════════════════════════════════════
# PÁGINA DE HISTÓRICO
# ═══════════════════════════════════════════════════════════════

def pagina_historico():
    st.title("📊 Histórico de Sessões")
    
    sessoes = carregar_sessoes()
    
    if not sessoes:
        st.info("Nenhuma sessão registrada ainda.")
        return
    
    st.metric("Total de Sessões", len(sessoes))
    
    st.markdown("### 📈 Evolução ao Longo do Tempo")
    historico_dicts = [s.to_dict() for s in sessoes]
    fig_timeline = criar_timeline_progresso(historico_dicts)
    st.plotly_chart(fig_timeline, use_container_width=True, key="timeline_historico")
    
    st.markdown("### 📋 Sessões Registradas")
    
    for i, sessao in enumerate(sessoes):
        with st.expander(f"{sessao.topico[:50]}... - {sessao.data_inicio.strftime('%d/%m/%Y')}", 
                         expanded=False,
                         key=f"expander_sessao_{i}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Área**: {sessao.area_vida}")
                st.write(f"**Status**: {'✅ Concluída' if sessao.concluida else '🔄 Em andamento'}")
            
            with col2:
                if sessao.avaliacoes_sefirot:
                    media = sum(sessao.avaliacoes_sefirot.values()) / len(sessao.avaliacoes_sefirot)
                    st.write(f"**Média Sefirot**: {media:.1f}/10")
            
            if sessao.avaliacoes_sefirot:
                fig_mini = criar_radar_sefirot(sessao.avaliacoes_sefirot)
                fig_mini.update_layout(height=300, margin=dict(t=30, b=30, l=30, r=30))
                st.plotly_chart(fig_mini, use_container_width=True, key=f"radar_historico_{sessao.id}")

# ═══════════════════════════════════════════════════════════════
# PÁGINA DE CASOS DE ESTUDO
# ═══════════════════════════════════════════════════════════════

def pagina_casos_estudo():
    st.title("📚 Casos de Estudo")
    
    caso = {
        'perfil': {'nome': 'M. S.', 'idade': 42, 'profissao': 'Gerente de Projetos', 'familia': 'Casado, 2 filhos'},
        'demanda': 'Sobrecarga trabalho, equipe desmotivada, pouco tempo família',
        'resultados': 'Redução 15h/semana, melhora relacionamento familiar, equipe mais autônoma'
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👤 Perfil")
        st.json(caso['perfil'])
        
        st.markdown("### 🎯 Demanda Inicial")
        st.info(caso['demanda'], icon="🎯", key="info_caso_demanda")
    
    with col2:
        st.markdown("### 📊 Resultados (3 meses)")
        st.success(caso['resultados'], icon="📊", key="success_caso_resultados")
        
        st.markdown("### 💡 Lições Aprendidas")
        st.markdown("""
        1. Gevurah (limites) foi ponto de alavancagem
        2. Ações pequenas geraram grandes mudanças
        3. Análise sistêmica revelou ciclos viciosos
        4. Integração ChaBaD + Emoções + Ação foi essencial
        """)

# ═══════════════════════════════════════════════════════════════
# PÁGINA SOBRE
# ═══════════════════════════════════════════════════════════════

def pagina_sobre():
    st.title("ℹ️ Sobre o Projeto")
    
    st.markdown("""
    ### 🌳 Coaching Sefirótico
    
    **Versão**: 3.0.1 (Com Orientação Ativa + Métricas Pré-Preenchidas)
    
    **MUDANÇA FUNDAMENTAL:**
    - ANTES: Programa coletava dados, usuário decidia ações
    - AGORA: Programa analisa e FORNECE orientação em cada etapa
    
    ### 🔒 GARANTIAS DE PRIVACIDADE E PRECISÃO
    
    | Garantia | Implementação |
    |----------|---------------|
    | **100% Local** | Nenhum dado sai do seu computador |
    | **Zero Alucinação** | Todo texto vem de base fechada (hard-coded) |
    | **Determinístico** | Mesma entrada = mesma saída sempre |
    | **Sem API** | Nenhuma conexão externa necessária |
    
    ### 📖 Fundamentação
    
    Este projeto integra três abordagens:
    
    1. **Cabalá Judaica** - Estrutura das 10 Sefirot como mapa da alma
    2. **Coaching** - Questionamento poderoso e plano de ação
    3. **Análise Sistêmica** - Interconexões e padrões
    4. **Análise Semântica Local** - Entende seu texto sem enviar para nuvem
    
    ### ⚠️ Aviso Importante
    
    Esta ferramenta é para **desenvolvimento pessoal e reflexão**.
    Não substitui acompanhamento psicológico ou psiquiátrico profissional.
    """)

# ═══════════════════════════════════════════════════════════════
# EXECUÇÃO
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()