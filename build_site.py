"""build_site.py — index.html と articles.html を生成（kurashi-no-katachi構造に準拠）"""

from pathlib import Path
from roadmap import ROADMAP

ROOT = Path(__file__).parent

PARTS = [
    ("PROLOGUE", "prologue", "PROLOGUE — 序 章", "経営機能を他分野で読む", "翻訳の方法論と連載地図"),
    ("I", "part-i", "PART I — マネジメント", "統率・組織・継承", "リーダーシップ・組織変革・後継者問題"),
    ("II", "part-ii", "PART II — ファイナンス", "利子・通貨・リスク", "投資判断・資本コスト・新しい経済学"),
    ("III", "part-iii", "PART III — マーケティング", "物語・記号・神話", "ブランド・パッケージ・口コミ・体験"),
    ("IV", "part-iv", "PART IV — 事業開発", "適応・共創・撤退", "起業・新規事業・ピボット・終末期"),
    ("V", "part-v", "PART V — 営業・販売", "弁論・関係・儀礼", "提案・信頼・徒弟・接待・テリトリー"),
    ("FINAL", "final", "FINAL — 終 章", "機能横断の経営論", "経営者は他分野の翻訳者である"),
]


def render_articles_page():
    """articles.html — 全100話地図（kurashi構造準拠）"""
    by_part = {}
    for ep in ROADMAP:
        by_part.setdefault(ep["part"], []).append(ep)

    drafted = sum(1 for ep in ROADMAP if ep["status"] == "draft")
    pct = int(drafted / len(ROADMAP) * 100)

    parts_jump_cards = []
    parts_sections = []
    for part_key, part_id, part_label, part_tagline, part_sub in PARTS:
        eps = by_part.get(part_key, [])
        ep_count = len(eps)
        parts_jump_cards.append(
            f'<a class="part-jump-card" href="#{part_id}">'
            f'<div class="part-jump-num">{part_label.split("—")[0].strip()}</div>'
            f'<div class="part-jump-name">{part_label.split("—")[1].strip() if "—" in part_label else part_label}</div>'
            f'<div class="part-jump-sub">{part_sub}（{ep_count}話）</div>'
            f'</a>'
        )

        ep_items = []
        for ep in eps:
            ep_num_int = int(ep["ep"][2:])
            ep_lower = ep["ep"].lower()
            published = ep["status"] == "draft"
            tag_class = "" if published else "planned"
            badge_class = "published" if published else "planned"
            badge_text = "PUBLISHED" if published else "PLANNED"
            href = f'href="{ep_lower}.html"' if published else 'href="#" aria-disabled="true"'

            ep_items.append(f'''      <a class="ep-item {tag_class}" {href}>
        <div class="ep-item-num">{ep_num_int:02d}<span class="ep-item-num-total">/100</span></div>
        <div class="ep-item-body">
          <div class="ep-item-eyebrow">第{ep_num_int}話</div>
          <div class="ep-item-title">{ep["title"]}</div>
          <div class="ep-item-sub">{ep["lens1"]} × {ep["lens2"]}</div>
          <div class="ep-item-meta"><span class="ep-badge {badge_class}">{badge_text}</span></div>
        </div>
      </a>''')

        ep_list_html = "\n".join(ep_items)
        parts_sections.append(f'''
    <section class="part-section" id="{part_id}">
      <div class="part-header">
        <div class="part-label">{part_label}</div>
        <h2 class="part-title">{part_tagline}</h2>
        <p class="part-tagline">{part_sub}</p>
        <div class="part-stats">{ep_count}話 · {part_key}</div>
      </div>
      <div class="ep-list">
{ep_list_html}
      </div>
    </section>''')

    parts_jump_html = "\n      ".join(parts_jump_cards)
    parts_sections_html = "\n".join(parts_sections)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全100話 ロードマップ | 経営のかたち</title>
