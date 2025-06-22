"""
🌈 文化プロトコル合成システム
Higher Kind文化プロトコルの合成・変換・進化システム

Author: システンスカフェ テックチーム
Date: 2025-06-21
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import random
import math

from app.models.culture_simulation_base import (
    CultureProtocol, ValueToken, Meme, Practice, Myth,
    ValueCategory, PracticeContext, CultureOrigin
)


class BlendStrategy(Enum):
    WEIGHTED_AVERAGE = "weighted_average"   # 重み付き平均
    DOMINANT_MERGE = "dominant_merge"       # 支配的要素中心
    CREATIVE_FUSION = "creative_fusion"     # 創造的融合
    SELECTIVE_COMBINE = "selective_combine"  # 選択的組み合わせ


class AmplificationTarget(Enum):
    INTUITION = "intuition"
    LOGIC = "logic"
    CREATIVITY = "creativity"
    EFFICIENCY = "efficiency"
    EMPATHY = "empathy"
    HARMONY = "harmony"
    INNOVATION = "innovation"


@dataclass
class BlendingResult:
    """合成結果"""
    new_protocol: CultureProtocol
    blend_ratio: Dict[str, float]
    strategy_used: BlendStrategy
    synthesis_notes: List[str]
    compatibility_score: float
    novelty_score: float
    timestamp: datetime


class CultureProtocolComposer:
    """文化プロトコル合成器"""
    
    def __init__(self):
        self.blend_history: List[BlendingResult] = []
        self.synthesis_templates = self._initialize_synthesis_templates()
    
    def blend_protocols(
        self,
        protocols: List[CultureProtocol],
        weights: List[float],
        strategy: BlendStrategy = BlendStrategy.CREATIVE_FUSION,
        custom_name: Optional[str] = None
    ) -> BlendingResult:
        """複数の文化プロトコルを合成"""
        
        if len(protocols) != len(weights):
            raise ValueError("プロトコル数と重みの数が一致しません")
        
        if len(protocols) < 2:
            raise ValueError("少なくとも2つのプロトコルが必要です")
        
        # 重みを正規化
        total_weight = sum(weights)
        normalized_weights = [w / total_weight for w in weights]
        
        # 戦略に基づく合成
        if strategy == BlendStrategy.WEIGHTED_AVERAGE:
            result = self._weighted_average_blend(protocols, normalized_weights)
        elif strategy == BlendStrategy.DOMINANT_MERGE:
            result = self._dominant_merge_blend(protocols, normalized_weights)
        elif strategy == BlendStrategy.CREATIVE_FUSION:
            result = self._creative_fusion_blend(protocols, normalized_weights)
        elif strategy == BlendStrategy.SELECTIVE_COMBINE:
            result = self._selective_combine_blend(protocols, normalized_weights)
        else:
            raise ValueError(f"未対応の合成戦略: {strategy}")
        
        # カスタム名の設定
        if custom_name:
            result['protocol'].name = custom_name
            result['protocol'].id = f"custom-{custom_name.lower().replace(' ', '-')}-v1"
        
        # 合成結果を記録
        blend_result = BlendingResult(
            new_protocol=result['protocol'],
            blend_ratio={protocols[i].name: normalized_weights[i] for i in range(len(protocols))},
            strategy_used=strategy,
            synthesis_notes=result['notes'],
            compatibility_score=self._calculate_compatibility_score(protocols),
            novelty_score=self._calculate_novelty_score(result['protocol'], protocols),
            timestamp=datetime.now()
        )
        
        self.blend_history.append(blend_result)
        return blend_result
    
    def _weighted_average_blend(self, protocols: List[CultureProtocol], weights: List[float]) -> Dict[str, Any]:
        """重み付き平均による合成"""
        
        # 価値観トークンの合成
        value_tokens = self._blend_value_tokens(protocols, weights, "average")
        
        # ミームの合成（簡易版）
        memes = []
        for i, protocol in enumerate(protocols):
            for meme in protocol.memes:
                # 重みに応じて選択
                if weights[i] >= 0.3:  # 30%以上の重みで採用
                    memes.append(meme)
        
        # 様式の合成（簡易版）
        practices = []
        for i, protocol in enumerate(protocols):
            for practice in protocol.practices:
                if weights[i] >= 0.3:
                    practices.append(practice)
        
        # 神話の合成（簡易版）
        myths = []
        for i, protocol in enumerate(protocols):
            for myth in protocol.myths:
                if weights[i] >= 0.3:
                    myths.append(myth)
        
        # 新しいプロトコル作成
        blended_name = " × ".join([p.name for p in protocols])
        new_protocol = CultureProtocol(
            id=f"blend-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            name=f"融合プロトコル: {blended_name}",
            description=f"重み付き平均による{len(protocols)}文化の融合",
            value_tokens=value_tokens,
            memes=memes,
            practices=practices,
            myths=myths,
            origin=CultureOrigin.SYNTHETIC,
            version="1.0.0",
            created_at=datetime.now(),
            tags=["fusion", "weighted_average"] + [tag for p in protocols for tag in p.tags]
        )
        
        return {
            'protocol': new_protocol,
            'notes': [
                f"重み付き平均により{len(protocols)}文化を融合",
                f"重み配分: {', '.join(f'{p.name}({w:.2f})' for p, w in zip(protocols, weights))}",
                "各要素の数値的平均を基に安定した合成を実現"
            ]
        }
    
    def _creative_fusion_blend(self, protocols: List[CultureProtocol], weights: List[float]) -> Dict[str, Any]:
        """創造的融合による合成"""
        
        # 価値観トークンの創造的合成
        value_tokens = self._blend_value_tokens(protocols, weights, "creative")
        
        # ミームの創造的変異
        memes = self._creative_meme_fusion(protocols, weights)
        
        # 様式の革新的組み合わせ
        practices = self._creative_practice_fusion(protocols, weights)
        
        # 神話の創造的統合
        myths = self._creative_myth_fusion(protocols, weights)
        
        # 創造的合成名
        fusion_concepts = self._generate_fusion_concepts(protocols)
        fusion_name = random.choice(fusion_concepts)
        
        new_protocol = CultureProtocol(
            id=f"creative-fusion-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            name=fusion_name,
            description=f"創造的融合により生まれた新認知様式: {', '.join(p.name for p in protocols)}の革新的統合",
            value_tokens=value_tokens,
            memes=memes,
            practices=practices,
            myths=myths,
            origin=CultureOrigin.EVOLVED,
            version="1.0.0",
            created_at=datetime.now(),
            tags=["creative_fusion", "emergent", "innovative"] + [tag for p in protocols for tag in p.tags[:2]]
        )
        
        return {
            'protocol': new_protocol,
            'notes': [
                f"創造的融合により新しい認知様式 '{fusion_name}' を創造",
                "元プロトコルの枠を超えた革新的な要素組み合わせ",
                "予期しない相乗効果による新しい文化的可能性の創発",
                f"融合概念: {', '.join(fusion_concepts[:3])}"
            ]
        }
    
    def _dominant_merge_blend(self, protocols: List[CultureProtocol], weights: List[float]) -> Dict[str, Any]:
        """支配的要素中心の合成"""
        
        # 最も重みの大きいプロトコルを基盤とする
        dominant_idx = weights.index(max(weights))
        dominant_protocol = protocols[dominant_idx]
        
        # 基盤プロトコルをベースに他の要素を追加
        value_tokens = list(dominant_protocol.value_tokens)
        memes = list(dominant_protocol.memes)
        practices = list(dominant_protocol.practices)
        myths = list(dominant_protocol.myths)
        
        # 他のプロトコルから選択的に要素を追加
        for i, protocol in enumerate(protocols):
            if i == dominant_idx:
                continue
            
            weight = weights[i]
            selection_threshold = 0.3  # 30%以上の重みで要素選択
            
            if weight >= selection_threshold:
                # 価値観の追加（重複チェック）
                for token in protocol.value_tokens[:2]:  # 上位2つまで
                    if not any(vt.name == token.name for vt in value_tokens):
                        # 重みに応じて価値を調整
                        adjusted_token = ValueToken(
                            name=token.name,
                            value=token.value * weight,
                            influence=token.influence * weight,
                            category=token.category
                        )
                        value_tokens.append(adjusted_token)
                
                # ミームの追加
                if protocol.memes:
                    selected_meme = protocol.memes[0]  # 最初のミームを採用
                    memes.append(selected_meme)
        
        new_protocol = CultureProtocol(
            id=f"dominant-merge-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            name=f"{dominant_protocol.name}拡張プロトコル",
            description=f"{dominant_protocol.name}を基盤とした多文化統合プロトコル",
            value_tokens=value_tokens,
            memes=memes,
            practices=practices,
            myths=myths,
            origin=CultureOrigin.EVOLVED,
            version="1.0.0",
            created_at=datetime.now(),
            tags=["dominant_merge", dominant_protocol.name.lower()] + [tag for p in protocols for tag in p.tags[:1]]
        )
        
        return {
            'protocol': new_protocol,
            'notes': [
                f"{dominant_protocol.name}を支配的基盤として採用",
                f"重み{weights[dominant_idx]:.2f}で基盤プロトコルの構造を維持",
                "他プロトコルから選択的に補強要素を統合",
                "安定性と一貫性を重視した段階的拡張"
            ]
        }
    
    def _selective_combine_blend(self, protocols: List[CultureProtocol], weights: List[float]) -> Dict[str, Any]:
        """選択的組み合わせによる合成"""
        
        # 各要素を個別に最適選択
        value_tokens = []
        memes = []
        practices = []
        myths = []
        
        # 価値観トークンの選択的組み合わせ
        all_value_tokens = []
        for i, protocol in enumerate(protocols):
            for token in protocol.value_tokens:
                all_value_tokens.append((token, weights[i]))
        
        # 重み付きスコアでソートして上位を選択
        all_value_tokens.sort(key=lambda x: x[0].value * x[1], reverse=True)
        selected_values = set()
        
        for token, weight in all_value_tokens[:5]:  # 上位5つまで
            if token.name not in selected_values:
                value_tokens.append(token)
                selected_values.add(token.name)
        
        # ミームの選択的組み合わせ
        all_memes = []
        for i, protocol in enumerate(protocols):
            for meme in protocol.memes:
                all_memes.append((meme, weights[i]))
        
        all_memes.sort(key=lambda x: x[0].resonance * x[1], reverse=True)
        for meme, weight in all_memes[:3]:  # 上位3つまで
            memes.append(meme)
        
        # 様式の選択的組み合わせ
        all_practices = []
        for i, protocol in enumerate(protocols):
            for practice in protocol.practices:
                all_practices.append((practice, weights[i]))
        
        all_practices.sort(key=lambda x: x[0].frequency * x[1], reverse=True)
        for practice, weight in all_practices[:4]:  # 上位4つまで
            practices.append(practice)
        
        # 神話の選択的組み合わせ
        all_myths = []
        for i, protocol in enumerate(protocols):
            for myth in protocol.myths:
                all_myths.append((myth, weights[i]))
        
        all_myths.sort(key=lambda x: x[0].influence * x[1], reverse=True)
        for myth, weight in all_myths[:2]:  # 上位2つまで
            myths.append(myth)
        
        new_protocol = CultureProtocol(
            id=f"selective-combine-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            name=f"選択統合プロトコル: {len(protocols)}文化精選",
            description="各文化から最適要素を選択的に統合した効率的認知様式",
            value_tokens=value_tokens,
            memes=memes,
            practices=practices,
            myths=myths,
            origin=CultureOrigin.SYNTHETIC,
            version="1.0.0",
            created_at=datetime.now(),
            tags=["selective", "optimized", "curated"] + [p.name.lower()[:4] for p in protocols]
        )
        
        return {
            'protocol': new_protocol,
            'notes': [
                "各文化から重み付きスコアで最適要素を選択",
                f"価値観{len(value_tokens)}、ミーム{len(memes)}、様式{len(practices)}、神話{len(myths)}を統合",
                "効率性と品質を重視した精選アプローチ",
                "冗長性を排除した洗練された文化要素構成"
            ]
        }
    
    def _blend_value_tokens(self, protocols: List[CultureProtocol], weights: List[float], method: str) -> List[ValueToken]:
        """価値観トークンの合成"""
        if method == "average":
            # カテゴリ別に平均値を計算
            category_values = {}
            category_counts = {}
            
            for i, protocol in enumerate(protocols):
                for token in protocol.value_tokens:
                    cat = token.category
                    if cat not in category_values:
                        category_values[cat] = 0.0
                        category_counts[cat] = 0.0
                    
                    category_values[cat] += token.value * weights[i]
                    category_counts[cat] += weights[i]
            
            # 平均化された価値観トークンを作成
            blended_tokens = []
            for cat, total_value in category_values.items():
                avg_value = total_value / category_counts[cat] if category_counts[cat] > 0 else 0.0
                
                blended_tokens.append(ValueToken(
                    name=f"統合{cat.value}",
                    value=min(avg_value, 1.0),
                    influence=0.7,
                    category=cat
                ))
            
            return blended_tokens
        
        elif method == "creative":
            # 創造的合成: 既存要素の組み合わせと新要素の創造
            creative_tokens = []
            
            # 高価値要素の特定
            high_value_tokens = []
            for i, protocol in enumerate(protocols):
                for token in protocol.value_tokens:
                    if token.value >= 0.8:
                        high_value_tokens.append((token, weights[i]))
            
            # 創造的価値観の生成
            if len(high_value_tokens) >= 2:
                # 2つの高価値要素から新しい価値観を創造
                token1, weight1 = high_value_tokens[0]
                token2, weight2 = high_value_tokens[1]
                
                fusion_value = min((token1.value * weight1 + token2.value * weight2) / (weight1 + weight2), 1.0)
                fusion_influence = min((token1.influence * weight1 + token2.influence * weight2) / (weight1 + weight2), 1.0)
                
                creative_tokens.append(ValueToken(
                    name=f"{token1.name}×{token2.name}融合",
                    value=fusion_value,
                    influence=fusion_influence,
                    category=token1.category  # 第一要素のカテゴリを採用
                ))
            
            # 既存の高価値要素も保持
            for token, weight in high_value_tokens[:3]:
                creative_tokens.append(ValueToken(
                    name=token.name,
                    value=token.value * 0.9,  # 少し減衰
                    influence=token.influence * weight,
                    category=token.category
                ))
            
            return creative_tokens
        
        else:
            # デフォルト: 最初のプロトコルの価値観を採用
            return protocols[0].value_tokens
    
    def _creative_meme_fusion(self, protocols: List[CultureProtocol], weights: List[float]) -> List[Meme]:
        """創造的ミーム融合"""
        fusion_memes = []
        
        # 各プロトコルから代表的ミームを選択
        representative_memes = []
        for i, protocol in enumerate(protocols):
            if protocol.memes:
                best_meme = max(protocol.memes, key=lambda m: m.resonance)
                representative_memes.append((best_meme, weights[i]))
        
        if len(representative_memes) >= 2:
            # ミーム融合の創造
            meme1, weight1 = representative_memes[0]
            meme2, weight2 = representative_memes[1]
            
            # 創造的融合ミーム
            fusion_content = self._generate_fusion_meme_content(meme1.content, meme2.content)
            fusion_memes.append(Meme(
                content=fusion_content,
                virality=(meme1.virality * weight1 + meme2.virality * weight2) / (weight1 + weight2),
                resonance=(meme1.resonance * weight1 + meme2.resonance * weight2) / (weight1 + weight2),
                origin=f"{meme1.origin} × {meme2.origin} 融合",
                mutations=[]
            ))
        
        # オリジナルミームも一部保持
        for meme, weight in representative_memes:
            if weight >= 0.3:  # 30%以上の重みなら保持
                fusion_memes.append(meme)
        
        return fusion_memes
    
    def _generate_fusion_meme_content(self, content1: str, content2: str) -> str:
        """2つのミーム内容から融合コンテンツを生成"""
        fusion_templates = [
            f"{content1}、そして{content2}",
            f"{content2}により{content1}",
            f"{content1}から{content2}へ",
            f"{content1}と{content2}の調和",
            f"心で{content1}、体で{content2}"
        ]
        return random.choice(fusion_templates)
    
    def _creative_practice_fusion(self, protocols: List[CultureProtocol], weights: List[float]) -> List[Practice]:
        """創造的様式融合"""
        fusion_practices = []
        
        # プロトコル間で様式の組み合わせを試行
        all_practices = []
        for i, protocol in enumerate(protocols):
            for practice in protocol.practices:
                all_practices.append((practice, weights[i]))
        
        # 高頻度・高重み様式を基に新様式を創造
        all_practices.sort(key=lambda x: x[0].frequency * x[1], reverse=True)
        
        if len(all_practices) >= 2:
            practice1, weight1 = all_practices[0]
            practice2, weight2 = all_practices[1]
            
            # 融合様式の創造
            fusion_practice = Practice(
                name=f"{practice1.name}+{practice2.name}統合法",
                description=f"{practice1.description}を{practice2.description}と組み合わせた統合的アプローチ",
                frequency=(practice1.frequency * weight1 + practice2.frequency * weight2) / (weight1 + weight2),
                context=practice1.context,  # より重要な文脈を採用
                triggers=practice1.triggers + practice2.triggers,
                outcomes=practice1.outcomes + practice2.outcomes
            )
            fusion_practices.append(fusion_practice)
        
        # 既存の様式も選択的に保持
        for practice, weight in all_practices[:3]:
            if weight >= 0.25:
                fusion_practices.append(practice)
        
        return fusion_practices
    
    def _creative_myth_fusion(self, protocols: List[CultureProtocol], weights: List[float]) -> List[Myth]:
        """創造的神話融合"""
        fusion_myths = []
        
        # 各プロトコルから影響力の高い神話を選択
        high_influence_myths = []
        for i, protocol in enumerate(protocols):
            for myth in protocol.myths:
                if myth.influence >= 0.7:
                    high_influence_myths.append((myth, weights[i]))
        
        if len(high_influence_myths) >= 2:
            myth1, weight1 = high_influence_myths[0]
            myth2, weight2 = high_influence_myths[1]
            
            # 融合神話の創造
            fusion_myth = Myth(
                name=f"{myth1.name}と{myth2.name}の交響",
                narrative=f"{myth1.narrative}。そして{myth2.narrative}。二つの物語が交わり、新たな伝説が生まれる。",
                symbolism=f"{myth1.symbolism}と{myth2.symbolism}の統合による全体性",
                archetypes=list(set(myth1.archetypes + myth2.archetypes)),
                influence=(myth1.influence * weight1 + myth2.influence * weight2) / (weight1 + weight2)
            )
            fusion_myths.append(fusion_myth)
        
        return fusion_myths
    
    def _generate_fusion_concepts(self, protocols: List[CultureProtocol]) -> List[str]:
        """融合概念名の生成"""
        concept_words = []
        
        # 各プロトコルからキーワードを抽出
        for protocol in protocols:
            # 名前からキーワード抽出
            if "グラヴィタ" in protocol.name:
                concept_words.extend(["重力", "引力", "核心"])
            if "デルタ" in protocol.name:
                concept_words.extend(["変化", "差分", "転換"])
            if "カドミオン" in protocol.name:
                concept_words.extend(["共鳴", "振動", "調和"])
            
            # 価値観から概念抽出
            for token in protocol.value_tokens:
                if "直感" in token.name:
                    concept_words.extend(["直感", "感知", "察知"])
                if "因果" in token.name:
                    concept_words.extend(["因果", "連鎖", "結果"])
        
        # 創造的組み合わせ
        fusion_concepts = [
            f"{concept_words[0]}×{concept_words[1]}プロトコル" if len(concept_words) >= 2 else "融合プロトコル",
            f"統合{concept_words[0]}システム" if concept_words else "統合システム",
            f"新世代{concept_words[0]}認知" if concept_words else "新世代認知",
            f"{concept_words[0]}ハイブリッド" if concept_words else "ハイブリッド",
            f"進化型{concept_words[0]}様式" if concept_words else "進化型様式"
        ]
        
        return fusion_concepts
    
    def _calculate_compatibility_score(self, protocols: List[CultureProtocol]) -> float:
        """プロトコル間の相性スコア計算"""
        if len(protocols) < 2:
            return 1.0
        
        total_compatibility = 0.0
        pair_count = 0
        
        for i in range(len(protocols)):
            for j in range(i + 1, len(protocols)):
                compatibility = self._calculate_pair_compatibility(protocols[i], protocols[j])
                total_compatibility += compatibility
                pair_count += 1
        
        return total_compatibility / pair_count if pair_count > 0 else 0.0
    
    def _calculate_pair_compatibility(self, protocol1: CultureProtocol, protocol2: CultureProtocol) -> float:
        """2つのプロトコル間の相性計算"""
        compatibility_factors = []
        
        # 価値観カテゴリの重複度
        cats1 = set(token.category for token in protocol1.value_tokens)
        cats2 = set(token.category for token in protocol2.value_tokens)
        category_overlap = len(cats1 & cats2) / len(cats1 | cats2) if cats1 | cats2 else 0.0
        compatibility_factors.append(category_overlap)
        
        # 様式文脈の重複度
        contexts1 = set(practice.context for practice in protocol1.practices)
        contexts2 = set(practice.context for practice in protocol2.practices)
        context_overlap = len(contexts1 & contexts2) / len(contexts1 | contexts2) if contexts1 | contexts2 else 0.0
        compatibility_factors.append(context_overlap)
        
        # タグの重複度
        tags1 = set(protocol1.tags)
        tags2 = set(protocol2.tags)
        tag_overlap = len(tags1 & tags2) / len(tags1 | tags2) if tags1 | tags2 else 0.0
        compatibility_factors.append(tag_overlap)
        
        return sum(compatibility_factors) / len(compatibility_factors)
    
    def _calculate_novelty_score(self, new_protocol: CultureProtocol, source_protocols: List[CultureProtocol]) -> float:
        """新規性スコア計算"""
        novelty_factors = []
        
        # 新しい価値観の割合
        new_value_names = set(token.name for token in new_protocol.value_tokens)
        source_value_names = set()
        for protocol in source_protocols:
            source_value_names.update(token.name for token in protocol.value_tokens)
        
        new_values_ratio = len(new_value_names - source_value_names) / len(new_value_names) if new_value_names else 0.0
        novelty_factors.append(new_values_ratio)
        
        # 新しいミームの割合
        new_meme_contents = set(meme.content for meme in new_protocol.memes)
        source_meme_contents = set()
        for protocol in source_protocols:
            source_meme_contents.update(meme.content for meme in protocol.memes)
        
        new_memes_ratio = len(new_meme_contents - source_meme_contents) / len(new_meme_contents) if new_meme_contents else 0.0
        novelty_factors.append(new_memes_ratio)
        
        # 要素組み合わせの複雑さ
        element_count = len(new_protocol.value_tokens) + len(new_protocol.memes) + len(new_protocol.practices) + len(new_protocol.myths)
        complexity_score = min(element_count / 10.0, 1.0)  # 10要素で最大
        novelty_factors.append(complexity_score)
        
        return sum(novelty_factors) / len(novelty_factors)
    
    def amplify_aspect(
        self,
        protocol: CultureProtocol,
        target: AmplificationTarget,
        intensity: float = 1.5
    ) -> CultureProtocol:
        """特定の側面を増幅"""
        
        # 元プロトコルのコピーを作成
        amplified_protocol = CultureProtocol(
            id=f"{protocol.id}-amplified-{target.value}",
            name=f"{protocol.name}（{target.value}増幅）",
            description=f"{protocol.description} - {target.value}を{intensity}倍に増幅",
            value_tokens=list(protocol.value_tokens),
            memes=list(protocol.memes),
            practices=list(protocol.practices),
            myths=list(protocol.myths),
            origin=CultureOrigin.EVOLVED,
            version=f"{protocol.version}+{target.value}",
            created_at=datetime.now(),
            tags=protocol.tags + [f"amplified_{target.value}"]
        )
        
        # 対象に応じた増幅
        if target == AmplificationTarget.INTUITION:
            self._amplify_intuition(amplified_protocol, intensity)
        elif target == AmplificationTarget.LOGIC:
            self._amplify_logic(amplified_protocol, intensity)
        elif target == AmplificationTarget.CREATIVITY:
            self._amplify_creativity(amplified_protocol, intensity)
        # 他の増幅タイプも同様に実装可能
        
        return amplified_protocol
    
    def _amplify_intuition(self, protocol: CultureProtocol, intensity: float):
        """直感の増幅"""
        for token in protocol.value_tokens:
            if "直感" in token.name or "感知" in token.name:
                token.value = min(token.value * intensity, 1.0)
                token.influence = min(token.influence * intensity, 1.0)
    
    def _amplify_logic(self, protocol: CultureProtocol, intensity: float):
        """論理の増幅"""
        for token in protocol.value_tokens:
            if "論理" in token.name or "分析" in token.name:
                token.value = min(token.value * intensity, 1.0)
                token.influence = min(token.influence * intensity, 1.0)
    
    def _amplify_creativity(self, protocol: CultureProtocol, intensity: float):
        """創造性の増幅"""
        for token in protocol.value_tokens:
            if "創造" in token.name or "発想" in token.name:
                token.value = min(token.value * intensity, 1.0)
                token.influence = min(token.influence * intensity, 1.0)
    
    def _initialize_synthesis_templates(self) -> Dict[str, Any]:
        """合成テンプレートの初期化"""
        return {
            "naming_patterns": [
                "{name1}×{name2}プロトコル",
                "統合{concept}システム",
                "新世代{attribute}認知",
                "{element}ハイブリッド",
                "進化型{characteristic}様式"
            ],
            "description_templates": [
                "{source1}と{source2}の革新的融合による新認知様式",
                "{concept}に特化した統合文化プロトコル",
                "複数文化の最適要素を統合した効率的思考システム"
            ]
        }
    
    def get_blend_recommendations(self, protocols: List[CultureProtocol]) -> List[Dict[str, Any]]:
        """推奨合成パターンの提案"""
        recommendations = []
        
        # 相性の良い組み合わせを特定
        for i in range(len(protocols)):
            for j in range(i + 1, len(protocols)):
                compatibility = self._calculate_pair_compatibility(protocols[i], protocols[j])
                
                if compatibility >= 0.3:  # 30%以上の相性
                    recommendations.append({
                        "protocols": [protocols[i].name, protocols[j].name],
                        "compatibility_score": compatibility,
                        "recommended_strategy": BlendStrategy.CREATIVE_FUSION if compatibility >= 0.6 else BlendStrategy.SELECTIVE_COMBINE,
                        "suggested_weights": [0.6, 0.4] if compatibility >= 0.6 else [0.5, 0.5],
                        "expected_benefits": self._predict_blend_benefits(protocols[i], protocols[j], compatibility)
                    })
        
        # 相性順にソート
        recommendations.sort(key=lambda x: x["compatibility_score"], reverse=True)
        return recommendations[:5]  # 上位5つまで
    
    def _predict_blend_benefits(self, protocol1: CultureProtocol, protocol2: CultureProtocol, compatibility: float) -> List[str]:
        """合成による期待効果の予測"""
        benefits = []
        
        if compatibility >= 0.7:
            benefits.append("高い相性による安定した融合効果")
        
        # 価値観の補完性チェック
        cats1 = set(token.category for token in protocol1.value_tokens)
        cats2 = set(token.category for token in protocol2.value_tokens)
        
        if ValueCategory.COGNITIVE in cats1 and ValueCategory.EMOTIONAL in cats2:
            benefits.append("認知と感情のバランス取れた統合")
        
        if ValueCategory.TEMPORAL in cats1 and ValueCategory.SOCIAL in cats2:
            benefits.append("時間認識と社会性の相乗効果")
        
        # 様式の多様性
        contexts1 = set(practice.context for practice in protocol1.practices)
        contexts2 = set(practice.context for practice in protocol2.practices)
        
        if len(contexts1 | contexts2) >= 3:
            benefits.append("多様な文脈での適用可能性")
        
        return benefits if benefits else ["基本的な文化要素の統合効果"]


# グローバルインスタンス
culture_composer = CultureProtocolComposer()