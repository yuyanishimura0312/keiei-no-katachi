"""build_site.py — index.html と articles.html を生成"""

from pathlib import Path
from roadmap import ROADMAP

ROOT = Path(__file__).parent

PART_NAMES = {
    "PROLOGUE": ("PROLOGUE — 序 章", "経営機能を他分野で読む"),
    "I": ("PART I — マネジメント", "統率・組織・継承"),
    "II": ("PART II — ファイナンス", "利子・通貨・リスク"),
    "III": ("PART III — マーケティング", "物語・記号・神話"),
    "IV": ("PART IV — 事業開発", "適応・共創・撤退"),
    "V": ("PART V — 営業・販売", "弁論・関係・儀礼"),
    "FINAL": ("FINAL — 終 章", "機能横断の経営論"),
}

PART_IDS = {
    "PROLOGUE": "prologue",
    "I": "part-i",
    "II": "part-ii",
    "III": "part-iii",
    "IV": "part-iv",
    "V": "part-v",
    "FINAL": "final",
}


def render_articles_page():
    """articles.html — 全100話地図"""
    by_part = {}
    for ep in ROADMAP:
        by_part.setdefault(ep["part"], []).append(ep)

    parts_html = []
    drafted = sum(1 for ep in ROADMAP if ep["status"] == "draft")
    pct = int(drafted / len(ROADMAP) * 100)

    for part_key in ["PROLOGUE", "I", "II", "III", "IV", "V", "FINAL"]:
        part_label, part_desc = PART_NAMES[part_key]
        part_id = PART_IDS[part_key]
        eps = by_part.get(part_key, [])
        ep_lis = []
        for ep in eps:
            ep_num_int = int(ep["ep"][2:])
            ep_lower = ep["ep"].lower()
            if ep["status"] == "draft":
                ep_lis.append(f'<li class="ep-row published"><a href="{ep_lower}.html"><span class="ep-row-num">第{ep_num_int}話</span><span class="ep-row-title">{ep["title"]}</span><span class="ep-row-lens">{ep["lens1"]} × {ep["lens2"]}</span></a></li>')
            else:
                ep_lis.append(f'<li class="ep-row planned"><span class="ep-row-num">第{ep_num_int}話</span><span class="ep-row-title">{ep["title"]}</span><span class="ep-row-lens">{ep["lens1"]} × {ep["lens2"]}</span><span class="ep-row-status">— 公開予定</span></li>')
        ul = "\n".join(ep_lis)
        parts_html.append(f'''
      <section class="part-section" id="{part_id}">
        <h2 class="part-title">{part_label}</h2>
        <p class="part-desc">{part_desc}</p>
        <ul class="ep-list">
{ul}
        </ul>
      </section>''')

    parts_block = "\n".join(parts_html)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全100話 | 経営のかたち</title>
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700;900&family=Noto+Serif+JP:wght@300;400;500;600;700;900&family=Judson:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<style>
.articles-hero {{ background: var(--bg); padding: 64px 24px 32px; border-bottom: 1px solid var(--line); text-align: center; }}
.articles-hero h1 {{ font-family: var(--serif); font-size: 28px; font-weight: 700; letter-spacing: 0.04em; margin-bottom: 12px; }}
.articles-hero p {{ font-family: var(--serif); font-size: 14.5px; color: var(--ink-soft); max-width: 640px; margin: 0 auto; line-height: 1.95; }}
.progress {{ font-family: var(--sans); font-size: 11px; letter-spacing: 0.18em; color: var(--accent); margin-top: 24px; }}
.articles-main {{ max-width: 860px; margin: 0 auto; padding: 56px 24px 80px; }}
.part-section {{ margin-bottom: 56px; }}
.part-title {{ font-family: var(--sans); font-size: 11px; letter-spacing: 0.32em; color: var(--accent); font-weight: 700; padding-bottom: 12px; border-bottom: 2px solid var(--ink); margin-bottom: 6px; }}
.part-desc {{ font-family: var(--serif); font-size: 14px; color: var(--ink-soft); margin-bottom: 22px; letter-spacing: 0.04em; }}
.ep-list {{ list-style: none; padding: 0; }}
.ep-row {{ padding: 14px 0; border-bottom: 1px solid var(--line-soft); display: block; }}
.ep-row a {{ display: grid; grid-template-columns: 80px 1fr; gap: 18px; align-items: baseline; text-decoration: none; }}
.ep-row.planned {{ display: grid; grid-template-columns: 80px 1fr auto; gap: 18px; align-items: baseline; opacity: 0.55; }}
.ep-row-num {{ font-family: var(--sans); font-size: 11px; letter-spacing: 0.16em; color: var(--accent); font-weight: 700; }}
.ep-row-title {{ font-family: var(--serif); font-size: 15.5px; color: var(--ink); letter-spacing: 0.04em; line-height: 1.7; font-weight: 600; }}
.ep-row.planned .ep-row-title {{ font-weight: 500; }}
.ep-row-lens {{ display: block; font-family: var(--sans); font-size: 11px; color: var(--ink-mute); margin-top: 4px; letter-spacing: 0.04em; }}
.ep-row-status {{ font-family: var(--sans); font-size: 10.5px; color: var(--ink-mute); letter-spacing: 0.12em; }}
.ep-row.published a:hover .ep-row-title {{ color: var(--accent); }}
</style>
</head>
<body>