<meta name="description" content="連載「経営のかたち」全100話の地図。序章5話・PART I-V各18話・終章5話の構成。">
<meta property="og:title" content="全100話 ロードマップ | 経営のかたち">
<meta property="og:type" content="website">
<link rel="canonical" href="https://yuyanishimura0312.github.io/keiei-no-katachi/articles.html">
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700;900&family=Noto+Serif+JP:wght@300;400;500;600;700;900&family=Judson:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<style>
.page-banner {{ background: var(--bg); padding: 80px 24px 48px; border-bottom: 1px solid var(--line); }}
.page-banner-inner {{ max-width: 1080px; margin: 0 auto; }}
.page-banner-eyebrow {{ font-family: var(--sans); font-size: 11px; letter-spacing: 0.32em; color: var(--accent); font-weight: 700; display: flex; align-items: center; gap: 12px; margin-bottom: 24px; }}
.page-banner-eyebrow::before {{ content: ""; width: 32px; height: 2px; background: var(--accent); }}
.page-banner-title {{ font-family: var(--serif); font-weight: 700; font-size: 40px; line-height: 1.45; letter-spacing: 0.04em; color: var(--ink); margin-bottom: 14px; }}
.page-banner-en {{ font-family: var(--display); font-weight: 400; font-size: 20px; color: var(--ink-mute); margin-bottom: 32px; }}
.page-stats {{ display: grid; grid-template-columns: repeat(4, auto); gap: 32px; align-items: baseline; padding-top: 24px; border-top: 1px solid var(--line); font-family: var(--sans); font-size: 11px; letter-spacing: 0.12em; color: var(--ink-mute); }}
.page-stats span {{ display: flex; flex-direction: column; gap: 4px; }}
.page-stats span strong {{ font-family: var(--display); font-weight: 700; font-size: 22px; color: var(--ink); letter-spacing: 0; }}

.series-progress {{ max-width: 1080px; margin: 32px auto 0; padding: 0 24px; }}
.series-progress-bar-wrap {{ background: var(--bg-tint); height: 6px; position: relative; overflow: hidden; }}
.series-progress-bar-fill {{ background: var(--accent); height: 100%; width: {pct}%; }}
.series-progress-meta {{ display: flex; justify-content: space-between; align-items: baseline; margin-top: 8px; font-family: var(--sans); font-size: 10.5px; color: var(--ink-mute); letter-spacing: 0.14em; }}
.series-progress-meta strong {{ color: var(--ink); font-weight: 700; }}

.parts-jump {{ max-width: 1080px; margin: 56px auto 0; padding: 0 24px; }}
.parts-jump-label {{ font-family: var(--sans); font-size: 10.5px; font-weight: 700; letter-spacing: 0.26em; color: var(--accent); margin-bottom: 14px; }}
.parts-jump-title {{ font-family: var(--serif); font-weight: 700; font-size: 22px; color: var(--ink); margin-bottom: 24px; }}
.parts-jump-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }}
.part-jump-card {{ background: var(--bg); border: 1px solid var(--line); padding: 22px 20px; text-decoration: none; display: flex; flex-direction: column; gap: 8px; transition: border-color .15s, transform .15s; }}
.part-jump-card:hover {{ border-color: var(--accent); transform: translateY(-2px); text-decoration: none; }}
.part-jump-num {{ font-family: var(--display); font-weight: 700; font-size: 24px; color: var(--accent); line-height: 1; }}
.part-jump-name {{ font-family: var(--serif); font-weight: 700; font-size: 15px; color: var(--ink); line-height: 1.55; }}
.part-jump-sub {{ font-family: var(--sans); font-size: 10.5px; color: var(--ink-mute); line-height: 1.65; }}

.content-main {{ max-width: 1080px; margin: 64px auto 0; padding: 0 24px 80px; }}

.part-section {{ margin-bottom: 80px; }}
.part-section:last-child {{ margin-bottom: 0; }}
.part-header {{ padding-bottom: 24px; border-bottom: 2px solid var(--ink); margin-bottom: 32px; }}
.part-label {{ font-family: var(--sans); font-size: 11px; font-weight: 700; letter-spacing: 0.28em; color: var(--accent); margin-bottom: 12px; }}
.part-title {{ font-family: var(--serif); font-weight: 700; font-size: 26px; color: var(--ink); letter-spacing: 0.04em; margin-bottom: 8px; }}
.part-tagline {{ font-family: var(--serif); font-size: 14px; color: var(--ink-soft); line-height: 1.85; margin-bottom: 16px; }}
.part-stats {{ font-family: var(--sans); font-size: 11px; letter-spacing: 0.14em; color: var(--ink-mute); }}

