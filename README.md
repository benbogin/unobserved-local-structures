Code for the paper [Unobserved Local Structures Make Compositional Generalization Hard](https://arxiv.org/pdf/2201.05899).

### Datasets 
Download all datasets we used in this paper (COVR, Overnight, Schema2QA, ATIS) together with their compositional splits: [uls_datasets.zip](https://www.cs.tau.ac.il/~benbogin/uls_datasets.zip)

The datasets file has the following format:
```
datasets
└── {dataset}
    ├── {dataset}.all.jsonl - all examples
    └── splits
        └── {template/n-ls/grammar}/{split_ID}/{dataset}.json - train/test example ids of specific splits
```

**Note:** Code to run pre-processing will be uploaded soon.

### Experiments

Code to run experiments will be uploaded soon.