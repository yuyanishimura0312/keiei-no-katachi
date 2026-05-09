"""generate.py — 各話のHTMLを生成する"""

from pathlib import Path
from articles_batch1 import ARTICLES_BATCH1
from articles_batch2 import ARTICLES_BATCH2
from articles_batch3 import ARTICLES_BATCH3
from articles_batch4 import ARTICLES_BATCH4
from articles_batch5 import ARTICLES_BATCH5
from articles_batch6 import ARTICLES_BATCH6
from articles_batch7 import ARTICLES_BATCH7
from articles_batch8 import ARTICLES_BATCH8

ARTICLES = ARTICLES_BATCH1 + ARTICLES_BATCH2 + ARTICLES_BATCH3 + ARTICLES_BATCH4 + ARTICLES_BATCH5 + ARTICLES_BATCH6 + ARTICLES_BATCH7 + ARTICLES_BATCH8

ROOT = Path(__file__).parent

EP_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>第{ep_num_int}話 ― {title_main} | 経営のかたち</title>
<meta name="description" content="経営のかたち第{ep_num_int}話。{title_sub_clean}">
<meta property="og:title" content="第{ep_num_int}話 ― {title_main}">
<meta property="og:description" content="{title_sub_clean}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://yuyanishimura0312.github.io/keiei-no-katachi/{ep_lower}.html">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://yuyanishimura0312.github.io/keiei-no-katachi/{ep_lower}.html">
<link rel="icon" href="https://esse-sense.com/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700;900&family=Noto+Serif+JP:wght@300;400;500;600;700;900&family=Judson:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="site-brand">
      <div class="site-brand-text">経営のかたち<small>KEIEI NO KATACHI / 他分野が経営の機能に出会うとき</small></div>
    </a>
    <nav class="site-nav">
      <a href="index.html">ホーム</a>
      <a href="articles.html">全100話</a>
    </nav>
  </div>
</header>

<section class="ep-hero">
  <div class="ep-hero-inner">
    <div class="ep-hero-eyebrow">{eyebrow}</div>
    <div class="ep-hero-num">{ep_num_int:02d}.<span class="ep-hero-num-total">/ 100</span></div>
    <h1 class="ep-hero-title">{title_main}</h1>
    <p class="ep-hero-subtitle">{title_sub}</p>
    <p class="ep-hero-en">{title_en}</p>
    <p class="ep-hero-lead">{lead}</p>
    <div class="ep-hero-meta">
      <span class="ep-hero-author"><strong>西村 勇也</strong>（NPO法人ミラツク 代表理事）</span>
      <span class="ep-hero-date">2026年5月9日</span>
      <span class="read-time">推定読了 {read_time}</span>
      <span style="color: var(--ink-mute);">学術領域: {domain}</span>
    </div>
  </div>
</section>

<div class="ep-layout">

  <aside class="toc-sidebar" aria-label="連載目次">
    <div class="toc-label">FULL SERIES — 全100話</div>
    <div class="toc-section">
      <a class="toc-part" href="articles.html#prologue">PROLOGUE — 序 章</a>
      <a class="toc-part-title" href="articles.html#prologue">経営機能を他分野で読む</a>
    </div>
    <div class="toc-section">
      <a class="toc-part" href="articles.html#part-i">PART I — マネジメント</a>
      <a class="toc-part-title" href="articles.html#part-i">統率・組織・継承</a>
    </div>
    <div class="toc-section">
      <a class="toc-part" href="articles.html#part-ii">PART II — ファイナンス</a>
      <a class="toc-part-title" href="articles.html#part-ii">利子・通貨・リスク</a>
    </div>
    <div class="toc-section">
      <a class="toc-part" href="articles.html#part-iii">PART III — マーケティング</a>
      <a class="toc-part-title" href="articles.html#part-iii">物語・記号・神話</a>
    </div>
    <div class="toc-section">
      <a class="toc-part" href="articles.html#part-iv">PART IV — 事業開発</a>
      <a class="toc-part-title" href="articles.html#part-iv">適応・共創・撤退</a>
    </div>
    <div class="toc-section">
      <a class="toc-part" href="articles.html#part-v">PART V — 営業・販売</a>
      <a class="toc-part-title" href="articles.html#part-v">弁論・関係・儀礼</a>
    </div>
    <div class="toc-section">
      <a class="toc-part" href="articles.html#final">FINAL — 終 章</a>
      <a class="toc-part-title" href="articles.html#final">機能横断の経営論</a>
    </div>
    <div class="toc-section">
      <span class="toc-current">第{ep_num_int}話 ― {title_main}</span>
    </div>
  </aside>

  <article class="ep-body" id="articleBody">
{body_html}
    <details class="reading-lens" open id="lens-academic-deep">
      <summary class="reading-lens-trigger">
        <span class="reading-lens-label">DEEPER</span>
        <span class="reading-lens-title">別レンズで深めると — {lens2}</span>
        <span class="reading-lens-arrow">▾</span>
      </summary>
      <div class="reading-lens-body">
{deep_html}
        <div class="signal-list">
{signals_html}
        </div>
      </div>
    </details>

    <details class="reading-lens" id="lens-key-reference">
      <summary class="reading-lens-trigger">
        <span class="reading-lens-label">KEY REFERENCE</span>
        <span class="reading-lens-title">この回の典拠</span>
        <span class="reading-lens-arrow">▾</span>
      </summary>
      <div class="reading-lens-body">
        <ul class="ref-list">
{refs_html}
        </ul>
      </div>
    </details>

    <section class="ep-question">
      <div class="ep-question-label">QUESTION FOR NEXT — 次号への問い</div>
      <p class="ep-question-q">{question}</p>
      <div class="ep-question-next">
        <span class="ep-question-next-meta">NEXT EPISODE</span>
        <span class="ep-question-next-title">第{next_ep_int}話「{next_title}」</span>
      </div>
    </section>

  </article>
