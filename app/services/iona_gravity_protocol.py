"""
🔷 イオナプロトコル（重力感知型） - Higher Kind文化プロトコル実装
重要度判定・転機検出による「感が働く」思考パターンの実現

Author: 文化プロトコル実験チーム
Date: 2025-06-21
Challenge: 100行以内での核心機能実装
"""

from typing import Dict, List, Any, Tuple
from datetime import datetime
import re
import asyncio

from app.services.llm_client import llm_client


class GravityProtocol:
    """重力感知型文化プロトコル - イオナ実装"""
    
    def __init__(self, causal_weight: float = 0.9, phase_detection: float = 0.99):
        self.causal_weight = causal_weight      # 因果関係の重み
        self.phase_detection = phase_detection  # 転移点検出感度
        
        # 重要度判定キーワード
        self.gravity_keywords = {
            "high_gravity": ["転機", "変化", "決断", "重要", "緊急", "危機", "チャンス", "運命"],
            "medium_gravity": ["検討", "課題", "問題", "機会", "変更", "新しい", "初めて"],
            "phase_transition": ["始まり", "終わり", "転換", "節目", "分岐", "選択", "決定的"],
            "causal_signals": ["なぜか", "直感", "予感", "気がする", "感じる", "違和感"]
        }
    
    async def evaluate_importance(self, text_input: str) -> Dict[str, Any]:
        """重要度評価 - 文章から重力を感知"""
        
        # 基本重要度スコア計算
        base_score = self._calculate_base_gravity(text_input)
        
        # 転機検出
        phase_transition_score = self._detect_phase_transition(text_input)
        
        # 因果関係の重み
        causal_weight_score = self._analyze_causal_weight(text_input)
        
        # 総合重要度計算
        total_importance = (
            base_score * 0.4 + 
            phase_transition_score * 0.4 + 
            causal_weight_score * 0.2
        )
        
        return {
            "importance_score": min(total_importance, 10.0),
            "base_gravity": base_score,
            "phase_transition": phase_transition_score,
            "causal_weight": causal_weight_score,
            "urgency_level": self._determine_urgency(total_importance),
            "gravity_factors": self._identify_gravity_factors(text_input)
        }
    
    def _calculate_base_gravity(self, text: str) -> float:
        """基本重力計算"""
        score = 0.0
        text_lower = text.lower()
        
        # 高重力キーワードチェック
        for keyword in self.gravity_keywords["high_gravity"]:
            if keyword in text_lower:
                score += 2.0
        
        # 中重力キーワードチェック  
        for keyword in self.gravity_keywords["medium_gravity"]:
            if keyword in text_lower:
                score += 1.0
                
        # 文章の長さ・複雑さ
        if len(text) > 100:
            score += 0.5
        if "?" in text or "！" in text:
            score += 0.3
            
        return min(score, 5.0)
    
    def _detect_phase_transition(self, text: str) -> float:
        """転機・相転移検出"""
        score = 0.0
        text_lower = text.lower()
        
        # 転移点キーワード
        for keyword in self.gravity_keywords["phase_transition"]:
            if keyword in text_lower:
                score += 1.5
        
        # 時間表現（変化の兆候）
        time_patterns = ["今まで", "これから", "初めて", "最後", "今後", "将来"]
        for pattern in time_patterns:
            if pattern in text_lower:
                score += 0.8
                
        return min(score * self.phase_detection, 5.0)
    
    def _analyze_causal_weight(self, text: str) -> float:
        """因果関係の重み分析"""
        score = 0.0
        text_lower = text.lower()
        
        # 直感・予感キーワード
        for keyword in self.gravity_keywords["causal_signals"]:
            if keyword in text_lower:
                score += 1.2
        
        # 因果関係表現
        causal_patterns = ["なので", "だから", "ため", "結果", "影響", "効果"]
        for pattern in causal_patterns:
            if pattern in text_lower:
                score += 0.6
                
        return min(score * self.causal_weight, 5.0)
    
    def _determine_urgency(self, importance_score: float) -> str:
        """緊急度判定"""
        if importance_score >= 8.0:
            return "critical"
        elif importance_score >= 6.0:
            return "high"
        elif importance_score >= 4.0:
            return "medium"
        else:
            return "low"
    
    def _identify_gravity_factors(self, text: str) -> List[str]:
        """重力要因特定"""
        factors = []
        text_lower = text.lower()
        
        # 各キーワードカテゴリをチェック
        for category, keywords in self.gravity_keywords.items():
            found_keywords = [kw for kw in keywords if kw in text_lower]
            if found_keywords:
                factors.append(f"{category}: {', '.join(found_keywords)}")
                
        return factors
    
    async def generate_response(self, context: str, importance_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """重要度に基づく応答生成"""
        
        importance_score = importance_analysis["importance_score"]
        urgency_level = importance_analysis["urgency_level"]
        
        # 重要度別プロンプト調整
        if urgency_level == "critical":
            gravity_prompt = "これは極めて重要で緊急性の高い状況です。慎重かつ迅速な判断が必要です。"
        elif urgency_level == "high":
            gravity_prompt = "これは重要な局面です。注意深く状況を分析し、適切な対応を検討してください。"
        elif urgency_level == "medium":
            gravity_prompt = "これは注意すべき状況です。現状を把握し、今後の展開を見守ってください。"
        else:
            gravity_prompt = "これは日常的な状況です。リラックスして自然に対応してください。"
        
        # LLMを使った応答生成
        enhanced_prompt = f"""
{gravity_prompt}

【重要度分析】
- 重要度スコア: {importance_score:.1f}/10
- 緊急度: {urgency_level}
- 重力要因: {', '.join(importance_analysis['gravity_factors'])}

【状況】
{context}

この状況に対して、重要度に応じた適切な応答・アドバイスを提供してください。
"""
        
        try:
            response = await llm_client.generate(enhanced_prompt, max_tokens=200)
            
            return {
                "gravity_response": response.strip(),
                "applied_gravity": importance_score,
                "urgency_level": urgency_level,
                "response_style": self._get_response_style(urgency_level),
                "decision_trace": {
                    "importance_factors": importance_analysis["gravity_factors"],
                    "gravity_adjustment": f"重要度{importance_score:.1f}に基づく{urgency_level}レベル応答"
                }
            }
            
        except Exception as e:
            # フォールバック応答
            return {
                "gravity_response": f"状況を{urgency_level}レベルの重要度で認識しました。慎重に対応することをお勧めします。",
                "applied_gravity": importance_score,
                "urgency_level": urgency_level,
                "response_style": "fallback",
                "error": str(e)
            }
    
    def _get_response_style(self, urgency_level: str) -> str:
        """応答スタイル決定"""
        styles = {
            "critical": "urgent_decisive",
            "high": "careful_analytical", 
            "medium": "attentive_balanced",
            "low": "relaxed_supportive"
        }
        return styles.get(urgency_level, "neutral")


# イオナプロトコル・インスタンス
iona_protocol = GravityProtocol()