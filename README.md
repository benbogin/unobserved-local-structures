Code and data for the paper [Unobserved Local Structures Make Compositional Generalization Hard](https://arxiv.org/pdf/2201.05899).

# COVR-10

COVR is a synthetic semantic parsing dataset used to evaluate sequence to sequence models for compositional generalization. COVR-10 contains 10 compositional splits, in which each test set contains a particular kind of unseen programs.

### The splits

| # | Acc.<sup>1</sup> (FT)<br>Bart/T5 | Acc.<sup>2</sup> (ICL)<br>GPT-3 | Example |  |
|-----|-----|-----|-----|-----|
| 8 | 0.34 | [0.68](covr/gpt3_experiments/8.md) | and (🟠eq (🔵query_attr [color] (with_relation (find (cat), chasing, wi... | [Details](covr/splits_details/8.md) |
| 25 | 0.59 | [0.53](covr/gpt3_experiments/25.md) | 🟠none (🔵filter (square, filter (square, find (cat))), with_relation (... | [Details](covr/splits_details/25.md) |
| 34 | 0.35 | [0.47](covr/gpt3_experiments/34.md) | or (eq (count (filter (...)), 4), 🟠exists (🔵with_relation (find (mous... | [Details](covr/splits_details/34.md) |
| 43 | 0.2 | [0.44](covr/gpt3_experiments/43.md) | 🟠and (eq (query_attr [color] (find (cat)), brown), 🔵some (find (cat),... | [Details](covr/splits_details/43.md) |
| 48 | 0 | [0.92](covr/gpt3_experiments/48.md) | 🟤query_attr [shape] (with_relation (filter (square, find (cat)), loo... | [Details](covr/splits_details/48.md) |
| 51 | 0.64 | [0.56](covr/gpt3_experiments/51.md) | or (eq (query_attr [color] (with_relation (find (mouse), playing wi... | [Details](covr/splits_details/51.md) |
| 99 | 0 | [0.95](covr/gpt3_experiments/99.md) | 🟤count (with_relation (filter (gray, find (animal)), chasing, with_r... | [Details](covr/splits_details/99.md) |
| 100 | 0.02 | [0.76](covr/gpt3_experiments/100.md) | 🟠and (eq (query_attr [shape] (find (cat)), white), 🔵exists (filter (t... | [Details](covr/splits_details/100.md) |
| 110 | 0.18 | [0.52](covr/gpt3_experiments/110.md) | or (eq (count (find (animal)), count (🟠with_relation (🔵filter (round,... | [Details](covr/splits_details/110.md) |
| 115 | 0.28 | [0.19](covr/gpt3_experiments/115.md) | or (🟠all (🔵with_relation (find (cat), chasing, with_relation (filter ... | [Details](covr/splits_details/115.md) |

🟠 and 🔵 represent an unseen pair of symbols in a given example. 🟤 represents a symbol that was unseen as a first token in the output sequence.

Splits are created using the Synchronous context-free grammar (SCFG) [rules](covr/grammar.txt) that have generated this dataset, by holding
out sets of rules that are not seen together during training.

* For details on this splitting method, see [our paper](https://arxiv.org/pdf/2201.05899) (Appendix B.2).
* You can see the set of unseen grammar rules for each split, along with training and test examples, by clicking on _Details_ for any desired split.
* See [the list of all grammar splits](covr/all_splits.md), which includes splits that were not selected for COVR-10. This list only includes grammar splits and not _n_-LS splits.


<sup>1</sup>Average exact match accuracy for BART-Base, BART-Large, T5-Base and T5-Large, fine-tuned (FT) separately on each split (see implementation details in the paper).

<sup>2</sup>Exact match accuracy of GPT-3, engine `text-davinci-002`, using OpenAI API. For each split we evaluated on a subset of 100 test examples. We use in-context learning (ICL): for each test instance, we sample 10 examples from the training set and add their source and target to the prompt. Click on the GPT-3 accuracy to see samples of prompts and outputs. 

# Datasets and splits used in paper 
Download all datasets we used in this paper (COVR, Overnight, Schema2QA, ATIS) together with their compositional splits: [uls_datasets.zip](https://www.cs.tau.ac.il/~benbogin/uls_datasets.zip)

The datasets file has the following format:

| Dataset | Split Method | # Splits | Download Dataset and splits | Comments
|---|---|---|---|---|
| COVR | Grammar/<br>_n_-LS | 124/<br>22 | [covr.zip](https://www.cs.tau.ac.il/~benbogin/covr.zip) |
| Overnight | Template | 5 (per domain) | [overnight.zip](https://www.cs.tau.ac.il/~benbogin/overnight.zip) | 
| Schema2QA | Template | 5 | [s2q.zip](https://www.cs.tau.ac.il/~benbogin/s2q.zip) | Both utterances and targets are normalized for better evaluation, and are anonymized to resolve column ambiguity
| Atis | Template | 5 | [atis.zip](https://www.cs.tau.ac.il/~benbogin/atis.zip) | Normalized variables for better evaluation

**Note:** Code to run pre-processing will be uploaded soon.

### Experiments

[Code to run experiments](experiments).