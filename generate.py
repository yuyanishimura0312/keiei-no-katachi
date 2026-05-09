"""generate.py — 各話のHTMLを生成する（kurashi-no-katachi構造に準拠）"""

from pathlib import Path
from articles_batch1 import ARTICLES_BATCH1
from articles_batch2 import ARTICLES_BATCH2
from articles_batch3 import ARTICLES_BATCH3
from articles_batch4 import ARTICLES_BATCH4
from articles_batch5 import ARTICLES_BATCH5
from articles_batch6 import ARTICLES_BATCH6
from articles_batch7 import ARTICLES_BATCH7
from articles_batch8 import ARTICLES_BATCH8
from articles_batch9 import ARTICLES_BATCH9
from articles_batch10 import ARTICLES_BATCH10
from articles_batch11 import ARTICLES_BATCH11
from articles_batch12 import ARTICLES_BATCH12
from articles_batch13 import ARTICLES_BATCH13
from articles_batch14 import ARTICLES_BATCH14
from articles_batch15 import ARTICLES_BATCH15
from articles_batch16 import ARTICLES_BATCH16
from articles_batch17 import ARTICLES_BATCH17
from articles_batch18 import ARTICLES_BATCH18
from articles_batch19 import ARTICLES_BATCH19
from articles_batch20 import ARTICLES_BATCH20

ARTICLES = (
    ARTICLES_BATCH1 + ARTICLES_BATCH2 + ARTICLES_BATCH3 + ARTICLES_BATCH4 + ARTICLES_BATCH5
    + ARTICLES_BATCH6 + ARTICLES_BATCH7 + ARTICLES_BATCH8 + ARTICLES_BATCH9 + ARTICLES_BATCH10
    + ARTICLES_BATCH11 + ARTICLES_BATCH12 + ARTICLES_BATCH13 + ARTICLES_BATCH14 + ARTICLES_BATCH15
    + ARTICLES_BATCH16 + ARTICLES_BATCH17 + ARTICLES_BATCH18 + ARTICLES_BATCH19 + ARTICLES_BATCH20
)

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

<div class="read-progress" aria-hidden="true"><div class="read-progress-bar" id="readProgressBar"></div></div>

<div class="site-header-strip"></div>
<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="site-brand">
      <div class="site-brand-mark"><img src="assets/miratuku-mark.png" alt="ミラツク"></div>
      <div class="site-brand-text">経営のかたち<small>KEIEI NO KATACHI / 他分野が経営の機能に出会うとき</small></div>
    </a>
    <nav class="site-nav">
      <a href="index.html">ホーム</a>
      <a href="articles.html">全100話</a>
      <a href="#newsletter">メルマガ</a>
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
      <span class="read-time" id="readTime">推定読了 {read_time}</span>
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

<section class="ep-actions" aria-label="読了後アクション">
  <div class="ep-actions-inner">
    <a class="ep-action-btn primary" href="#newsletter">メルマガで次話を受け取る</a>
    <a class="ep-action-btn" href="#comments">この話に感想を送る</a>
    <a class="ep-action-btn" href="articles.html">全100話の地図へ</a>
  </div>
</section>

<nav class="ep-nav">
  <div class="ep-nav-inner">
    {prev_html}
    {next_html}
  </div>
</nav>

<section class="feedback-section" id="comments">
  <div class="feedback-inner">
    <div class="feedback-label">COMMENTS ・ 感想・コメント</div>
    <h2 class="feedback-title">この話に感想を送る</h2>
    <p class="feedback-desc">読んで感じたこと、気になった一文、ご質問、関連する話題――どのようなものでも歓迎します。編集長（西村）に直接届きます。</p>
    <form class="feedback-form" id="fbForm" onsubmit="return false;">
      <div class="feedback-field">
        <label for="fbSuggestion">コメント <span style="color:var(--accent);">*</span></label>
        <textarea id="fbSuggestion" placeholder="ご自由にお書きください" required></textarea>
      </div>
      <div class="feedback-row">
        <div class="feedback-field"><label for="fbName">お名前（任意）</label><input type="text" id="fbName" autocomplete="name" placeholder="匿名でも構いません"></div>
        <div class="feedback-field"><label for="fbEmail">メール（任意・返信が必要なときのみ）</label><input type="email" id="fbEmail" autocomplete="email" placeholder="返信不要なら空欄で"></div>
      </div>
      <button type="button" class="feedback-submit" id="fbSubmit" onclick="submitFeedback()">送信する</button>
    </form>
    <div class="feedback-done" id="fbDone">ありがとうございました。コメントを受け取りました。</div>
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

<script src="script.js"></script>
<script>
const EPISODE_ID = '{ep_lower}';
const EPISODE_TITLE = '第{ep_num_int}話 ― {title_main}';
</script>

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
      <span class="ep-nav-title">― 連載完結 ―</span>
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

    print(f"Total: {len(ARTICLES)} HTML files generated")


if __name__ == "__main__":
    main()
