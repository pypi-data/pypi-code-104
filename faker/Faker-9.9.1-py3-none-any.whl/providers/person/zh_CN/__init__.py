from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ["{{last_name}}{{first_name}}"]

    first_names_male = [
        "伟",
        "强",
        "磊",
        "洋",
        "勇",
        "军",
        "杰",
        "涛",
        "超",
        "明",
        "刚",
        "平",
        "辉",
        "鹏",
        "华",
        "飞",
        "鑫",
        "波",
        "斌",
        "宇",
        "浩",
        "凯",
        "健",
        "俊",
        "帆",
        "帅",
        "旭",
        "宁",
        "龙",
        "林",
        "欢",
        "佳",
        "阳",
        "建华",
        "亮",
        "成",
        "建",
        "峰",
        "建国",
        "建军",
        "晨",
        "瑞",
        "志强",
        "兵",
        "雷",
        "东",
        "博",
        "彬",
        "坤",
        "想",
        "岩",
        "杨",
        "文",
        "利",
        "楠",
        "红霞",
        "建平",
    ]

    first_names_female = [
        "芳",
        "娜",
        "敏",
        "静",
        "秀英",
        "丽",
        "艳",
        "娟",
        "霞",
        "秀兰",
        "燕",
        "玲",
        "桂英",
        "丹",
        "萍",
        "红",
        "玉兰",
        "桂兰",
        "英",
        "梅",
        "莉",
        "秀珍",
        "婷",
        "玉梅",
        "玉珍",
        "凤英",
        "晶",
        "玉英",
        "颖",
        "雪",
        "慧",
        "红梅",
        "倩",
        "琴",
        "兰英",
        "畅",
        "云",
        "洁",
        "柳",
        "淑珍",
        "春梅",
        "海燕",
        "冬梅",
        "秀荣",
        "桂珍",
        "莹",
        "秀云",
        "桂荣",
        "秀梅",
        "丽娟",
        "婷婷",
        "玉华",
        "琳",
        "雪梅",
        "淑兰",
        "丽丽",
        "玉",
        "秀芳",
        "欣",
        "淑英",
        "桂芳",
        "丽华",
        "丹丹",
        "桂香",
        "淑华",
        "荣",
        "秀华",
        "桂芝",
        "小红",
        "金凤",
        "瑜",
        "桂花",
        "璐",
        "凤兰",
    ]

    first_names = first_names_male + first_names_female

    # From https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E5%A7%93%E6%B0%8F%E6%8E%92%E5%90%8D
    last_names = OrderedDict(
        (
            ("王", 7.170),
            ("李", 7.000),
            ("张", 6.740),
            ("刘", 5.100),
            ("陈", 4.610),
            ("杨", 3.220),
            ("黄", 2.450),
            ("吴", 2.000),
            ("赵", 2.000),
            ("周", 1.900),
            ("徐", 1.450),
            ("孙", 1.380),
            ("马", 1.290),
            ("朱", 1.280),
            ("胡", 1.160),
            ("林", 1.130),
            ("郭", 1.130),
            ("何", 1.060),
            ("高", 1.000),
            ("罗", 0.950),
            ("郑", 0.930),
            ("梁", 0.850),
            ("谢", 0.760),
            ("宋", 0.700),
            ("唐", 0.690),
            ("许", 0.660),
            ("邓", 0.620),
            ("冯", 0.620),
            ("韩", 0.610),
            ("曹", 0.600),
            ("曾", 0.580),
            ("彭", 0.580),
            ("萧", 0.560),
            ("蔡", 0.530),
            ("潘", 0.520),
            ("田", 0.520),
            ("董", 0.510),
            ("袁", 0.500),
            ("于", 0.480),
            ("余", 0.480),
            ("叶", 0.480),
            ("蒋", 0.480),
            ("杜", 0.470),
            ("苏", 0.460),
            ("魏", 0.450),
            ("程", 0.450),
            ("吕", 0.450),
            ("丁", 0.430),
            ("沈", 0.410),
            ("任", 0.410),
            ("姚", 0.400),
            ("卢", 0.400),
            ("傅", 0.400),
            ("钟", 0.400),
            ("姜", 0.390),
            ("崔", 0.380),
            ("谭", 0.380),
            ("廖", 0.370),
            ("范", 0.360),
            ("汪", 0.360),
            ("陆", 0.360),
            ("金", 0.350),
            ("石", 0.340),
            ("戴", 0.340),
            ("贾", 0.330),
            ("韦", 0.320),
            ("夏", 0.320),
            ("邱", 0.320),
            ("方", 0.310),
            ("侯", 0.300),
            ("邹", 0.300),
            ("熊", 0.290),
            ("孟", 0.290),
            ("秦", 0.290),
            ("白", 0.280),
            ("江", 0.280),
            ("阎", 0.270),
            ("薛", 0.260),
            ("尹", 0.260),
            ("段", 0.240),
            ("雷", 0.240),
            ("黎", 0.220),
            ("史", 0.210),
            ("龙", 0.210),
            ("陶", 0.210),
            ("贺", 0.210),
            ("顾", 0.200),
            ("毛", 0.200),
            ("郝", 0.200),
            ("龚", 0.200),
            ("邵", 0.200),
            ("万", 0.190),
            ("钱", 0.190),
            ("严", 0.190),
            ("赖", 0.180),
            ("覃", 0.180),
            ("洪", 0.180),
            ("武", 0.180),
            ("莫", 0.180),
            ("孔", 0.170),
            ("汤", 0.170),
            ("向", 0.170),
            ("常", 0.160),
            ("温", 0.160),
            ("康", 0.160),
            ("施", 0.150),
            ("文", 0.150),
            ("牛", 0.150),
            ("樊", 0.150),
            ("葛", 0.150),
            ("邢", 0.140),
            ("安", 0.130),
            ("齐", 0.130),
            ("易", 0.130),
            ("乔", 0.130),
            ("伍", 0.130),
            ("庞", 0.130),
            ("颜", 0.120),
            ("倪", 0.120),
            ("庄", 0.120),
            ("聂", 0.120),
            ("章", 0.120),
            ("鲁", 0.110),
            ("岳", 0.110),
            ("翟", 0.110),
            ("殷", 0.110),
            ("詹", 0.110),
            ("申", 0.110),
            ("欧", 0.110),
            ("耿", 0.110),
            ("关", 0.100),
            ("兰", 0.100),
            ("焦", 0.100),
            ("俞", 0.100),
            ("左", 0.100),
            ("柳", 0.100),
            ("甘", 0.095),
            ("祝", 0.090),
            ("包", 0.087),
            ("宁", 0.083),
            ("尚", 0.082),
            ("符", 0.082),
            ("舒", 0.082),
            ("阮", 0.082),
            ("柯", 0.080),
            ("纪", 0.080),
            ("梅", 0.079),
            ("童", 0.079),
            ("凌", 0.078),
            ("毕", 0.078),
            ("单", 0.076),
            ("季", 0.076),
            ("裴", 0.076),
            ("霍", 0.075),
            ("涂", 0.075),
            ("成", 0.075),
            ("苗", 0.075),
            ("谷", 0.075),
            ("盛", 0.074),
            ("曲", 0.074),
            ("翁", 0.073),
            ("冉", 0.073),
            ("骆", 0.073),
            ("蓝", 0.072),
            ("路", 0.072),
            ("游", 0.071),
            ("辛", 0.070),
            ("靳", 0.069),
            ("欧阳", 0.068),
            ("管", 0.065),
            ("柴", 0.065),
            ("蒙", 0.062),
            ("鲍", 0.062),
            ("华", 0.061),
            ("喻", 0.061),
            ("祁", 0.061),
            ("蒲", 0.056),
            ("房", 0.056),
            ("滕", 0.055),
            ("屈", 0.055),
            ("饶", 0.055),
            ("解", 0.053),
            ("牟", 0.053),
            ("艾", 0.052),
            ("尤", 0.052),
            ("阳", 0.050),
            ("时", 0.050),
            ("穆", 0.048),
            ("农", 0.047),
            ("司", 0.044),
            ("卓", 0.043),
            ("古", 0.043),
            ("吉", 0.043),
            ("缪", 0.043),
            ("简", 0.043),
            ("车", 0.043),
            ("项", 0.043),
            ("连", 0.043),
            ("芦", 0.042),
            ("麦", 0.041),
            ("褚", 0.041),
            ("娄", 0.040),
            ("窦", 0.040),
            ("戚", 0.040),
            ("岑", 0.039),
            ("景", 0.039),
            ("党", 0.039),
            ("宫", 0.039),
            ("费", 0.039),
            ("卜", 0.038),
            ("冷", 0.038),
            ("晏", 0.038),
            ("席", 0.036),
            ("卫", 0.036),
            ("米", 0.035),
            ("柏", 0.035),
            ("宗", 0.034),
            ("瞿", 0.033),
            ("桂", 0.033),
            ("全", 0.033),
            ("佟", 0.033),
            ("应", 0.033),
            ("臧", 0.032),
            ("闵", 0.032),
            ("苟", 0.032),
            ("邬", 0.032),
            ("边", 0.032),
            ("卞", 0.032),
            ("姬", 0.032),
            ("师", 0.031),
            ("和", 0.031),
            ("仇", 0.030),
            ("栾", 0.030),
            ("隋", 0.030),
            ("商", 0.030),
            ("刁", 0.030),
            ("沙", 0.030),
            ("荣", 0.029),
            ("巫", 0.029),
            ("寇", 0.029),
            ("桑", 0.028),
            ("郎", 0.028),
            ("甄", 0.027),
            ("丛", 0.027),
            ("仲", 0.027),
            ("虞", 0.026),
            ("敖", 0.026),
            ("巩", 0.026),
            ("明", 0.026),
            ("佘", 0.025),
            ("池", 0.025),
            ("查", 0.025),
            ("麻", 0.025),
            ("苑", 0.025),
            ("迟", 0.024),
            ("邝", 0.024),
            ("官", 0.023),
            ("封", 0.023),
            ("谈", 0.023),
            ("匡", 0.023),
            ("鞠", 0.230),
            ("惠", 0.022),
            ("荆", 0.022),
            ("乐", 0.022),
            ("冀", 0.021),
            ("郁", 0.021),
            ("胥", 0.021),
            ("南", 0.021),
            ("班", 0.021),
            ("储", 0.021),
            ("原", 0.020),
            ("栗", 0.020),
            ("燕", 0.020),
            ("楚", 0.020),
            ("鄢", 0.020),
            ("劳", 0.019),
            ("谌", 0.019),
            ("奚", 0.017),
            ("皮", 0.017),
            ("粟", 0.017),
            ("冼", 0.017),
            ("蔺", 0.017),
            ("楼", 0.017),
            ("盘", 0.017),
            ("满", 0.016),
            ("闻", 0.016),
            ("位", 0.016),
            ("厉", 0.016),
            ("伊", 0.016),
            ("仝", 0.015),
            ("区", 0.015),
            ("郜", 0.015),
            ("海", 0.015),
            ("阚", 0.015),
            ("花", 0.015),
            ("权", 0.014),
            ("强", 0.014),
            ("帅", 0.014),
            ("屠", 0.014),
            ("豆", 0.014),
            ("朴", 0.014),
            ("盖", 0.014),
            ("练", 0.014),
            ("廉", 0.014),
            ("禹", 0.014),
            ("井", 0.013),
            ("祖", 0.013),
            ("漆", 0.013),
            ("巴", 0.013),
            ("丰", 0.013),
            ("支", 0.013),
            ("卿", 0.013),
            ("国", 0.013),
            ("狄", 0.013),
            ("平", 0.013),
            ("计", 0.012),
            ("索", 0.012),
            ("宣", 0.012),
            ("晋", 0.012),
            ("相", 0.012),
            ("初", 0.012),
            ("门", 0.012),
            ("云", 0.012),
            ("容", 0.012),
            ("敬", 0.011),
            ("来", 0.011),
            ("扈", 0.011),
            ("晁", 0.011),
            ("芮", 0.011),
            ("都", 0.011),
            ("普", 0.011),
            ("阙", 0.011),
            ("浦", 0.011),
            ("戈", 0.011),
            ("伏", 0.011),
            ("鹿", 0.011),
            ("薄", 0.011),
            ("邸", 0.011),
            ("雍", 0.010),
            ("辜", 0.010),
            ("羊", 0.010),
            ("阿", 0.010),
            ("乌", 0.010),
            ("母", 0.010),
            ("裘", 0.010),
            ("亓", 0.010),
            ("修", 0.010),
            ("邰", 0.010),
            ("赫", 0.010),
            ("杭", 0.010),
            ("况", 0.0094),
            ("那", 0.0093),
            ("宿", 0.0093),
            ("鲜", 0.0092),
            ("印", 0.0091),
            ("逯", 0.0091),
            ("隆", 0.0090),
            ("茹", 0.0090),
            ("诸", 0.0089),
            ("战", 0.0088),
            ("慕", 0.0086),
            ("危", 0.0084),
            ("玉", 0.0084),
            ("银", 0.0084),
            ("亢", 0.0083),
            ("嵇", 0.0082),
            ("公", 0.0082),
            ("哈", 0.0081),
            ("湛", 0.0079),
            ("宾", 0.0077),
            ("戎", 0.0076),
            ("勾", 0.0076),
            ("茅", 0.0076),
            ("利", 0.0076),
            ("于", 0.0074),
            ("呼", 0.0074),
            ("居", 0.0074),
            ("揭", 0.0073),
            ("干", 0.0072),
            ("但", 0.0072),
            ("尉", 0.0071),
            ("冶", 0.0071),
            ("斯", 0.0070),
            ("元", 0.0069),
            ("束", 0.0068),
            ("檀", 0.0068),
            ("衣", 0.0067),
            ("信", 0.0067),
            ("展", 0.0067),
            ("阴", 0.0067),
            ("昝", 0.0066),
            ("智", 0.0065),
            ("幸", 0.0065),
            ("奉", 0.0064),
            ("植", 0.0064),
            ("衡", 0.0063),
            ("富", 0.0063),
            ("尧", 0.0060),
            ("闭", 0.0060),
            ("由", 0.0060),
        )
    )

    romanized_formats = ("{{first_romanized_name}} {{last_romanized_name}}",)

    # From https://en.wikipedia.org/wiki/Chinese_given_name#Common_Chinese_names,
    # with accents stripped
    first_romanized_names = (
        "Chao",
        "Fang",
        "Gang",
        "Guiying",
        "Jie",
        "Jing",
        "Juan",
        "Jun",
        "Lei",
        "Li",
        "Min",
        "Ming",
        "Na",
        "Ping",
        "Qiang",
        "Tao",
        "Wei",
        "Xia",
        "Xiulan",
        "Xiuying",
        "Yang",
        "Yong",
        "Yan",
    )

    # From https://en.wikipedia.org/wiki/List_of_common_Chinese_surnames
    # with accents stripped
    last_romanized_names = (
        "Bai",
        "Cai",
        "Cao",
        "Chang",
        "Chen",
        "Cheng",
        "Cui",
        "Dai",
        "Deng",
        "Ding",
        "Dong",
        "Du",
        "Duan",
        "Fan",
        "Fang",
        "Feng",
        "Fu",
        "Gao",
        "Gong",
        "Gu",
        "Guo",
        "Han",
        "Hao",
        "He",
        "Hou",
        "Hu",
        "Huang",
        "Jia",
        "Jiang",
        "Jin",
        "Kang",
        "Kong",
        "Lai",
        "Lei",
        "Li",
        "Liang",
        "Liao",
        "Lin",
        "Liu",
        "Long",
        "Lu",
        "Luo",
        "Ma",
        "Mao",
        "Meng",
        "Mo",
        "Pan",
        "Peng",
        "Qian",
        "Qiao",
        "Qin",
        "Qiu",
        "Ren",
        "Shao",
        "Shen",
        "Shi",
        "Song",
        "Su",
        "Sun",
        "Tan",
        "Tang",
        "Tao",
        "Tian",
        "Wan",
        "Wang",
        "Wei",
        "Wen",
        "Wu",
        "Xia",
        "Xiang",
        "Xiao",
        "Xie",
        "Xiong",
        "Xu",
        "Xue",
        "Yan",
        "Yang",
        "Yao",
        "Ye",
        "Yi",
        "Yin",
        "Yu",
        "Yuan",
        "Zeng",
        "Zhang",
        "Zhao",
        "Zheng",
        "Zhong",
        "Zhou",
        "Zhu",
        "Zou",
    )

    def romanized_name(self) -> str:
        """
        @example 'Chao Bai'
        """
        pattern: str = self.random_element(self.romanized_formats)
        return self.generator.parse(pattern)

    def first_romanized_name(self) -> str:
        """
        @example 'Chao'
        """
        return self.random_element(self.first_romanized_names)

    def last_romanized_name(self) -> str:
        """
        @example 'Chao'
        """
        return self.random_element(self.last_romanized_names)
