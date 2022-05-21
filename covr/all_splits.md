| # | Acc. (FT)<br>Bart/T5 | Acc. (ICL)<br>GPT-3 | Example |  |
|-----|-----|-----|-----|-----|
| 0 | 1 |  | and (eq (query_attr [shape] (find (cat)), white), exists (filter (t... | [Details](splits_details/0.md) |
| 1 | 1 |  | and (lt (count (find (cat)), 2), exists (find (dog)))... | [Details](splits_details/1.md) |
| 2 | 1 | [0.83](gpt3_experiments/2.md) | choose (query_attr [shape] (with_relation (filter (triangle, filter... | [Details](splits_details/2.md) |
| 3 | 0.43 | [0.67](gpt3_experiments/3.md) | and (eq (query_attr [color] (filter (black, filter (triangle, find ... | [Details](splits_details/3.md) |
| 4 | 0.99 |  | or (eq (count (with_relation (find (animal), looking at, with_relat... | [Details](splits_details/4.md) |
| 6 | 1 |  | eq (query_attr [shape] (filter (gray, filter (round, find (mouse)))... | [Details](splits_details/6.md) |
| 7 | 1 | [0.85](gpt3_experiments/7.md) | choose (query_attr [color] (filter (black, filter (square, find (mo... | [Details](splits_details/7.md) |
| 8 | 0.34 | [0.68](gpt3_experiments/8.md) | and (eq (query_attr [color] (with_relation (find (cat), chasing, wi... | [Details](splits_details/8.md) |
| 9 | 1 |  | and (eq (query_attr [shape] (find (animal)), brown), most (with_rel... | [Details](splits_details/9.md) |
| 10 | 0.99 |  | and (lt (count (with_relation (find (dog), looking at, find (mouse)... | [Details](splits_details/10.md) |
| 11 | 0.8 | [0.79](gpt3_experiments/11.md) | choose (query_attr [shape] (with_relation (filter (square, find (an... | [Details](splits_details/11.md) |
| 12 | 0.74 |  | or (gt (count (with_relation (filter (round, find (cat)), playing w... | [Details](splits_details/12.md) |
| 13 | 1 |  | and (gt (count (with_relation (filter (round, find (dog)), chasing,... | [Details](splits_details/13.md) |
| 14 | 0.99 |  | or (lt (count (with_relation (filter (white, find (cat)), looking a... | [Details](splits_details/14.md) |
| 15 | 0.41 | [0.85](gpt3_experiments/15.md) | query_attr [shape] (with_relation (find (cat), playing with, with_r... | [Details](splits_details/15.md) |
| 16 | 0.98 |  | or (none (find (animal), filter (gray, scene ())), lt (count (with_... | [Details](splits_details/16.md) |
| 17 | 0.95 |  | eq (query_attr [shape] (with_relation (find (mouse), looking at, wi... | [Details](splits_details/17.md) |
| 18 | 0.99 |  | and (lt (count (filter (triangle, filter (round, find (mouse)))), c... | [Details](splits_details/18.md) |
| 19 | 0.99 |  | or (none (with_relation (filter (triangle, filter (gray, find (mous... | [Details](splits_details/19.md) |
| 20 | 1 |  | choose (query_attr [shape] (with_relation (filter (round, filter (b... | [Details](splits_details/20.md) |
| 21 | 1 |  | and (exists (filter (square, filter (brown, find (mouse)))), gt (co... | [Details](splits_details/21.md) |
| 22 | 0.99 |  | or (eq (query_attr [shape] (find (cat)), query_attr [shape] (with_r... | [Details](splits_details/22.md) |
| 23 | 0.95 |  | and (all (find (cat), with_relation (scene (), looking at, find (mo... | [Details](splits_details/23.md) |
| 24 | 0.88 | [0.86](gpt3_experiments/24.md) | query_attr [color] (with_relation (find (mouse), looking at, filter... | [Details](splits_details/24.md) |
| 25 | 0.59 | [0.53](gpt3_experiments/25.md) | none (filter (square, filter (square, find (cat))), with_relation (... | [Details](splits_details/25.md) |
| 26 | 0.98 |  | or (none (find (animal), filter (gray, scene ())), lt (count (with_... | [Details](splits_details/26.md) |
| 27 | 1 |  | and (eq (count (filter (round, filter (black, find (animal)))), 4),... | [Details](splits_details/27.md) |
| 28 | 0.26 | [0.28](gpt3_experiments/28.md) | most (with_relation (filter (white, filter (square, find (cat))), l... | [Details](splits_details/28.md) |
| 29 | 0.99 |  | or (most (filter (square, find (cat)), with_relation (scene (), cha... | [Details](splits_details/29.md) |
| 30 | 1 |  | or (exists (filter (brown, filter (brown, find (dog)))), lt (count ... | [Details](splits_details/30.md) |
| 31 | 0.3 | [0.93](gpt3_experiments/31.md) | count (with_relation (filter (round, find (dog)), playing with, wit... | [Details](splits_details/31.md) |
| 32 | 1 |  | or (gt (count (filter (square, filter (round, find (mouse)))), 2), ... | [Details](splits_details/32.md) |
| 33 | 1 |  | query_attr [shape] (with_relation (filter (round, filter (round, fi... | [Details](splits_details/33.md) |
| 34 | 0.35 | [0.47](gpt3_experiments/34.md) | or (eq (count (filter (...)), 4), exists (with_relation (find (mous... | [Details](splits_details/34.md) |
| 35 | 1 |  | and (eq (query_attr [shape] (find (cat)), round), gt (count (with_r... | [Details](splits_details/35.md) |
| 36 | 0.98 |  | and (eq (query_attr [color] (filter (white, filter (white, find (ca... | [Details](splits_details/36.md) |
| 37 | 1 |  | and (eq (count (with_relation (filter (triangle, find (cat)), chasi... | [Details](splits_details/37.md) |
| 38 | 1 |  | or (exists (find (animal)), most (with_relation (filter (black, fin... | [Details](splits_details/38.md) |
| 39 | 0.98 |  | and (eq (query_attr [color] (find (dog)), query_attr [color] (filte... | [Details](splits_details/39.md) |
| 40 | 0.95 |  | eq (count (with_relation (filter (square, filter (black, find (dog)... | [Details](splits_details/40.md) |
| 41 | 1 |  | or (lt (count (with_relation (filter (square, filter (brown, find (... | [Details](splits_details/41.md) |
| 42 | 1 | [0.69](gpt3_experiments/42.md) | or (eq (count (find (dog)), count (find (cat))), lt (count (filter ... | [Details](splits_details/42.md) |
| 43 | 0.2 | [0.44](gpt3_experiments/43.md) | and (eq (query_attr [color] (find (cat)), brown), some (find (cat),... | [Details](splits_details/43.md) |
| 44 | 0.99 |  | and (eq (query_attr [shape] (find (animal)), query_attr [shape] (wi... | [Details](splits_details/44.md) |
| 45 | 0.61 | [0.74](gpt3_experiments/45.md) | and (exists (with_relation (find (cat), chasing, with_relation (fin... | [Details](splits_details/45.md) |
| 46 | 0.95 |  | exists (with_relation (filter (brown, filter (triangle, find (dog))... | [Details](splits_details/46.md) |
| 47 | 0.99 |  | or (eq (query_attr [shape] (filter (square, find (mouse))), gray), ... | [Details](splits_details/47.md) |
| 48 | 0 | [0.92](gpt3_experiments/48.md) | query_attr [shape] (with_relation (filter (square, find (cat)), loo... | [Details](splits_details/48.md) |
| 49 | 0.99 |  | or (eq (query_attr [color] (find (mouse)), query_attr [shape] (find... | [Details](splits_details/49.md) |
| 50 | 0.93 |  | or (exists (filter (triangle, filter (triangle, find (dog)))), eq (... | [Details](splits_details/50.md) |
| 51 | 0.64 | [0.56](gpt3_experiments/51.md) | or (eq (query_attr [color] (with_relation (find (mouse), playing wi... | [Details](splits_details/51.md) |
| 52 | 0.99 |  | or (exists (find (mouse)), eq (query_attr [color] (find (mouse)), q... | [Details](splits_details/52.md) |
| 53 | 0.83 |  | gt (count (with_relation (filter (black, filter (square, find (dog)... | [Details](splits_details/53.md) |
| 54 | 0.99 |  | and (lt (count (find (cat)), 2), exists (find (dog)))... | [Details](splits_details/54.md) |
| 55 | 0.99 | [0.8](gpt3_experiments/55.md) | or (exists (with_relation (find (animal), playing with, with_relati... | [Details](splits_details/55.md) |
| 56 | 0.99 |  | and (eq (query_attr [shape] (find (cat)), white), exists (filter (t... | [Details](splits_details/56.md) |
| 57 | 0.92 |  | or (eq (count (filter (triangle, find (cat))), count (filter (white... | [Details](splits_details/57.md) |
| 58 | 1 |  | or (eq (count (with_relation (find (animal), looking at, with_relat... | [Details](splits_details/58.md) |
| 59 | 1 |  | and (all (find (cat), with_relation (scene (), looking at, find (mo... | [Details](splits_details/59.md) |
| 60 | 0.96 |  | and (eq (query_attr [shape] (filter (round, find (animal))), query_... | [Details](splits_details/60.md) |
| 61 | 1 |  | and (exists (filter (round, find (animal))), eq (query_attr [shape]... | [Details](splits_details/61.md) |
| 62 | 0.99 |  | or (eq (query_attr [color] (find (cat)), query_attr [shape] (with_r... | [Details](splits_details/62.md) |
| 63 | 1 |  | and (none (with_relation (find (dog), chasing, with_relation (find ... | [Details](splits_details/63.md) |
| 64 | 1 |  | or (eq (query_attr [color] (find (dog)), gray), eq (count (filter (... | [Details](splits_details/64.md) |
| 65 | 0.94 |  | eq (query_attr [shape] (filter (round, find (cat))), square)... | [Details](splits_details/65.md) |
| 66 | 0.62 | [0.82](gpt3_experiments/66.md) | choose (query_attr [shape] (with_relation (find (animal), chasing, ... | [Details](splits_details/66.md) |
| 67 | 0.98 |  | and (eq (query_attr [color] (find (dog)), query_attr [color] (filte... | [Details](splits_details/67.md) |
| 68 | 0.75 | [0.57](gpt3_experiments/68.md) | or (most (with_relation (find (dog), looking at, with_relation (fil... | [Details](splits_details/68.md) |
| 69 | 1 | [0.81](gpt3_experiments/69.md) | choose (query_attr [shape] (with_relation (filter (round, find (ani... | [Details](splits_details/69.md) |
| 70 | 0.99 |  | or (exists (with_relation (filter (gray, find (dog)), chasing, with... | [Details](splits_details/70.md) |
| 71 | 0.99 |  | or (eq (count (find (animal)), 4), eq (query_attr [color] (with_rel... | [Details](splits_details/71.md) |
| 72 | 0.97 |  | choose (query_attr [color] (with_relation (filter (triangle, filter... | [Details](splits_details/72.md) |
| 73 | 0.96 |  | and (eq (query_attr [shape] (with_relation (filter (gray, find (ani... | [Details](splits_details/73.md) |
| 74 | 0.99 |  | and (lt (count (filter (triangle, filter (round, find (mouse)))), c... | [Details](splits_details/74.md) |
| 75 | 0.99 |  | eq (query_attr [shape] (with_relation (find (cat), playing with, fi... | [Details](splits_details/75.md) |
| 76 | 0.65 | [0.66](gpt3_experiments/76.md) | some (with_relation (find (dog), playing with, with_relation (find ... | [Details](splits_details/76.md) |
| 77 | 0.99 |  | and (eq (query_attr [shape] (filter (square, find (animal))), query... | [Details](splits_details/77.md) |
| 78 | 1 | [0.88](gpt3_experiments/78.md) | choose (count (with_relation (find (cat), looking at, with_relation... | [Details](splits_details/78.md) |
| 79 | 0.98 |  | or (gt (count (filter (black, filter (round, find (cat)))), 3), eq ... | [Details](splits_details/79.md) |
| 80 | 1 |  | eq (query_attr [color] (filter (triangle, filter (round, find (mous... | [Details](splits_details/80.md) |
| 81 | 1 |  | eq (query_attr [shape] (with_relation (filter (round, filter (gray,... | [Details](splits_details/81.md) |
| 82 | 0.99 |  | or (eq (query_attr [shape] (find (cat)), query_attr [shape] (with_r... | [Details](splits_details/82.md) |
| 83 | 0.99 |  | and (eq (query_attr [color] (find (cat)), query_attr [shape] (with_... | [Details](splits_details/83.md) |
| 84 | 1 |  | query_attr [color] (with_relation (filter (gray, find (dog)), looki... | [Details](splits_details/84.md) |
| 85 | 0.99 |  | or (eq (query_attr [color] (find (cat)), query_attr [shape] (with_r... | [Details](splits_details/85.md) |
| 86 | 0.99 |  | and (eq (query_attr [color] (find (dog)), query_attr [shape] (with_... | [Details](splits_details/86.md) |
| 87 | 1 |  | choose (count (with_relation (find (mouse), looking at, with_relati... | [Details](splits_details/87.md) |
| 88 | 1 |  | choose (count (with_relation (filter (white, find (mouse)), looking... | [Details](splits_details/88.md) |
| 89 | 0.65 | [0.87](gpt3_experiments/89.md) | lt (count (filter (white, find (dog))), count (find (cat)))... | [Details](splits_details/89.md) |
| 90 | 0.7 | [0.96](gpt3_experiments/90.md) | exists (filter (square, filter (brown, find (mouse))))... | [Details](splits_details/90.md) |
| 91 | 0.75 | [0.89](gpt3_experiments/91.md) | lt (count (find (dog)), count (with_relation (find (dog), chasing, ... | [Details](splits_details/91.md) |
| 92 | 0.69 | [0.59](gpt3_experiments/92.md) | or (all (with_relation (find (cat), chasing, with_relation (filter ... | [Details](splits_details/92.md) |
| 93 | 1 |  | lt (count (with_relation (filter (white, filter (black, find (dog))... | [Details](splits_details/93.md) |
| 94 | 1 |  | and (eq (query_attr [color] (find (cat)), query_attr [shape] (filte... | [Details](splits_details/94.md) |
| 95 | 0.94 |  | choose (count (with_relation (filter (gray, find (cat)), playing wi... | [Details](splits_details/95.md) |
| 96 | 1 |  | or (none (find (animal), filter (gray, scene ())), lt (count (with_... | [Details](splits_details/96.md) |
| 97 | 0.99 |  | and (eq (query_attr [shape] (filter (square, find (mouse))), query_... | [Details](splits_details/97.md) |
| 98 | 0.74 |  | and (exists (with_relation (filter (brown, find (cat)), chasing, fi... | [Details](splits_details/98.md) |
| 99 | 0 | [0.95](gpt3_experiments/99.md) | count (with_relation (filter (gray, find (animal)), chasing, with_r... | [Details](splits_details/99.md) |
| 100 | 0.02 | [0.76](gpt3_experiments/100.md) | and (eq (query_attr [shape] (find (cat)), white), exists (filter (t... | [Details](splits_details/100.md) |
| 101 | 1 |  | or (eq (query_attr [color] (with_relation (find (mouse), playing wi... | [Details](splits_details/101.md) |
| 102 | 1 |  | and (eq (count (find (mouse)), count (with_relation (find (dog), pl... | [Details](splits_details/102.md) |
| 103 | 0.99 |  | or (eq (query_attr [color] (with_relation (find (dog), chasing, wit... | [Details](splits_details/103.md) |
| 104 | 1 |  | choose (count (with_relation (filter (triangle, find (animal)), pla... | [Details](splits_details/104.md) |
| 105 | 1 |  | count (with_relation (filter (square, filter (brown, find (animal))... | [Details](splits_details/105.md) |
| 106 | 1 |  | and (exists (with_relation (find (cat), playing with, filter (trian... | [Details](splits_details/106.md) |
| 107 | 0.97 |  | gt (count (filter (white, filter (white, find (mouse)))), count (wi... | [Details](splits_details/107.md) |
| 108 | 1 | [](gpt3_experiments/108.md) | choose (query_attr [color] (with_relation (find (dog), looking at, ... | [Details](splits_details/108.md) |
| 109 | 0.99 |  | and (eq (count (filter (white, filter (white, find (animal)))), 4),... | [Details](splits_details/109.md) |
| 110 | 0.18 | [0.52](gpt3_experiments/110.md) | or (eq (count (find (animal)), count (with_relation (filter (round,... | [Details](splits_details/110.md) |
| 111 | 0.97 |  | or (lt (count (with_relation (filter (triangle, find (mouse)), play... | [Details](splits_details/111.md) |
| 112 | 1 |  | eq (count (with_relation (find (cat), chasing, find (dog))), 3)... | [Details](splits_details/112.md) |
| 113 | 1 |  | none (with_relation (filter (square, filter (square, find (animal))... | [Details](splits_details/113.md) |
| 114 | 1 |  | gt (count (with_relation (filter (white, find (animal)), chasing, f... | [Details](splits_details/114.md) |
| 115 | 0.28 | [0.19](gpt3_experiments/115.md) | or (all (with_relation (find (cat), chasing, with_relation (filter ... | [Details](splits_details/115.md) |
| 116 | 0.99 |  | and (lt (count (with_relation (filter (square, filter (square, find... | [Details](splits_details/116.md) |
| 117 | 1 |  | or (none (find (animal), filter (gray, scene ())), lt (count (with_... | [Details](splits_details/117.md) |
| 118 | 0.5 | [0.92](gpt3_experiments/118.md) | eq (count (with_relation (filter (black, filter (white, find (anima... | [Details](splits_details/118.md) |
| 119 | 0.98 |  | or (exists (with_relation (find (animal), looking at, find (cat))),... | [Details](splits_details/119.md) |
| 120 | 0.99 |  | and (lt (count (find (dog)), count (find (cat))), eq (query_attr [s... | [Details](splits_details/120.md) |
| 121 | 0.85 | [0.91](gpt3_experiments/121.md) | choose (count (with_relation (find (dog), playing with, with_relati... | [Details](splits_details/121.md) |
| 122 | 0.99 |  | and (some (with_relation (filter (brown, find (cat)), looking at, f... | [Details](splits_details/122.md) |
| 123 | 0.99 |  | or (eq (query_attr [shape] (with_relation (filter (round, find (ani... | [Details](splits_details/123.md) |
