"""
streamlit_app/utils/sefirot_guidance.py
Módulo de Orientação Sefirótica - Integrado com Análise Semântica
"""

from typing import Dict, List
from dataclasses import dataclass

@dataclass
class SefirahGuidance:
    nome: str
    significacao_profunda: str
    sinal_desequilibrio: str
    raiz_espiritual: str
    pratica_corretiva: str
    meditacao_chabad: str
    exemplo_biblico: str
    afirmacao_transformadora: str

class SefirotGuidanceEngine:
    """
    Engine de orientação baseada na sabedoria Chabad-Chassidut
    INTEGRADA com análise semântica local
    """
    
    def __init__(self):
        self.guidance_db = self._carregar_guidance()
    
    def _carregar_guidance(self) -> Dict[str, SefirahGuidance]:
        return {
            'Chessed': SefirahGuidance(
                nome='Chessed (חסד)',
                significacao_profunda='Amor divino que se expande sem limites. Não é apenas "ser bom", é espelhar o atributo de Deus de doar continuamente.',
                sinal_desequilibrio='Baixa: Frieza emocional, isolamento, dificuldade de conectar. Alta: Doação sem limites, autoanulação, permitir que outros não cresçam.',
                raiz_espiritual='Segundo o Tanya, Chessed vem da contemplação da grandeza divina. Quando você medita sobre quanto Deus lhe dá, o amor flui naturalmente.',
                pratica_corretiva='Baixa: 3 atos de bondade consciente por dia (mesmo pequenos). Alta: Antes de doar, pergunte: "Isso ajuda a pessoa a crescer ou cria dependência?"',
                meditacao_chabad='Por 5 minutos: "Deus me deu vida, respiração, oportunidades. Se Ele doa sem limite, posso aprender a doar com sabedoria."',
                exemplo_biblico='Abraão Avinu - sentava na entrada de sua tenda esperando hóspedes. Mas também estabelecia limites (circuncisão, educação de Isaac).',
                afirmacao_transformadora='"Eu dou com sabedoria, recebendo com gratidão. Meu amor é forte e tem limites saudáveis."'
            ),
            'Gevurah': SefirahGuidance(
                nome='Gevurah (גבורה)',
                significacao_profunda='Força de restrição e limite. Não é "dureza", é o poder de dizer não para proteger o sagrado.',
                sinal_desequilibrio='Baixa: Sem limites, caos, permissividade. Alta: Rigidez, controle excessivo, dificuldade de perdoar.',
                raiz_espiritual='Gevurah vem do reconhecimento de que recursos são finitos. Limites não são punição - são estrutura para o crescimento.',
                pratica_corretiva='Baixa: Estabeleça 1 limite claro esta semana. Alta: Pratique 1 ato de flexibilidade consciente.',
                meditacao_chabad='Por 5 minutos: "Meus limites me protegem e protegem os outros. Dizer não é às vezes o maior sim."',
                exemplo_biblico='Isaac Avinu - permitiu ser amarrado no altar (auto-restrição), mas também cavou poços e persistiu contra oposição.',
                afirmacao_transformadora='"Meus limites são sagrados. Eu os estabeleço com amor e os mantenho com firmeza."'
            ),
            'Tiferet': SefirahGuidance(
                nome='Tiferet (תפארת)',
                significacao_profunda='Harmonia e compaixão verdadeira. Não é "meio-termo", é integrar opostos em algo maior.',
                sinal_desequilibrio='Baixa: Conflito interno constante, dificuldade de decisão. Alta: Conivência disfarçada de compaixão.',
                raiz_espiritual='Tiferet é o atributo de Jacó - a verdade que integra. Vem de alinhar coração e mente em direção ao propósito.',
                pratica_corretiva='Quando em conflito, pergunte: "Qual ação honra tanto minha verdade quanto o bem do outro?"',
                meditacao_chabad='Por 5 minutos: "Não preciso escolher entre ser bom e ser forte. Posso ser ambos com sabedoria."',
                exemplo_biblico='Jacó Avinu - lutou com anjo e homem, integrou Chessed (Abraão) e Gevurah (Isaac) em sua alma.',
                afirmacao_transformadora='"Eu integro opostos em harmonia. Minha compaixão tem força, minha força tem compaixão."'
            ),
            'Netzach': SefirahGuidance(
                nome='Netzach (נצח)',
                significacao_profunda='Persistência e vitória duradoura. Não é teimosia, é manter direção apesar dos obstáculos.',
                sinal_desequilibrio='Baixa: Desistência fácil, falta de direção. Alta: Teimosia, agressividade, não ouvir feedback.',
                raiz_espiritual='Netzach vem da conexão com um propósito maior que os obstáculos momentâneos.',
                pratica_corretiva='Baixa: Comprometa-se com 1 projeto por 30 dias sem abandonar. Alta: Antes de insistir, pergunte: "Isso é propósito ou ego?"',
                meditacao_chabad='Por 5 minutos: "Minha persistência vem de conexão com propósito, não de necessidade de vencer."',
                exemplo_biblico='Moisés - liderou 40 anos no deserto, enfrentou Faraó e o próprio povo, sempre com direção clara.',
                afirmacao_transformadora='"Eu persisto com propósito, não com teimosia. Sei quando avançar e quando ajustar."'
            ),
            'Hod': SefirahGuidance(
                nome='Hod (הוד)',
                significacao_profunda='Humildade e reconhecimento verdadeiro. Não é auto-anulação, é ver a realidade claramente.',
                sinal_desequilibrio='Baixa: Arrogância, não reconhecer contribuições alheias. Alta: Baixa autoestima, não reconhecer próprias conquistas.',
                raiz_espiritual='Hod vem do reconhecimento de que tudo vem de Deus. Humildade não é pensar menos de si, é pensar em si menos.',
                pratica_corretiva='Baixa: Agradeça 3 pessoas especificamente esta semana. Alta: Celebre 1 conquista sua sem minimizar.',
                meditacao_chabad='Por 5 minutos: "Meus talentos são presentes. Usá-los plenamente é honrar Quem os deu."',
                exemplo_biblico='Aaron HaKohen - se alegrava com o sucesso de Moisés, sem competição. "Vejo teu sucesso e me alegro."',
                afirmacao_transformadora='"Reconheço meus dons e os dos outros. Humildade me faz maior, não menor."'
            ),
            'Yesod': SefirahGuidance(
                nome='Yesod (יסוד)',
                significacao_profunda='Fundação e integridade. É alinhar intenção, palavra e ação em uma só direção.',
                sinal_desequilibrio='Baixa: Inconsistência, quebra de confiança. Alta: Rigidez moral, julgar outros severamente.',
                raiz_espiritual='Yesod é o atributo de José - manteve integridade no Egito, entre tentações e poder.',
                pratica_corretiva='Antes de falar, pergunte: "Isso é verdade? É necessário? É gentil?" Cumpra o que promete, mesmo que pequeno.',
                meditacao_chabad='Por 5 minutos: "Minha palavra tem peso. Alinho o que penso, falo e faço."',
                exemplo_biblico='José HaTzadik - resistiu à tentação, manteve integridade na prisão e no palácio.',
                afirmacao_transformadora='"Minha integridade é minha fundação. Pensamento, palavra e ação estão alinhados."'
            ),
            'Malchut': SefirahGuidance(
                nome='Malchut (מלכות)',
                significacao_profunda='Realização e manifestação no mundo físico. Não é poder sobre outros, é trazer o divino para o concreto.',
                sinal_desequilibrio='Baixa: Muitos planos, pouca execução. Alta: Arrogância, controle excessivo sobre resultados.',
                raiz_espiritual='Malchut não tem luz própria - recebe das outras Sefirot. Realização vem de ser canal, não fonte.',
                pratica_corretiva='Baixa: Complete 1 projeto parado esta semana. Alta: Antes de agir, pergunte: "Estou servindo ou controlando?"',
                meditacao_chabad='Por 5 minutos: "Ação concreta é onde o espiritual encontra o físico. Pequenos passos manifestam grandes visões."',
                exemplo_biblico='Rei David - guerreiro, poeta, rei. Manifestou visão espiritual em reino concreto, com falhas e arrependimento.',
                afirmacao_transformadora='"Manifesto minha visão em ação concreta. Cada pequeno passo é sagrado."'
            )
        }
    
    def gerar_orientacao_completa(self, 
                                   avaliacoes: Dict[str, int], 
                                   analise_intelectual: Dict,
                                   analise_semantica: Dict = None) -> Dict:
        """
        Gera orientação completa baseada nas avaliações + análise intelectual + semântica
        """
        orientacao = {
            'sefirot_criticas': [],
            'pares_desequilibrados': [],
            'orientacao_prioritaria': '',
            'plano_espiritual': [],
            'meditacao_semanal': '',
            'texto_chassidico': '',
            'analise_semantica': analise_semantica
        }
        
        # 1. Identificar Sefirot críticas (≤4 ou ≥8)
        for sefirah, valor in avaliacoes.items():
            if valor <= 4 or valor >= 8:
                guidance = self.guidance_db.get(sefirah)
                if guidance:
                    orientacao['sefirot_criticas'].append({
                        'sefirah': sefirah,
                        'valor': valor,
                        'tipo': 'baixa' if valor <= 4 else 'elevada',
                        'guidance': guidance
                    })
        
        # 2. Identificar pares desequilibrados
        pares = [
            ('Chessed', 'Gevurah'),
            ('Netzach', 'Hod'),
            ('Yesod', 'Malchut')
        ]
        
        for sef1, sef2 in pares:
            val1 = avaliacoes.get(sef1, 5)
            val2 = avaliacoes.get(sef2, 5)
            diferenca = abs(val1 - val2)
            
            if diferenca >= 3:
                orientacao['pares_desequilibrados'].append({
                    'par': f'{sef1}-{sef2}',
                    'sef1_valor': val1,
                    'sef2_valor': val2,
                    'diferenca': diferenca,
                    'recomendacao': self._gerar_recomendacao_par(sef1, sef2, val1, val2)
                })
        
        # 3. Determinar orientação prioritária
        orientacao['orientacao_prioritaria'] = self._determinar_prioridade(orientacao, analise_semantica)
        
        # 4. Criar plano espiritual de 7 dias
        orientacao['plano_espiritual'] = self._criar_plano_semanal(orientacao, avaliacoes)
        
        # 5. Selecionar meditação semanal
        orientacao['meditacao_semanal'] = self._selecionar_meditacao(orientacao)
        
        # 6. Adicionar texto chassídico relevante
        orientacao['texto_chassidico'] = self._selecionar_texto_chassidico(orientacao)
        
        return orientacao
    
    def _gerar_recomendacao_par(self, sef1: str, sef2: str, val1: int, val2: int) -> str:
        guidance1 = self.guidance_db.get(sef1)
        guidance2 = self.guidance_db.get(sef2)
        
        if val1 > val2 + 2:
            return f"Fortalecer {sef2}: {guidance2.pratica_corretiva.split(':')[1] if ':' in guidance2.pratica_corretiva else guidance2.pratica_corretiva}"
        elif val2 > val1 + 2:
            return f"Fortalecer {sef1}: {guidance1.pratica_corretiva.split(':')[1] if ':' in guidance1.pratica_corretiva else guidance1.pratica_corretiva}"
        else:
            return "Equilíbrio adequado - manter práticas atuais"
    
    def _determinar_prioridade(self, orientacao: Dict, analise_semantica: Dict = None) -> str:
        if not orientacao['sefirot_criticas']:
            return "Seu equilíbrio geral está bom. Foque em manter as práticas atuais e aprofundar a conexão espiritual."
        
        # Se há análise semântica, usar para priorizar
        if analise_semantica and analise_semantica.get('sefirot_predominantes'):
            for item in analise_semantica['sefirot_predominantes'][:2]:
                sefirah = item['sefirah']
                for crit in orientacao['sefirot_criticas']:
                    if crit['sefirah'] == sefirah:
                        g = crit['guidance']
                        return f"🎯 PRIORIDADE: {crit['sefirah']} está {crit['tipo']} (confirmado por análise textual). {g.pratica_corretiva}"
        
        # Priorizar Tiferet se estiver crítica
        for crit in orientacao['sefirot_criticas']:
            if crit['sefirah'] == 'Tiferet':
                return f"🎯 PRIORIDADE: {crit['sefirah']} está {crit['tipo']}. Como centro integrador, isso afeta todas as outras áreas. {crit['guidance'].pratica_corretiva}"
        
        crit = orientacao['sefirot_criticas'][0]
        return f"🎯 PRIORIDADE: {crit['sefirah']} está {crit['tipo']}. {crit['guidance'].pratica_corretiva}"
    
    def _criar_plano_semanal(self, orientacao: Dict, avaliacoes: Dict) -> List[Dict]:
        plano = []
        
        sefirot_trabalho = []
        for crit in orientacao.get('sefirot_criticas', [])[:3]:
            sefirot_trabalho.append(crit['sefirah'])
        
        if not sefirot_trabalho:
            sefirot_trabalho = sorted(avaliacoes.items(), key=lambda x: x[1])[:3]
            sefirot_trabalho = [s[0] for s in sefirot_trabalho]
        
        dias = [
            "Dia 1 - Consciência",
            "Dia 2 - Ação",
            "Dia 3 - Reflexão",
            "Dia 4 - Integração",
            "Dia 5 - Expansão",
            "Dia 6 - Consolidação",
            "Dia 7 - Celebração"
        ]
        
        for i, dia in enumerate(dias):
            sefirah = sefirot_trabalho[i % len(sefirot_trabalho)]
            guidance = self.guidance_db.get(sefirah)
            
            plano.append({
                'dia': dia,
                'sefirah': sefirah,
                'pratica': guidance.pratica_corretiva if guidance else 'Reflita sobre esta área',
                'meditacao': guidance.meditacao_chabad if guidance else '5 minutos de silêncio consciente'
            })
        
        return plano
    
    def _selecionar_meditacao(self, orientacao: Dict) -> str:
        if orientacao.get('sefirot_criticas'):
            sefirah = orientacao['sefirot_criticas'][0]['sefirah']
            guidance = self.guidance_db.get(sefirah)
            return guidance.meditacao_chabad if guidance else "5 minutos de silêncio consciente"
        return "5 minutos: 'Estou em equilíbrio. Mantenho esta consciência em todas as minhas ações.'"
    
    def _selecionar_texto_chassidico(self, orientacao: Dict) -> str:
        textos = {
            'Chessed': '📖 DO TANYA (Capítulo 43): "O amor a Deus vem da contemplação de Sua grandeza e de quanto Ele nos dá continuamente. Quando meditamos sobre isso, o coração naturalmente se expande em amor."',
            'Gevurah': '📖 DO TANYA (Capítulo 9): "A restrição não é punição - é o poder de criar espaço para o sagrado crescer. Como o tzimtzum divino, nossos limites criam possibilidade."',
            'Tiferet': '📖 LIKUTEI TORAH: "A verdade verdadeira integra todos os opostos. Quando coração e mente se alinham, a alma brilha em sua completude."',
            'Netzach': '📖 DO REBBE RASHAB: "Persistência verdadeira vem de conexão com algo maior que os obstáculos. Quando você sabe POR QUE, o COMO se revela."',
            'Hod': '📖 DO BAAL SHEM TOV: "Humildade não é pensar menos de si - é pensar em si menos. Quando você reconhece a fonte de seus dons, pode usá-los plenamente."',
            'Yesod': '📖 DO TANYA (Capítulo 30): "Integridade é alinhar pensamento, palavra e ação. Cada alinhamento traz luz ao mundo."',
            'Malchut': '📖 LIKUTEI AMARIM: "O físico não é obstáculo ao espiritual - é seu recipiente. Cada ação concreta é oportunidade de trazer o divino ao mundo."'
        }
        
        if orientacao.get('sefirot_criticas'):
            sefirah = orientacao['sefirot_criticas'][0]['sefirah']
            return textos.get(sefirah, textos['Tiferet'])
        
        return textos['Tiferet']
    
    def gerar_relatorio_orientacao(self, orientacao: Dict) -> str:
        relatorio = """
╔══════════════════════════════════════════════════════════════╗
║         🌳 ORIENTAÇÃO SEFIRÓTICA - CHABAD-CHASSIDUT          ║
╚══════════════════════════════════════════════════════════════╝

"""
        relatorio += f"🎯 ORIENTAÇÃO PRIORITÁRIA\n"
        relatorio += f"{'─' * 60}\n"
        relatorio += f"{orientacao['orientacao_prioritaria']}\n\n"
        
        if orientacao['sefirot_criticas']:
            relatorio += f"⚠️ SEFIROT QUE MERECEM ATENÇÃO\n"
            relatorio += f"{'─' * 60}\n"
            for crit in orientacao['sefirot_criticas']:
                g = crit['guidance']
                relatorio += f"\n{crit['sefirah']} ({crit['valor']}/10 - {crit['tipo'].upper()})\n"
                relatorio += f"  📖 Significação: {g.significacao_profunda}\n"
                relatorio += f"  ⚠️ Sinal: {g.sinal_desequilibrio}\n"
                relatorio += f"  🔧 Prática: {g.pratica_corretiva}\n"
                relatorio += f"  💭 Afirmação: {g.afirmacao_transformadora}\n"
        
        if orientacao['pares_desequilibrados']:
            relatorio += f"\n\n⚖️ PARES DESEQUILIBRADOS\n"
            relatorio += f"{'─' * 60}\n"
            for par in orientacao['pares_desequilibrados']:
                relatorio += f"\n{par['par']}: {par['sef1_valor']} vs {par['sef2_valor']} (diferença: {par['diferenca']})\n"
                relatorio += f"  💡 {par['recomendacao']}\n"
        
        relatorio += f"\n\n📅 PLANO ESPIRITUAL DE 7 DIAS\n"
        relatorio += f"{'─' * 60}\n"
        for dia in orientacao['plano_espiritual']:
            relatorio += f"\n{dia['dia']} - {dia['sefirah']}\n"
            relatorio += f"  🛠️ Prática: {dia['pratica'][:100]}...\n"
            relatorio += f"  🧘 Meditação: {dia['meditacao'][:80]}...\n"
        
        relatorio += f"\n\n🧘 MEDITAÇÃO DA SEMANA\n"
        relatorio += f"{'─' * 60}\n"
        relatorio += f"{orientacao['meditacao_semanal']}\n"
        
        relatorio += f"\n\n📚 SABEDORIA CHASSÍDICA\n"
        relatorio += f"{'─' * 60}\n"
        relatorio += f"{orientacao['texto_chassidico']}\n"
        
        return relatorio