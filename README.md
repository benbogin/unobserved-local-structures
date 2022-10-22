Code and data for the paper [Unobserved Local Structures Make Compositional Generalization Hard](https://arxiv.org/pdf/2201.05899).

# COVR-10

COVR is a synthetic semantic parsing dataset used to evaluate sequence to sequence models for compositional generalization. COVR-10 contains 10 compositional splits, in which each test set contains a particular kind of unseen programs.

### The splits

| # | Acc.<sup>1</sup> (FT)<br>Bart/T5 | Acc.<sup>2</sup> (ICL)<br>GPT-3 | 2-ULSs<br>(unobserved local structures<sup>3</sup>) | Example |
|-----|-----|-----|-----|-----|
| [8](covr/splits_details/8.md) | 0.34 | [0.51](covr/gpt3_experiments/8.md) | eq+triangle<br> eq+brown<br> eq+gray<br> eq+round<br> eq+query_attr[color]<br> eq+black<br> eq+white<br> eq+query_attr[shape]<br> eq+square<br> | **Both the color of cat that is chasing black triangle mouse that is playing with ...**<br>and (🟠eq (🔵query_attr [color] (with_relation (find (cat), chasing, with_relation (... |
| [25](covr/splits_details/25.md) | 0.59 | [0.23](covr/gpt3_experiments/25.md) | and+some<br> none+filter<br> filter+scene<br> some+filter<br> most+filter<br> exists+filter<br> all+filter<br> | **None of square square cat are playing with dog that is looking at white animal...**<br>🟠none (🔵filter (square, filter (square, find (cat))), with_relation (scene (), pla... |
| [34](covr/splits_details/34.md) | 0.35 | [0.38](covr/gpt3_experiments/34.md) | all+with_relation<br> with_relation+scene<br> exists+with_relation<br> none+with_relation<br> most+with_relation<br> some+with_relation<br> | **Either the number of white animal that is looking at square brown animal that is...**<br>or (eq (count (🔵with_relation (filter (white, find (animal)), looking at, ...), 4... |
| [43](covr/splits_details/43.md) | 0.2 | [0.11](covr/gpt3_experiments/43.md) | and+some<br> and+most<br> or+all<br> and+all<br> or+none<br> and+none<br> or+most<br> or+some<br> | **Both the color of cat is equal to brown and some of cat are brown ...**<br>🟠and (eq (query_attr [color] (find (cat)), brown), 🔵some (find (cat), filter (brow... |
| [48](covr/splits_details/48.md) | 0 | [0.85](covr/gpt3_experiments/48.md) | \<s>+query_attr[shape]<br> \<s>+query_attr[color]<br> | **What is the shape of square cat that is looking at black brown animal that is lo...**<br>🟤query_attr [shape] (with_relation (filter (square, find (cat)), looking at, with... |
| [51](covr/splits_details/51.md) | 0.64 | [0.35](covr/gpt3_experiments/51.md) |  | **Either the color of mouse that is playing with mouse that is chasing triangle br...**<br>or (eq (query_attr [color] (with_relation (find (mouse), playing with, with_rela... |
| [99](covr/splits_details/99.md) | 0 | [0.89](covr/gpt3_experiments/99.md) | \<s>+count<br> | **What is the number of gray animal that is chasing gray mouse that is playing wit...**<br>🟤count (with_relation (filter (gray, find (animal)), chasing, with_relation (filt... |
| [100](covr/splits_details/100.md) | 0.02 | [0.18](covr/gpt3_experiments/100.md) | and+exists<br> exists+find<br> or+exists<br> | **Both the shape of cat is equal to white and there is triangle black cat ...**<br>🟠and (eq (query_attr [shape] (find (cat)), white), 🔵exists (filter (triangle, filt... |
| [110](covr/splits_details/110.md) | 0.18 | [0.33](covr/gpt3_experiments/110.md) | with_relation+filter<br> | **Either the number of animal is equal to the number of round dog that is chasing ...**<br>or (eq (count (find (animal)), count (🟠with_relation (🔵filter (round, find (dog)),... |
| [115](covr/splits_details/115.md) | 0.28 | [0.05](covr/gpt3_experiments/115.md) | all+with_relation<br> with_relation+scene<br> none+with_relation<br> most+with_relation<br> some+with_relation<br> | **Either all of cat that is chasing triangle triangle cat that is playing with mou...**<br>or (🟠all (🔵with_relation (find (cat), chasing, with_relation (filter (triangle, fi... |
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

<sup>2</sup>Exact match accuracy of GPT-3, engine `text-davinci-002`, using OpenAI API. For each split we evaluated on a subset of 100 test examples. We use in-context learning (ICL): for each test instance, we randomly sample 10 examples from the training set and add their source and target to the prompt. Click on the GPT-3 accuracy to see samples of prompts and outputs. 

<sup>3</sup>Unobserved local structures of size 2 (2-LS), considering only parent-child relations. 

# Download datasets and splits used in paper 

| Dataset | Split Method | # Splits | Download Dataset and splits | Comments
|---|---|---|---|---|
| COVR-10 | Grammar | 10 | [covr10.zip](https://www.cs.tau.ac.il/~benbogin/covr10.zip) |
| COVR | Grammar/<br>_n_-LS | 124/<br>22 | [covr.zip](https://www.cs.tau.ac.il/~benbogin/covr.zip) |
| Overnight | Template | 5 (per domain) | [overnight.zip](https://www.cs.tau.ac.il/~benbogin/overnight.zip) | 
| Schema2QA | Template | 5 | [s2q.zip](https://www.cs.tau.ac.il/~benbogin/s2q.zip) | Both utterances and targets are normalized for better evaluation, and are anonymized to resolve column ambiguity
| Atis | Template | 5 | [atis.zip](https://www.cs.tau.ac.il/~benbogin/atis.zip) | Normalized variables for better evaluation

### Experiments

[Code to run experiments](experiments).

[Code to compute easiness](easiness).