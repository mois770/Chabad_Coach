"""
Módulo principal da lógica das Sefirot - Análise Numérica
MANTIDO: Usado para scores e cálculos básicos
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime
import json

@dataclass
class SefirahData:
    nome: str
    hebraico: str
    atributo: str
    pergunta_diagnostico: str
    pergunta_coaching: str
    desequilibrio_excesso: str
    desequilibrio_falta: str
    cor: str = "#FFFFFF"

class SefirotEngine:
    """Motor de análise baseado nas Sefirot (numérico)"""
    
    def __init__(self):
        self.sefirot_emocionais = {
            'Chessed': SefirahData(
                nome='Chessed', hebraico='חסד', atributo='Bondade/Expansão',
                pergunta_diagnostico='Você tem sido generoso demais ou recebido pouco reconhecimento?',
                pergunta_coaching='Onde você pode expandir sua generosidade sem se esgotar?',
                desequilibrio_excesso='Permissividade, autoanulação, doação sem limites',
                desequilibrio_falta='Frieza, egoísmo, dificuldade de acolher',
                cor='#FFB347'
            ),
            'Gevurah': SefirahData(
                nome='Gevurah', hebraico='גבורה', atributo='Força/Limite',
                pergunta_diagnostico='Você tem sido muito rígido ou tem dificuldade de estabelecer limites?',
                pergunta_coaching='Que limite saudável você precisa estabelecer ou flexibilizar?',
                desequilibrio_excesso='Rigidez, crueldade, controle excessivo',
                desequilibrio_falta='Falta de disciplina, caos, permissividade',
                cor='#FF6961'
            ),
            'Tiferet': SefirahData(
                nome='Tiferet', hebraico='תפארת', atributo='Harmonia/Compaixão',
                pergunta_diagnostico='Você consegue equilibrar dar e receber, firmeza e acolhimento?',
                pergunta_coaching='Qual caminho integra compaixão e justiça nesta situação?',
                desequilibrio_excesso='Conivência disfarçada de compaixão',
                desequilibrio_falta='Conflito interno, dificuldade de encontrar equilíbrio',
                cor='#77DD77'
            ),
            'Netzach': SefirahData(
                nome='Netzach', hebraico='נצח', atributo='Persistência/Vitória',
                pergunta_diagnostico='Você tem persistido por convicção ou por teimosia/ego?',
                pergunta_coaching='O que vale a pena manter em sua jornada de longo prazo?',
                desequilibrio_excesso='Teimosia, agressividade, dominação',
                desequilibrio_falta='Desistência fácil, falta de direção',
                cor='#AEC6CF'
            ),
            'Hod': SefirahData(
                nome='Hod', hebraico='הוד', atributo='Humildade/Reconhecimento',
                pergunta_diagnostico='Você reconhece suas conquistas e as dos outros?',
                pergunta_coaching='Onde você precisa praticar mais humildade ou autovalorização?',
                desequilibrio_excesso='Passividade, baixa autoestima, vergonha tóxica',
                desequilibrio_falta='Arrogância, dificuldade de reconhecer o outro',
                cor='#B39EB5'
            ),
            'Yesod': SefirahData(
                nome='Yesod', hebraico='יסוד', atributo='Fundação/Integridade',
                pergunta_diagnostico='Suas ações estão alinhadas com seus valores e palavras?',
                pergunta_coaching='Como garantir integridade entre intenção e ação?',
                desequilibrio_excesso='Rigidez moral, julgamento dos outros',
                desequilibrio_falta='Instabilidade, quebra de confiança, inconsistência',
                cor='#FDFD96'
            ),
            'Malchut': SefirahData(
                nome='Malchut', hebraico='מלכות', atributo='Realização/Manifestação',
                pergunta_diagnostico='Você tem conseguido concretizar seus projetos e planos?',
                pergunta_coaching='Qual passo concreto você pode dar nas próximas 48 horas?',
                desequilibrio_excesso='Arrogância, controle excessivo',
                desequilibrio_falta='Sentimento de insignificância, dificuldade de finalizar',
                cor='#FFB7CE'
            )
        }
        
        self.sefirot_intelectuais = {
            'Chochmah': {'nome': 'Chochmah', 'hebraico': 'חכמה', 'atributo': 'Sabedoria/Visão'},
            'Binah': {'nome': 'Binah', 'hebraico': 'בינה', 'atributo': 'Entendimento/Análise'},
            'Daat': {'nome': 'Daat', 'hebraico': 'דעת', 'atributo': 'Conhecimento/Conexão'}
        }
    
    def calcular_equilibrio(self, avaliacoes: Dict[str, int]) -> Dict:
        """Calcula índices de equilíbrio entre Sefirot complementares"""
        pares = [
            ('Chessed', 'Gevurah', 'Chessed-Gevurah'),
            ('Netzach', 'Hod', 'Netzach-Hod'),
            ('Yesod', 'Malchut', 'Yesod-Malchut')
        ]
        
        resultados = {}
        for sef1, sef2, nome_par in pares:
            val1 = avaliacoes.get(sef1, 5)
            val2 = avaliacoes.get(sef2, 5)
            diferenca = abs(val1 - val2)
            media = (val1 + val2) / 2
            
            resultados[nome_par] = {
                'sefirah1': sef1,
                'sefirah2': sef2,
                'valor1': val1,
                'valor2': val2,
                'diferenca': diferenca,
                'media': media,
                'equilibrado': diferenca <= 2,
                'recomendacao': self._gerar_recomendacao_par(sef1, sef2, val1, val2)
            }
        
        return resultados
    
    def _gerar_recomendacao_par(self, sef1: str, sef2: str, val1: int, val2: int) -> str:
        if val1 > val2 + 2:
            return f"Fortalecer {sef2} para equilibrar com {sef1}"
        elif val2 > val1 + 2:
            return f"Fortalecer {sef1} para equilibrar com {sef2}"
        else:
            return "Equilíbrio adequado entre estas energias"
    
    def gerar_insights(self, avaliacoes: Dict[str, int]) -> List[str]:
        """Gera insights automáticos baseados nas avaliações numéricas"""
        insights = []
        
        min_sefirot = sorted(avaliacoes.items(), key=lambda x: x[1])[:2]
        for sefirah, valor in min_sefirot:
            if valor <= 4:
                dados = self.sefirot_emocionais.get(sefirah)
                if dados:
                    insights.append(f"⚠️ {dados.nome} está baixa ({valor}/10): {dados.desequilibrio_falta}")
        
        max_sefirot = sorted(avaliacoes.items(), key=lambda x: x[1], reverse=True)[:2]
        for sefirah, valor in max_sefirot:
            if valor >= 8:
                dados = self.sefirot_emocionais.get(sefirah)
                if dados:
                    insights.append(f"📈 {dados.nome} está elevada ({valor}/10): Cuidado com {dados.desequilibrio_excesso}")
        
        if avaliacoes.get('Tiferet', 5) <= 4:
            insights.append("🎯 Tiferet baixa indica dificuldade de integração - foque em harmonizar opostos")
        
        return insights if insights else ["✅ Equilíbrio geral satisfatório - mantenha as práticas atuais"]


@dataclass
class CoachingSession:
    """Representa uma sessão completa de coaching"""
    id: str
    usuario_nome: str
    data_inicio: datetime
    topico: str
    area_vida: str
    analise_intelectual: Dict = field(default_factory=dict)
    avaliacoes_sefirot: Dict = field(default_factory=dict)
    analise_sistema: Dict = field(default_factory=dict)
    plano_acao: List[Dict] = field(default_factory=list)
    notas: str = ""
    concluida: bool = False
    data_conclusao: Optional[datetime] = None
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'usuario_nome': self.usuario_nome,
            'data_inicio': self.data_inicio.isoformat(),
            'topico': self.topico,
            'area_vida': self.area_vida,
            'analise_intelectual': self.analise_intelectual,
            'avaliacoes_sefirot': self.avaliacoes_sefirot,
            'analise_sistema': self.analise_sistema,
            'plano_acao': self.plano_acao,
            'notas': self.notas,
            'concluida': self.concluida,
            'data_conclusao': self.data_conclusao.isoformat() if self.data_conclusao else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'CoachingSession':
        return cls(
            id=data['id'],
            usuario_nome=data['usuario_nome'],
            data_inicio=datetime.fromisoformat(data['data_inicio']),
            topico=data['topico'],
            area_vida=data['area_vida'],
            analise_intelectual=data.get('analise_intelectual', {}),
            avaliacoes_sefirot=data.get('avaliacoes_sefirot', {}),
            analise_sistema=data.get('analise_sistema', {}),
            plano_acao=data.get('plano_acao', []),
            notas=data.get('notas', ''),
            concluida=data.get('concluida', False),
            data_conclusao=datetime.fromisoformat(data['data_conclusao']) if data.get('data_conclusao') else None
        )