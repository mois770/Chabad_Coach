"""
streamlit_app/utils/sefirot_semantic_analyzer.py
Análise semântica LOCAL com ZERO alucinação - 100% privacidade

GARANTIAS:
- Todo texto vem de base fechada (hard-coded)
- Nenhum conteúdo é gerado por LLM
- Similaridade é calculada deterministicamente
- Nada sai do computador do usuário
"""

from sentence_transformers import SentenceTransformer
import numpy as np
from typing import Dict, List
from dataclasses import dataclass
import warnings

# Suprimir warnings do transformers
warnings.filterwarnings("ignore", category=FutureWarning)

@dataclass
class ConhecimentoSefirah:
    """Texto de conhecimento fechado sobre cada Sefirah"""
    sefirah: str
    descricao: str
    fonte: str
    pratica_corretiva: str
    meditacao: str
    sinal_desequilibrio: str
    afirmacao_transformadora: str
    exemplo_biblico: str
    embedding: np.ndarray = None

class SemanticSefirotAnalyzer:
    """
    Analisador semântico LOCAL - ZERO alucinação, 100% privacidade
    
    FUNCIONAMENTO:
    1. Texto do usuário é convertido em embedding (vetor numérico)
    2. Embedding é comparado com base de conhecimento fechada
    3. Similaridade de cosseno determina quais Sefirot são relevantes
    4. Textos de orientação vêm EXCLUSIVAMENTE da base fechada
    5. NADA é gerado ou inventado
    """
    
    def __init__(self, modelo_nome: str = 'paraphrase-multilingual-MiniLM-L12-v2'):
        self.modelo_nome = modelo_nome
        self.modelo = None
        self.base_conhecimento = []
        self._inicializar_base_conhecimento()
    
    def inicializar_modelo(self):
        """Carrega modelo de embeddings (feito uma vez por sessão)"""
        if self.modelo is None:
            print(f"🔄 Carregando modelo de embeddings ({self.modelo_nome})...")
            print("⏱️ Isso pode levar 30-60 segundos na primeira execução")
            self.modelo = SentenceTransformer(self.modelo_nome)
            print("✅ Modelo carregado com sucesso")
    
    def _inicializar_base_conhecimento(self):
        """
        Carrega base de conhecimento FECHADA
        Todos os textos são hard-coded - nada é buscado externamente
        """
        self.base_conhecimento = [
            ConhecimentoSefirah(
                sefirah='Chessed',
                descricao='Amor expansivo, doação sem limites, generosidade, acolhimento, cuidar dos outros, bondade, ajudar, família, presentes',
                fonte='Tanya, Capítulo 43',
                pratica_corretiva='3 atos de bondade consciente por dia. Antes de doar, pergunte: "Isso ajuda a pessoa a crescer ou cria dependência?"',
                meditacao='Deus me deu vida, respiração, oportunidades. Se Ele doa sem limite, posso aprender a doar com sabedoria.',
                sinal_desequilibrio='Frieza emocional, isolamento, dificuldade de conectar, ou doação sem limites que cria dependência',
                afirmacao_transformadora='Eu dou com sabedoria, recebendo com gratidão. Meu amor é forte e tem limites saudáveis.',
                exemplo_biblico='Abraão Avinu - sentava na entrada de sua tenda esperando hóspedes. Mas também estabelecia limites.'
            ),
            ConhecimentoSefirah(
                sefirah='Gevurah',
                descricao='Limites, restrição, disciplina, controle, dizer não, estrutura, justiça, força, fronteira, regras, organização',
                fonte='Tanya, Capítulo 9',
                pratica_corretiva='Estabeleça 1 limite claro esta semana. Antes de dizer sim, pergunte: "Isso me protege ou me limita?"',
                meditacao='Meus limites me protegem e protegem os outros. Dizer não é às vezes o maior sim.',
                sinal_desequilibrio='Sem limites, caos, permissividade, ou rigidez excessiva e controle',
                afirmacao_transformadora='Meus limites são sagrados. Eu os estabeleço com amor e os mantenho com firmeza.',
                exemplo_biblico='Isaac Avinu - permitiu ser amarrado no altar (auto-restrição), mas também cavou poços e persistiu.'
            ),
            ConhecimentoSefirah(
                sefirah='Tiferet',
                descricao='Equilíbrio, harmonia, compaixão, integrar opostos, verdade, beleza interior, centro, paz, conexão, propósito',
                fonte='Likutei Torah',
                pratica_corretiva='Quando em conflito, pergunte: "Qual ação honra tanto minha verdade quanto o bem do outro?"',
                meditacao='Não preciso escolher entre ser bom e ser forte. Posso ser ambos com sabedoria.',
                sinal_desequilibrio='Conflito interno constante, dificuldade de decisão, ou conivência disfarçada de compaixão',
                afirmacao_transformadora='Eu integro opostos em harmonia. Minha compaixão tem força, minha força tem compaixão.',
                exemplo_biblico='Jacó Avinu - lutou com anjo e homem, integrou Chessed (Abraão) e Gevurah (Isaac) em sua alma.'
            ),
            ConhecimentoSefirah(
                sefirah='Netzach',
                descricao='Persistência, vitória, duração, ambição, liderança, não desistir, objetivos, meta, continuar, esforço',
                fonte='Rebbe Rashab',
                pratica_corretiva='Comprometa-se com 1 projeto por 30 dias sem abandonar. Antes de insistir, pergunte: "Isso é propósito ou ego?"',
                meditacao='Minha persistência vem de conexão com propósito, não de necessidade de vencer.',
                sinal_desequilibrio='Desistência fácil, falta de direção, ou teimosia e agressividade',
                afirmacao_transformadora='Eu persisto com propósito, não com teimosia. Sei quando avançar e quando ajustar.',
                exemplo_biblico='Moisés - liderou 40 anos no deserto, enfrentou Faraó e o próprio povo, sempre com direção clara.'
            ),
            ConhecimentoSefirah(
                sefirah='Hod',
                descricao='Humildade, gratidão, reconhecimento, submissão saudável, esplendor, agradecer, mérito, valor, celebrar',
                fonte='Baal Shem Tov',
                pratica_corretiva='Agradeça 3 pessoas especificamente esta semana. Celebre 1 conquista sua sem minimizar.',
                meditacao='Meus talentos são presentes. Usá-los plenamente é honrar Quem os deu.',
                sinal_desequilibrio='Arrogância, não reconhecer contribuições alheias, ou baixa autoestima',
                afirmacao_transformadora='Reconheço meus dons e os dos outros. Humildade me faz maior, não menor.',
                exemplo_biblico='Aaron HaKohen - se alegrava com o sucesso de Moisés, sem competição.'
            ),
            ConhecimentoSefirah(
                sefirah='Yesod',
                descricao='Fundação, integridade, conexão, confiança, alinhamento, transmissão, coerência, verdade, palavra, compromisso',
                fonte='Tanya, Capítulo 30',
                pratica_corretiva='Antes de falar, pergunte: "Isso é verdade? É necessário? É gentil?" Cumpra o que promete.',
                meditacao='Minha palavra tem peso. Alinho o que penso, falo e faço.',
                sinal_desequilibrio='Inconsistência, quebra de confiança, ou rigidez moral e julgamento',
                afirmacao_transformadora='Minha integridade é minha fundação. Pensamento, palavra e ação estão alinhados.',
                exemplo_biblico='José HaTzadik - resistiu à tentação, manteve integridade na prisão e no palácio.'
            ),
            ConhecimentoSefirah(
                sefirah='Malchut',
                descricao='Realização, manifestação, ação concreta, realeza, presença, executar, fazer, prático, completar, finalizar',
                fonte='Likutei Amarim',
                pratica_corretiva='Complete 1 projeto parado esta semana. Antes de agir, pergunte: "Estou servindo ou controlando?"',
                meditacao='Ação concreta é onde o espiritual encontra o físico. Pequenos passos manifestam grandes visões.',
                sinal_desequilibrio='Muitos planos, pouca execução, ou arrogância e controle excessivo',
                afirmacao_transformadora='Manifesto minha visão em ação concreta. Cada pequeno passo é sagrado.',
                exemplo_biblico='Rei David - guerreiro, poeta, rei. Manifestou visão espiritual em reino concreto.'
            )
        ]
    
    def _calcular_embeddings_base(self):
        """Pré-calcula embeddings de toda a base de conhecimento"""
        self.inicializar_modelo()
        
        for conhecimento in self.base_conhecimento:
            if conhecimento.embedding is None:
                texto_completo = f"{conhecimento.descricao} {conhecimento.pratica_corretiva}"
                conhecimento.embedding = self.modelo.encode(texto_completo)
    
    def analisar_texto_usuario(self, analise_intelectual: Dict) -> Dict:
        """
        Analisa texto do usuário com similaridade semântica
        RETORNA APENAS dados da base fechada - ZERO geração nova
        """
        self._calcular_embeddings_base()
        
        texto_completo = ' '.join([
            analise_intelectual.get('chochmah', ''),
            analise_intelectual.get('binah', ''),
            analise_intelectual.get('daat', '')
        ])
        
        if not texto_completo.strip():
            return {
                'sefirot_predominantes': [],
                'ranking_completo': [],
                'confianca': 'baixa',
                'texto_analisado': '',
                'erro': 'Texto vazio ou não fornecido'
            }
        
        texto_embedding = self.modelo.encode(texto_completo)
        
        similaridades = []
        for conhecimento in self.base_conhecimento:
            similaridade = self._cosine_similarity(texto_embedding, conhecimento.embedding)
            similaridades.append({
                'sefirah': conhecimento.sefirah,
                'similaridade': round(float(similaridade), 4),
                'conhecimento': conhecimento
            })
        
        similaridades.sort(key=lambda x: x['similaridade'], reverse=True)
        
        sefirot_predominantes = [
            s for s in similaridades if s['similaridade'] > 0.45
        ][:3]
        
        return {
            'sefirot_predominantes': sefirot_predominantes,
            'ranking_completo': similaridades,
            'confianca': 'alta' if len(sefirot_predominantes) >= 2 else 'média',
            'texto_analisado': texto_completo[:200] + '...' if len(texto_completo) > 200 else texto_completo
        }
    
    def combinar_com_scores_numericos(self, 
                                       analise_semantica: Dict,
                                       avaliacoes_numericas: Dict[str, int]) -> Dict:
        """
        Combina análise semântica com scores numéricos
        DECISÃO DETERMINÍSTICA baseada em regras claras
        """
        orientacao = {}
        
        for item in analise_semantica.get('sefirot_predominantes', []):
            sefirah = item['sefirah']
            similaridade = item['similaridade']
            score_numerico = avaliacoes_numericas.get(sefirah, 5)
            conhecimento = item['conhecimento']
            
            if score_numerico <= 4 and similaridade > 0.55:
                prioridade = 'crítica'
                confianca = 'alta'
                acao = 'intervenção_imediata'
            elif score_numerico >= 8 and similaridade > 0.55:
                prioridade = 'atenção'
                confianca = 'alta'
                acao = 'equilibrar'
            elif score_numerico <= 4 or score_numerico >= 8:
                prioridade = 'observar'
                confianca = 'média'
                acao = 'monitorar'
            else:
                prioridade = 'manter'
                confianca = 'baixa'
                acao = 'nenhuma'
            
            orientacao[sefirah] = {
                'score_numerico': score_numerico,
                'similaridade_semantica': similaridade,
                'prioridade': prioridade,
                'confianca': confianca,
                'acao_recomendada': acao,
                'concordancia': 'sim' if (score_numerico <= 4 or score_numerico >= 8) and similaridade > 0.55 else 'parcial',
                'fonte': conhecimento.fonte,
                'pratica_corretiva': conhecimento.pratica_corretiva,
                'meditacao': conhecimento.meditacao,
                'sinal_desequilibrio': conhecimento.sinal_desequilibrio,
                'afirmacao_transformadora': conhecimento.afirmacao_transformadora,
                'exemplo_biblico': conhecimento.exemplo_biblico
            }
        
        return orientacao
    
    def _cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        """Calcula similaridade de cosseno (determinístico)"""
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def gerar_relatorio_sem_alucinacao(self, orientacao: Dict) -> str:
        """
        Gera relatório usando APENAS textos da base fechada
        ZERO geração de conteúdo novo
        """
        relatorio = "\n╔══════════════════════════════════════════════════════════════╗\n"
        relatorio += "║         🌳 ORIENTAÇÃO SEFIRÓTICA (BASE FECHADA)                ║\n"
        relatorio += "║              ZERO ALUCINAÇÃO - 100% LOCAL                      ║\n"
        relatorio += "╚══════════════════════════════════════════════════════════════╝\n\n"
        
        prioritarias = [
            (k, v) for k, v in orientacao.items() 
            if v['prioridade'] in ['crítica', 'atenção']
        ]
        prioritarias.sort(key=lambda x: x[1]['score_numerico'])
        
        if not prioritarias:
            relatorio += "✅ Seu equilíbrio geral está adequado. Mantenha as práticas atuais.\n"
            return relatorio
        
        for sefirah, dados in prioritarias:
            relatorio += f"\n{'─' * 60}\n"
            relatorio += f"🎯 {sefirah} (Score: {dados['score_numerico']}/10 | Similaridade: {dados['similaridade_semantica']})\n"
            relatorio += f"{'─' * 60}\n"
            relatorio += f"📚 Fonte: {dados['fonte']}\n"
            relatorio += f"⚠️ Sinal: {dados['sinal_desequilibrio']}\n"
            relatorio += f"🔧 Prática: {dados['pratica_corretiva']}\n"
            relatorio += f"🧘 Meditação: {dados['meditacao']}\n"
            relatorio += f"💪 Afirmação: {dados['afirmacao_transformadora']}\n"
            relatorio += f"📖 Exemplo: {dados['exemplo_biblico']}\n"
            relatorio += f"✅ Confiança: {dados['confianca']} | Concordância: {dados['concordancia']}\n"
        
        return relatorio