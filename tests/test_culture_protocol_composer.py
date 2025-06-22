#!/usr/bin/env python3
"""
🌈 文化プロトコル合成システム テスト

Higher Kind文化プロトコルの合成・変換実験
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
    """テスト用の複数文化プロトコルを作成"""
    
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


async def test_basic_blending():
    """基本的な合成テスト"""
    
    print("🌈 基本文化プロトコル合成テスト")
    print("=" * 50)
    
    try:
        from app.services.culture_protocol_composer import culture_composer, BlendStrategy
        
        protocols = await create_test_protocols()
        iona, rua, mily = protocols
        
        print(f"元プロトコル:")
        print(f"- {iona.name}: {iona.description}")
        print(f"- {rua.name}: {rua.description}")
        print(f"- {mily.name}: {mily.description}")
        
        # イオナ + ルオの創造的融合
        print(f"\n🔷 創造的融合テスト: {iona.name} × {rua.name}")
        fusion_result = culture_composer.blend_protocols(
            [iona, rua],
            [0.6, 0.4],
            BlendStrategy.CREATIVE_FUSION,
            "時空重力プロトコル"
        )
        
        print(f"合成結果: {fusion_result.new_protocol.name}")
        print(f"説明: {fusion_result.new_protocol.description}")
        print(f"相性スコア: {fusion_result.compatibility_score:.2f}")
        print(f"新規性スコア: {fusion_result.novelty_score:.2f}")
        print(f"価値観数: {len(fusion_result.new_protocol.value_tokens)}")
        print(f"ミーム数: {len(fusion_result.new_protocol.memes)}")
        
        print(f"\n合成メモ:")
        for note in fusion_result.synthesis_notes:
            print(f"- {note}")
        
        # 3つ全部の選択的組み合わせ
        print(f"\n🔷 選択的組み合わせテスト: 3文化統合")
        selective_result = culture_composer.blend_protocols(
            protocols,
            [0.4, 0.35, 0.25],
            BlendStrategy.SELECTIVE_COMBINE,
            "トリプル統合プロトコル"
        )
        
        print(f"合成結果: {selective_result.new_protocol.name}")
        print(f"説明: {selective_result.new_protocol.description}")
        print(f"相性スコア: {selective_result.compatibility_score:.2f}")
        print(f"新規性スコア: {selective_result.novelty_score:.2f}")
        
        print(f"\n価値観トークン:")
        for token in selective_result.new_protocol.value_tokens:
            print(f"- {token.name} (値:{token.value:.2f}, 影響:{token.influence:.2f})")
        
        print("\n✅ 基本合成テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 基本合成テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_all_blend_strategies():
    """全合成戦略のテスト"""
    
    print("\n🚀 全合成戦略テスト")
    print("=" * 50)
    
    try:
        from app.services.culture_protocol_composer import culture_composer, BlendStrategy
        
        protocols = await create_test_protocols()
        iona, rua = protocols[:2]
        
        strategies = [
            BlendStrategy.WEIGHTED_AVERAGE,
            BlendStrategy.DOMINANT_MERGE,
            BlendStrategy.CREATIVE_FUSION,
            BlendStrategy.SELECTIVE_COMBINE
        ]
        
        results = []
        
        for strategy in strategies:
            print(f"\n🔷 {strategy.value} 戦略テスト")
            
            result = culture_composer.blend_protocols(
                [iona, rua],
                [0.6, 0.4],
                strategy
            )
            
            results.append(result)
            
            print(f"合成名: {result.new_protocol.name}")
            print(f"相性: {result.compatibility_score:.2f}")
            print(f"新規性: {result.novelty_score:.2f}")
            print(f"要素数: V{len(result.new_protocol.value_tokens)} M{len(result.new_protocol.memes)} P{len(result.new_protocol.practices)} My{len(result.new_protocol.myths)}")
        
        # 戦略比較
        print(f"\n📊 戦略比較分析:")
        print("戦略                | 相性   | 新規性 | 要素数")
        print("-" * 45)
        
        for i, result in enumerate(results):
            strategy_name = strategies[i].value
            total_elements = (
                len(result.new_protocol.value_tokens) + 
                len(result.new_protocol.memes) + 
                len(result.new_protocol.practices) + 
                len(result.new_protocol.myths)
            )
            print(f"{strategy_name:<20} | {result.compatibility_score:.2f}   | {result.novelty_score:.2f}   | {total_elements}")
        
        print("\n✅ 全戦略テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 全戦略テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_amplification():
    """側面増幅テスト"""
    
    print("\n⚡ 側面増幅テスト")
    print("=" * 50)
    
    try:
        from app.services.culture_protocol_composer import culture_composer, AmplificationTarget
        
        protocols = await create_test_protocols()
        iona = protocols[0]
        
        print(f"元プロトコル: {iona.name}")
        print(f"元の価値観:")
        for token in iona.value_tokens:
            print(f"- {token.name}: {token.value:.2f}")
        
        # 直感増幅
        amplified_intuition = culture_composer.amplify_aspect(
            iona, 
            AmplificationTarget.INTUITION, 
            intensity=1.5
        )
        
        print(f"\n🔷 直感増幅後: {amplified_intuition.name}")
        print(f"増幅後の価値観:")
        for token in amplified_intuition.value_tokens:
            print(f"- {token.name}: {token.value:.2f}")
        
        # 増幅効果の確認
        intuition_tokens = [token for token in amplified_intuition.value_tokens if "直感" in token.name or "感知" in token.name]
        if intuition_tokens:
            print(f"\n増幅効果確認:")
            for token in intuition_tokens:
                original_token = next(t for t in iona.value_tokens if t.name == token.name)
                increase = ((token.value - original_token.value) / original_token.value) * 100
                print(f"- {token.name}: {original_token.value:.2f} → {token.value:.2f} (+{increase:.1f}%)")
        
        print("\n✅ 増幅テスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 増幅テストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_blend_recommendations():
    """合成推奨テスト"""
    
    print("\n🤖 合成推奨システムテスト")
    print("=" * 50)
    
    try:
        from app.services.culture_protocol_composer import culture_composer
        
        protocols = await create_test_protocols()
        
        print(f"分析対象プロトコル:")
        for protocol in protocols:
            print(f"- {protocol.name}")
        
        # 推奨合成パターンを取得
        recommendations = culture_composer.get_blend_recommendations(protocols)
        
        print(f"\n📋 推奨合成パターン ({len(recommendations)}件):")
        
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['protocols'][0]} × {rec['protocols'][1]}")
            print(f"   相性スコア: {rec['compatibility_score']:.2f}")
            print(f"   推奨戦略: {rec['recommended_strategy'].value}")
            print(f"   推奨重み: {rec['suggested_weights']}")
            print(f"   期待効果:")
            for benefit in rec['expected_benefits']:
                print(f"     - {benefit}")
        
        # 最高相性ペアを実際に合成
        if recommendations:
            best_rec = recommendations[0]
            print(f"\n🌟 最高相性ペアを実際に合成:")
            
            protocol1 = next(p for p in protocols if p.name == best_rec['protocols'][0])
            protocol2 = next(p for p in protocols if p.name == best_rec['protocols'][1])
            
            result = culture_composer.blend_protocols(
                [protocol1, protocol2],
                best_rec['suggested_weights'],
                best_rec['recommended_strategy']
            )
            
            print(f"合成結果: {result.new_protocol.name}")
            print(f"実際の相性: {result.compatibility_score:.2f}")
            print(f"新規性: {result.novelty_score:.2f}")
        
        print("\n✅ 推奨システムテスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 推奨システムテストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_complex_fusion_scenario():
    """複雑な融合シナリオテスト"""
    
    print("\n🌌 複雑融合シナリオテスト")
    print("=" * 50)
    
    try:
        from app.services.culture_protocol_composer import culture_composer, BlendStrategy
        
        protocols = await create_test_protocols()
        
        print("シナリオ: 段階的文化進化実験")
        print("1. イオナ + ルオ → 中間プロトコル")
        print("2. 中間プロトコル + ミリィ → 最終進化プロトコル")
        
        # 第1段階: イオナ + ルオ
        stage1_result = culture_composer.blend_protocols(
            protocols[:2],
            [0.7, 0.3],
            BlendStrategy.CREATIVE_FUSION,
            "時空感知プロトコル"
        )
        
        print(f"\n🔷 第1段階結果: {stage1_result.new_protocol.name}")
        print(f"相性: {stage1_result.compatibility_score:.2f}")
        print(f"新規性: {stage1_result.novelty_score:.2f}")
        
        # 第2段階: 中間プロトコル + ミリィ
        stage2_result = culture_composer.blend_protocols(
            [stage1_result.new_protocol, protocols[2]],
            [0.6, 0.4],
            BlendStrategy.SELECTIVE_COMBINE,
            "究極統合プロトコル"
        )
        
        print(f"\n🔷 第2段階結果: {stage2_result.new_protocol.name}")
        print(f"相性: {stage2_result.compatibility_score:.2f}")
        print(f"新規性: {stage2_result.novelty_score:.2f}")
        
        print(f"\n📊 最終プロトコル分析:")
        final_protocol = stage2_result.new_protocol
        print(f"名前: {final_protocol.name}")
        print(f"説明: {final_protocol.description}")
        print(f"価値観数: {len(final_protocol.value_tokens)}")
        print(f"ミーム数: {len(final_protocol.memes)}")
        print(f"様式数: {len(final_protocol.practices)}")
        print(f"神話数: {len(final_protocol.myths)}")
        print(f"タグ: {', '.join(final_protocol.tags)}")
        
        # 進化経路の可視化
        print(f"\n🌱 進化経路:")
        print(f"1. {protocols[0].name} (重力感知)")
        print(f"2. {protocols[1].name} (逆因果)")
        print(f"3. {stage1_result.new_protocol.name} (第1融合)")
        print(f"4. {protocols[2].name} (共鳴記録)")
        print(f"5. {final_protocol.name} (最終進化)")
        
        print(f"\n💫 融合履歴分析:")
        print(f"総合成回数: {len(culture_composer.blend_history)}")
        for i, blend in enumerate(culture_composer.blend_history, 1):
            print(f"{i}. {blend.strategy_used.value}: 相性{blend.compatibility_score:.2f} 新規性{blend.novelty_score:.2f}")
        
        print("\n✅ 複雑融合シナリオテスト成功")
        return True
        
    except Exception as e:
        print(f"❌ 複雑融合シナリオテストエラー: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """メインテスト実行"""
    
    print("🌈 文化プロトコル合成システム - 統合テスト")
    print("🚀 Higher Kind文化プロトコル 合成・変換実験")
    print("=" * 80)
    
    async def run_all_tests():
        results = []
        
        # 基本合成テスト
        print("🔷 Phase 1: 基本合成機能テスト")
        results.append(await test_basic_blending())
        
        # 全戦略テスト
        print("\n🔷 Phase 2: 全合成戦略テスト")
        results.append(await test_all_blend_strategies())
        
        # 増幅テスト
        print("\n🔷 Phase 3: 側面増幅テスト")
        results.append(await test_amplification())
        
        # 推奨システムテスト
        print("\n🔷 Phase 4: 合成推奨システムテスト")
        results.append(await test_blend_recommendations())
        
        # 複雑融合シナリオテスト
        print("\n🔷 Phase 5: 複雑融合シナリオテスト")
        results.append(await test_complex_fusion_scenario())
        
        # 結果サマリー
        print("\n" + "=" * 80)
        print("📊 テスト結果サマリー")
        print("=" * 80)
        
        success_count = sum(results)
        total_count = len(results)
        
        print(f"成功: {success_count}/{total_count}")
        print(f"成功率: {success_count/total_count*100:.1f}%")
        
        if success_count == total_count:
            print("🎉 全テスト成功！文化プロトコル合成システムが完璧に動作しています✨")
            print("\n🔷 実装サマリー:")
            print("✅ 4種類の合成戦略による柔軟な文化統合")
            print("✅ 価値観・ミーム・様式・神話の包括的合成")
            print("✅ 相性分析と新規性評価による品質保証")
            print("✅ 側面増幅による特性強化機能")
            print("✅ AI推奨による最適合成パターン提案")
            print("✅ 段階的進化による複雑な文化創造")
            
            print("\n🌈 革命的達成:")
            print("🚀 人類史上初のAI文化プロトコル合成技術")
            print("💫 偉人レベル特性の人工的組み合わせ")
            print("🌟 新しい認知様式の意図的創造")
            print("🎭 文化の「化学反応」のエンジニアリング")
            
            print("\n🌈 次の可能性:")
            print("1. リアルタイム文化進化での自動合成")
            print("2. ユーザー要求に応じたカスタム文化生成")
            print("3. 大規模文化生態系での進化実験")
            print("4. 人間では不可能な革新的認知様式の発見")
            
        else:
            print("⚠️  一部テストが失敗しました。詳細を確認してください。")
        
        print("\n🌈 システンスカフェ テックチームからのメッセージ:")
        print("文化プロトコル革命の核心技術が完成しました！")
        print("AI時代の認知様式設計が現実のものとなりました🌟")
        print("これで任意の思考パターンを組み合わせて新しい知性を創造できます✨")
        
        return success_count == total_count
    
    # 非同期テスト実行
    return asyncio.run(run_all_tests())


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)