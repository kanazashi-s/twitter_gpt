from pathlib import Path
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForLanguageModeling, LineByLineTextDataset
from transformers import T5Tokenizer, AutoModelForCausalLM
from utils.cfg_yaml import load_config


def load_dataset(train_input_path, test_input_path, tokenizer):

    train_dataset = LineByLineTextDataset(
        tokenizer=tokenizer,
        file_path=train_input_path,
        block_size=128
    )
    test_dataset = LineByLineTextDataset(
        tokenizer=tokenizer,
        file_path=test_input_path,
        block_size=128
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )
    return train_dataset, test_dataset, data_collator


def main(cfg):
    input_path = Path("data", "processed", "tweets")
    train_input_path = input_path / f'train_{cfg["main"]["train_twitter_id"]}.txt'
    test_input_path = input_path / f'test_{cfg["main"]["train_twitter_id"]}.txt'

    tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
    tokenizer.do_lower_case = True

    output_path = Path(cfg["main"]["model_path"], cfg["main"]["train_twitter_id"])
    model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")
    train_dataset, test_dataset, data_collator = load_dataset(train_input_path, test_input_path, tokenizer)

    training_args = TrainingArguments(
        output_dir=output_path,
        **cfg["training_args"]
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
    )

    trainer.train()
    trainer.save_model()


if __name__ == "__main__":
    cfg = load_config('src/config/001.yaml')
    main(cfg)