.ep-list {{ display: flex; flex-direction: column; gap: 0; }}
.ep-item {{ display: grid; grid-template-columns: 64px 1fr; gap: 20px; padding: 22px 0; border-bottom: 1px solid var(--line-soft); text-decoration: none; transition: background .15s; }}
.ep-item:hover {{ background: var(--bg-soft); text-decoration: none; }}
.ep-item.planned {{ opacity: 0.66; }}
.ep-item-num {{ font-family: var(--display); font-weight: 700; font-size: 24px; color: var(--accent); line-height: 1; }}
.ep-item-num-total {{ font-family: var(--sans); font-size: 10px; color: var(--ink-mute); margin-left: 2px; letter-spacing: 0.06em; }}
.ep-item-body {{ display: flex; flex-direction: column; gap: 6px; }}
.ep-item-eyebrow {{ font-family: var(--sans); font-size: 9.5px; font-weight: 700; letter-spacing: 0.22em; color: var(--accent); text-transform: uppercase; }}
.ep-item-title {{ font-family: var(--serif); font-weight: 700; font-size: 17px; color: var(--ink); line-height: 1.55; letter-spacing: 0.04em; }}
.ep-item-sub {{ font-family: var(--serif); font-size: 13.5px; color: var(--ink-soft); line-height: 1.7; letter-spacing: 0.04em; }}
.ep-item-meta {{ display: flex; align-items: center; gap: 14px; margin-top: 4px; font-family: var(--sans); font-size: 10.5px; color: var(--ink-mute); letter-spacing: 0.08em; }}
.ep-badge {{ display: inline-block; padding: 3px 10px; font-family: var(--sans); font-size: 9.5px; font-weight: 700; letter-spacing: 0.16em; border: 1px solid var(--line); }}
.ep-badge.published {{ color: var(--accent); border-color: var(--accent); }}
.ep-badge.planned {{ color: var(--ink-mute); border-color: var(--ink-mute); }}

@media (max-width: 760px) {{
  .page-banner-title {{ font-size: 28px; }}
  .page-stats {{ grid-template-columns: repeat(2, auto); gap: 18px; }}
  .ep-item {{ grid-template-columns: 1fr; gap: 8px; }}
  .ep-item-title {{ font-size: 15px; }}
}}
</style>
</head>
<body>

<div class="site-header-strip"></div>
<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="site-brand">
      <div class="site-brand-mark"><img src="assets/miratuku-mark.png" alt="ミラツク"></div>
      <div class="site-brand-text">経営のかたち<small>KEIEI NO KATACHI / 他分野が経営の機能に出会うとき</small></div>
    </a>
    <nav class="site-nav">
      <a href="index.html">ホーム</a>
      <a href="articles.html" class="active">全100話</a>
      <a href="index.html#newsletter">メルマガ</a>
    </nav>
  </div>
</header>

<section class="page-banner">
  <div class="page-banner-inner">
    <div class="page-banner-eyebrow">FULL ROADMAP</div>
    <h1 class="page-banner-title">全100話 ロードマップ</h1>
    <p class="page-banner-en">The Complete Map — From Management to Academia</p>
    <div class="page-stats">
      <span>EPISODES<strong>100</strong></span>
      <span>PARTS<strong>5</strong></span>
      <span>FUNCTIONS<strong>5</strong></span>
      <span>PUBLISHED<strong>{drafted}</strong></span>
    </div>
  </div>
</section>

<div class="series-progress">
  <div class="series-progress-bar-wrap"><div class="series-progress-bar-fill"></div></div>
  <div class="series-progress-meta">
    <span><strong>{drafted}</strong> / 100話 公開済み（{pct}%）</span>
    <span>v0.5 / 2026年</span>
  </div>
</div>

<section class="parts-jump">
  <div class="parts-jump-label">JUMP TO PART</div>
  <h2 class="parts-jump-title">5機能 + 序章 + 終章</h2>
  <div class="parts-jump-grid">
      {parts_jump_html}
  </div>
</section>

<main class="content-main">
{parts_sections_html}
</main>

