from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        "{{first_name}} {{last_name}}",
        "{{first_name}} {{last_name}}",
        "{{last_name}}, {{first_name}}",
    )

    # First 20 names from here
    # https://www.babycenter.in/l25020672/top-20-indian-boys-names-of-2016-photos
    # Next 20 names from here
    # https://www.babycenter.in/l25020674/top-20-indian-girls-names-of-2016-photos
    first_names = (
        "मुहम्मद",
        "आरव",
        "अर्जुन",
        "रायन",
        "आद्विक",
        "अथर्व",
        "रेयांश",
        "अयान",
        "विहान",
        "साई",
        "अद्वैत",
        "शौर्य",
        "विआन",
        "आरुष",
        "इशान",
        "अयांश",
        "पार्थ",
        "देन्यल",
        "किआन",
        "विवान",
        "आद्या",
        "अनन्या",
        "शनाया",
        "फ़ातिमा",
        "श्री",
        "अनाया",
        "अनिका",
        "मायरा",
        "इनाया",
        "अमायरा",
        "आन्वी",
        "स्वरा",
        "ज़ारा",
        "मरियम",
        "आराध्या",
        "तन्वी",
        "दीया",
        "अद्विका",
        "ईवा",
        "आव्या",
        "अभय",
        "आदित्य",
        "अजित",
        "अखिल",
        "अमर",
        "आनन्द",
        "अंकुर",
        "अनुपम",
        "अशोक",
        "चन्दना",
        "गणेश",
        "गौतम",
        "गोविंदा",
        "हनुमान्",
        "इन्द्रजित",
        "ईश",
        "जगन्नाथ",
        "जगदीश",
        "जयदेव",
        "जितेन्द्र",
        "कैलाश",
        "कालिदास",
        "कम्बोज",
        "किरण",
        "ललित",
        "मानदीप",
        "मोहन",
        "मुकेश",
        "नरेन्द्र",
        "नारायण",
        "निखिल",
        "प्रभाकर",
        "प्रबोध",
        "प्रदीप",
        "प्रणव",
        "प्रेम",
        "राजीव",
        "रतन",
        "रोहन",
        "विष्णु",
        "विक्रम",
        "विजया",
        "विजय",
        "विवेक",
        "यश",
        "अभिलाषा",
        "अदिती",
        "ऐश्वर्या",
        "अमिता",
        "अंकिता",
        "आशा",
        "अवनी",
        "भरत",
        "चेतना",
        "दिव्या",
        "एषा",
        "इन्दु",
        "जया",
        "जयन्ती",
        "ज्योत्सना",
        "कान्ती",
        "कुमारी",
        "लता",
        "लीला",
        "मालती",
        "मोहिनी",
        "निशा",
        "पूर्णिमा",
        "पुष्पा",
        "रचना",
        "रजनी",
        "रश्मी",
        "रिया",
        "सरला",
        "सरस्वती",
        "सावित्री",
        "शक्ति",
        "शान्ता",
        "शर्मिला",
        "श्यामा",
        "सुलभा",
        "तृष्णा",
        "विद्या",
        "अली",
        "हासन",
        "हुसैन",
        "ज़ाकिर",
        "रिज़वान",
        "फ़रहान",
        "ज़ोया",
    )

    last_names = (
        "पाटिल",
        "शर्मा",
        "आचार्य",
        "अग्रवाल",
        "सिंह",
        "अहलुवालिया",
        "आहूजा",
        "पुष्कर",
        "शिरोळे",
        "गायकवाड",
        "गावित",
        "शिरोळे",
        "बापट",
        "अरोड़ा",
        "बाबू",
        "बादामी",
        "जमानत",
        "बजाज",
        "बक्षी",
        "बालकृष्णन",
        "बालासुब्रमणियम",
        "बसु",
        "भंडारी",
        "चौधरी",
        "चौहान",
        "छाबरा",
        "दादा",
        "डानी",
        "डार",
        "दारा",
        "दत्ता",
        "दवे",
        "दयाल",
        "धालीवाल",
        "दीक्षित",
        "दोषी",
        "दुआ",
        "दूबे",
        "ढींगरा",
        "वाल",
        "साया",
        "बना",
        "ड़ाल",
        "गर्ग",
        "गणेश",
        "गांगुली",
        "गुप्ता",
        "हेगडे",
        "जोशी",
        "काले",
        "कृष्णा",
        "कृष्णमूर्ति",
        "कृष्णन",
        "कुलकर्णी",
        "कुमार",
        "कुण्डा",
        "नाम",
        "रामलला",
        "लता",
        "लोदी",
        "लोकनाट्यों",
        "विकावि",
        "लाल",
        "लाला",
        "वफादार",
        "लूथरा",
        "मदन",
        "मगर",
        "भारत",
        "महावीर",
        "महादेव",
        "महाजन",
        "महाराज",
        "मजूमदार",
        "मल्लिक",
        "सेनाधीश",
        "माने",
        "मंगल",
        "मंगत",
        "रामशर्मा",
        "मणि",
        "मान",
        "श्रीविमल",
        "कुमार",
        "मंडल",
        "अली",
        "हासन",
        "हुसैन",
        "खान",
        "अब्बासी",
        "नूरानी",
    )
