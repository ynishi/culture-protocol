# app/services/llm_client.py - シンプルなLLM切り替えクライアント
import os
import json
import httpx
from typing import Dict, Any, Optional
import random

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class LLMClient:
    """
    シンプルなLLM切り替えクライアント
    
    環境変数LLM_TYPEで以下を切り替え:
    - runpod: RunPod Llama API
    - openai: OpenAI API
    - mock: モックレスポンス
    """
    
    def __init__(self):
        # 環境変数を明示的に再読み込み
        from dotenv import load_dotenv
        load_dotenv(override=True)
        
        self.llm_type = os.getenv("LLM_TYPE", "mock").lower()
        
        # RunPod設定
        self.runpod_url = os.getenv("LLAMA_API_URL", "http://localhost:8080")
        self.runpod_key = os.getenv("LLAMA_API_KEY", "")
        
        # OpenAI設定
        self.openai_key = os.getenv("OPENAI_API_KEY", "")
        if OPENAI_AVAILABLE and self.openai_key:
            self.openai_client = openai.OpenAI(api_key=self.openai_key)
        else:
            self.openai_client = None
        
        print(f"LLMClient initialized with provider: {self.llm_type}")
    
    async def generate(self, prompt: str, max_tokens: int = 500) -> str:
        """
        プロンプトからテキストを生成
        
        Args:
            prompt: 入力プロンプト
            max_tokens: 最大トークン数
            
        Returns:
            生成されたテキスト
        """
        try:
            if self.llm_type == "runpod":
                return await self._runpod_generate(prompt, max_tokens)
            elif self.llm_type == "openai":
                return await self._openai_generate(prompt, max_tokens)
            else:
                return self._mock_generate(prompt)
        except Exception as e:
            print(f"LLM generation failed ({self.llm_type}): {e}")
            # フォールバックとしてモックを返す
            return self._mock_generate(prompt)
    
    async def _runpod_generate(self, prompt: str, max_tokens: int) -> str:
        """RunPod Llama APIでテキスト生成"""
        if not self.runpod_url or not self.runpod_key:
            raise ValueError("RunPod configuration missing")
        
        # RunPod Ollama API形式
        payload = {
            "model": "llama2",  # または利用可能なモデル名
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens,
                "temperature": 0.7
            }
        }
        
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.runpod_key
        }
        
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{self.runpod_url}/ollama/api/generate",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "").strip()
    
    async def _openai_generate(self, prompt: str, max_tokens: int) -> str:
        """OpenAI APIでテキスト生成"""
        if not self.openai_client:
            raise ValueError("OpenAI client not available")
        
        # OpenAI APIは同期関数なので、awaitは不要
        response = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    
    def _mock_generate(self, prompt: str) -> str:
        """モックレスポンス生成"""
        
        # Chronicle Ambient Pulse用のJSON応答
        if "環境音" in prompt and "JSON形式" in prompt:
            mock_ambient_responses = [
                {
                    "emotion": {
                        "primary": "✨わくわく",
                        "intensity": 4,
                        "color": "#ff6b6b",
                        "pulse_speed": "medium",
                        "texture": "sparkling"
                    },
                    "atmosphere": {
                        "description": "新しいアイデアの芽が育つ、創造的なエネルギーに満ちた空間です",
                        "mood_emoji": "✨💡🌟",
                        "energy_level": 8
                    },
                    "story_potential": {
                        "score": 8,
                        "moment_type": "創造の瞬間",
                        "capture_worthy": True,
                        "suggested_title": "アイデアが花開いた午後"
                    }
                },
                {
                    "emotion": {
                        "primary": "💕ほんわか",
                        "intensity": 3,
                        "color": "#4ecdc4",
                        "pulse_speed": "gentle",
                        "texture": "warm"
                    },
                    "atmosphere": {
                        "description": "穏やかな午後の光に包まれて、心地よい会話が流れています",
                        "mood_emoji": "😊☕🌅",
                        "energy_level": 6
                    },
                    "story_potential": {
                        "score": 7,
                        "moment_type": "日常の輝き",
                        "capture_worthy": True,
                        "suggested_title": "カフェに咲いた小さな花"
                    }
                },
                {
                    "emotion": {
                        "primary": "🤔深い話",
                        "intensity": 4,
                        "color": "#45b7d1",
                        "pulse_speed": "slow",
                        "texture": "deep"
                    },
                    "atmosphere": {
                        "description": "心の奥深くに響く、大切な想いが交わされる特別な時間です",
                        "mood_emoji": "🤔💭💫",
                        "energy_level": 7
                    },
                    "story_potential": {
                        "score": 9,
                        "moment_type": "心の交流",
                        "capture_worthy": True,
                        "suggested_title": "つながりを感じた瞬間"
                    }
                }
            ]
            
            # ランダムに選択してJSON文字列として返す
            selected_response = random.choice(mock_ambient_responses)
            return json.dumps(selected_response, ensure_ascii=False, indent=2)
        
        # 従来のモック応答
        mock_responses = [
            "これは感情豊かな会話ですね。温かい雰囲気が伝わってきます。",
            "とても興味深い内容です。参加者の皆さんの個性が光っています。",
            "心温まる交流が感じられる素敵な会話です。",
            "発見と学びに満ちた有意義な時間だったようですね。",
            "みんなで過ごした特別な瞬間が美しく描かれています。"
        ]
        
        # プロンプトの内容に応じて適切なレスポンスを選択
        if "感情" in prompt or "emotion" in prompt.lower():
            return "この会話からは温かい感情と親しみやすい雰囲気が感じられます。参加者同士の良好な関係性が伝わってきます。"
        elif "タイトル" in prompt or "title" in prompt.lower():
            titles = [
                "カフェで生まれた小さな発見",
                "心温まる午後の会話",
                "新しい仲間との特別な時間",
                "みんなで紡いだ美しい物語",
                "いつものカフェでの素敵な出会い"
            ]
            return random.choice(titles)
        elif "改善" in prompt or "enhance" in prompt.lower():
            return "それは、いつものカフェでのことでした。\n\n午後の柔らかな陽射しが窓から差し込む中、新しい出会いが生まれようとしていました。最初は少し緊張気味だった会話も、共通の話題が見つかると、だんだんと和やかな雰囲気に変わっていきます。\n\nお互いの笑顔が交わされる瞬間、そこには特別な温かさが生まれていました。何気ない会話の中にも、きっと大切な何かが隠されているのでしょう。\n\nそんな小さな発見が、今日もカフェの片隅で静かに輝いています。"
        else:
            return random.choice(mock_responses)
    
    def get_provider_info(self) -> Dict[str, Any]:
        """現在のプロバイダー情報を取得"""
        return {
            "provider": self.llm_type,
            "runpod_configured": bool(self.runpod_url and self.runpod_key),
            "openai_configured": bool(self.openai_client),
            "available_providers": ["runpod", "openai", "mock"]
        }

# グローバルインスタンス
llm_client = LLMClient()