<section class="newsletter" id="newsletter">
  <div class="newsletter-inner">
    <div class="newsletter-eyebrow">EMERGING FUTURE NEWSLETTER</div>
    <h2 class="newsletter-title">新しい話の公開を、まずメールで。</h2>
    <p class="newsletter-desc">本連載「経営のかたち」の更新通知、ミラツクの未来洞察・学術翻訳の最新情報をお届けします。配信停止はいつでも可能です。</p>
    <form class="nl-form" id="nlForm" onsubmit="return false;">
      <div class="nl-step active" id="nlStep1">
        <div class="nl-field"><input type="email" id="nlEmail" placeholder="メールアドレス" autocomplete="email"></div>
        <button type="button" class="nl-btn" onclick="nlNext()">次へ →</button>
        <div class="nl-trust">連載更新・実践事例・関連トピックをお届けします</div>
      </div>
      <div class="nl-step" id="nlStep2">
        <div class="nl-row">
          <div class="nl-field"><input type="text" id="nlName" placeholder="お名前" autocomplete="name"></div>
          <div class="nl-field"><input type="text" id="nlOrg" placeholder="所属（任意）" autocomplete="organization"></div>
        </div>
        <label class="nl-consent"><input type="checkbox" id="nlConsent" checked> メールマガジン配信に同意します。配信停止はいつでも可能です。</label>
        <button type="button" class="nl-btn" id="nlBtn" onclick="submitNl()">登録する</button>
      </div>
    </form>
    <div class="nl-done" id="nlDone">ようこそ。確認メールをお送りしました。<br>これから一緒に「経営のかたち」を読み解いていきましょう。</div>
  </div>
</section>

<script>
const NEWSLETTER_API = 'https://claude-code-manual-app.vercel.app/api/community';

function nlNext() {{
  const v = document.getElementById('nlEmail').value.trim();
  if (!v || !v.includes('@')) {{
    document.getElementById('nlEmail').style.borderColor = 'var(--accent)';
    document.getElementById('nlEmail').focus();
    setTimeout(() => document.getElementById('nlEmail').style.borderColor = '', 2000);
    return;
  }}
  document.getElementById('nlStep1').classList.remove('active');
  document.getElementById('nlStep2').classList.add('active');
  document.getElementById('nlName').focus();
}}
async function submitNl() {{
  const name = document.getElementById('nlName').value.trim();
  const org = document.getElementById('nlOrg').value.trim();
  const email = document.getElementById('nlEmail').value.trim();
  const consent = document.getElementById('nlConsent').checked;
  const btn = document.getElementById('nlBtn');
  if (!name) {{ document.getElementById('nlName').focus(); return; }}
  if (!consent) {{ alert('メールマガジン配信への同意が必要です'); return; }}
  btn.disabled = true;
  btn.textContent = '登録中…';
  try {{
    const res = await fetch(NEWSLETTER_API, {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ name, org, email, source: 'keiei-no-katachi/articles' }}),
    }});
    if (!res.ok) throw new Error('failed');
    document.getElementById('nlForm').classList.add('hide');
    document.getElementById('nlDone').classList.add('show');
  }} catch (e) {{
    alert('登録に失敗しました。少し時間をおいて再度お試しください。');
    btn.disabled = false;
    btn.textContent = '登録する';
  }}
}}
</script>

<footer class="site-footer">
  <div class="site-footer-inner">
    <div class="site-footer-cols">
      <div class="site-footer-col">
        <h4>ABOUT</h4>
        <p><strong>経営のかたち ― 他分野が経営の機能に出会うとき</strong></p>
        <p style="margin-top:8px;color:var(--ink-mute);">経営の主要5機能（マネジメント・ファイナンス・マーケティング・事業開発・営業販売）を、他分野の研究知で読み直す全100話連載。NPO法人ミラツク代表理事・西村勇也。</p>
      </div>
      <div class="site-footer-col">
        <h4>NAVIGATION</h4>
        <ul>
          <li><a href="index.html">ホーム</a></li>
          <li><a href="articles.html">全100話 一覧</a></li>
          <li><a href="#newsletter">メルマガ登録</a></li>
        </ul>
      </div>
      <div class="site-footer-col">
        <h4>MIRA TUKU</h4>
        <ul>
          <li><a href="https://emerging-future.org/" target="_blank" rel="noopener">emerging-future.org</a></li>
          <li><a href="https://github.com/yuyanishimura0312/keiei-no-katachi" target="_blank" rel="noopener">GitHub</a></li>
        </ul>
      </div>
    </div>
    <div class="site-disclaimer" style="padding: 24px 0; border-top: 1px solid var(--line); font-family: var(--serif); font-size: 12.5px; line-height: 1.95; color: var(--ink-mute); letter-spacing: 0.04em;">
      <p style="margin-bottom: 6px;"><strong style="color: var(--ink-soft);">本連載の利用について</strong></p>
      <p>本連載で紹介する研究内容は2025年時点までの公表知見に基づくもので、その後の研究で更新される可能性があります。引用した数値・効果は集団傾向であり、個別の経営判断における結果を保証するものではありません。実務への適用は、組織の文脈に応じてご検討ください。研究の存在・年代・著者は実在検証を行っていますが、解釈や要約に誤りを発見された場合はコメント欄からご指摘ください。</p>
    </div>
    <div class="site-footer-bottom">
      <span>© 2026 NPO法人ミラツク</span>
      <span>経営のかたち ― 他分野が経営の機能に出会うとき</span>
    </div>
  </div>
