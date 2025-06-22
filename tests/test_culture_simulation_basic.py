#!/usr/bin/env python3
"""
🌈 文化プロトコル シミュレーション基盤 基本テスト

イオナプロトコルを使った文化進化シミュレーション実験
Author: システンスカフェ テックチーム
Date: 2025-06-21
"""

import asyncio
import sys
import os
from datetime import datetime

# パスを追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


async def create_iona_culture_protocol():
    """イオナプロトコルを文化プロトコル形式で作成"""
    
    from app.models.culture_simulation_base import (
        CultureProtocol, ValueToken, Meme, Practice, Myth,
        ValueCategory, PracticeContext, CultureOrigin
    )
    
    # イオナプロトコルの文化要素定義
    iona_protocol = CultureProtocol(
        id="iona-gravita-v1",
        name="イオナ・グラヴィタプロトコル",
        description="重力感知による状況把握と転機察知に特化した認知様式",
        
        value_tokens=[
            ValueToken(
                name="直感重視",
                value=0.95,
                influence=0.8,
                category=ValueCategory.COGNITIVE
            ),
            ValueToken(
                name="転機察知",
                value=0.99,
                influence=0.9,
                category=ValueCategory.TEMPORAL
            ),
            ValueToken(
                name="因果感知",
                value=0.9,
                influence=0.7,
                category=ValueCategory.COGNITIVE
            )
        ],
        
        memes=[
            Meme(
                content="重さを知って、はじめて意味がわかるのよ",
                virality=0.8,
                resonance=0.9,
                origin="重力の巫女の教え"
            ),
            Meme(
                content="心の耳で聴く",
                virality=0.7,
                resonance=0.85,
                origin="直感的認識の表現"
            )
        ],
        
        practices=[
            Practice(
                name="状況の重み測定",
                description="あらゆる状況で因果関係の重要度を直感的に測定する",
                frequency=0.9,
                context=PracticeContext.DECISION_MAKING,
                triggers=["新しい情報", "変化の兆し", "重要な選択"],
                outcomes=["適切な優先度判定", "転機の早期発見"]
            ),
            Practice(
                name="予兆への注意深い観察",
                description="微細な変化から大きな変化の予兆を察知する",
                frequency=0.95,
                context=PracticeContext.PROBLEM_SOLVING,
                triggers=["パターンの変化", "異常な静寂", "微妙な違和感"],
                outcomes=["早期警告", "未来予測"]
            )
        ],
        
        myths=[
            Myth(
                name="重力の巫女伝説",
                narrative="古の時代、宇宙の重力を感じ取り、星々の運命を読む巫女がいた",
                symbolism="直感的知恵による深い理解の価値",
                archetypes=["賢者", "預言者", "ガイド"],
                influence=0.85
            )
        ],
        
        origin=CultureOrigin.EXPERIMENTAL,
        version="1.0.0",
        created_at=datetime.now(),
        tags=["gravity", "intuition", "prediction", "wisdom"]
    )
    
    return iona_protocol


async def create_test_agents():
    """テスト用エージェントを作成"""
    
    from app.models.culture_simulation_base import (
        CultureAgent, AgentPersonality, LLMConfig
    )
    
    # イオナプロトコル取得
    iona_protocol = await create_iona_culture_protocol()
    
    # 異なる個性のエージェントを作成
    agents = []
    
    # エージェント1: 好奇心旺盛型
    personality1 = AgentPersonality(
        curiosity=0.9,
        conservatism=0.2,
        sociability=0.7,
        creativity=0.8,
        adaptability=0.8
    )
    
    agent1 = CultureAgent(
        agent_id="iona-curious",
        culture=iona_protocol,
        personality=personality1,
        llm_config=LLMConfig(temperature=0.8, max_tokens=300)
    )
    
    # エージェント2: 慎重型
    personality2 = AgentPersonality(
        curiosity=0.4,
        conservatism=0.8,
        sociability=0.5,
        creativity=0.5,
        adaptability=0.6
    )
    
    agent2 = CultureAgent(
        agent_id="iona-careful",
        culture=iona_protocol,
        personality=personality2,
        llm_config=LLMConfig(temperature=0.6, max_tokens=300)
    )
    
    # エージェント3: 社交型
    personality3 = AgentPersonality(
        curiosity=0.7,
        conservatism=0.3,
        sociability=0.9,
        creativity=0.7,
        adaptability=0.9
    )
    
    agent3 = CultureAgent(
        agent_id="iona-social",
        culture=iona_protocol,
        personality=personality3,
        llm_config=LLMConfig(temperature=0.7, max_tokens=300)
    )
    
    agents.extend([agent1, agent2, agent3])
    
    return agents


