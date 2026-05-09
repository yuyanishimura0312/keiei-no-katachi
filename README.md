# 経営のかたち — 他分野が経営の機能に出会うとき

NPO法人ミラツクの100話連載。経営の主要5機能（マネジメント・ファイナンス・マーケティング・事業開発・営業販売）を、他分野の研究知（人類学・哲学・生態学・神経科学・神話学・進化生物学等）で読み直す Translational Editor 型連載。

## 構造

序章5 + PART I-V × 18 + 終章5 = 100話

| 部 | テーマ | 範囲 |
|---|---|---|
| 序章 | 連載序論・方法論 | EP001-005 |
| PART I | マネジメント | EP006-023 |
| PART II | ファイナンス | EP024-041 |
| PART III | マーケティング | EP042-059 |
| PART IV | 事業開発 | EP060-077 |
| PART V | 営業・販売 | EP078-095 |
| 終章 | 連載総括 | EP096-100 |

詳細ロードマップ: [`roadmap.md`](roadmap.md)

## 制作ルール v0.5

各話は **2レンズ設計** で構成:
- **本文（第1レンズ）**: 1,200-1,500字、6段落、直感的・物語的
- **DEEPER（第2レンズ）**: 400-500字、3段落、別分野で同じ問いを照らす

### フォーマット
- 文体: ですます調
- 数字: アラビア数字
- SIGNAL: 3個、出典・年・hedging済
- KEY REFERENCE: 5-6件、DOI付き
- QUESTION FOR NEXT: 次話への問い

### 設計原則
- 分野はベストフィット優先（文化的偏りを排除、東西新旧を等価に扱う）
- 全100話で50以上の異なる分野を動員
- 古典（古代〜近代）と最先端（2010年代以降）を同等の比重

## 制作チーム

`/keiei-team` オーケストレーターから順次起動:
1. `/keiei-planner` — EP仕様設計
2. `/keiei-researcher` — DB統合リサーチ（academic-oracle・signal-db他）
3. `/keiei-web-researcher` — Web追加リサーチ（DOI付き直近論文）
4. `/keiei-writer` — 本文執筆（1,200-1,500字、6段落）
5. `/keiei-deeper` — DEEPER執筆（第2レンズで400-500字）
6. `/keiei-editor` — A/B/C評価ゲート、ファクトチェック
7. `/keiei-publisher` — データ統合・HTML生成・公開

## 想定読者

経営実務者（管理職・経営者・起業家・新規事業担当）

## 関連連載

- [暮らしのかたち](https://yuyanishimura0312.github.io/kurashi-no-katachi/) — 学術×暮らしのシーン27（生活者編）
- [事業のかたち](https://stg.miratuku-journal.org/i_academias/) — 学術×事業18領域（業界編）
- [変化のかたち](https://yuyanishimura0312.github.io/henka-no-katachi/) — 5メタ型×15サブ型×3底流（変容編）

## 開発

```bash
python3 generate.py     # 各話HTMLを生成
python3 build_site.py   # index.html / articles.html を構築
```

## 著者

西村勇也（NPO法人ミラツク 代表理事）
