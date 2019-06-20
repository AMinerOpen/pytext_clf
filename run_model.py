import sys
import pytext

config_file = sys.argv[1]
model_file = sys.argv[2]

config = pytext.load_config(config_file)
predictor = pytext.create_predictor(config, model_file)

id2name = {
        '0': '数理科学',
        '1': '化学科学',
        '2': '生命科学',
        '3': '地球科学',
        '4': '工程与材料科学',
        '5': '信息科学',
        '6': '管理科学',
        '7': '医学科学'
}

text = input('请输入一行文本：')
words = list(text.replace('\n', '').replace('\r', '').replace('\t', '').lower())
result = predictor({"raw_text":' '.join(words)})
doc_label_scores_prefix = (
        'scores:' if any(r.startswith('scores:') for r in result)
        else 'doc_scores:'
        )
best_doc_label = max(
        (label for label in result if label.startswith(doc_label_scores_prefix)),
        key=lambda label: result[label][0],
        )[len(doc_label_scores_prefix):]
print(id2name[best_doc_label])