<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="site-brand">
      <div class="site-brand-text">経営のかたち<small>KEIEI NO KATACHI / 他分野が経営の機能に出会うとき</small></div>
    </a>
    <nav class="site-nav">
      <a href="index.html">ホーム</a>
      <a href="articles.html" class="active">全100話</a>
    </nav>
  </div>
</header>

<section class="articles-hero">
  <h1>全100話の地図</h1>
  <p>5つの経営機能を他分野の研究知で読み直す100話。各話に2つのレンズを置き、本文と DEEPER の両方から、経営の機能を別の学問の言葉で照らします。</p>
  <div class="progress">公開: {drafted}/100話 ({pct}%)</div>
</section>

<main class="articles-main">
{parts_block}
</main>

<section class="disclaimer">
  <div class="disclaimer-inner">
    本連載で紹介する研究内容は2025年時点までの公表知見に基づくもので、その後の研究で更新される可能性があります。引用した数値・効果は集団傾向であり、個別の経営判断における結果を保証するものではありません。実務への適用は、組織の文脈に応じてご検討ください。
  </div>
</section>

<footer class="site-footer">
  <div class="site-footer-inner">
    <div class="site-footer-bottom">
      <span>© NPO法人ミラツク / 経営のかたち</span>
      <span>2026 — 100話連載</span>
    </div>
  </div>
</footer>