</div>

<nav class="ep-nav">
  <div class="ep-nav-inner">
    {prev_html}
    {next_html}
  </div>
</nav>

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


def render_paragraphs(paragraphs):
    return "\n".join(f"    <p>{p}</p>" for p in paragraphs)


def render_signals(signals):
    items = []
    for s in signals:
        items.append(f'          <div class="signal-item"><div class="signal-num">{s["id"]}</div><p class="signal-text">{s["stat"]}</p></div>')
    return "\n".join(items)


def render_refs(refs):
    items = []
    for r in refs:
        items.append(f'          <li><strong>{r["text"]}</strong><span class="ref-doi">{r["doi"]}</span></li>')
    return "\n".join(items)


def render_nav(prev_article, next_article):
    if prev_article:
        prev_n = int(prev_article["ep_number"][2:])
        prev_html = f'''<a class="ep-nav-link" href="{prev_article["ep_number"].lower()}.html">
      <span class="ep-nav-label">← PREV</span>
      <span class="ep-nav-title">第{prev_n}話「{prev_article["title_main"]}」</span>
    </a>'''
    else:
        prev_html = '''<a class="ep-nav-link disabled" href="#" aria-disabled="true">
      <span class="ep-nav-label">← PREV</span>
      <span class="ep-nav-title">― 連載のはじまり ―</span>
    </a>'''

    if next_article:
        next_n = int(next_article["ep_number"][2:])
        next_html = f'''<a class="ep-nav-link next" href="{next_article["ep_number"].lower()}.html">
      <span class="ep-nav-label">NEXT →</span>
      <span class="ep-nav-title">第{next_n}話「{next_article["title_main"]}」</span>
    </a>'''
    else:
        next_html = '''<a class="ep-nav-link next disabled" href="#" aria-disabled="true">
      <span class="ep-nav-label">NEXT →</span>
      <span class="ep-nav-title">― 公開予定 ―</span>
    </a>'''

    return prev_html, next_html


def main():
    for i, article in enumerate(ARTICLES):
        ep_num_int = int(article["ep_number"][2:])
        ep_lower = article["ep_number"].lower()
        title_sub_clean = article["title_sub"].replace("―", "").strip()

        prev_article = ARTICLES[i - 1] if i > 0 else None
        next_article = ARTICLES[i + 1] if i < len(ARTICLES) - 1 else None

        prev_html, next_html = render_nav(prev_article, next_article)

        # next_ep_int handling - even when next_article is None, we still have next_ep in data
        try:
            next_ep_int = int(article["next_ep"][2:])
        except (KeyError, ValueError):
            next_ep_int = ep_num_int + 1

        html = EP_TEMPLATE.format(
            ep_num_int=ep_num_int,
            ep_lower=ep_lower,
            title_main=article["title_main"],
            title_sub=article["title_sub"],
            title_sub_clean=title_sub_clean,
            title_en=article["title_en"],
            eyebrow=article["eyebrow"],
            lead=article["lead"],
            read_time=article["read_time"],
            domain=article["domain"],
            body_html=render_paragraphs(article["body_paragraphs"]),
            lens2=article["lens2"],
            deep_html=render_paragraphs(article["academic_deep_paragraphs"]),
            signals_html=render_signals(article["signals"]),
            refs_html=render_refs(article["key_references"]),
            question=article["question"],
            next_ep_int=next_ep_int,
            next_title=article.get("next_title", ""),
            prev_html=prev_html,
            next_html=next_html,
        )

        out_path = ROOT / f"{ep_lower}.html"
        out_path.write_text(html, encoding="utf-8")
        print(f"  generated: {out_path.name}")

    print(f"\nTotal: {len(ARTICLES)} HTML files")


if __name__ == "__main__":
    main()
