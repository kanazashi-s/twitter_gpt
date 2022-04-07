from pathlib import Path
from transformers import T5Tokenizer, AutoModelForCausalLM
from utils.cfg_yaml import load_config


def generate_catchphrase(cfg, input_text, is_print_results=True):
    tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
    tokenizer.do_lower_case = True

    model_path = Path(cfg["main"]["model_path"], cfg["main"]["train_twitter_id"])
    model = AutoModelForCausalLM.from_pretrained(model_path).cuda()
    model.eval()

    input_text = f"<s>{input_text}"
    input_ids = tokenizer.encode(input_text, return_tensors='pt').cuda()

    print("start generation...")
    out = model.generate(
        input_ids,
        **cfg["prediction"],
        max_length=len(input_ids[0]) + cfg["prediction_add"]["max_length"],
        min_length=len(input_ids[0]) + cfg["prediction_add"]["min_length"],
    )

    print('-' * 5, '生成キャッチフレーズ', '-' * 5)
    sents = []
    for sent in tokenizer.batch_decode(out):
        sent = sent.replace('<s>', '')
        sent = sent.replace('</s>', '')
        sents.append(sent)
        if is_print_results:
            print(sent)

    return sents


if __name__ == "__main__":
    cfg = load_config('src/config/001.yaml')
    sents = generate_catchphrase(cfg, "データ分析")
