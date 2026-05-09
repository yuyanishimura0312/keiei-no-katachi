"""経営のかたち — 100話ロードマップ v0.5.1

各話には2つの分野レンズが割り当てられる:
- lens1: 本文の主分野（直感的・物語的）
- lens2: DEEPERの第2分野（理論的補強または対比）
"""

ROADMAP = [
    # 序章
    {"ep": "EP001", "part": "PROLOGUE", "title": "経営機能を「他分野で読む」とは", "lens1": "経営学史", "lens2": "翻訳論", "status": "draft"},
    {"ep": "EP002", "part": "PROLOGUE", "title": "経営学だけでは届かない領域", "lens1": "知識社会学", "lens2": "学際研究方法論", "status": "draft"},
    {"ep": "EP003", "part": "PROLOGUE", "title": "5機能と他分野マップ", "lens1": "機能主義経営論", "lens2": "タクソノミー論", "status": "draft"},
    {"ep": "EP004", "part": "PROLOGUE", "title": "ベストプラクティスの限界", "lens1": "経営理論批判", "lens2": "暗黙知論", "status": "draft"},
    {"ep": "EP005", "part": "PROLOGUE", "title": "翻訳という方法論", "lens1": "Translational Science", "lens2": "哲学的解釈学", "status": "draft"},

    # PART I マネジメント
    {"ep": "EP006", "part": "I", "title": "リーダーシップは贈与の連鎖だった", "lens1": "経済人類学", "lens2": "神経科学", "status": "draft"},
    {"ep": "EP007", "part": "I", "title": "組織の血液循環", "lens1": "細胞生物学", "lens2": "ネットワーク科学", "status": "draft"},
    {"ep": "EP008", "part": "I", "title": "撤退戦の哲学", "lens1": "老荘思想", "lens2": "ゲーム理論", "status": "draft"},
    {"ep": "EP009", "part": "I", "title": "暗黙知は儀礼で渡される", "lens1": "知識論", "lens2": "認知言語学", "status": "draft"},
    {"ep": "EP010", "part": "I", "title": "群れの動きと組織行動", "lens1": "動物行動学", "lens2": "群知能", "status": "draft"},
    {"ep": "EP011", "part": "I", "title": "意思決定する身体", "lens1": "神経科学", "lens2": "哲学", "status": "draft"},
    {"ep": "EP012", "part": "I", "title": "オフィスは記憶の容器", "lens1": "環境心理学", "lens2": "古代修辞学", "status": "draft"},
    {"ep": "EP013", "part": "I", "title": "働き方の歴史", "lens1": "経済史", "lens2": "時間人類学", "status": "draft"},
    {"ep": "EP014", "part": "I", "title": "評価制度と公正世界仮説", "lens1": "社会心理学", "lens2": "政治哲学", "status": "draft"},
    {"ep": "EP015", "part": "I", "title": "多様性と生態系の安定", "lens1": "生態学", "lens2": "複雑系", "status": "draft"},
    {"ep": "EP016", "part": "I", "title": "組織変革は相転移する", "lens1": "複雑系物理学", "lens2": "縁起観", "status": "draft"},
    {"ep": "EP017", "part": "I", "title": "失敗の儀礼", "lens1": "文化人類学", "lens2": "ナラティブ療法", "status": "draft"},
    {"ep": "EP018", "part": "I", "title": "創造性と即興演劇", "lens1": "演劇研究", "lens2": "認知心理学", "status": "draft"},
    {"ep": "EP019", "part": "I", "title": "後継者問題と能の伝承", "lens1": "芸能史", "lens2": "進化生物学", "status": "draft"},
    {"ep": "EP020", "part": "I", "title": "コモンズの経営", "lens1": "政治哲学", "lens2": "生態学", "status": "draft"},
    {"ep": "EP021", "part": "I", "title": "距離をどう保つか", "lens1": "文化人類学", "lens2": "愛着理論", "status": "draft"},
    {"ep": "EP022", "part": "I", "title": "沈黙のマネジメント", "lens1": "比較宗教学", "lens2": "認知科学", "status": "draft"},
    {"ep": "EP023", "part": "I", "title": "終わりの設計", "lens1": "死生学", "lens2": "ハイデガー哲学", "status": "draft"},

    # PART II ファイナンス
    {"ep": "EP024", "part": "II", "title": "利子の起源", "lens1": "経済史", "lens2": "比較宗教学", "status": "draft"},
    {"ep": "EP025", "part": "II", "title": "投資判断と狩猟採集", "lens1": "進化心理学", "lens2": "行動経済学", "status": "draft"},
    {"ep": "EP026", "part": "II", "title": "リスクは身体で感じる", "lens1": "生理学", "lens2": "実存哲学", "status": "draft"},
    {"ep": "EP027", "part": "II", "title": "バランスシートの哲学", "lens1": "数学史", "lens2": "構造主義", "status": "planned"},
    {"ep": "EP028", "part": "II", "title": "通貨は贈与から生まれた", "lens1": "経済人類学", "lens2": "言語学", "status": "planned"},
    {"ep": "EP029", "part": "II", "title": "流動性と河川", "lens1": "水文学", "lens2": "古代ギリシア哲学", "status": "planned"},
    {"ep": "EP030", "part": "II", "title": "バブルと群衆", "lens1": "社会心理学", "lens2": "ジラール", "status": "planned"},
    {"ep": "EP031", "part": "II", "title": "資本コストと時間哲学", "lens1": "ベルクソン", "lens2": "熱力学", "status": "planned"},
    {"ep": "EP032", "part": "II", "title": "損切りの神経科学", "lens1": "プロスペクト理論", "lens2": "ストア派", "status": "planned"},
    {"ep": "EP033", "part": "II", "title": "為替と境界の人類学", "lens1": "国境研究", "lens2": "言語学", "status": "planned"},
    {"ep": "EP034", "part": "II", "title": "ESG投資の倫理学", "lens1": "環境哲学", "lens2": "先住民研究", "status": "planned"},
    {"ep": "EP035", "part": "II", "title": "企業価値は物語である", "lens1": "ナラティブ経済学", "lens2": "ナラトロジー", "status": "planned"},
    {"ep": "EP036", "part": "II", "title": "資本市場の神話", "lens1": "神話論", "lens2": "ユング心理学", "status": "planned"},
    {"ep": "EP037", "part": "II", "title": "配当と種子", "lens1": "農学", "lens2": "進化遺伝学", "status": "planned"},
    {"ep": "EP038", "part": "II", "title": "暗号通貨と信頼", "lens1": "ルーマン社会学", "lens2": "ゲーム理論", "status": "planned"},
    {"ep": "EP039", "part": "II", "title": "相続の民俗学", "lens1": "民俗学", "lens2": "デュメジル神話学", "status": "planned"},
    {"ep": "EP040", "part": "II", "title": "余剰の使い方", "lens1": "経済人類学", "lens2": "バタイユ", "status": "planned"},
    {"ep": "EP041", "part": "II", "title": "仏教経済学", "lens1": "思想史", "lens2": "脱成長論", "status": "planned"},

    # PART III マーケティング
    {"ep": "EP042", "part": "III", "title": "ブランドは現代の神話", "lens1": "比較神話学", "lens2": "記号学", "status": "planned"},
    {"ep": "EP043", "part": "III", "title": "価格は知覚される", "lens1": "心理物理学", "lens2": "神経経済学", "status": "planned"},
    {"ep": "EP044", "part": "III", "title": "物語の構造とマーケティング", "lens1": "ナラトロジー", "lens2": "認知言語学", "status": "planned"},
    {"ep": "EP045", "part": "III", "title": "共感の神経科学", "lens1": "ミラーニューロン", "lens2": "現象学", "status": "planned"},
    {"ep": "EP046", "part": "III", "title": "パッケージは記号である", "lens1": "記号論", "lens2": "美学", "status": "planned"},
    {"ep": "EP047", "part": "III", "title": "口コミは都市伝説", "lens1": "民俗学", "lens2": "進化生物学", "status": "planned"},
    {"ep": "EP048", "part": "III", "title": "顧客体験の現象学", "lens1": "メルロ＝ポンティ", "lens2": "体験経済論", "status": "planned"},
    {"ep": "EP049", "part": "III", "title": "色彩と認知", "lens1": "色彩心理学", "lens2": "文化人類学", "status": "planned"},
    {"ep": "EP050", "part": "III", "title": "店舗の音楽", "lens1": "環境音響学", "lens2": "音楽人類学", "status": "planned"},
    {"ep": "EP051", "part": "III", "title": "ヴィジュアル人類学とブランド", "lens1": "写真人類学", "lens2": "パース記号学", "status": "planned"},
    {"ep": "EP052", "part": "III", "title": "インフルエンサーは現代の祭司", "lens1": "宗教社会学", "lens2": "ウェーバー", "status": "planned"},
    {"ep": "EP053", "part": "III", "title": "レビュー文化と告解", "lens1": "フーコー", "lens2": "ゴッフマン", "status": "planned"},
    {"ep": "EP054", "part": "III", "title": "ノスタルジアの記憶研究", "lens1": "自伝的記憶", "lens2": "プルースト的記憶論", "status": "planned"},
    {"ep": "EP055", "part": "III", "title": "ロゴと紋章学", "lens1": "中世史", "lens2": "パース記号学", "status": "planned"},
    {"ep": "EP056", "part": "III", "title": "キャンペーンは儀礼である", "lens1": "文化人類学", "lens2": "演劇論", "status": "planned"},
    {"ep": "EP057", "part": "III", "title": "別れの作法", "lens1": "文化人類学", "lens2": "心理学", "status": "planned"},
    {"ep": "EP058", "part": "III", "title": "ブランド再生と神話の更新", "lens1": "神話論", "lens2": "文学理論", "status": "planned"},
    {"ep": "EP059", "part": "III", "title": "集合無意識とマーケティング", "lens1": "ユング", "lens2": "認知科学", "status": "planned"},

    # PART IV 事業開発
    {"ep": "EP060", "part": "IV", "title": "ピボットと進化生物学", "lens1": "進化生物学", "lens2": "中国兵法", "status": "planned"},
    {"ep": "EP061", "part": "IV", "title": "共創とコモンズ", "lens1": "政治哲学", "lens2": "進化人類学", "status": "planned"},
    {"ep": "EP062", "part": "IV", "title": "起業家精神と冒険の構造", "lens1": "神話学", "lens2": "心理学", "status": "planned"},
    {"ep": "EP063", "part": "IV", "title": "アクセラレーターと孵化", "lens1": "発生学", "lens2": "文化人類学", "status": "planned"},
    {"ep": "EP064", "part": "IV", "title": "オープンイノベーションと菌糸体", "lens1": "菌類学", "lens2": "ネットワーク科学", "status": "planned"},
    {"ep": "EP065", "part": "IV", "title": "M&Aの結婚人類学", "lens1": "婚姻儀礼研究", "lens2": "心理学", "status": "planned"},
    {"ep": "EP066", "part": "IV", "title": "提携と外交史", "lens1": "国際関係史", "lens2": "ゲーム理論", "status": "planned"},
    {"ep": "EP067", "part": "IV", "title": "撤退の生態学", "lens1": "個体数調整", "lens2": "軍事戦略", "status": "planned"},
    {"ep": "EP068", "part": "IV", "title": "新規事業と母体", "lens1": "発生生物学", "lens2": "経営学", "status": "planned"},
    {"ep": "EP069", "part": "IV", "title": "試行錯誤の前史", "lens1": "19世紀科学史", "lens2": "プラグマティズム", "status": "planned"},
    {"ep": "EP070", "part": "IV", "title": "プロトタイプは演劇である", "lens1": "スタニスラフスキー", "lens2": "認知科学", "status": "planned"},
    {"ep": "EP071", "part": "IV", "title": "シーズと農学", "lens1": "育種学", "lens2": "民俗学", "status": "planned"},
    {"ep": "EP072", "part": "IV", "title": "仮説検証の科学哲学", "lens1": "ポパー", "lens2": "ベイズ統計", "status": "planned"},
    {"ep": "EP073", "part": "IV", "title": "顧客発見はフィールドワーク", "lens1": "文化人類学", "lens2": "現象学", "status": "planned"},
    {"ep": "EP074", "part": "IV", "title": "ユニットエコノミクスと血流", "lens1": "循環器学", "lens2": "生態学", "status": "planned"},
    {"ep": "EP075", "part": "IV", "title": "アライアンスと縄張り", "lens1": "動物行動学", "lens2": "経済学", "status": "planned"},
    {"ep": "EP076", "part": "IV", "title": "ステージゲートと通過儀礼", "lens1": "文化人類学", "lens2": "発達心理学", "status": "planned"},
    {"ep": "EP077", "part": "IV", "title": "事業の終末期医療", "lens1": "死生学", "lens2": "医療人類学", "status": "planned"},

    # PART V 営業・販売
    {"ep": "EP078", "part": "V", "title": "提案は弁論術である", "lens1": "アリストテレス修辞学", "lens2": "認知心理学", "status": "planned"},
    {"ep": "EP079", "part": "V", "title": "クロージングの民俗学", "lens1": "民俗学", "lens2": "ゲーム理論", "status": "planned"},
    {"ep": "EP080", "part": "V", "title": "反論処理の弁証法", "lens1": "古代ギリシア哲学", "lens2": "認知言語学", "status": "planned"},
    {"ep": "EP081", "part": "V", "title": "質問の技法と精神分析", "lens1": "ラカン", "lens2": "教育心理学", "status": "planned"},
    {"ep": "EP082", "part": "V", "title": "信頼の長距離交易", "lens1": "経済人類学", "lens2": "進化生物学", "status": "planned"},
    {"ep": "EP083", "part": "V", "title": "紹介と互酬性", "lens1": "マリノフスキ", "lens2": "ネットワーク分析", "status": "planned"},
    {"ep": "EP084", "part": "V", "title": "オムニチャネルと多声性", "lens1": "バフチン", "lens2": "認知科学", "status": "planned"},
    {"ep": "EP085", "part": "V", "title": "営業同行と徒弟制度", "lens1": "中世ギルド史", "lens2": "状況的学習論", "status": "planned"},
    {"ep": "EP086", "part": "V", "title": "テリトリーと縄張り", "lens1": "エソロジー", "lens2": "都市計画", "status": "planned"},
    {"ep": "EP087", "part": "V", "title": "ロールプレイと演劇技法", "lens1": "スタニスラフスキー", "lens2": "ゴッフマン", "status": "planned"},
    {"ep": "EP088", "part": "V", "title": "CRMと社会的記憶", "lens1": "アルブヴァクス", "lens2": "神経科学", "status": "planned"},
    {"ep": "EP089", "part": "V", "title": "ノルマ文化と贖罪儀礼", "lens1": "宗教学", "lens2": "心理学", "status": "planned"},
    {"ep": "EP090", "part": "V", "title": "値引きは贈与の変形", "lens1": "モース贈与論", "lens2": "行動経済学", "status": "planned"},
    {"ep": "EP091", "part": "V", "title": "接待と饗応の人類学", "lens1": "ホスピタリティ研究", "lens2": "比較宗教学", "status": "planned"},
    {"ep": "EP092", "part": "V", "title": "オンラインセールスの身体性", "lens1": "現象学", "lens2": "認知科学", "status": "planned"},
    {"ep": "EP093", "part": "V", "title": "名刺と象徴交換", "lens1": "シンボル人類学", "lens2": "中世紋章学", "status": "planned"},
    {"ep": "EP094", "part": "V", "title": "営業会議は告白室", "lens1": "フーコー権力論", "lens2": "演劇論ブレヒト", "status": "planned"},
    {"ep": "EP095", "part": "V", "title": "退職と引き継ぎの儀礼", "lens1": "通過儀礼", "lens2": "経営学", "status": "planned"},

    # 終章
    {"ep": "EP096", "part": "FINAL", "title": "機能横断のパターン", "lens1": "統合論", "lens2": "システム思考", "status": "planned"},
    {"ep": "EP097", "part": "FINAL", "title": "経営者は他分野の翻訳者である", "lens1": "翻訳論", "lens2": "SECIモデル", "status": "planned"},
    {"ep": "EP098", "part": "FINAL", "title": "機能の死と新たな機能の誕生", "lens1": "機能進化論", "lens2": "技術史", "status": "planned"},
    {"ep": "EP099", "part": "FINAL", "title": "AI時代の機能再考", "lens1": "AI×経営", "lens2": "ハイデガー哲学", "status": "planned"},
    {"ep": "EP100", "part": "FINAL", "title": "あなた自身の機能論を書く", "lens1": "メタ", "lens2": "省察的実践家論", "status": "planned"},
]


def stats():
    """Roadmap statistics."""
    by_part = {}
    by_status = {}
    for ep in ROADMAP:
        by_part[ep["part"]] = by_part.get(ep["part"], 0) + 1
        by_status[ep["status"]] = by_status.get(ep["status"], 0) + 1
    return {"total": len(ROADMAP), "by_part": by_part, "by_status": by_status}


if __name__ == "__main__":
    s = stats()
    print(f"Total: {s['total']}")
    print(f"By part: {s['by_part']}")
    print(f"By status: {s['by_status']}")
