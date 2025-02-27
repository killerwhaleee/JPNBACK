from transformers import pipeline

# 设置 Hugging Face Token
from huggingface_hub import login


# 加载模型
model_name = "Helsinki-NLP/opus-mt-ja-en"  # 这里用的是日文到英文的翻译模型，或可以根据需求换其他模型
translator = pipeline("translation", model=model_name)

# 日文句子
sentence = "私は昨日、友達と映画を見に行きました。"

# 如果想让模型解释语法，可以换成其他模型或任务，比如生成解释
# 示例：用T5模型来生成句子解释
explanation_model = pipeline("text2text-generation", model="t5-small")

explanation = explanation_model(f"Explain the sentence: {sentence}")


def translate_sentence(sentence):
    translation = translator(sentence, src_lang="ja", tgt_lang="en")
    return translation


print("翻译结果:", translate_sentence(sentence))
