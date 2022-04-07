from utils.cfg_yaml import load_config
from utils.mlflow import MlflowWriter
import data
import train
import predict


def main():
    cfg = load_config('src/config/001.yaml')
    EXPERIMENT_NAME = cfg["main"]["experiment_name"]
    writer = MlflowWriter(EXPERIMENT_NAME)

    data.create_dataset.main()

    if cfg["main"]["is_train"]:
        train.train_model.main(cfg)

    predict.save_prediction.main(cfg)

    if not cfg['main']['debug']:
        writer.log_params_from_dict(cfg)
        writer.log_artifact(cfg["main"]["results_path"])
    writer.set_terminated()


if __name__ == "__main__":
    main()