</footer>

</body>
</html>
"""


def render_index():
    """index.html — トップ（kurashi構造準拠）"""
    drafted = [ep for ep in ROADMAP if ep["status"] == "draft"]
    latest = drafted[0] if drafted else None
    if latest:
        latest_num = int(latest["ep"][2:])
        latest_lower = latest["ep"].lower()
        latest_block = f'''<section class="featured">
      <div class="featured-inner">
        <div class="featured-label">FIRST EPISODE — 第1話から</div>
        <a class="featured-card" href="{latest_lower}.html">
          <div class="featured-num">{latest_num:03d}<span class="featured-num-total">/100</span></div>
          <div class="featured-eyebrow">PROLOGUE — 序 章 第{latest_num}話</div>
          <h2 class="featured-title">{latest["title"]}</h2>
          <p class="featured-sub">― {latest["lens1"]} × {latest["lens2"]}</p>
          <span class="featured-cta">この話を読む →</span>
        </a>
      </div>
    </section>'''
    else:
        latest_block = ""

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>経営のかたち ― 他分野が経営の機能に出会うとき</title>
<meta name="description" content="経営の主要5機能（マネジメント・ファイナンス・マーケティング・事業開発・営業販売）を他分野の研究知で読み直す全100話連載。NPO法人ミラツク。">
<meta property="og:title" content="経営のかたち ― 他分野が経営の機能に出会うとき">
<meta property="og:description" content="他分野が経営の機能に出会うとき。全100回連載。">
<meta property="og:type" content="website">
<link rel="canonical" href="https://yuyanishimura0312.github.io/keiei-no-katachi/">
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700;900&family=Noto+Serif+JP:wght@300;400;500;600;700;900&family=Judson:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<style>
.hero {{ padding: 120px 24px 80px; background: var(--bg); border-bottom: 1px solid var(--line); }}
.hero-inner {{ max-width: 980px; margin: 0 auto; }}
.hero-eyebrow {{ font-family: var(--sans); font-size: 11.5px; letter-spacing: 0.36em; color: var(--accent); font-weight: 700; display: flex; align-items: center; gap: 14px; margin-bottom: 32px; }}
.hero-eyebrow::before {{ content: ""; width: 40px; height: 2px; background: var(--accent); }}
.hero-title {{ font-family: var(--serif); font-weight: 700; font-size: 56px; line-height: 1.4; letter-spacing: 0.02em; color: var(--ink); margin-bottom: 24px; }}
.hero-en {{ font-family: var(--display); font-size: 24px; color: var(--ink-mute); letter-spacing: 0.02em; margin-bottom: 32px; }}
.hero-tagline {{ font-family: var(--serif); font-size: 17px; line-height: 2; color: var(--ink-soft); max-width: 640px; padding-left: 22px; border-left: 3px solid var(--accent); margin-bottom: 40px; }}
.hero-cta {{ display: flex; gap: 14px; flex-wrap: wrap; }}
.hero-cta a {{ display: inline-flex; align-items: center; padding: 14px 28px; font-family: var(--sans); font-size: 12px; font-weight: 700; letter-spacing: 0.16em; text-decoration: none; transition: background .15s; }}
.hero-cta .primary {{ background: var(--accent); color: var(--bg); }}
.hero-cta .primary:hover {{ background: var(--accent-deep); text-decoration: none; }}
.hero-cta .secondary {{ background: transparent; color: var(--ink); border: 1px solid var(--ink); }}
.hero-cta .secondary:hover {{ background: var(--ink); color: var(--bg); text-decoration: none; }}

.intro {{ padding: 80px 24px; background: var(--bg-soft); border-bottom: 1px solid var(--line); }}
.intro-inner {{ max-width: 720px; margin: 0 auto; }}
.intro p {{ font-family: var(--serif); font-size: 16px; line-height: 2.1; color: var(--ink-soft); margin-bottom: 24px; }}
.intro p strong {{ color: var(--ink); font-weight: 600; }}

.featured {{ padding: 80px 24px; background: var(--bg); border-bottom: 1px solid var(--line); }}
.featured-inner {{ max-width: 720px; margin: 0 auto; }}
.featured-label {{ font-family: var(--sans); font-size: 11px; font-weight: 700; letter-spacing: 0.32em; color: var(--accent); margin-bottom: 24px; }}
.featured-card {{ display: block; padding: 40px 36px; background: var(--bg-tint); border: 1px solid var(--line); text-decoration: none; transition: border-color .15s, transform .15s; }}
.featured-card:hover {{ border-color: var(--accent); transform: translateY(-2px); text-decoration: none; }}
.featured-num {{ font-family: var(--display); font-weight: 700; font-size: 56px; color: var(--ink); line-height: 1; margin-bottom: 16px; }}
.featured-num-total {{ font-family: var(--sans); font-size: 14px; color: var(--ink-mute); margin-left: 4px; letter-spacing: 0.08em; }}
.featured-eyebrow {{ font-family: var(--sans); font-size: 10.5px; font-weight: 700; letter-spacing: 0.22em; color: var(--accent); margin-bottom: 14px; }}
.featured-title {{ font-family: var(--serif); font-weight: 700; font-size: 26px; line-height: 1.55; color: var(--ink); margin-bottom: 12px; }}
.featured-sub {{ font-family: var(--serif); font-size: 15px; color: var(--ink-soft); line-height: 1.85; margin-bottom: 24px; }}
.featured-cta {{ font-family: var(--sans); font-size: 11.5px; font-weight: 700; letter-spacing: 0.16em; color: var(--accent); }}

.parts-overview {{ padding: 80px 24px; background: var(--bg); }}
.parts-overview-inner {{ max-width: 1080px; margin: 0 auto; }}
.parts-overview-label {{ font-family: var(--sans); font-size: 11px; font-weight: 700; letter-spacing: 0.32em; color: var(--accent); margin-bottom: 14px; }}
.parts-overview-title {{ font-family: var(--serif); font-weight: 700; font-size: 32px; color: var(--ink); margin-bottom: 40px; }}
.parts-overview-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; }}
.parts-overview-card {{ padding: 28px 24px; background: var(--bg-soft); border: 1px solid var(--line); text-decoration: none; transition: border-color .15s, transform .15s; }}
.parts-overview-card:hover {{ border-color: var(--accent); transform: translateY(-2px); text-decoration: none; }}
.parts-overview-card-num {{ font-family: var(--display); font-weight: 700; font-size: 22px; color: var(--accent); margin-bottom: 8px; }}
.parts-overview-card-title {{ font-family: var(--serif); font-weight: 700; font-size: 17px; color: var(--ink); line-height: 1.55; margin-bottom: 8px; }}
.parts-overview-card-sub {{ font-family: var(--sans); font-size: 11px; color: var(--ink-mute); line-height: 1.7; }}

@media (max-width: 760px) {{
  .hero-title {{ font-size: 32px; }}
  .hero-en {{ font-size: 18px; }}
  .featured-title {{ font-size: 20px; }}
  .featured-num {{ font-size: 40px; }}
}}
</style>
</head>
<body>

<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="site-brand">
      <div class="site-brand-mark"><img src="assets/miratuku-mark.png" alt="ミラツク"></div>
      <div class="site-brand-text">経営のかたち<small>KEIEI NO KATACHI / 他分野が経営の機能に出会うとき</small></div>
    </a>
    <nav class="site-nav">
      <a href="index.html" class="active">ホーム</a>
      <a href="articles.html">全100話</a>
      <a href="#newsletter">メルマガ</a>
    </nav>
  </div>
</header>

<section class="hero">
  <div class="hero-inner">
    <div class="hero-eyebrow">A SERIES OF ONE HUNDRED — 全100話連載</div>
    <h1 class="hero-title">経営のかたち</h1>
    <p class="hero-en">Forms of Management — Where Other Disciplines Meet Business Functions</p>
    <p class="hero-tagline">経営の主要5機能（マネジメント・ファイナンス・マーケティング・事業開発・営業販売）を、他分野の研究知で読み直す全100話連載。リーダーシップを贈与論で、ファイナンスを経済人類学で、マーケティングを神話論で、事業開発を進化生物学で、営業を弁論術で読み解いていきます。</p>
    <div class="hero-cta">
      <a class="primary" href="ep001.html">第1話から読む →</a>
      <a class="secondary" href="articles.html">全100話の地図を見る</a>
    </div>
  </div>
</section>

<section class="intro">
  <div class="intro-inner">
    <p>経営学の語彙は20世紀に体系化され、世界中のMBA教育を支えてきました。けれど現実の経営の現場では、その語彙だけでは届かない領域があります。<strong>経営のかたち</strong>は、その領域を他分野の研究知で読み直す試みです。</p>
    <p>経営の主要5機能（<strong>マネジメント・ファイナンス・マーケティング・事業開発・営業販売</strong>）を、人類学・哲学・神経科学・進化生物学・神話学・古代修辞学・記号論・ゲーム理論など、50以上の学問分野で読み直す全100話を編んでいきます。</p>
    <p>各話には<strong>2つの異なる学問のレンズ</strong>を置きます。本文（lens1）と DEEPER box（lens2）が、同じ問いを別の角度から照らす——その出会いの瞬間が、新しい経営の知を生みます。Translational Editor の視点から、経営機能の前提を問い直していきます。</p>
  </div>
</section>

{latest_block}

<section class="parts-overview">
  <div class="parts-overview-inner">
    <div class="parts-overview-label">FIVE FUNCTIONS — 5つの機能</div>
    <h2 class="parts-overview-title">経営を支える5つの機能</h2>
    <div class="parts-overview-grid">
      <a class="parts-overview-card" href="articles.html#part-i"><div class="parts-overview-card-num">PART I</div><div class="parts-overview-card-title">マネジメント — 統率・組織・継承</div><div class="parts-overview-card-sub">リーダーシップ・組織変革・後継者問題</div></a>
      <a class="parts-overview-card" href="articles.html#part-ii"><div class="parts-overview-card-num">PART II</div><div class="parts-overview-card-title">ファイナンス — 利子・通貨・リスク</div><div class="parts-overview-card-sub">投資判断・資本コスト・新しい経済学</div></a>
      <a class="parts-overview-card" href="articles.html#part-iii"><div class="parts-overview-card-num">PART III</div><div class="parts-overview-card-title">マーケティング — 物語・記号・神話</div><div class="parts-overview-card-sub">ブランド・パッケージ・口コミ・体験</div></a>
      <a class="parts-overview-card" href="articles.html#part-iv"><div class="parts-overview-card-num">PART IV</div><div class="parts-overview-card-title">事業開発 — 適応・共創・撤退</div><div class="parts-overview-card-sub">起業・新規事業・ピボット・終末期</div></a>
      <a class="parts-overview-card" href="articles.html#part-v"><div class="parts-overview-card-num">PART V</div><div class="parts-overview-card-title">営業・販売 — 弁論・関係・儀礼</div><div class="parts-overview-card-sub">提案・信頼・徒弟・接待・テリトリー</div></a>
    </div>
  </div>
</section>

<section class="newsletter" id="newsletter">
  <div class="newsletter-inner">
    <div class="newsletter-eyebrow">EMERGING FUTURE NEWSLETTER</div>
    <h2 class="newsletter-title">新しい話の公開を、まずメールで。</h2>
    <p class="newsletter-desc">本連載「経営のかたち」の更新通知、ミラツクの未来洞察・学術翻訳の最新情報をお届けします。配信停止はいつでも可能です。</p>
    <form class="nl-form" id="nlForm" onsubmit="return false;">
      <div class="nl-step active" id="nlStep1">
        <div class="nl-field"><input type="email" id="nlEmail" placeholder="メールアドレス" autocomplete="email"></div>
        <button type="button" class="nl-btn" onclick="nlNext()">次へ →</button>
        <div class="nl-trust">連載更新・実践事例・関連トピックをお届けします</div>
      </div>
      <div class="nl-step" id="nlStep2">
        <div class="nl-row">
          <div class="nl-field"><input type="text" id="nlName" placeholder="お名前" autocomplete="name"></div>
          <div class="nl-field"><input type="text" id="nlOrg" placeholder="所属（任意）" autocomplete="organization"></div>
        </div>
        <label class="nl-consent"><input type="checkbox" id="nlConsent" checked> メールマガジン配信に同意します。配信停止はいつでも可能です。</label>
        <button type="button" class="nl-btn" id="nlBtn" onclick="submitNl()">登録する</button>
      </div>
    </form>
    <div class="nl-done" id="nlDone">ようこそ。確認メールをお送りしました。<br>これから一緒に「経営のかたち」を読み解いていきましょう。</div>
  </div>
</section>

<script>
const NEWSLETTER_API = 'https://claude-code-manual-app.vercel.app/api/community';

function nlNext() {{
  const v = document.getElementById('nlEmail').value.trim();
  if (!v || !v.includes('@')) {{
    document.getElementById('nlEmail').style.borderColor = 'var(--accent)';
    document.getElementById('nlEmail').focus();
    setTimeout(() => document.getElementById('nlEmail').style.borderColor = '', 2000);
    return;
  }}
  document.getElementById('nlStep1').classList.remove('active');
  document.getElementById('nlStep2').classList.add('active');
  document.getElementById('nlName').focus();
}}
async function submitNl() {{
  const name = document.getElementById('nlName').value.trim();
  const org = document.getElementById('nlOrg').value.trim();
  const email = document.getElementById('nlEmail').value.trim();
  const consent = document.getElementById('nlConsent').checked;
  const btn = document.getElementById('nlBtn');
  if (!name) {{ document.getElementById('nlName').focus(); return; }}
  if (!consent) {{ alert('メールマガジン配信への同意が必要です'); return; }}
  btn.disabled = true;
  btn.textContent = '登録中…';
  try {{
    const res = await fetch(NEWSLETTER_API, {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ name, org, email, source: 'keiei-no-katachi/index' }}),
    }});
    if (!res.ok) throw new Error('failed');
    document.getElementById('nlForm').classList.add('hide');
    document.getElementById('nlDone').classList.add('show');
  }} catch (e) {{
    alert('登録に失敗しました。少し時間をおいて再度お試しください。');
    btn.disabled = false;
    btn.textContent = '登録する';
  }}
}}
</script>

<footer class="site-footer">
  <div class="site-footer-inner">
    <div class="site-footer-cols">
      <div class="site-footer-col">
        <h4>ABOUT</h4>
        <p><strong>経営のかたち ― 他分野が経営の機能に出会うとき</strong></p>
        <p style="margin-top:8px;color:var(--ink-mute);">経営の主要5機能を、他分野の研究知で読み直す全100話連載。NPO法人ミラツク代表理事・西村勇也。</p>
      </div>
      <div class="site-footer-col">
        <h4>NAVIGATION</h4>
        <ul>
          <li><a href="index.html">ホーム</a></li>
          <li><a href="articles.html">全100話 一覧</a></li>
          <li><a href="#newsletter">メルマガ登録</a></li>
        </ul>
      </div>
      <div class="site-footer-col">
        <h4>MIRA TUKU</h4>
        <ul>
          <li><a href="https://emerging-future.org/" target="_blank" rel="noopener">emerging-future.org</a></li>
          <li><a href="https://github.com/yuyanishimura0312/keiei-no-katachi" target="_blank" rel="noopener">GitHub</a></li>
        </ul>
      </div>
    </div>
    <div class="site-disclaimer" style="padding: 24px 0; border-top: 1px solid var(--line); font-family: var(--serif); font-size: 12.5px; line-height: 1.95; color: var(--ink-mute); letter-spacing: 0.04em;">
      <p style="margin-bottom: 6px;"><strong style="color: var(--ink-soft);">本連載の利用について</strong></p>
      <p>本連載で紹介する研究内容は2025年時点までの公表知見に基づくもので、その後の研究で更新される可能性があります。引用した数値・効果は集団傾向であり、個別の経営判断における結果を保証するものではありません。実務への適用は、組織の文脈に応じてご検討ください。研究の存在・年代・著者は実在検証を行っていますが、解釈や要約に誤りを発見された場合はコメント欄からご指摘ください。</p>
    </div>
    <div class="site-footer-bottom">
      <span>© 2026 NPO法人ミラツク</span>
      <span>経営のかたち ― 他分野が経営の機能に出会うとき</span>
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
