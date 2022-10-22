import argparse
import json
from collections import OrderedDict
from glob import glob
from pprint import pprint

import numpy as np
from dotenv import load_dotenv
from tqdm import tqdm

from easiness_predictor import EasinessPredictor

argparse = argparse.ArgumentParser()
argparse.add_argument("dataset", choices=["covr", "overnight", "atis", "s2q"])
argparse.add_argument("--splits", default="grammar")
argparse.add_argument("--datasets-path", default="../datasets")
args = argparse.parse_args()

load_dotenv(dotenv_path="../.env")


def analyze_dataset(dataset, config, splits):
    """
    Print an analysis of the dataset, including average easiness predictions for the splits of interest
    """
    all_examples = [
        json.loads(l) for l in open(f"{args.datasets_path}/{dataset}/all.jsonl")
    ]
    datasets_examples_by_qid = {l["qid"]: l for l in all_examples}
    splits = glob(f"{args.datasets_path}/{dataset}/splits/{splits}/*/*.json")

    rows = {}
    for split_info_path in tqdm(splits):
        split_info = json.load(open(split_info_path))
        row = OrderedDict()

        train_targets = [
            datasets_examples_by_qid[qid]["target"] for qid in split_info["train"]
        ]
        predictor = EasinessPredictor(train_targets, config)

        score_debug = {}
        confidence, binary_targets, targets = [], [], []

        for qid in split_info["test"]:
            ex = datasets_examples_by_qid[qid]

            easiness_prediction = predictor.predict_easiness_for_example(ex["target"])
            score_debug[ex["qid"]] = easiness_prediction
            confidence.append(easiness_prediction["final_score"])

        if not confidence:
            print(
                f"cannot analyze model predictions for split `{split_info_path}` as no examples were found"
            )
            continue

        row["unseen_pairs"] = list(
            {
                eval(b)
                for s in score_debug.values()
                for b in s.get("structure", {}).get("debug_info", [])
            }
        )

        row["easiness_score"] = np.mean(confidence)

        pprint({k: v for k, v in row.items() if k not in ["debug", "unseen_pairs"]})

        rows[split_info_path] = row

    pprint({k: v for k, v in rows.items() if k != "rows"})


if __name__ == "__main__":
    cfg = {
        "structures": {
            "type": "ast",
            "n": 2,
            "add_parent_child": True,
            "add_adjacent_sibling": True,
        },
        "find_similar": "01",
        "position": False,
        "length": False,
        "random": False,
    }
    analyze_dataset(args.dataset, cfg, args.splits)
