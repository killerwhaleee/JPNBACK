import MeCab
import CaboCha

# 初始化 MeCab 和 CaboCha
mecab = MeCab.Tagger("-Ochasen")  # 解析出词性
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
def format_mecab_output(result):
    lines = result.strip().split("\n")  # 将结果按行分割
    lines = [line for line in lines if line != "EOS"]
    parsed_result = []
    for line in lines:
        parts = line.split("\t")  # 将行按制表符分割
        if len(parts) >= 4:
            parsed_result.append(
                {
                    "word": parts[0],
                    "reading": parts[1],
                    "base_form": parts[2],
                    "pos": parts[3],
                }
            )
            print("parsed_result", parsed_result)
    return parsed_result


def format_cabocha_output(cabocha_result):
    return cabocha_result.strip().split("\n")


def analyze_sentence(sentence):
    mecab_result = mecab.parse(sentence)
    cabocha_result = cabocha.parse(sentence).toString(CaboCha.FORMAT_TREE)

    return {
        "mecab": format_mecab_output(mecab_result),
        "cabocha": format_cabocha_output(cabocha_result),
    }
