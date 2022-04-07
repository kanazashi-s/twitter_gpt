from pathlib import Path
import pandas as pd
import predict
from utils.cfg_yaml import load_config


def main(cfg):
    prediction_inputs_df = pd.read_csv(Path("data", "raw", "prediction_inputs.csv"))
    output_path = Path(cfg["main"]["results_path"])
    output_path.mkdir(parents=True, exist_ok=True)

    results = []
    task_func_map = {
        "copy_from_description": predict.copy_from_description.generate_catchphrase,
        "copy_without_description": predict.copy_without_description.generate_catchphrase,
    }

    for _, row in prediction_inputs_df.iterrows():
        results.append(task_func_map[cfg["main"]["task"]](cfg, *row))

    with open(output_path / "results.txt", "w") as f:
        for result, (idx, row) in zip(results, prediction_inputs_df.iterrows()):
            f.write("\n=====\n")
            f.write(f"入力: {','.join(row)}\n")
            for line in result:
                f.write(line + '\n')


if __name__ == "__main__":
    cfg = load_config('src/config/001.yaml')
    main(cfg)
