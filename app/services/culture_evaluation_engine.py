"""
🌈 文化評価軸エンジン
Higher Kind文化プロトコルの多次元分析・品質評価・相性計算システム

Author: システンスカフェ テックチーム
Date: 2025-06-21
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import math
import numpy as np
from collections import defaultdict

from app.models.culture_simulation_base import (
    CultureProtocol, ValueToken, Meme, Practice, Myth,
    ValueCategory, PracticeContext, CultureAgent
)


class TimeHorizon(Enum):
    IMMEDIATE = "immediate"            # 即座・瞬間 (秒〜分)
    SHORT_TERM = "short_term"          # 短期 (時間〜日)
    MEDIUM_TERM = "medium_term"        # 中期 (週〜月)
    LONG_TERM = "long_term"            # 長期 (年〜decade)
    GENERATIONAL = "generational"      # 世代間 (数十年〜)
    ETERNAL = "eternal"                # 永続的・無時間的


class TrustBuildingStyle(Enum):
    INSTITUTIONAL = "institutional"    # 制度・規則ベース
    RELATIONAL = "relational"         # 関係性・人格ベース
    PERFORMANCE = "performance"        # 実績・成果ベース
    RECIPROCAL = "reciprocal"         # 相互利益ベース
    INTUITIVE = "intuitive"            # 直感・感情ベース


class CognitiveStyle(Enum):
    INTUITIVE = "intuitive"
    ANALYTICAL = "analytical"
    HOLISTIC = "holistic"
    SEQUENTIAL = "sequential"


class SocialOrientation(Enum):
    INDIVIDUALISTIC = "individualistic"
    COLLECTIVISTIC = "collectivistic"
    BALANCED = "balanced"


class CommunicationStyle(Enum):
    DIRECT = "direct"
    INDIRECT = "indirect"
    CONTEXTUAL = "contextual"
    EXPRESSIVE = "expressive"


class ListeningStyle(Enum):
    ACTIVE_PROBING = "active_probing"  # 積極的質問型
    EMPATHETIC = "empathetic"          # 共感型
    ANALYTICAL = "analytical"          # 分析型
    PATIENT = "patient"                # 忍耐型
    INTUITIVE = "intuitive"            # 直感型


class FeedbackStyle(Enum):
    DIRECT_IMMEDIATE = "direct_immediate"
    CONSTRUCTIVE_DELAYED = "constructive_delayed"
    INDIRECT_SUGGESTIVE = "indirect_suggestive"
    POSITIVE_FOCUSED = "positive_focused"
    GROWTH_ORIENTED = "growth_oriented"


@dataclass
class TimePerceptionProfile:
    """時間認識プロファイル - 時間軸・優先度の捉え方"""
    time_horizon: TimeHorizon           # 思考の時間範囲
    urgency_bias: float                 # 緊急性重視度 (0.0-1.0)
    planning_depth: float               # 計画の深さ (0.0-1.0)
    adaptive_speed: float               # 変化への適応速度 (0.0-1.0)
    cyclical_thinking: float            # 循環的思考傾向 (0.0-1.0)
    moment_awareness: float             # 現在瞬間への意識 (0.0-1.0)


@dataclass
class RelationshipModelProfile:
    """関係性モデルプロファイル - 個人vs集団、階層vs水平の価値観"""
    individualism_collectivism: float   # 個人主義←→集団主義 (-1.0 to 1.0)
    hierarchy_equality: float           # 階層重視←→平等重視 (-1.0 to 1.0)
    autonomy_interdependence: float     # 自律性←→相互依存 (-1.0 to 1.0)
    competition_cooperation: float      # 競争←→協力 (-1.0 to 1.0)
    formality_informality: float        # 形式重視←→非形式 (-1.0 to 1.0)
    trust_building: TrustBuildingStyle  # 信頼構築スタイル


@dataclass
class CognitionStyleProfile:
    """認知スタイルプロファイル - 思考・学習・問題解決のパターン"""
    analytical_holistic: float          # 分析的←→全体的 (-1.0 to 1.0)
    abstract_concrete: float            # 抽象的←→具体的 (-1.0 to 1.0)
    intuition_logic: float              # 直感←→論理 (-1.0 to 1.0)
    exploration_exploitation: float     # 探索←→活用 (-1.0 to 1.0)
    risk_tolerance: float               # リスク許容度 (0.0-1.0)
    ambiguity_tolerance: float          # 曖昧さ許容度 (0.0-1.0)


@dataclass
class CommunicationStyleProfile:
    """コミュニケーションスタイルプロファイル"""
    directness_indirectness: float      # 直接的←→間接的 (-1.0 to 1.0)
    context_dependency: float           # 文脈依存度 (0.0-1.0)
    emotional_expression: float         # 感情表現度 (0.0-1.0)
    listening_style: ListeningStyle     # 聞き方のスタイル
    feedback_style: FeedbackStyle       # フィードバックスタイル


@dataclass
class DecisionMakingProfile:
    """意思決定プロファイル"""
    consensus_autocracy: float          # 合意重視←→独断重視 (-1.0 to 1.0)
    data_intuition: float               # データ重視←→直感重視 (-1.0 to 1.0)
    speed_accuracy: float               # 速度重視←→正確性重視 (-1.0 to 1.0)
    reversibility_commitment: float     # 可逆性←→コミットメント (-1.0 to 1.0)
    stakeholder_consideration: float    # ステークホルダー考慮度 (0.0-1.0)


@dataclass
class AdaptabilityProfile:
    """適応性プロファイル"""
    learning_agility: float             # 学習俊敏性 (0.0-1.0)
    change_resilience: float            # 変化耐性 (0.0-1.0)
    innovation_openness: float          # 革新開放性 (0.0-1.0)
    tradition_respect: float            # 伝統尊重度 (0.0-1.0)
    experiment_comfort: float           # 実験への快適さ (0.0-1.0)


@dataclass
class CultureEvaluationAxis:
    """文化評価軸 - 文化プロトコルの比較分析のための多次元評価"""
    time_perception: TimePerceptionProfile
    relationship_model: RelationshipModelProfile
    cognition_style: CognitionStyleProfile
    communication_style: CommunicationStyleProfile
    decision_making: DecisionMakingProfile
    adaptability: AdaptabilityProfile


@dataclass
class CultureQualityMetrics:
    """文化品質指標"""
    coherence_score: float              # 一貫性スコア (0.0-1.0)
    complexity_score: float             # 複雑性スコア (0.0-1.0)
    adaptability_score: float           # 適応性スコア (0.0-1.0)
    innovation_potential: float         # 革新可能性 (0.0-1.0)
    stability_score: float              # 安定性スコア (0.0-1.0)
    uniqueness_score: float             # 独自性スコア (0.0-1.0)
    practical_utility: float            # 実用性スコア (0.0-1.0)
    
    @property
    def overall_quality(self) -> float:
        """総合品質スコア"""
        weights = {
            'coherence': 0.2,
            'complexity': 0.15,
            'adaptability': 0.2,
            'innovation': 0.15,
            'stability': 0.1,
            'uniqueness': 0.1,
            'utility': 0.1
        }
        
        return (
            self.coherence_score * weights['coherence'] +
            self.complexity_score * weights['complexity'] +
            self.adaptability_score * weights['adaptability'] +
            self.innovation_potential * weights['innovation'] +
            self.stability_score * weights['stability'] +
            self.uniqueness_score * weights['uniqueness'] +
            self.practical_utility * weights['utility']
        )


@dataclass
class CultureCompatibilityMatrix:
    """文化相性マトリックス"""
    culture_a_id: str
    culture_b_id: str
    compatibility_score: float          # 総合相性 (0.0-1.0)
    synergy_potential: float            # 相乗効果ポテンシャル (0.0-1.0)
    conflict_risk: float                # 対立リスク (0.0-1.0)
    
    # 詳細相性分析
    value_alignment: float              # 価値観の一致度
    practice_compatibility: float       # 様式の互換性
    communication_harmony: float        # コミュニケーションの調和
    temporal_synchronization: float     # 時間認識の同期度
    
    collaboration_recommendations: List[str]  # 協働推奨事項
    potential_challenges: List[str]           # 潜在的課題


class CultureEvaluationEngine:
    """文化評価軸エンジン"""
    
    def __init__(self):
        self.evaluation_history: List[Dict[str, Any]] = []
        self.benchmark_protocols: Dict[str, CultureProtocol] = {}
        
        # 評価基準の重み設定
        self.evaluation_weights = {
            'time_perception': 0.2,
            'relationship_model': 0.2,
            'cognition_style': 0.2,
            'communication_style': 0.15,
            'decision_making': 0.15,
            'adaptability': 0.1
        }
    
    def analyze_culture_protocol(self, protocol: CultureProtocol) -> CultureEvaluationAxis:
        """文化プロトコルの多次元分析"""
        
        # 時間認識プロファイル分析
        time_perception = self._analyze_time_perception(protocol)
        
        # 関係性モデル分析
        relationship_model = self._analyze_relationship_model(protocol)
        
        # 認知スタイル分析
        cognition_style = self._analyze_cognition_style(protocol)
        
        # コミュニケーションスタイル分析
        communication_style = self._analyze_communication_style(protocol)
        
        # 意思決定プロファイル分析
        decision_making = self._analyze_decision_making(protocol)
        
        # 適応性プロファイル分析
        adaptability = self._analyze_adaptability(protocol)
        
        return CultureEvaluationAxis(
            time_perception=time_perception,
            relationship_model=relationship_model,
            cognition_style=cognition_style,
            communication_style=communication_style,
            decision_making=decision_making,
            adaptability=adaptability
        )
    
    def _analyze_time_perception(self, protocol: CultureProtocol) -> TimePerceptionProfile:
        """時間認識の分析"""
        
        # 価値観トークンから時間認識特性を抽出
        temporal_values = [token for token in protocol.value_tokens if token.category == ValueCategory.TEMPORAL]
        
        # デフォルト値
        urgency_bias = 0.5
        planning_depth = 0.5
        adaptive_speed = 0.5
        cyclical_thinking = 0.5
        moment_awareness = 0.5
        time_horizon = TimeHorizon.MEDIUM_TERM
        
        # 時間関連キーワード分析
        for token in temporal_values:
            if "転機" in token.name or "察知" in token.name:
                urgency_bias = min(urgency_bias + token.value * 0.3, 1.0)
                adaptive_speed = min(adaptive_speed + token.value * 0.2, 1.0)
                time_horizon = TimeHorizon.SHORT_TERM
            
            if "未来" in token.name or "長期" in token.name:
                planning_depth = min(planning_depth + token.value * 0.4, 1.0)
                time_horizon = TimeHorizon.LONG_TERM
                urgency_bias = max(urgency_bias - token.value * 0.2, 0.0)
            
            if "現在" in token.name or "瞬間" in token.name:
                moment_awareness = min(moment_awareness + token.value * 0.3, 1.0)
                time_horizon = TimeHorizon.IMMEDIATE
        
        # 様式から時間認識を推定
        for practice in protocol.practices:
            if "測定" in practice.name or "分析" in practice.name:
                planning_depth = min(planning_depth + practice.frequency * 0.2, 1.0)
            
            if "即座" in practice.description or "迅速" in practice.description:
                urgency_bias = min(urgency_bias + practice.frequency * 0.2, 1.0)
        
        return TimePerceptionProfile(
            time_horizon=time_horizon,
            urgency_bias=urgency_bias,
            planning_depth=planning_depth,
            adaptive_speed=adaptive_speed,
            cyclical_thinking=cyclical_thinking,
            moment_awareness=moment_awareness
        )
    
    def _analyze_relationship_model(self, protocol: CultureProtocol) -> RelationshipModelProfile:
        """関係性モデルの分析"""
        
        # 社会的価値観を分析
        social_values = [token for token in protocol.value_tokens if token.category == ValueCategory.SOCIAL]
        
        # デフォルト値（中立）
        individualism_collectivism = 0.0
        hierarchy_equality = 0.0
        autonomy_interdependence = 0.0
        competition_cooperation = 0.0
        formality_informality = 0.0
        trust_building = TrustBuildingStyle.RELATIONAL
        
        # 社会的キーワード分析
        for token in social_values:
            if "調和" in token.name or "協力" in token.name:
                individualism_collectivism += token.value * 0.5  # より集団主義的
                competition_cooperation += token.value * 0.4     # より協力的
            
            if "個人" in token.name or "自立" in token.name:
                individualism_collectivism -= token.value * 0.5  # より個人主義的
                autonomy_interdependence -= token.value * 0.3    # より自律的
        
        # 様式から関係性モデルを推定
        for practice in protocol.practices:
            if practice.context == PracticeContext.RELATIONSHIP:
                if "共鳴" in practice.name or "調和" in practice.name:
                    individualism_collectivism += practice.frequency * 0.3
                    competition_cooperation += practice.frequency * 0.3
            
            if practice.context == PracticeContext.COMMUNICATION:
                if "直接" in practice.description:
                    formality_informality -= practice.frequency * 0.2
                elif "間接" in practice.description:
                    formality_informality += practice.frequency * 0.2
        
        # ミームから信頼構築スタイルを推定
        for meme in protocol.memes:
            if "心" in meme.content or "感じ" in meme.content:
                trust_building = TrustBuildingStyle.INTUITIVE
            elif "実績" in meme.content or "成果" in meme.content:
                trust_building = TrustBuildingStyle.PERFORMANCE
        
        # 値を-1.0〜1.0の範囲に正規化
        individualism_collectivism = max(-1.0, min(1.0, individualism_collectivism))
        hierarchy_equality = max(-1.0, min(1.0, hierarchy_equality))
        autonomy_interdependence = max(-1.0, min(1.0, autonomy_interdependence))
        competition_cooperation = max(-1.0, min(1.0, competition_cooperation))
        formality_informality = max(-1.0, min(1.0, formality_informality))
        
        return RelationshipModelProfile(
            individualism_collectivism=individualism_collectivism,
            hierarchy_equality=hierarchy_equality,
            autonomy_interdependence=autonomy_interdependence,
            competition_cooperation=competition_cooperation,
            formality_informality=formality_informality,
            trust_building=trust_building
        )
    
    def _analyze_cognition_style(self, protocol: CultureProtocol) -> CognitionStyleProfile:
        """認知スタイルの分析"""
        
        # 認知的価値観を分析
        cognitive_values = [token for token in protocol.value_tokens if token.category == ValueCategory.COGNITIVE]
        
        # デフォルト値（中立）
        analytical_holistic = 0.0
        abstract_concrete = 0.0
        intuition_logic = 0.0
        exploration_exploitation = 0.0
        risk_tolerance = 0.5
        ambiguity_tolerance = 0.5
        
        # 認知的キーワード分析
        for token in cognitive_values:
            if "直感" in token.name or "感知" in token.name:
                intuition_logic += token.value * 0.6  # より直感的
                ambiguity_tolerance = min(ambiguity_tolerance + token.value * 0.3, 1.0)
            
            if "論理" in token.name or "分析" in token.name:
                intuition_logic -= token.value * 0.6  # より論理的
                analytical_holistic -= token.value * 0.4  # より分析的
            
            if "因果" in token.name:
                analytical_holistic -= token.value * 0.3  # 因果分析は分析的
            
            if "創造" in token.name or "革新" in token.name:
                exploration_exploitation += token.value * 0.4  # より探索的
                risk_tolerance = min(risk_tolerance + token.value * 0.3, 1.0)
        
        # 様式から認知スタイルを推定
        for practice in protocol.practices:
            if "測定" in practice.name or "分析" in practice.name:
                analytical_holistic -= practice.frequency * 0.2
            
            if "観察" in practice.name or "感知" in practice.name:
                intuition_logic += practice.frequency * 0.2
                abstract_concrete += practice.frequency * 0.1  # 観察は具体的
        
        # 値を-1.0〜1.0の範囲に正規化
        analytical_holistic = max(-1.0, min(1.0, analytical_holistic))
        abstract_concrete = max(-1.0, min(1.0, abstract_concrete))
        intuition_logic = max(-1.0, min(1.0, intuition_logic))
        exploration_exploitation = max(-1.0, min(1.0, exploration_exploitation))
        
        return CognitionStyleProfile(
            analytical_holistic=analytical_holistic,
            abstract_concrete=abstract_concrete,
            intuition_logic=intuition_logic,
            exploration_exploitation=exploration_exploitation,
            risk_tolerance=risk_tolerance,
            ambiguity_tolerance=ambiguity_tolerance
        )
    
    def _analyze_communication_style(self, protocol: CultureProtocol) -> CommunicationStyleProfile:
        """コミュニケーションスタイルの分析"""
        
        # デフォルト値
        directness_indirectness = 0.0
        context_dependency = 0.5
        emotional_expression = 0.5
        listening_style = ListeningStyle.EMPATHETIC
        feedback_style = FeedbackStyle.CONSTRUCTIVE_DELAYED
        
        # 感情的価値観を分析
        emotional_values = [token for token in protocol.value_tokens if token.category == ValueCategory.EMOTIONAL]
        
        for token in emotional_values:
            if "表現" in token.name:
                emotional_expression = min(emotional_expression + token.value * 0.3, 1.0)
                directness_indirectness -= token.value * 0.2  # 表現重視は直接的
        
        # 様式からコミュニケーションスタイルを推定
        communication_practices = [p for p in protocol.practices if p.context == PracticeContext.COMMUNICATION]
        
        for practice in communication_practices:
            if "直接" in practice.description:
                directness_indirectness -= practice.frequency * 0.3
                feedback_style = FeedbackStyle.DIRECT_IMMEDIATE
            
            if "察知" in practice.description or "感知" in practice.description:
                context_dependency = min(context_dependency + practice.frequency * 0.2, 1.0)
                listening_style = ListeningStyle.INTUITIVE
        
        # ミームから感情表現度を推定
        for meme in protocol.memes:
            if "心" in meme.content or "感じ" in meme.content:
                emotional_expression = min(emotional_expression + meme.resonance * 0.2, 1.0)
        
        directness_indirectness = max(-1.0, min(1.0, directness_indirectness))
        
        return CommunicationStyleProfile(
            directness_indirectness=directness_indirectness,
            context_dependency=context_dependency,
            emotional_expression=emotional_expression,
            listening_style=listening_style,
            feedback_style=feedback_style
        )
    
    def _analyze_decision_making(self, protocol: CultureProtocol) -> DecisionMakingProfile:
        """意思決定プロファイルの分析"""
        
        # デフォルト値
        consensus_autocracy = 0.0
        data_intuition = 0.0
        speed_accuracy = 0.0
        reversibility_commitment = 0.0
        stakeholder_consideration = 0.5
        
        # 意思決定関連の様式を分析
        decision_practices = [p for p in protocol.practices if p.context == PracticeContext.DECISION_MAKING]
        
        for practice in decision_practices:
            if "直感" in practice.description:
                data_intuition += practice.frequency * 0.4
            
            if "測定" in practice.name or "分析" in practice.name:
                data_intuition -= practice.frequency * 0.3
                speed_accuracy -= practice.frequency * 0.2  # 分析は時間がかかる
            
            if "迅速" in practice.description or "即座" in practice.description:
                speed_accuracy += practice.frequency * 0.3
        
        # 関係性の価値観から合意重視度を推定
        social_values = [token for token in protocol.value_tokens if token.category == ValueCategory.SOCIAL]
        for token in social_values:
            if "調和" in token.name or "協力" in token.name:
                consensus_autocracy += token.value * 0.3
                stakeholder_consideration = min(stakeholder_consideration + token.value * 0.2, 1.0)
        
        # 値を-1.0〜1.0の範囲に正規化
        consensus_autocracy = max(-1.0, min(1.0, consensus_autocracy))
        data_intuition = max(-1.0, min(1.0, data_intuition))
        speed_accuracy = max(-1.0, min(1.0, speed_accuracy))
        reversibility_commitment = max(-1.0, min(1.0, reversibility_commitment))
        
        return DecisionMakingProfile(
            consensus_autocracy=consensus_autocracy,
            data_intuition=data_intuition,
            speed_accuracy=speed_accuracy,
            reversibility_commitment=reversibility_commitment,
            stakeholder_consideration=stakeholder_consideration
        )
    
    def _analyze_adaptability(self, protocol: CultureProtocol) -> AdaptabilityProfile:
        """適応性プロファイルの分析"""
        
        # デフォルト値
        learning_agility = 0.5
        change_resilience = 0.5
        innovation_openness = 0.5
        tradition_respect = 0.5
        experiment_comfort = 0.5
        
        # 価値観から適応性を分析
        for token in protocol.value_tokens:
            if "適応" in token.name or "変化" in token.name:
                learning_agility = min(learning_agility + token.value * 0.3, 1.0)
                change_resilience = min(change_resilience + token.value * 0.3, 1.0)
            
            if "革新" in token.name or "創造" in token.name:
                innovation_openness = min(innovation_openness + token.value * 0.4, 1.0)
                experiment_comfort = min(experiment_comfort + token.value * 0.3, 1.0)
            
            if "伝統" in token.name or "継承" in token.name:
                tradition_respect = min(tradition_respect + token.value * 0.3, 1.0)
                innovation_openness = max(innovation_openness - token.value * 0.2, 0.0)
        
        # 学習関連の様式から学習俊敏性を推定
        learning_practices = [p for p in protocol.practices if p.context == PracticeContext.LEARNING]
        for practice in learning_practices:
            learning_agility = min(learning_agility + practice.frequency * 0.2, 1.0)
        
        return AdaptabilityProfile(
            learning_agility=learning_agility,
            change_resilience=change_resilience,
            innovation_openness=innovation_openness,
            tradition_respect=tradition_respect,
            experiment_comfort=experiment_comfort
        )
    
    def calculate_quality_metrics(self, protocol: CultureProtocol) -> CultureQualityMetrics:
        """文化品質指標の計算"""
        
        # 一貫性スコア - 要素間の論理的整合性
        coherence_score = self._calculate_coherence(protocol)
        
        # 複雑性スコア - 要素の多様性と相互関係
        complexity_score = self._calculate_complexity(protocol)
        
        # 適応性スコア - 変化への対応能力
        adaptability_score = self._calculate_adaptability_score(protocol)
        
        # 革新可能性 - 新しいアイデア創出力
        innovation_potential = self._calculate_innovation_potential(protocol)
        
        # 安定性スコア - 内部構造の安定性
        stability_score = self._calculate_stability(protocol)
        
        # 独自性スコア - 他文化との差別化度
        uniqueness_score = self._calculate_uniqueness(protocol)
        
        # 実用性スコア - 実際の問題解決能力
        practical_utility = self._calculate_practical_utility(protocol)
        
        return CultureQualityMetrics(
            coherence_score=coherence_score,
            complexity_score=complexity_score,
            adaptability_score=adaptability_score,
            innovation_potential=innovation_potential,
            stability_score=stability_score,
            uniqueness_score=uniqueness_score,
            practical_utility=practical_utility
        )
    
    def _calculate_coherence(self, protocol: CultureProtocol) -> float:
        """一貫性スコアの計算"""
        coherence_factors = []
        
        # 価値観トークン間の一貫性
        if len(protocol.value_tokens) > 1:
            category_consistency = len(set(token.category for token in protocol.value_tokens)) / len(protocol.value_tokens)
            coherence_factors.append(1.0 - category_consistency)  # カテゴリが集中しているほど一貫性が高い
        
        # 様式と価値観の一貫性
        practice_value_alignment = 0.0
        for practice in protocol.practices:
            for token in protocol.value_tokens:
                if any(keyword in practice.description.lower() for keyword in token.name.lower().split()):
                    practice_value_alignment += 0.1
        
        practice_value_alignment = min(practice_value_alignment, 1.0)
        coherence_factors.append(practice_value_alignment)
        
        # ミームと価値観の一貫性
        meme_value_alignment = 0.0
        for meme in protocol.memes:
            for token in protocol.value_tokens:
                if any(keyword in meme.content.lower() for keyword in token.name.lower().split()):
                    meme_value_alignment += 0.1
        
        meme_value_alignment = min(meme_value_alignment, 1.0)
        coherence_factors.append(meme_value_alignment)
        
        return sum(coherence_factors) / len(coherence_factors) if coherence_factors else 0.5
    
    def _calculate_complexity(self, protocol: CultureProtocol) -> float:
        """複雑性スコアの計算"""
        # 要素数の多様性
        element_count = len(protocol.value_tokens) + len(protocol.memes) + len(protocol.practices) + len(protocol.myths)
        
        # 要素間の関係性の複雑さ
        relationship_complexity = 0.0
        
        # 価値観の影響度の分散
        if protocol.value_tokens:
            influence_variance = np.var([token.influence for token in protocol.value_tokens])
            relationship_complexity += influence_variance
        
        # 様式の文脈多様性
        if protocol.practices:
            context_diversity = len(set(practice.context for practice in protocol.practices)) / len(protocol.practices)
            relationship_complexity += context_diversity
        
        # 正規化
        normalized_element_count = min(element_count / 15.0, 1.0)  # 15要素で最大
        normalized_relationship = min(relationship_complexity, 1.0)
        
        return (normalized_element_count + normalized_relationship) / 2.0
    
    def _calculate_adaptability_score(self, protocol: CultureProtocol) -> float:
        """適応性スコアの計算"""
        adaptability_indicators = []
        
        # 時間関連の価値観
        temporal_values = [token for token in protocol.value_tokens if token.category == ValueCategory.TEMPORAL]
        if temporal_values:
            temporal_adaptability = sum(token.value for token in temporal_values) / len(temporal_values)
            adaptability_indicators.append(temporal_adaptability)
        
        # 学習・問題解決関連の様式
        adaptive_practices = [p for p in protocol.practices if p.context in [PracticeContext.LEARNING, PracticeContext.PROBLEM_SOLVING]]
        if adaptive_practices:
            practice_adaptability = sum(practice.frequency for practice in adaptive_practices) / len(adaptive_practices)
            adaptability_indicators.append(practice_adaptability)
        
        # 変化関連のキーワード
        change_keywords = ["変化", "適応", "転機", "進化", "成長"]
        change_relevance = 0.0
        
        for token in protocol.value_tokens:
            if any(keyword in token.name for keyword in change_keywords):
                change_relevance += token.value * 0.2
        
        for practice in protocol.practices:
            if any(keyword in practice.description for keyword in change_keywords):
                change_relevance += practice.frequency * 0.1
        
        change_relevance = min(change_relevance, 1.0)
        adaptability_indicators.append(change_relevance)
        
        return sum(adaptability_indicators) / len(adaptability_indicators) if adaptability_indicators else 0.5
    
    def _calculate_innovation_potential(self, protocol: CultureProtocol) -> float:
        """革新可能性の計算"""
        innovation_factors = []
        
        # 創造性関連の価値観
        creative_keywords = ["創造", "革新", "発明", "直感", "想像"]
        creativity_score = 0.0
        
        for token in protocol.value_tokens:
            if any(keyword in token.name for keyword in creative_keywords):
                creativity_score += token.value * token.influence
        
        creativity_score = min(creativity_score, 1.0)
        innovation_factors.append(creativity_score)
        
        # 実験・探索的な様式
        experimental_practices = [p for p in protocol.practices if "実験" in p.description or "探索" in p.description]
        if experimental_practices:
            experimental_score = sum(practice.frequency for practice in experimental_practices) / len(experimental_practices)
            innovation_factors.append(experimental_score)
        
        # ミームの新規性
        meme_innovation = 0.0
        for meme in protocol.memes:
            if meme.virality > 0.7:  # 高拡散力のミームは革新的
                meme_innovation += 0.2
        
        meme_innovation = min(meme_innovation, 1.0)
        innovation_factors.append(meme_innovation)
        
        return sum(innovation_factors) / len(innovation_factors) if innovation_factors else 0.5
    
    def _calculate_stability(self, protocol: CultureProtocol) -> float:
        """安定性スコアの計算"""
        stability_factors = []
        
        # 価値観の一貫性
        if protocol.value_tokens:
            value_stability = 1.0 - np.std([token.value for token in protocol.value_tokens])
            stability_factors.append(max(value_stability, 0.0))
        
        # 様式の頻度の安定性
        if protocol.practices:
            practice_stability = 1.0 - np.std([practice.frequency for practice in protocol.practices])
            stability_factors.append(max(practice_stability, 0.0))
        
        # 神話の影響度
        if protocol.myths:
            myth_stability = sum(myth.influence for myth in protocol.myths) / len(protocol.myths)
            stability_factors.append(myth_stability)
        
        return sum(stability_factors) / len(stability_factors) if stability_factors else 0.5
    
    def _calculate_uniqueness(self, protocol: CultureProtocol) -> float:
        """独自性スコアの計算"""
        uniqueness_factors = []
        
        # タグの独自性
        common_tags = ["experimental", "basic", "simple"]
        unique_tags = [tag for tag in protocol.tags if tag not in common_tags]
        tag_uniqueness = len(unique_tags) / len(protocol.tags) if protocol.tags else 0.0
        uniqueness_factors.append(tag_uniqueness)
        
        # 価値観の組み合わせの独自性
        value_combination_score = 0.0
        if len(protocol.value_tokens) > 1:
            category_diversity = len(set(token.category for token in protocol.value_tokens))
            value_combination_score = category_diversity / len(ValueCategory)
        
        uniqueness_factors.append(value_combination_score)
        
        # ミームの独自性
        meme_uniqueness = 0.0
        for meme in protocol.memes:
            if len(meme.content) > 20:  # 長いミームは独自性が高い
                meme_uniqueness += 0.2
        
        meme_uniqueness = min(meme_uniqueness, 1.0)
        uniqueness_factors.append(meme_uniqueness)
        
        return sum(uniqueness_factors) / len(uniqueness_factors) if uniqueness_factors else 0.5
    
    def _calculate_practical_utility(self, protocol: CultureProtocol) -> float:
        """実用性スコアの計算"""
        utility_factors = []
        
        # 様式の実用性
        practical_contexts = [PracticeContext.DECISION_MAKING, PracticeContext.PROBLEM_SOLVING, PracticeContext.COMMUNICATION]
        practical_practices = [p for p in protocol.practices if p.context in practical_contexts]
        
        if practical_practices:
            utility_score = sum(practice.frequency for practice in practical_practices) / len(practical_practices)
            utility_factors.append(utility_score)
        
        # 価値観の実用性
        practical_values = [token for token in protocol.value_tokens if token.influence > 0.7]
        if practical_values:
            value_utility = len(practical_values) / len(protocol.value_tokens)
            utility_factors.append(value_utility)
        
        return sum(utility_factors) / len(utility_factors) if utility_factors else 0.5
    
    def calculate_compatibility(self, protocol_a: CultureProtocol, protocol_b: CultureProtocol) -> CultureCompatibilityMatrix:
        """文化間相性の詳細計算"""
        
        # 各軸での分析
        axis_a = self.analyze_culture_protocol(protocol_a)
        axis_b = self.analyze_culture_protocol(protocol_b)
        
        # 価値観の一致度
        value_alignment = self._calculate_value_alignment(protocol_a, protocol_b)
        
        # 様式の互換性
        practice_compatibility = self._calculate_practice_compatibility(protocol_a, protocol_b)
        
        # コミュニケーションの調和
        communication_harmony = self._calculate_communication_harmony(axis_a.communication_style, axis_b.communication_style)
        
        # 時間認識の同期度
        temporal_synchronization = self._calculate_temporal_synchronization(axis_a.time_perception, axis_b.time_perception)
        
        # 総合相性の計算
        compatibility_score = (
            value_alignment * 0.3 +
            practice_compatibility * 0.25 +
            communication_harmony * 0.25 +
            temporal_synchronization * 0.2
        )
        
        # 相乗効果ポテンシャル
        synergy_potential = self._calculate_synergy_potential(protocol_a, protocol_b)
        
        # 対立リスク
        conflict_risk = self._calculate_conflict_risk(axis_a, axis_b)
        
        # 協働推奨事項と潜在的課題
        collaboration_recommendations = self._generate_collaboration_recommendations(axis_a, axis_b, compatibility_score)
        potential_challenges = self._identify_potential_challenges(axis_a, axis_b, conflict_risk)
        
        return CultureCompatibilityMatrix(
            culture_a_id=protocol_a.id,
            culture_b_id=protocol_b.id,
            compatibility_score=compatibility_score,
            synergy_potential=synergy_potential,
            conflict_risk=conflict_risk,
            value_alignment=value_alignment,
            practice_compatibility=practice_compatibility,
            communication_harmony=communication_harmony,
            temporal_synchronization=temporal_synchronization,
            collaboration_recommendations=collaboration_recommendations,
            potential_challenges=potential_challenges
        )
    
    def _calculate_value_alignment(self, protocol_a: CultureProtocol, protocol_b: CultureProtocol) -> float:
        """価値観の一致度計算"""
        alignment_score = 0.0
        
        # カテゴリ別の価値観比較
        for category in ValueCategory:
            values_a = [token for token in protocol_a.value_tokens if token.category == category]
            values_b = [token for token in protocol_b.value_tokens if token.category == category]
            
            if values_a and values_b:
                avg_value_a = sum(token.value for token in values_a) / len(values_a)
                avg_value_b = sum(token.value for token in values_b) / len(values_b)
                
                # 値の近さを評価
                value_distance = abs(avg_value_a - avg_value_b)
                category_alignment = 1.0 - value_distance
                alignment_score += category_alignment * 0.2  # 各カテゴリは20%の重み
        
        return max(0.0, min(1.0, alignment_score))
    
    def _calculate_practice_compatibility(self, protocol_a: CultureProtocol, protocol_b: CultureProtocol) -> float:
        """様式の互換性計算"""
        compatibility_factors = []
        
        # 文脈の重複度
        contexts_a = set(practice.context for practice in protocol_a.practices)
        contexts_b = set(practice.context for practice in protocol_b.practices)
        
        if contexts_a and contexts_b:
            context_overlap = len(contexts_a & contexts_b) / len(contexts_a | contexts_b)
            compatibility_factors.append(context_overlap)
        
        # 頻度の調和
        if protocol_a.practices and protocol_b.practices:
            freq_a = sum(practice.frequency for practice in protocol_a.practices) / len(protocol_a.practices)
            freq_b = sum(practice.frequency for practice in protocol_b.practices) / len(protocol_b.practices)
            
            freq_harmony = 1.0 - abs(freq_a - freq_b)
            compatibility_factors.append(freq_harmony)
        
        return sum(compatibility_factors) / len(compatibility_factors) if compatibility_factors else 0.5
    
    def _calculate_communication_harmony(self, comm_a: CommunicationStyleProfile, comm_b: CommunicationStyleProfile) -> float:
        """コミュニケーション調和度計算"""
        harmony_factors = []
        
        # 直接性の調和
        directness_harmony = 1.0 - abs(comm_a.directness_indirectness - comm_b.directness_indirectness) / 2.0
        harmony_factors.append(directness_harmony)
        
        # 感情表現の調和
        emotion_harmony = 1.0 - abs(comm_a.emotional_expression - comm_b.emotional_expression)
        harmony_factors.append(emotion_harmony)
        
        # 文脈依存度の調和
        context_harmony = 1.0 - abs(comm_a.context_dependency - comm_b.context_dependency)
        harmony_factors.append(context_harmony)
        
        return sum(harmony_factors) / len(harmony_factors)
    
    def _calculate_temporal_synchronization(self, time_a: TimePerceptionProfile, time_b: TimePerceptionProfile) -> float:
        """時間認識同期度計算"""
        sync_factors = []
        
        # 緊急性バイアスの同期
        urgency_sync = 1.0 - abs(time_a.urgency_bias - time_b.urgency_bias)
        sync_factors.append(urgency_sync)
        
        # 計画深度の同期
        planning_sync = 1.0 - abs(time_a.planning_depth - time_b.planning_depth)
        sync_factors.append(planning_sync)
        
        # 適応速度の同期
        adaptive_sync = 1.0 - abs(time_a.adaptive_speed - time_b.adaptive_speed)
        sync_factors.append(adaptive_sync)
        
        # 時間範囲の相性
        horizon_compatibility = 1.0 if time_a.time_horizon == time_b.time_horizon else 0.5
        sync_factors.append(horizon_compatibility)
        
        return sum(sync_factors) / len(sync_factors)
    
    def _calculate_synergy_potential(self, protocol_a: CultureProtocol, protocol_b: CultureProtocol) -> float:
        """相乗効果ポテンシャル計算"""
        synergy_factors = []
        
        # 補完的価値観
        categories_a = set(token.category for token in protocol_a.value_tokens)
        categories_b = set(token.category for token in protocol_b.value_tokens)
        
        complementary_categories = len(categories_a ^ categories_b)  # 排他的論理和
        total_categories = len(categories_a | categories_b)
        
        if total_categories > 0:
            complementarity = complementary_categories / total_categories
            synergy_factors.append(complementarity)
        
        # 様式の相乗効果
        practices_a_contexts = set(practice.context for practice in protocol_a.practices)
        practices_b_contexts = set(practice.context for practice in protocol_b.practices)
        
        if practices_a_contexts and practices_b_contexts:
            practice_complementarity = len(practices_a_contexts ^ practices_b_contexts) / len(practices_a_contexts | practices_b_contexts)
            synergy_factors.append(practice_complementarity)
        
        return sum(synergy_factors) / len(synergy_factors) if synergy_factors else 0.5
    
    def _calculate_conflict_risk(self, axis_a: CultureEvaluationAxis, axis_b: CultureEvaluationAxis) -> float:
        """対立リスク計算"""
        conflict_factors = []
        
        # 関係性モデルの対立
        relationship_conflicts = [
            abs(axis_a.relationship_model.individualism_collectivism - axis_b.relationship_model.individualism_collectivism),
            abs(axis_a.relationship_model.competition_cooperation - axis_b.relationship_model.competition_cooperation),
            abs(axis_a.relationship_model.hierarchy_equality - axis_b.relationship_model.hierarchy_equality)
        ]
        
        avg_relationship_conflict = sum(relationship_conflicts) / len(relationship_conflicts) / 2.0  # 正規化
        conflict_factors.append(avg_relationship_conflict)
        
        # 意思決定スタイルの対立
        decision_conflicts = [
            abs(axis_a.decision_making.consensus_autocracy - axis_b.decision_making.consensus_autocracy),
            abs(axis_a.decision_making.data_intuition - axis_b.decision_making.data_intuition),
            abs(axis_a.decision_making.speed_accuracy - axis_b.decision_making.speed_accuracy)
        ]
        
        avg_decision_conflict = sum(decision_conflicts) / len(decision_conflicts) / 2.0  # 正規化
        conflict_factors.append(avg_decision_conflict)
        
        return sum(conflict_factors) / len(conflict_factors)
    
    def _generate_collaboration_recommendations(self, axis_a: CultureEvaluationAxis, axis_b: CultureEvaluationAxis, compatibility: float) -> List[str]:
        """協働推奨事項生成"""
        recommendations = []
        
        if compatibility >= 0.7:
            recommendations.append("高い相性により自然な協働が期待される")
        
        # コミュニケーションスタイルに基づく推奨
        if abs(axis_a.communication_style.directness_indirectness - axis_b.communication_style.directness_indirectness) > 0.5:
            recommendations.append("コミュニケーションスタイルの違いを明確化し、相互理解を促進する")
        
        # 時間認識に基づく推奨
        if abs(axis_a.time_perception.urgency_bias - axis_b.time_perception.urgency_bias) > 0.3:
            recommendations.append("緊急性認識の違いを考慮した役割分担を設定する")
        
        # 意思決定スタイルに基づく推奨
        if abs(axis_a.decision_making.consensus_autocracy - axis_b.decision_making.consensus_autocracy) > 0.5:
            recommendations.append("意思決定プロセスを事前に合意し、混乱を回避する")
        
        return recommendations if recommendations else ["基本的な相互理解から開始することを推奨"]
    
    def _identify_potential_challenges(self, axis_a: CultureEvaluationAxis, axis_b: CultureEvaluationAxis, conflict_risk: float) -> List[str]:
        """潜在的課題の特定"""
        challenges = []
        
        if conflict_risk >= 0.6:
            challenges.append("高い対立リスクにより慎重なアプローチが必要")
        
        # 関係性モデルの課題
        if abs(axis_a.relationship_model.individualism_collectivism - axis_b.relationship_model.individualism_collectivism) > 0.6:
            challenges.append("個人主義vs集団主義の価値観対立")
        
        if abs(axis_a.relationship_model.competition_cooperation - axis_b.relationship_model.competition_cooperation) > 0.6:
            challenges.append("競争vs協力の姿勢の違い")
        
        # 認知スタイルの課題
        if abs(axis_a.cognition_style.intuition_logic - axis_b.cognition_style.intuition_logic) > 0.6:
            challenges.append("直感vs論理の思考アプローチの相違")
        
        return challenges if challenges else ["特段の課題は予測されない"]


# グローバルインスタンス
culture_evaluator = CultureEvaluationEngine()