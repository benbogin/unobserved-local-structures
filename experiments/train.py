import os
import argparse
import time

from allennlp.commands.train import train_model
from allennlp.common import Params
from allennlp.common.util import import_module_and_submodules
from allennlp.common.params import with_overrides, parse_overrides


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument("name", nargs="?", default="", help="Experiment name")

    args.add_argument(
        "--model-name", choices=["bart", "bart-large", "t5", "t5-large"], required=True
    )
    args.add_argument(
        "--dataset", choices=["covr", "overnight", "atis", "s2q"], required=True
    )
    args.add_argument("--split-name", type=str, default="", required=True)
    args.add_argument(
        "--instance-source",
        choices=["source", "paraphrased"],
        default="source",
        help="for overnight: `source` for synthetic, `paraphrased` for the natural language version.",
    )
    args.add_argument("--datasets-path", default="../datasets")
    args.add_argument("--domain", help="overnight's domain")
    args.add_argument("--recover", action="store_true")
    args.add_argument("-o", "--overrides", type=str, default="")

    return args.parse_args()


def get_experiment_name(name, dataset, domain, model_name):
    if name:
        name = f"{name}-"
    name += f"{dataset}"
    if dataset == "overnight":
        name += f"-{domain}-"
    name += f"-{model_name}"
    name += "_" + str(time.time()).replace(".", "")
    return name


def get_full_model_name(model_name):
    if model_name == "bart":
        return "facebook/bart-base"
    elif model_name == "t5":
        return "t5-base"
    elif model_name == "t5-large":
        return "t5-large"
    elif model_name == "bart-large":
        return "facebook/bart-large"
    raise ValueError(model_name)


def merge_settings(base, to_merge, override):
    output = with_overrides(base, to_merge)
    output = with_overrides(output, parse_overrides(override))
    return output


def main_train():
    args = parse_args()
    import_module_and_submodules("src")

    # load base config
    settings = Params.from_file("configs/base.jsonnet", args.overrides).params

    # set training and test path
    dataset_with_domain = args.dataset
    if args.domain:
        dataset_with_domain = f"{args.dataset}/{args.domain}"

    settings[
        "train_data_path"
    ] = f"{args.datasets_path}/{dataset_with_domain}/all.jsonl"
    settings[
        "validation_data_path"
    ] = f"@{args.datasets_path}/{dataset_with_domain}/all.jsonl"
    settings["dataset_reader"][
        "split_path"
    ] = f"{args.datasets_path}/{dataset_with_domain}/splits/{args.split_name}/split.json"

    dataset_specific_config_path = f"../configs/{args.dataset}.jsonnet"
    if os.path.exists(dataset_specific_config_path):
        dataset_settings = Params.from_file(f"../configs/{args.dataset}.jsonnet").params
        settings = merge_settings(settings, dataset_settings, args.overrides)

    # set model name based on command line args
    model_name = get_full_model_name(args.model_name)
    settings["dataset_reader"]["source_tokenizer"]["model_name"] = model_name
    settings["dataset_reader"]["source_token_indexers"]["tokens"][
        "model_name"
    ] = model_name
    settings["model"]["model_name"] = model_name

    # set experiment name and path
    parent_experiments_path = "runs"
    experiment_name = get_experiment_name(
        args.name, args.dataset, args.domain, args.model_name
    )
    serialization_dir = experiment_name.replace("/", "-")
    serialization_dir_path = os.path.join(
        parent_experiments_path, serialization_dir
    ).replace(" ", "_")

    # call AllenNLP to start training
    train_model(
        params=Params(settings),
        serialization_dir=serialization_dir_path,
        recover=args.recover,
    )


if __name__ == "__main__":
    main_train()