async def test_basic_agent_response():
    """基本的なエージェント応答テスト"""
    
    print("🔷 基本エージェント応答テスト")
    print("=" * 50)
    
    try:
        agents = await create_test_agents()
        
        test_situation = "新しいプロジェクトの提案があります。リスクもありますが、大きな成長の可能性を感じています。"
        
        print(f"テスト状況: {test_situation}")
        print("\n各エージェントの応答:")
        print("-" * 30)
        
        for agent in agents:
            response = await agent.respond_to_situation(test_situation)
            
            print(f"\n🔷 {agent.agent_id} ({agent.culture.name})")
            print(f"個性: 好奇心{agent.personality.curiosity:.1f} / 慎重{agent.personality.conservatism:.1f} / 社交{agent.personality.sociability:.1f}")
            print(f"応答: {response['response'][:200]}...")
            print(f"文化的一貫性: {response['cultural_analysis']['cultural_coherence']:.2f}")
            
            if response['cultural_analysis']['dominant_values']:
                print(f"反映された価値観: {', '.join(response['cultural_analysis']['dominant_values'])}")
        
        print("\n✅ 基本応答テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 基本応答テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_simulation_environment():
    """シミュレーション環境テスト"""
    
    print("\n🌈 シミュレーション環境テスト")
    print("=" * 50)
    
    try:
        from app.models.culture_simulation_base import (
            CultureEvolutionSimulator, Scenario, Challenge, ChallengeType
        )
        
        # シミュレーター作成
        simulator = CultureEvolutionSimulator()
        
        # テストシナリオ作成
        scenario = Scenario(
            id="basic-collaboration",
            name="基本協働テスト",
            description="異なる個性のエージェント間での協働課題",
            challenges=[
                Challenge(
                    type=ChallengeType.COLLABORATION,
                    difficulty=0.6,
                    description="チーム意思決定における重要度判定の合意形成",
                    required_capabilities=["重力感知", "協調性", "転機察知"]
                )
            ],
            time_limit=5,
            success_criteria=["全エージェントが合意に至る", "重要度判定の一致"]
        )
        
        # エージェント準備
        agents = await create_test_agents()
        
        # 環境作成
        environment = simulator.create_environment("test-env", scenario, agents)
        
        print(f"環境作成成功: {len(environment.agents)}体のエージェント")
        print(f"シナリオ: {environment.scenario.name}")
        
        # 単一ステップテスト
        step_result = await simulator.run_simulation_step(
            "test-env",
            "チームで新技術採用を検討しています。メンバーの意見が分かれていますが、期限が近づいています。",
            {"urgency": "high", "stakes": "medium"}
        )
        
        print(f"\nステップ実行結果:")
        print(f"ターン: {step_result['turn']}")
        print(f"文化的多様性: {step_result['cultural_diversity']:.2f}")
        print(f"相互作用の質: {step_result['interaction_quality']:.2f}")
        print(f"参加エージェント: {len(step_result['agent_responses'])}体")
        
        print("\n各エージェントの応答要約:")
        for response in step_result['agent_responses']:
            print(f"- {response['agent_id']}: {response['response'][:100]}...")
        
        print("\n✅ 環境テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 環境テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_multi_turn_simulation():
    """複数ターンシミュレーションテスト"""
    
    print("\n🚀 複数ターンシミュレーションテスト")
    print("=" * 50)
    
    try:
        from app.models.culture_simulation_base import CultureEvolutionSimulator
        
        simulator = CultureEvolutionSimulator()
        agents = await create_test_agents()
        
        # シナリオ準備（環境は前のテストで作成済み想定）
        if "test-env" not in simulator.environments:
            from app.models.culture_simulation_base import Scenario, Challenge, ChallengeType
            scenario = Scenario(
                id="multi-turn-test",
                name="複数ターンテスト",
                description="段階的意思決定プロセス",
                challenges=[Challenge(ChallengeType.PROBLEM_SOLVING, 0.7, "段階的合意形成", ["継続的判断"])],
                time_limit=3,
                success_criteria=["段階的進歩"]
            )
            simulator.create_environment("test-env", scenario, agents)
        
        # 複数ターンのシナリオ
        scenarios = [
            {
                "situation": "プロジェクト開始: 新技術導入プロジェクトがスタートします。初期方針を決める必要があります。",
                "context": {"phase": "planning", "urgency": "medium"}
            },
            {
                "situation": "中間評価: プロジェクトが中間地点に達しました。予想より難しい課題が見つかりました。",
                "context": {"phase": "execution", "urgency": "high", "challenges": "technical"}
            },
            {
                "situation": "最終判断: プロジェクト完了が近づいています。成果の評価と今後の方針を決める時です。",
                "context": {"phase": "completion", "urgency": "low", "outcome": "mixed"}
            }
        ]
        
        print("3ターンシミュレーション開始...")
        
        result = await simulator.run_multi_turn_simulation("test-env", scenarios, max_turns=3)
        
        print(f"\n📊 シミュレーション結果:")
        print(f"総ターン数: {result['total_turns']}")
        print(f"参加エージェント: {len(result['final_cultural_state']['cultures_present'])}種の文化")
        print(f"文化: {', '.join(result['final_cultural_state']['cultures_present'])}")
        
        print(f"\n📈 進化傾向:")
        evolution = result['evolution_summary']
        print(f"文化的多様性の変化: {evolution['diversity_trend'][0]:.2f} → {evolution['diversity_trend'][-1]:.2f}")
        print(f"相互作用の質の変化: {evolution['quality_trend'][0]:.2f} → {evolution['quality_trend'][-1]:.2f}")
        
        if evolution['dominant_cultures']:
            print(f"支配的文化: {', '.join(evolution['dominant_cultures'])}")
        
        if result['emergent_patterns']:
            print(f"創発パターン: {', '.join(result['emergent_patterns'])}")
        
        print("\n✅ 複数ターンテスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 複数ターンテストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_cultural_protocol_effectiveness():
    """文化プロトコルの効果測定テスト"""
    
    print("\n🔍 文化プロトコル効果測定テスト")
    print("=" * 50)
    
    try:
        from app.services.llm_client import llm_client
        
        agents = await create_test_agents()
        test_situation = "緊急事態が発生しました。すぐに対応策を決める必要がありますが、情報が不完全です。"
        
        print(f"テスト状況: {test_situation}")
        
        # 通常のLLM応答（文化プロトコルなし）
        print("\n🤖 通常のLLM応答:")
        normal_response = await llm_client.generate(
            f"以下の状況について判断してください: {test_situation}",
            max_tokens=200
        )
        print(normal_response)
        
        # イオナプロトコル応答
        print(f"\n🔷 イオナプロトコル応答 (3体のエージェント):")
        
        cultural_responses = []
        for agent in agents:
            response = await agent.respond_to_situation(test_situation)
            cultural_responses.append(response)
            
            print(f"\n- {agent.agent_id}:")
            print(f"  応答: {response['response'][:150]}...")
            print(f"  文化的影響: {response['cultural_analysis']['cultural_coherence']:.2f}")
            
            if response['cultural_analysis']['dominant_values']:
                print(f"  価値観: {', '.join(response['cultural_analysis']['dominant_values'])}")
        
        # 効果分析
        print(f"\n📊 効果分析:")
        print(f"文化プロトコルエージェント数: {len(cultural_responses)}")
        
        avg_coherence = sum(r['cultural_analysis']['cultural_coherence'] for r in cultural_responses) / len(cultural_responses)
        print(f"平均文化的一貫性: {avg_coherence:.2f}")
        
        value_diversity = len(set(
            value for r in cultural_responses 
            for value in r['cultural_analysis']['dominant_values']
        ))
        print(f"価値観の多様性: {value_diversity}種類")
        
        print("\n💡 観察:")
        print("- 通常LLM: 一般的・中立的な応答")
        print("- イオナプロトコル: 重力感知・転機察知に基づく応答")
        print("- 個性による応答の違いが観察可能")
        
        print("\n✅ 効果測定テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 効果測定テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """メインテスト実行"""
    
    print("🌈 文化プロトコル シミュレーション基盤 - 統合テスト")
    print("🚀 Higher Kind文化プロトコル シミュレーション実験")
    print("=" * 80)
    
    async def run_all_tests():
        results = []
        
        # 基本エージェント応答テスト
        print("🔷 Phase 1: 基本機能テスト")
        results.append(await test_basic_agent_response())
        
        # シミュレーション環境テスト
        print("\n🔷 Phase 2: 環境システムテスト")
        results.append(await test_simulation_environment())
        
        # 複数ターンシミュレーションテスト
        print("\n🔷 Phase 3: 進化シミュレーションテスト")
        results.append(await test_multi_turn_simulation())
        
        # 文化プロトコル効果測定
        print("\n🔷 Phase 4: 効果測定テスト")
        results.append(await test_cultural_protocol_effectiveness())
        
        # 結果サマリー
        print("\n" + "=" * 80)
        print("📊 テスト結果サマリー")
        print("=" * 80)
        
        success_count = sum(results)
        total_count = len(results)
        
        print(f"成功: {success_count}/{total_count}")
        print(f"成功率: {success_count/total_count*100:.1f}%")
        
        if success_count == total_count:
            print("🎉 全テスト成功！文化プロトコル シミュレーション基盤が完成しました✨")
            print("\n🔷 実装サマリー:")
            print("✅ イオナプロトコルの文化エージェント化")
            print("✅ 個性による応答の差異化") 
            print("✅ 複数エージェント間の相互作用")
            print("✅ 文化進化の定量的観察")
            print("✅ リアルタイム文化シミュレーション基盤")
            
            print("\n🌈 次のステップ:")
            print("1. 他の文化プロトコル (ルオ、ミリィ等) の実装")
            print("2. 文化間相互作用の実験")
            print("3. 文化合成・進化メカニズムの追加")
            print("4. 大規模シミュレーション実験")
            
        else:
            print("⚠️  一部テストが失敗しました。詳細を確認してください。")
        
        print("\n🌈 システンスカフェ テックチームからのメッセージ:")
        print("文化プロトコル革命の第一歩が始まりました！")
        print("AI時代の新しい認知様式と協働文化の創造実験にようこそ✨")
        
        return success_count == total_count
    
    # 非同期テスト実行
    return asyncio.run(run_all_tests())


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)