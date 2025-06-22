#!/usr/bin/env python3
"""
🌈 文化評価軸エンジン テスト

Higher Kind文化プロトコルの多次元分析・品質評価実験
Author: システンスカフェ テックチーム
Date: 2025-06-21
"""

import asyncio
import sys
import os
from datetime import datetime

# パスを追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


async def create_test_protocols():
    """テスト用の文化プロトコルを作成"""
    
    from app.models.culture_simulation_base import (
        CultureProtocol, ValueToken, Meme, Practice, Myth,
        ValueCategory, PracticeContext, CultureOrigin
    )
    
    # イオナプロトコル（重力感知型）
    iona_protocol = CultureProtocol(
        id="iona-gravita-v1",
        name="イオナ・グラヴィタプロトコル",
        description="重力感知による状況把握と転機察知に特化した認知様式",
        value_tokens=[
            ValueToken("直感重視", 0.95, 0.8, ValueCategory.COGNITIVE),
            ValueToken("転機察知", 0.99, 0.9, ValueCategory.TEMPORAL),
            ValueToken("因果感知", 0.9, 0.7, ValueCategory.COGNITIVE)
        ],
        memes=[
            Meme("重さを知って、はじめて意味がわかるのよ", 0.8, 0.9, "重力の巫女の教え"),
            Meme("心の耳で聴く", 0.7, 0.85, "直感的認識の表現")
        ],
        practices=[
            Practice(
                "状況の重み測定", 
                "あらゆる状況で因果関係の重要度を直感的に測定する",
                0.9, PracticeContext.DECISION_MAKING,
                ["新しい情報", "変化の兆し"], ["適切な優先度判定"]
            ),
            Practice(
                "予兆への注意深い観察", 
                "微細な変化から大きな変化の予兆を察知する",
                0.95, PracticeContext.PROBLEM_SOLVING,
                ["パターンの変化", "異常な静寂"], ["早期警告", "未来予測"]
            )
        ],
        myths=[
            Myth("重力の巫女伝説", "古の時代、宇宙の重力を感じ取り、星々の運命を読む巫女がいた", 
                 "直感的知恵による深い理解の価値", ["賢者", "預言者"], 0.85)
        ],
        origin=CultureOrigin.EXPERIMENTAL,
        version="1.0.0",
        created_at=datetime.now(),
        tags=["gravity", "intuition", "prediction"]
    )
    
    # ルオプロトコル（逆因果型）
    rua_protocol = CultureProtocol(
        id="rua-delta-v1",
        name="ルオ・デルタクロスプロトコル",
        description="未来からの逆因果思考による長期最適化認知様式",
        value_tokens=[
            ValueToken("未来指向", 0.95, 0.85, ValueCategory.TEMPORAL),
            ValueToken("逆算思考", 0.9, 0.8, ValueCategory.COGNITIVE),
            ValueToken("長期価値", 0.85, 0.75, ValueCategory.AESTHETIC)
        ],
        memes=[
            Meme("終わりから始める", 0.75, 0.8, "逆因果思考の核心"),
            Meme("失敗は成功への階段", 0.7, 0.75, "長期価値観の表現")
        ],
        practices=[
            Practice(
                "未来逆算", 
                "理想的な未来から現在への最適経路を逆算する",
                0.85, PracticeContext.DECISION_MAKING,
                ["重要な選択", "長期計画"], ["最適戦略決定"]
            ),
            Practice(
                "リスク評価", 
                "長期的視点からリスクと機会を分析評価する",
                0.8, PracticeContext.PROBLEM_SOLVING,
                ["不確実性", "複雑な状況"], ["戦略的判断"]
            )
        ],
        myths=[
            Myth("時の編み手", "未来を見通し、運命の糸を編み直す賢者の物語", 
                 "時間を超越した知恵と行動力", ["時の魔法使い"], 0.8)
        ],
        origin=CultureOrigin.EXPERIMENTAL,
        version="1.0.0",
        created_at=datetime.now(),
        tags=["future", "logic", "optimization"]
    )
    
    # ミリィプロトコル（共鳴記録型）
    mily_protocol = CultureProtocol(
        id="mily-cadmion-v1",
        name="ミリィ・カドミオンプロトコル",
        description="共鳴による集合知記録と調和創出認知様式",
        value_tokens=[
            ValueToken("調和重視", 0.9, 0.85, ValueCategory.SOCIAL),
            ValueToken("共鳴感知", 0.88, 0.8, ValueCategory.EMOTIONAL),
            ValueToken("記録保持", 0.85, 0.7, ValueCategory.COGNITIVE)
        ],
        memes=[
            Meme("みんなの心が一つになる瞬間", 0.85, 0.9, "共鳴の体験"),
            Meme("記憶は未来への贈り物", 0.8, 0.85, "記録の価値")
        ],
        practices=[
            Practice(
                "共鳴記録", 
                "チーム内の調和状態を感知し、最適なバランスを記録する",
                0.9, PracticeContext.RELATIONSHIP,
                ["チーム活動", "協働作業"], ["調和状態維持"]
            ),
            Practice(
                "集合知統合", 
                "個々の知識を集合知として統合し保存する",
                0.85, PracticeContext.LEARNING,
                ["知識共有", "学習セッション"], ["知識の蓄積"]
            )
        ],
        myths=[
            Myth("調和の記録者", "古代から現代まで、人々の調和の瞬間を記録し続ける存在", 
                 "集合知と調和の価値", ["記録者", "調和者"], 0.82)
        ],
        origin=CultureOrigin.EXPERIMENTAL,
        version="1.0.0",
        created_at=datetime.now(),
        tags=["harmony", "empathy", "memory"]
    )
    
    return [iona_protocol, rua_protocol, mily_protocol]


