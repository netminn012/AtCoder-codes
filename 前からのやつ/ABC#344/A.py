import re
# 例の文字列
text = input()
# 2つの|で囲まれた部分を削除
cleaned_text = re.sub(r'\|.*?\|', '', text)
print(cleaned_text)