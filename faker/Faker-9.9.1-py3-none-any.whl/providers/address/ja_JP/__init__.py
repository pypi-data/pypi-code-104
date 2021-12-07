from .. import Provider as AddressProvider


class Provider(AddressProvider):
    address_formats = (
        "{{prefecture}}{{city}}{{town}}{{chome}}{{ban}}{{gou}}",
        "{{prefecture}}{{city}}{{town}}{{chome}}{{ban}}{{gou}} {{town}}{{building_name}}{{building_number}}",
        "{{prefecture}}{{city}}{{town}}{{chome}}{{ban}}{{gou}} {{building_name}}{{town}}{{building_number}}",
    )

    building_number_formats = ("###",)

    countries = (
        "アフガニスタン",
        "アルバニア",
        "アルジェリア",
        "アメリカ領サモア",
        "アンドラ",
        "アンゴラ",
        "アンギラ",
        "南極大陸",
        "アンティグアバーブーダ",
        "アルゼンチン",
        "アルメニア",
        "アルバ",
        "オーストラリア",
        "オーストリア",
        "アゼルバイジャン",
        "バハマ",
        "バーレーン",
        "バングラデシュ",
        "バルバドス",
        "ベラルーシ",
        "ベルギー",
        "ベリーズ",
        "ベナン",
        "バミューダ島",
        "ブータン",
        "ボリビア",
        "ボスニア・ヘルツェゴビナ",
        "ボツワナ",
        "ブーベ島",
        "ブラジル",
        "イギリス領インド洋地域",
        "イギリス領ヴァージン諸島",
        "ブルネイ",
        "ブルガリア",
        "ブルキナファソ",
        "ブルンジ",
        "カンボジア",
        "カメルーン",
        "カナダ",
        "カーボベルデ",
        "ケイマン諸島",
        "中央アフリカ共和国",
        "チャド",
        "チリ",
        "中国",
        "クリスマス島",
        "ココス諸島",
        "コロンビア",
        "コモロ",
        "コンゴ共和国",
        "クック諸島",
        "コスタリカ",
        "コートジボワール",
        "クロアチア",
        "キューバ",
        "キプロス共和国",
        "チェコ共和国",
        "デンマーク",
        "ジブチ共和国",
        "ドミニカ国",
        "ドミニカ共和国",
        "エクアドル",
        "エジプト",
        "エルサルバドル",
        "赤道ギニア共和国",
        "エリトリア",
        "エストニア",
        "エチオピア",
        "フェロー諸島",
        "フォークランド諸島",
        "フィジー共和国",
        "フィンランド",
        "フランス",
        "フランス領ギアナ",
        "フランス領ポリネシア",
        "フランス領極南諸島",
        "ガボン",
        "ガンビア",
        "グルジア",
        "ドイツ",
        "ガーナ",
        "ジブラルタル",
        "ギリシャ",
        "グリーンランド",
        "グレナダ",
        "グアドループ",
        "グアム",
        "グアテマラ",
        "ガーンジー",
        "ギニア",
        "ギニアビサウ",
        "ガイアナ",
        "ハイチ",
        "ハード島とマクドナルド諸島",
        "バチカン市国",
        "ホンジュラス",
        "香港",
        "ハンガリー",
        "アイスランド",
        "インド",
        "インドネシア",
        "イラン",
        "イラク",
        "アイルランド共和国",
        "マン島",
        "イスラエル",
        "イタリア",
        "ジャマイカ",
        "日本",
        "ジャージー島",
        "ヨルダン",
        "カザフスタン",
        "ケニア",
        "キリバス",
        "朝鮮",
        "韓国",
        "クウェート",
        "キルギス共和国",
        "ラオス人民民主共和国",
        "ラトビア",
        "レバノン",
        "レソト",
        "リベリア",
        "リビア国",
        "リヒテンシュタイン",
        "リトアニア",
        "ルクセンブルク",
        "マカオ",
        "マケドニア共和国",
        "マダガスカル",
        "マラウィ",
        "マレーシア",
        "モルディブ",
        "マリ",
        "マルタ共和国",
        "マーシャル諸島",
        "マルティニーク",
        "モーリタニア・イスラム共和国",
        "モーリシャス",
        "マヨット",
        "メキシコ",
        "ミクロネシア連邦",
        "モルドバ共和国",
        "モナコ公国",
        "モンゴル",
        "モンテネグロ共和国",
        "モントセラト",
        "モロッコ",
        "モザンビーク",
        "ミャンマー",
        "ナミビア",
        "ナウル",
        "ネパール",
        "オランダ領アンティル",
        "オランダ",
        "ニューカレドニア",
        "ニュージーランド",
        "ニカラグア",
        "ニジェール",
        "ナイジェリア",
        "ニース",
        "ノーフォーク島",
        "北マリアナ諸島",
        "ノルウェー",
        "オマーン",
        "パキスタン",
        "パラオ",
        "パレスチナ自治区",
        "パナマ",
        "パプアニューギニア",
        "パラグアイ",
        "ペルー",
        "フィリピン",
        "ピトケアン諸島",
        "ポーランド",
        "ポルトガル",
        "プエルトリコ",
        "カタール",
        "レユニオン",
        "ルーマニア",
        "ロシア",
        "ルワンダ",
        "サン・バルテルミー島",
        "セントヘレナ",
        "セントクリストファー・ネイビス連邦",
        "セントルシア",
        "セント・マーチン島",
        "サンピエール島・ミクロン島",
        "セントビンセント・グレナディーン",
        "サモア",
        "サンマリノ",
        "サントメプリンシペ",
        "サウジアラビア",
        "セネガル",
        "セルビア",
        "セイシェル",
        "シエラレオネ",
        "シンガポール",
        "スロバキア",
        "スロベニア",
        "ソロモン諸島",
        "ソマリア",
        "南アフリカ共和国",
        "サウスジョージア・サウスサンドウィッチ諸島",
        "スペイン",
        "スリランカ",
        "スーダン",
        "スリナム",
        "スヴァールバル諸島およびヤンマイエン島",
        "スワジランド王国",
        "スウェーデン",
        "スイス",
        "シリア",
        "台湾",
        "タジキスタン共和国",
        "タンザニア",
        "タイ",
        "東ティモール",
        "トーゴ",
        "トケラウ",
        "トンガ",
        "トリニダード・トバゴ",
        "チュニジア",
        "トルコ",
        "トルクメニスタン",
        "タークス・カイコス諸島",
        "ツバル",
        "ウガンダ",
        "ウクライナ",
        "アラブ首長国連邦",
        "イギリス",
        "アメリカ合衆国",
        "合衆国領有小離島",
        "アメリカ領ヴァージン諸島",
        "ウルグアイ",
        "ウズベキスタン",
        "バヌアツ",
        "ベネズエラ",
        "ベトナム",
        "ウォリス・フツナ",
        "西サハラ",
        "イエメン",
        "ザンビア",
        "ジンバブエ",
    )

    prefectures = (
        "北海道",
        "青森県",
        "岩手県",
        "宮城県",
        "秋田県",
        "山形県",
        "福島県",
        "茨城県",
        "栃木県",
        "群馬県",
        "埼玉県",
        "千葉県",
        "東京都",
        "神奈川県",
        "新潟県",
        "富山県",
        "石川県",
        "福井県",
        "山梨県",
        "長野県",
        "岐阜県",
        "静岡県",
        "愛知県",
        "三重県",
        "滋賀県",
        "京都府",
        "大阪府",
        "兵庫県",
        "奈良県",
        "和歌山県",
        "鳥取県",
        "島根県",
        "岡山県",
        "広島県",
        "山口県",
        "徳島県",
        "香川県",
        "愛媛県",
        "高知県",
        "福岡県",
        "佐賀県",
        "長崎県",
        "熊本県",
        "大分県",
        "宮崎県",
        "鹿児島県",
        "沖縄県",
    )

    cities = (
        "八千代市",
        "我孫子市",
        "鴨川市",
        "鎌ケ谷市",
        "君津市",
        "富津市",
        "浦安市",
        "四街道市",
        "袖ケ浦市",
        "八街市",
        "印西市",
        "白井市",
        "富里市",
        "南房総市",
        "匝瑳市",
        "香取市",
        "山武市",
        "いすみ市",
        "大網白里市",
        "印旛郡酒々井町",
        "印旛郡印旛村",
        "印旛郡本埜村",
        "印旛郡栄町",
        "香取郡神崎町",
        "香取郡多古町",
        "香取郡東庄町",
        "山武郡九十九里町",
        "山武郡芝山町",
        "山武郡横芝光町",
        "長生郡一宮町",
        "長生郡睦沢町",
        "長生郡長生村",
        "長生郡白子町",
        "長生郡長柄町",
        "長生郡長南町",
        "夷隅郡大多喜町",
        "夷隅郡御宿町",
        "安房郡鋸南町",
        "千代田区",
        "中央区",
        "港区",
        "新宿区",
        "文京区",
        "台東区",
        "墨田区",
        "江東区",
        "品川区",
        "目黒区",
        "大田区",
        "世田谷区",
        "渋谷区",
        "中野区",
        "杉並区",
        "豊島区",
        "北区",
        "荒川区",
        "板橋区",
        "練馬区",
        "足立区",
        "葛飾区",
        "江戸川区",
        "八王子市",
        "立川市",
        "武蔵野市",
        "三鷹市",
        "青梅市",
        "府中市",
        "昭島市",
        "調布市",
        "町田市",
        "小金井市",
        "小平市",
        "日野市",
        "東村山市",
        "国分寺市",
        "国立市",
        "福生市",
        "狛江市",
        "東大和市",
        "清瀬市",
        "東久留米市",
        "武蔵村山市",
        "多摩市",
        "稲城市",
        "羽村市",
        "あきる野市",
        "西東京市",
        "西多摩郡瑞穂町",
        "西多摩郡日の出町",
        "西多摩郡檜原村",
        "西多摩郡奥多摩町",
        "大島町",
        "利島村",
        "新島村",
        "神津島村",
        "三宅島三宅村",
        "御蔵島村",
        "八丈島八丈町",
        "青ヶ島村",
        "小笠原村",
        "横浜市鶴見区",
        "横浜市神奈川区",
        "横浜市西区",
        "横浜市中区",
        "横浜市南区",
        "横浜市保土ケ谷区",
        "横浜市磯子区",
        "横浜市金沢区",
        "横浜市港北区",
        "横浜市戸塚区",
        "横浜市港南区",
        "横浜市旭区",
        "横浜市緑区",
        "横浜市瀬谷区",
        "横浜市栄区",
        "横浜市泉区",
        "横浜市青葉区",
        "横浜市都筑区",
        "川崎市川崎区",
        "川崎市幸区",
        "川崎市中原区",
        "川崎市高津区",
        "川崎市多摩区",
        "川崎市宮前区",
    )

    towns = (
        "丹勢",
        "中宮祠",
        "手岡",
        "東和町",
        "所野",
        "土沢",
        "独鈷沢",
        "轟",
        "土呂部",
        "中小来川",
        "長畑",
        "中鉢石町",
        "中三依",
        "西小来川",
        "西川",
        "日光",
        "東三島",
        "東大和町",
        "蟇沼",
        "二つ室",
        "方京",
        "細竹",
        "前弥六",
        "前弥六南町",
        "松浦町",
        "南赤田",
        "南郷屋",
        "美原町",
        "無栗屋",
        "睦",
        "百村",
        "箭坪",
        "山中新田",
        "油井",
        "湯宮",
        "豊町",
        "湯本塩原",
        "横林",
        "四区町",
        "渡辺",
        "氏家",
        "氏家新田",
        "卯の里",
        "小入",
        "大中",
        "押上",
        "柿木沢",
        "柿木沢新田",
        "鍛冶ケ沢",
        "上高野",
        "上吉羽",
        "木立",
        "権現堂",
        "幸手",
        "下宇和田",
        "下吉羽",
        "神明内",
        "外国府間",
        "千塚",
        "天神島",
        "戸島",
        "中川崎",
        "長間",
        "西関宿",
        "花島",
        "平須賀",
        "細野",
        "松石",
        "太田ヶ谷",
        "上広谷",
        "五味ヶ谷",
        "脚折",
        "脚折町",
        "鶴ヶ丘",
        "羽折町",
        "藤金",
        "九段南",
        "皇居外苑",
        "麹町",
        "猿楽町",
        "外神田",
        "西神田",
        "隼町",
        "東神田",
        "一ツ橋",
        "日比谷公園",
        "平河町",
        "丸の内",
        "丸の内ＪＰタワー",
        "四番町",
        "六番町",
        "明石町",
        "勝どき",
        "京橋",
        "月島",
        "北青山",
        "港南",
        "芝浦",
        "芝公園",
        "芝大門",
        "白金",
        "白金台",
        "台場",
        "高輪",
        "虎ノ門",
        "虎ノ門虎ノ門ヒルズ森タワー",
        "大京町",
        "高田馬場",
        "箪笥町",
        "津久戸町",
        "筑土八幡町",
        "戸塚町",
        "富久町",
        "戸山",
        "秋葉原",
        "浅草",
        "浅草橋",
        "池之端",
        "今戸",
        "入谷",
        "上野公園",
        "上野桜木",
        "雷門",
        "北上野",
        "蔵前",
        "千束",
        "台東",
        "鳥越",
        "西浅草",
        "日本堤",
        "橋場",
        "花川戸",
        "東浅草",
        "東上野",
        "松が谷",
        "三筋",
        "三ノ輪",
        "元浅草",
        "竜泉",
        "吾妻橋",
    )

    building_names = (
        "パレス",
        "ハイツ",
        "コーポ",
        "アーバン",
        "クレスト",
        "パーク",
        "シティ",
        "シャルム",
        "コート",
    )

    def administrative_unit(self) -> str:
        """
        :example '東京都'
        """
        return self.random_element(self.prefectures)

    prefecture = administrative_unit

    def city(self) -> str:
        """
        :example '台東区'
        """
        return self.random_element(self.cities)

    def town(self) -> str:
        """
        :example '浅草'
        """
        return self.random_element(self.towns)

    def chome(self) -> str:
        """
        :example '1丁目'
        """
        return "%d丁目" % self.generator.random.randint(1, 42)

    def ban(self) -> str:
        """
        :example '3番'
        """
        return "%d番" % self.generator.random.randint(1, 27)

    def gou(self) -> str:
        """
        :example '10号'
        """
        return "%d号" % self.generator.random.randint(1, 20)

    def building_name(self) -> str:
        """
        :example 'コーポ芝浦'
        """
        return self.random_element(self.building_names)

    def postcode(self) -> str:
        """
        :example '101-1212'
        """
        return "%03d-%04d" % (
            self.generator.random.randint(0, 999),
            self.generator.random.randint(0, 9999),
        )

    def zipcode(self) -> str:
        return self.postcode()