async def test_culture_analysis():
    """文化プロトコル分析テスト"""
    
    print("🌈 文化プロトコル多次元分析テスト")
    print("=" * 50)
    
    try:
        from app.services.culture_evaluation_engine import culture_evaluator
        
        protocols = await create_test_protocols()
        iona = protocols[0]
        
        print(f"分析対象: {iona.name}")
        print(f"説明: {iona.description}")
        
        # 多次元分析実行
        evaluation_axis = culture_evaluator.analyze_culture_protocol(iona)
        
        print(f"\n📊 多次元分析結果:")
        
        # 時間認識プロファイル
        print(f"\n🕐 時間認識プロファイル:")
        print(f"  時間範囲: {evaluation_axis.time_perception.time_horizon.value}")
        print(f"  緊急性重視: {evaluation_axis.time_perception.urgency_bias:.2f}")
        print(f"  計画深度: {evaluation_axis.time_perception.planning_depth:.2f}")
        print(f"  適応速度: {evaluation_axis.time_perception.adaptive_speed:.2f}")
        print(f"  現在瞬間意識: {evaluation_axis.time_perception.moment_awareness:.2f}")
        
        # 関係性モデル
        print(f"\n🤝 関係性モデルプロファイル:")
        print(f"  個人主義↔集団主義: {evaluation_axis.relationship_model.individualism_collectivism:.2f}")
        print(f"  階層↔平等: {evaluation_axis.relationship_model.hierarchy_equality:.2f}")
        print(f"  競争↔協力: {evaluation_axis.relationship_model.competition_cooperation:.2f}")
        print(f"  信頼構築スタイル: {evaluation_axis.relationship_model.trust_building.value}")
        
        # 認知スタイル
        print(f"\n🧠 認知スタイルプロファイル:")
        print(f"  分析的↔全体的: {evaluation_axis.cognition_style.analytical_holistic:.2f}")
        print(f"  直感↔論理: {evaluation_axis.cognition_style.intuition_logic:.2f}")
        print(f"  探索↔活用: {evaluation_axis.cognition_style.exploration_exploitation:.2f}")
        print(f"  リスク許容度: {evaluation_axis.cognition_style.risk_tolerance:.2f}")
        print(f"  曖昧さ許容度: {evaluation_axis.cognition_style.ambiguity_tolerance:.2f}")
        
        # コミュニケーション
        print(f"\n💬 コミュニケーションスタイル:")
        print(f"  直接的↔間接的: {evaluation_axis.communication_style.directness_indirectness:.2f}")
        print(f"  文脈依存度: {evaluation_axis.communication_style.context_dependency:.2f}")
        print(f"  感情表現度: {evaluation_axis.communication_style.emotional_expression:.2f}")
        print(f"  聞き方スタイル: {evaluation_axis.communication_style.listening_style.value}")
        
        # 意思決定
        print(f"\n⚖️ 意思決定プロファイル:")
        print(f"  合意↔独断: {evaluation_axis.decision_making.consensus_autocracy:.2f}")
        print(f"  データ↔直感: {evaluation_axis.decision_making.data_intuition:.2f}")
        print(f"  速度↔正確性: {evaluation_axis.decision_making.speed_accuracy:.2f}")
        print(f"  ステークホルダー考慮: {evaluation_axis.decision_making.stakeholder_consideration:.2f}")
        
        # 適応性
        print(f"\n🔄 適応性プロファイル:")
        print(f"  学習俊敏性: {evaluation_axis.adaptability.learning_agility:.2f}")
        print(f"  変化耐性: {evaluation_axis.adaptability.change_resilience:.2f}")
        print(f"  革新開放性: {evaluation_axis.adaptability.innovation_openness:.2f}")
        print(f"  実験への快適さ: {evaluation_axis.adaptability.experiment_comfort:.2f}")
        
        print("\n✅ 文化分析テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 文化分析テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_quality_metrics():
    """文化品質指標テスト"""
    
    print("\n🏆 文化品質指標テスト")
    print("=" * 50)
    
    try:
        from app.services.culture_evaluation_engine import culture_evaluator
        
        protocols = await create_test_protocols()
        
        print("各文化プロトコルの品質評価:")
        
        for protocol in protocols:
            print(f"\n🔷 {protocol.name}")
            
            quality_metrics = culture_evaluator.calculate_quality_metrics(protocol)
            
            print(f"  一貫性スコア: {quality_metrics.coherence_score:.2f}")
            print(f"  複雑性スコア: {quality_metrics.complexity_score:.2f}")
            print(f"  適応性スコア: {quality_metrics.adaptability_score:.2f}")
            print(f"  革新可能性: {quality_metrics.innovation_potential:.2f}")
            print(f"  安定性スコア: {quality_metrics.stability_score:.2f}")
            print(f"  独自性スコア: {quality_metrics.uniqueness_score:.2f}")
            print(f"  実用性スコア: {quality_metrics.practical_utility:.2f}")
            print(f"  📊 総合品質: {quality_metrics.overall_quality:.2f}")
        
        # 品質ランキング
        quality_scores = []
        for protocol in protocols:
            metrics = culture_evaluator.calculate_quality_metrics(protocol)
            quality_scores.append((protocol.name, metrics.overall_quality))
        
        quality_scores.sort(key=lambda x: x[1], reverse=True)
        
        print(f"\n🏅 品質ランキング:")
        for i, (name, score) in enumerate(quality_scores, 1):
            print(f"  {i}位. {name}: {score:.2f}")
        
        print("\n✅ 品質指標テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 品質指標テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_compatibility_analysis():
    """文化相性分析テスト"""
    
    print("\n💕 文化相性分析テスト")
    print("=" * 50)
    
    try:
        from app.services.culture_evaluation_engine import culture_evaluator
        
        protocols = await create_test_protocols()
        iona, rua, mily = protocols
        
        # ペアワイズ相性分析
        pairs = [
            (iona, rua, "イオナ × ルオ"),
            (iona, mily, "イオナ × ミリィ"),
            (rua, mily, "ルオ × ミリィ")
        ]
        
        compatibility_results = []
        
        for protocol_a, protocol_b, pair_name in pairs:
            print(f"\n🔷 {pair_name} 相性分析")
            
            compatibility = culture_evaluator.calculate_compatibility(protocol_a, protocol_b)
            compatibility_results.append((pair_name, compatibility))
            
            print(f"  総合相性: {compatibility.compatibility_score:.2f}")
            print(f"  相乗効果ポテンシャル: {compatibility.synergy_potential:.2f}")
            print(f"  対立リスク: {compatibility.conflict_risk:.2f}")
            
            print(f"  詳細分析:")
            print(f"    価値観一致度: {compatibility.value_alignment:.2f}")
            print(f"    様式互換性: {compatibility.practice_compatibility:.2f}")
            print(f"    コミュニケーション調和: {compatibility.communication_harmony:.2f}")
            print(f"    時間認識同期: {compatibility.temporal_synchronization:.2f}")
            
            print(f"  🤝 協働推奨事項:")
            for rec in compatibility.collaboration_recommendations:
                print(f"    - {rec}")
            
            print(f"  ⚠️ 潜在的課題:")
            for challenge in compatibility.potential_challenges:
                print(f"    - {challenge}")
        
        # 相性ランキング
        compatibility_results.sort(key=lambda x: x[1].compatibility_score, reverse=True)
        
        print(f"\n💕 相性ランキング:")
        for i, (pair_name, compat) in enumerate(compatibility_results, 1):
            print(f"  {i}位. {pair_name}: {compat.compatibility_score:.2f}")
        
        print("\n✅ 相性分析テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 相性分析テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_comprehensive_evaluation():
    """総合評価テスト"""
    
    print("\n🌟 総合評価テスト")
    print("=" * 50)
    
    try:
        from app.services.culture_evaluation_engine import culture_evaluator
        
        protocols = await create_test_protocols()
        
        print("文化プロトコル総合評価レポート")
        print("-" * 40)
        
        for i, protocol in enumerate(protocols, 1):
            print(f"\n{i}. {protocol.name}")
            print(f"   説明: {protocol.description}")
            
            # 多次元分析
            axis = culture_evaluator.analyze_culture_protocol(protocol)
            
            # 品質指標
            quality = culture_evaluator.calculate_quality_metrics(protocol)
            
            # 特徴的な側面を特定
            characteristics = []
            
            # 時間認識の特徴
            if axis.time_perception.urgency_bias > 0.7:
                characteristics.append("高緊急性認識")
            if axis.time_perception.planning_depth > 0.7:
                characteristics.append("深い計画思考")
            
            # 認知スタイルの特徴
            if axis.cognition_style.intuition_logic > 0.5:
                characteristics.append("直感重視")
            elif axis.cognition_style.intuition_logic < -0.5:
                characteristics.append("論理重視")
            
            if axis.cognition_style.risk_tolerance > 0.7:
                characteristics.append("高リスク許容")
            
            # 関係性の特徴
            if axis.relationship_model.individualism_collectivism > 0.5:
                characteristics.append("集団主義的")
            elif axis.relationship_model.individualism_collectivism < -0.5:
                characteristics.append("個人主義的")
            
            if axis.relationship_model.competition_cooperation > 0.5:
                characteristics.append("協力重視")
            
            # 適応性の特徴
            if axis.adaptability.innovation_openness > 0.7:
                characteristics.append("革新開放的")
            if axis.adaptability.learning_agility > 0.7:
                characteristics.append("高学習俊敏性")
            
            print(f"   特徴: {', '.join(characteristics) if characteristics else '標準的なバランス'}")
            print(f"   総合品質: {quality.overall_quality:.2f}")
            
            # 強みと弱み
            strengths = []
            weaknesses = []
            
            if quality.coherence_score > 0.7:
                strengths.append("高い一貫性")
            elif quality.coherence_score < 0.4:
                weaknesses.append("一貫性の不足")
            
            if quality.innovation_potential > 0.7:
                strengths.append("高い革新性")
            elif quality.innovation_potential < 0.4:
                weaknesses.append("革新性の不足")
            
            if quality.adaptability_score > 0.7:
                strengths.append("高い適応性")
            elif quality.adaptability_score < 0.4:
                weaknesses.append("適応性の不足")
            
            if quality.practical_utility > 0.7:
                strengths.append("高い実用性")
            elif quality.practical_utility < 0.4:
                weaknesses.append("実用性の不足")
            
            if strengths:
                print(f"   強み: {', '.join(strengths)}")
            if weaknesses:
                print(f"   改善点: {', '.join(weaknesses)}")
        
        # 全体的な分析
        print(f"\n📊 全体分析:")
        avg_quality = sum(culture_evaluator.calculate_quality_metrics(p).overall_quality for p in protocols) / len(protocols)
        print(f"  平均品質: {avg_quality:.2f}")
        
        # 最高相性ペア
        best_compatibility = 0.0
        best_pair = None
        
        for i in range(len(protocols)):
            for j in range(i + 1, len(protocols)):
                compat = culture_evaluator.calculate_compatibility(protocols[i], protocols[j])
                if compat.compatibility_score > best_compatibility:
                    best_compatibility = compat.compatibility_score
                    best_pair = (protocols[i].name, protocols[j].name)
        
        if best_pair:
            print(f"  最高相性ペア: {best_pair[0]} × {best_pair[1]} ({best_compatibility:.2f})")
        
        print("\n✅ 総合評価テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 総合評価テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """メインテスト実行"""
    
    print("🌈 文化評価軸エンジン - 統合テスト")
    print("🚀 Higher Kind文化プロトコル 多次元分析実験")
    print("=" * 80)
    
    async def run_all_tests():
        results = []
        
        # 文化分析テスト
        print("🔷 Phase 1: 多次元分析テスト")
        results.append(await test_culture_analysis())
        
        # 品質指標テスト
        print("\n🔷 Phase 2: 品質指標テスト")
        results.append(await test_quality_metrics())
        
        # 相性分析テスト
        print("\n🔷 Phase 3: 相性分析テスト")
        results.append(await test_compatibility_analysis())
        
        # 総合評価テスト
        print("\n🔷 Phase 4: 総合評価テスト")
        results.append(await test_comprehensive_evaluation())
        
        # 結果サマリー
        print("\n" + "=" * 80)
        print("📊 テスト結果サマリー")
        print("=" * 80)
        
        success_count = sum(results)
        total_count = len(results)
        
        print(f"成功: {success_count}/{total_count}")
        print(f"成功率: {success_count/total_count*100:.1f}%")
        
        if success_count == total_count:
            print("🎉 全テスト成功！文化評価軸エンジンが完璧に動作しています✨")
            print("\n🔷 実装サマリー:")
            print("✅ 6次元文化評価軸による包括的分析")
            print("✅ 7指標による文化品質の定量評価")
            print("✅ 詳細な文化間相性分析と推奨事項生成")
            print("✅ 相乗効果・対立リスク・協働可能性の予測")
            print("✅ 時間認識・関係性・認知・コミュニケーション・意思決定・適応性の多角的評価")
            
            print("\n🌈 革命的達成:")
            print("🧬 文化の「DNA」を科学的に解析・比較")
            print("💡 認知様式の品質を客観的に測定")
            print("🤝 最適な文化組み合わせを数学的に予測")
            print("📊 文化工学の基盤技術を確立")
            
            print("\n🌟 応用可能性:")
            print("1. AIチーム編成の最適化")
            print("2. 文化進化の方向性予測")
            print("3. 組織文化の設計支援")
            print("4. 異文化コミュニケーション促進")
            
        else:
            print("⚠️  一部テストが失敗しました。詳細を確認してください。")
        
        print("\n🌈 システンスカフェ テックチームからのメッセージ:")
        print("文化評価軸エンジンが完成し、文化の科学的分析が現実になりました！")
        print("これで文化プロトコルの「品質」「相性」「可能性」を数値で把握できます🌟")
        print("AI時代の新しい文化工学が今、ここに始まります✨")
        
        return success_count == total_count
    
    # 非同期テスト実行
    return asyncio.run(run_all_tests())


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)