</body>
</html>
"""


def render_index():
    """index.html — トップ"""
    drafted = [ep for ep in ROADMAP if ep["status"] == "draft"]
    latest = drafted[-1] if drafted else None
    if latest:
        latest_num = int(latest["ep"][2:])
        latest_lower = latest["ep"].lower()
        latest_block = f'''<a href="{latest_lower}.html" class="latest-card">
  <span class="latest-label">最新話 — 第{latest_num}話</span>
  <span class="latest-title">{latest["title"]}</span>
  <span class="latest-lens">{latest["lens1"]} × {latest["lens2"]}</span>
</a>'''
    else:
        latest_block = ""

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>経営のかたち — 他分野が経営の機能に出会うとき</title>
<meta name="description" content="経営の主要5機能を他分野の研究知で読み直す100話連載。NPO法人ミラツク。">
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700;900&family=Noto+Serif+JP:wght@300;400;500;600;700;900&family=Judson:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<style>
.hero {{ background: var(--bg); padding: 96px 24px 80px; text-align: center; border-bottom: 1px solid var(--line); }}
.hero-inner {{ max-width: 760px; margin: 0 auto; }}
.hero-mark {{ font-family: var(--sans); font-size: 11px; letter-spacing: 0.32em; color: var(--accent); margin-bottom: 24px; font-weight: 700; }}
.hero h1 {{ font-family: var(--serif); font-size: 38px; font-weight: 700; letter-spacing: 0.04em; line-height: 1.5; margin-bottom: 18px; }}
.hero-sub {{ font-family: var(--serif); font-size: 17px; color: var(--ink-soft); margin-bottom: 36px; line-height: 1.95; letter-spacing: 0.04em; }}
.hero-en {{ font-family: var(--display); font-size: 18px; color: var(--ink-mute); margin-bottom: 40px; }}
.latest-card {{ display: block; max-width: 560px; margin: 0 auto; padding: 28px 32px; background: var(--bg-tint); border: 1px solid var(--line); text-align: left; transition: border-color .15s; }}
.latest-card:hover {{ border-color: var(--accent); text-decoration: none; }}
.latest-label {{ display: block; font-family: var(--sans); font-size: 10px; letter-spacing: 0.22em; color: var(--accent); font-weight: 700; margin-bottom: 10px; }}
.latest-title {{ display: block; font-family: var(--serif); font-size: 19px; font-weight: 700; color: var(--ink); margin-bottom: 6px; line-height: 1.6; }}
.latest-lens {{ display: block; font-family: var(--sans); font-size: 11px; color: var(--ink-mute); letter-spacing: 0.04em; }}
.concept {{ max-width: 720px; margin: 0 auto; padding: 64px 24px 48px; }}
.concept h2 {{ font-family: var(--sans); font-size: 11px; letter-spacing: 0.32em; color: var(--accent); margin-bottom: 22px; font-weight: 700; }}
.concept p {{ font-family: var(--serif); font-size: 15.5px; line-height: 2; margin-bottom: 22px; letter-spacing: 0.04em; color: var(--ink-soft); }}
.parts-grid {{ max-width: 1080px; margin: 0 auto; padding: 24px 24px 80px; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; }}
.part-card {{ padding: 28px 24px; background: var(--bg-tint); border: 1px solid var(--line); transition: border-color .15s; text-decoration: none; }}
.part-card:hover {{ border-color: var(--accent); }}
.part-card-label {{ font-family: var(--sans); font-size: 10px; letter-spacing: 0.22em; color: var(--accent); font-weight: 700; margin-bottom: 10px; display: block; }}
.part-card-title {{ font-family: var(--serif); font-size: 17px; color: var(--ink); margin-bottom: 6px; font-weight: 700; line-height: 1.5; }}
.part-card-meta {{ font-family: var(--sans); font-size: 11px; color: var(--ink-mute); letter-spacing: 0.04em; }}
@media (max-width: 760px) {{
  .hero h1 {{ font-size: 26px; }}
  .hero-sub {{ font-size: 14.5px; }}
}}
</style>
</head>
<body>

<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="site-brand">
      <div class="site-brand-text">経営のかたち<small>KEIEI NO KATACHI / 他分野が経営の機能に出会うとき</small></div>
    </a>
    <nav class="site-nav">
      <a href="index.html" class="active">ホーム</a>
      <a href="articles.html">全100話</a>
    </nav>
  </div>
</header>

<section class="hero">
  <div class="hero-inner">
    <div class="hero-mark">NPO法人ミラツク × 他分野研究</div>
    <h1>経営のかたち</h1>
    <p class="hero-sub">他分野が経営の機能に出会うとき<br>—— 経営学の語彙の外側へ100話</p>
    <div class="hero-en">KEIEI NO KATACHI</div>
{latest_block}
  </div>
</section>

<section class="concept">
  <h2>連載コンセプト</h2>
  <p>経営学だけでは届かない領域があります。リーダーシップは贈与論で、ファイナンスは経済人類学と進化生物学で、マーケティングは神話論と記号学で、事業開発は進化生態学で、営業は弁論術で読み直すと、新しい実務判断が見えてきます。</p>
  <p>本連載は、経営の主要5機能（マネジメント・ファイナンス・マーケティング・事業開発・営業販売）を、他分野の研究知の前提条件へ翻訳する Translational Editor 型の100話です。各話には2つのレンズを置き、本文と DEEPER で異なる学問が同じ問いに到達していることを示します。</p>
</section>

<section class="parts-grid">
  <a href="articles.html#prologue" class="part-card">
    <span class="part-card-label">PROLOGUE</span>
    <div class="part-card-title">序章 — 経営機能を他分野で読む</div>
    <div class="part-card-meta">EP001-005 — 5話</div>
  </a>
  <a href="articles.html#part-i" class="part-card">
    <span class="part-card-label">PART I</span>
    <div class="part-card-title">マネジメント — 統率・組織・継承</div>
    <div class="part-card-meta">EP006-023 — 18話</div>
  </a>
  <a href="articles.html#part-ii" class="part-card">
    <span class="part-card-label">PART II</span>
    <div class="part-card-title">ファイナンス — 利子・通貨・リスク</div>
    <div class="part-card-meta">EP024-041 — 18話</div>
  </a>
  <a href="articles.html#part-iii" class="part-card">
    <span class="part-card-label">PART III</span>
    <div class="part-card-title">マーケティング — 物語・記号・神話</div>
    <div class="part-card-meta">EP042-059 — 18話</div>
  </a>
  <a href="articles.html#part-iv" class="part-card">
    <span class="part-card-label">PART IV</span>
    <div class="part-card-title">事業開発 — 適応・共創・撤退</div>
    <div class="part-card-meta">EP060-077 — 18話</div>
  </a>
  <a href="articles.html#part-v" class="part-card">
    <span class="part-card-label">PART V</span>
    <div class="part-card-title">営業・販売 — 弁論・関係・儀礼</div>
    <div class="part-card-meta">EP078-095 — 18話</div>
  </a>
  <a href="articles.html#final" class="part-card">
    <span class="part-card-label">FINAL</span>
    <div class="part-card-title">終章 — 機能横断の経営論</div>
    <div class="part-card-meta">EP096-100 — 5話</div>
  </a>
</section>

<section class="disclaimer">
  <div class="disclaimer-inner">
    本連載で紹介する研究内容は2025年時点までの公表知見に基づくもので、その後の研究で更新される可能性があります。引用した数値・効果は集団傾向であり、個別の経営判断における結果を保証するものではありません。実務への適用は、組織の文脈に応じてご検討ください。
  </div>
</section>

<footer class="site-footer">
  <div class="site-footer-inner">
    <div class="site-footer-bottom">
      <span>© NPO法人ミラツク / 経営のかたち</span>
      <span>2026 — 100話連載</span>
    </div>
  </div>
</footer>

</body>
</html>
"""


def main():
    (ROOT / "articles.html").write_text(render_articles_page(), encoding="utf-8")
    print("  built: articles.html")
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")
    print("  built: index.html")


if __name__ == "__main__":
    main()
