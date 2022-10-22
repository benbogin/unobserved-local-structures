import json

OVERNIGHT_DOMAINS = ['basketball', 'blocks', 'calendar', 'calendarplus', 'geo880', 'housing', 'publications', 'recipes',
                     'restaurants', 'socialnetwork']

OVERNIGHT_ALL_DOMAINS = ['basketball', 'blocks', 'calendar', 'calendarplus', 'geo880', 'housing', 'publications', 'recipes',
                     'restaurants', 'socialnetwork', 'regex']


def load_overnight_data_file(filepath: str):
    def lines_to_dict(ex_lines):
        ex = {}
        for i, line in enumerate(ex_lines):
            if line.startswith('  (utterance "'):
                ex['paraphrased'] = line.split('  (utterance "')[1][:-3]
            if line.startswith('  (original "'):
                ex['source'] = line.split('  (original "')[1][:-3]
            if line.startswith('  (targetFormula '):
                ex['target'] = ex_lines[i + 1].strip()
                ex['target'] = ex['target'].replace("edu.stanford.nlp.sempre.overnight.SimpleWorld.", "")
        return ex

    examples = []

    curr_example_lines = []
    for line in open(filepath, "rt"):
        if line.strip() == "(example" and curr_example_lines:
            examples.append(curr_example_lines)
            curr_example_lines = []
        curr_example_lines.append(line)
    if curr_example_lines:
        examples.append(curr_example_lines)

    return [lines_to_dict(ex) for ex in examples]


if __name__ == "__main__":
    for dataset in OVERNIGHT_ALL_DOMAINS:
        examples_per_subset = {}
        for subset in ['train', 'test']:
            examples_per_subset[subset] = load_overnight_data_file(f"../overnight/original/{dataset}.paraphrases.{subset}.examples")
            with open(f"overnight/{dataset}.{subset}.jsonl", "wt") as file_out:
                for i, ex in enumerate(examples_per_subset[subset]):
                    ex['qid'] = f'{dataset}_{subset}_{i}'
                    file_out.write(json.dumps(ex) + "\n")
        with open(f"overnight/{dataset}.all.jsonl", "wt") as file_out:
            for i, ex in enumerate(examples_per_subset['train'] + examples_per_subset['test']):
                file_out.write(json.dumps(ex) + "\n")
