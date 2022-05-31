Code and data for the paper [Unobserved Local Structures Make Compositional Generalization Hard](https://arxiv.org/pdf/2201.05899).

# COVR-10

COVR is a synthetic semantic parsing dataset used to evaluate sequence to sequence models for compositional generalization. COVR-10 contains 10 compositional splits, in which each test set contains a particular kind of unseen programs.

### The splits

| # | Acc.<sup>1</sup> (FT)<br>Bart/T5 | Acc.<sup>2</sup> (ICL)<br>GPT-3 | 2-ULSs<br>(unobserved local structures<sup>3</sup>) | Example |
|-----|-----|-----|-----|-----|
| [8](covr/splits_details/8.md) | 0.34 | [0.68](covr/gpt3_experiments/8.md) | eq+triangle<br> eq+brown<br> eq+gray<br> eq+round<br> eq+query_attr[color]<br> eq+black<br> eq+white<br> eq+query_attr[shape]<br> eq+square<br> | and (🟠eq (🔵query_attr [color] (with_relation (find (cat), chasing, wi... |
| [25](covr/splits_details/25.md) | 0.59 | [0.53](covr/gpt3_experiments/25.md) | and+some<br> none+filter<br> filter+scene<br> some+filter<br> most+filter<br> exists+filter<br> all+filter<br> | 🟠none (🔵filter (square, filter (square, find (cat))), with_relation (... |
| [34](covr/splits_details/34.md) | 0.35 | [0.47](covr/gpt3_experiments/34.md) | all+with_relation<br> with_relation+scene<br> exists+with_relation<br> none+with_relation<br> most+with_relation<br> some+with_relation<br> | or (eq (count (filter (...)), 4), 🟠exists (🔵with_relation (find (mous... |
| [43](covr/splits_details/43.md) | 0.2 | [0.44](covr/gpt3_experiments/43.md) | and+some<br> and+most<br> or+all<br> and+all<br> or+none<br> and+none<br> or+most<br> or+some<br> | 🟠and (eq (query_attr [color] (find (cat)), brown), 🔵some (find (cat),... |
| [48](covr/splits_details/48.md) | 0 | [0.92](covr/gpt3_experiments/48.md) | \<s>+query_attr[shape]<br> \<s>+query_attr[color]<br> | 🟤query_attr [shape] (with_relation (filter (square, find (cat)), loo... |
| [51](covr/splits_details/51.md) | 0.64 | [0.56](covr/gpt3_experiments/51.md) |  | or (eq (query_attr [color] (with_relation (find (mouse), playing wi... |
| [99](covr/splits_details/99.md) | 0 | [0.95](covr/gpt3_experiments/99.md) | \<s>+count<br> | 🟤count (with_relation (filter (gray, find (animal)), chasing, with_r... |
| [100](covr/splits_details/100.md) | 0.02 | [0.76](covr/gpt3_experiments/100.md) | and+exists<br> exists+find<br> or+exists<br> | 🟠and (eq (query_attr [shape] (find (cat)), white), 🔵exists (filter (t... |
| [110](covr/splits_details/110.md) | 0.18 | [0.52](covr/gpt3_experiments/110.md) | with_relation+filter<br> | or (eq (count (find (animal)), count (🟠with_relation (🔵filter (round,... |
| [115](covr/splits_details/115.md) | 0.28 | [0.19](covr/gpt3_experiments/115.md) | all+with_relation<br> with_relation+scene<br> none+with_relation<br> most+with_relation<br> some+with_relation<br> | or (🟠all (🔵with_relation (find (cat), chasing, with_relation (filter ... |
| [More](covr/all_splits.md)

🟠 and 🔵 represent an unseen pair of symbols in a given example. 🟤 represents a symbol that was unseen as a first token in the output sequence.

Splits are created using the Synchronous context-free grammar (SCFG) [rules](covr/grammar.txt) that have generated this dataset, by holding
out sets of rules that are not seen together during training.

* For details on this splitting method, see [our paper](https://arxiv.org/pdf/2201.05899) (Appendix B.2).
* You can see the set of unseen grammar rules for each split, along with training and test examples, by clicking on _Details_ for any desired split.
* See [the list of all grammar splits](covr/all_splits.md), which includes splits that were not selected for COVR-10. This list only includes grammar splits and not _n_-LS splits.
* Download [COVR-10](https://www.cs.tau.ac.il/~benbogin/covr10.zip)

-----------------
<sup>1</sup>Average exact match accuracy for BART-Base, BART-Large, T5-Base and T5-Large, fine-tuned (FT) separately on each split (see implementation details in the paper).

<sup>2</sup>Exact match accuracy of GPT-3, engine `text-davinci-002`, using OpenAI API. For each split we evaluated on a subset of 100 test examples. We use in-context learning (ICL): for each test instance, we sample 10 examples from the training set and add their source and target to the prompt. Click on the GPT-3 accuracy to see samples of prompts and outputs. 

<sup>3</sup>Unobserved local structures of size 2 (2-LS), considering only parent-child relations. 

# Datasets and splits used in paper 
Download all datasets we used in this paper (COVR, Overnight, Schema2QA, ATIS) together with their compositional splits: [uls_datasets.zip](https://www.cs.tau.ac.il/~benbogin/uls_datasets.zip)

The datasets file has the following format:

| Dataset | Split Method | # Splits | Download Dataset and splits | Comments
|---|---|---|---|---|
| COVR-10 | Grammar | 10 | [covr10.zip](https://www.cs.tau.ac.il/~benbogin/covr10.zip) |
| COVR | Grammar/<br>_n_-LS | 124/<br>22 | [covr.zip](https://www.cs.tau.ac.il/~benbogin/covr.zip) |
| Overnight | Template | 5 (per domain) | [overnight.zip](https://www.cs.tau.ac.il/~benbogin/overnight.zip) | 
| Schema2QA | Template | 5 | [s2q.zip](https://www.cs.tau.ac.il/~benbogin/s2q.zip) | Both utterances and targets are normalized for better evaluation, and are anonymized to resolve column ambiguity
| Atis | Template | 5 | [atis.zip](https://www.cs.tau.ac.il/~benbogin/atis.zip) | Normalized variables for better evaluation

**Note:** Code to run pre-processing will be uploaded soon.

### Experiments

[Code to run experiments](experiments).