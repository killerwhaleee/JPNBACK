import MeCab
import CaboCha

# 初始化 MeCab 和 CaboCha
mecab = MeCab.Tagger("-d /opt/homebrew/lib/mecab/dic/ipadic")  # 解析出词性
cabocha = CaboCha.Parser()


def get_grammar_details(grammar_id: int):
    """查询语法详情"""
    # 假数据，后续可替换为数据库查询
    grammar_data = {
        1: {
            "grammar": "～ばいい",
            "meaning": "表示建议",
            "example": "もっと勉強すればいいよ。",
        },
        2: {
            "grammar": "～てもいい",
            "meaning": "表示许可",
            "example": "ここで写真を撮ってもいいですか？",     
        },
    }
    return grammar_data.get(grammar_id, {"error": "Grammar not found"})


# def analyze_sentence(sentence):
#     # """用 MeCab 分词"""
#     mecab_result = mecab.parse(sentence)
#     print("\n[Mecab 分词结果]:\n", mecab_result)

#     # """ 用 CaboCha 解析句法结构 """
#     tree = cabocha.parse(sentence)
#     parsed_tree = tree.toString(CaboCha.FORMAT_TREE)  # 确保是字符串
#     print("\n[CaboCha 句法结构]:\n", parsed_tree)

#     return {
#         "mecab": mecab_result,
#         "cabocha": parsed_tree,
#     }


# 格式化输出
def format_mecab_output(_result):
    print("result233", _result)
    result = []
    for line in _result.strip().split("\n"):
        if line == "EOS":
            continue  # 跳过 EOS 行
            
        parts = line.split("\t")
        word = parts[0]
        features = parts[1].split(",")

        entry = {
            "word": word,
            "pos": features[0],  # 词性
            "pos_detail_1": features[1] if len(features) > 1 else "",
            "pos_detail_2": features[2] if len(features) > 2 else "",
            "base_form": features[6] if len(features) > 6 else word,  # 原型
            "reading": features[7] if len(features) > 7 else ""
        }
        result.append(entry)

    return result


def format_cabocha_output(cabocha_result):
    return cabocha_result.strip().split("\n")


def analyze_sentence(sentence):
    print("sentence", sentence)
    mecab_result = mecab.parse(sentence)
    print("mecab_result", mecab_result)
    cabocha_result = cabocha.parse(sentence).toString(CaboCha.FORMAT_TREE)
    print("cabocha_result", cabocha_result)

    return {
        "mecab": format_mecab_output(mecab_result),
        "cabocha": format_cabocha_output(cabocha_result),
    }
