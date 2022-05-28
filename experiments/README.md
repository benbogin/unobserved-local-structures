# Running experiments

We use AllenNLP + huggingface.

1. Install all required packages
```
pip install -r requirements.txt
```
2. Download the [datasets and splits](../) you wish to train on to any directory.
3. Run the following command to train:
    ```
    python --model-name bart --dataset covr --split-name grammar/8 --datasets-path ../datasets
    ```

    * The value of `--model-name` can be `bart/bart-large/t5/t5-large`
    * The value of `--dataset` can be `covr/overnight/atis/s2q`
    * The value of `--split-name` can be replaced with the name of the split you want to train on: this will be the same as the directory path
      under the dataset directory
    * The value of `--datasets-path` should point to the directory where you have downloaded the datasets to
    * For overnight, use `--domain` to set the domain you want to train on.
   
   For example, to run T5-large on Overnight, blocks domain:
    ```
    python --model-name t5-large --dataset overnight --domain blocks --split-name template/split_0 --datasets-path ../datasets
    ```