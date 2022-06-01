| # | Bart-B (FT) | Bart-L (FT) | T5-B (FT) | T5-L (FT) | avg (FT) | GPT-3<br>(ICL) | 2-ULSs | Predicted Easiness |  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| [0](splits_details/0.md) | 0.99 | 1 | 0.99 | 1 | 1 |  |  | 1 | [Details](splits_details/0.md) |
| [1](splits_details/1.md) | 1 | 1 | 0.99 | 0.99 | 1 |  |  | 0.91 | [Details](splits_details/1.md) |
| [2](splits_details/2.md) | 1 | 1 | 1 | 1 | 1 | [0.62](gpt3_experiments/2.md) |  | 1 | [Details](splits_details/2.md) |
| [3](splits_details/3.md) | 0 | 0 | 0.87 | 0.86 | 0.43 | [0.42](gpt3_experiments/3.md) | and+eq<br> or+eq<br> | 0.09 | [Details](splits_details/3.md) |
| [4](splits_details/4.md) | 0.99 | 1 | 1 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/4.md) |
| [6](splits_details/6.md) | 1 | 1 | 0.99 | 1 | 1 |  |  | 1 | [Details](splits_details/6.md) |
| [7](splits_details/7.md) | 1 | 1 | 1 | 1 | 1 | [0.36](gpt3_experiments/7.md) |  | 1 | [Details](splits_details/7.md) |
| [8](splits_details/8.md) | 0.93 | 0.42 | 0 | 0.01 | 0.34 | [0.51](gpt3_experiments/8.md) | eq+triangle<br> eq+brown<br> eq+gray<br> eq+round<br> eq+query_attr[color]<br> eq+black<br> eq+white<br> eq+query_attr[shape]<br> eq+square<br> | 0.19 | [Details](splits_details/8.md) |
| [9](splits_details/9.md) | 1 | 1 | 0.99 | 1 | 1 |  |  | 1 | [Details](splits_details/9.md) |
| [10](splits_details/10.md) | 0.99 | 1 | 0.99 | 0.97 | 0.99 |  |  | 1 | [Details](splits_details/10.md) |
| [11](splits_details/11.md) | 1 | 1 | 0.26 | 0.93 | 0.8 | [0.47](gpt3_experiments/11.md) | query_attr[shape]+with_relation<br> query_attr[color]+with_relation<br> | 0.49 | [Details](splits_details/11.md) |
| [12](splits_details/12.md) | 0.99 | 0 | 0.99 | 0.99 | 0.74 |  |  | 1 | [Details](splits_details/12.md) |
| [13](splits_details/13.md) | 1 | 1 | 1 | 1 | 1 |  | and+lt<br> and+gt<br> | 0.91 | [Details](splits_details/13.md) |
| [14](splits_details/14.md) | 0.99 | 1 | 0.99 | 0.99 | 0.99 |  |  | 0.98 | [Details](splits_details/14.md) |
| [15](splits_details/15.md) | 0.39 | 0.35 | 0.51 | 0.37 | 0.41 | [0.65](gpt3_experiments/15.md) | choose+round<br> choose+white<br> \<s>+query_attr[color]<br> \<s>+query_attr[shape]<br> choose+query_attr[color]<br> choose+black<br> choose+gray<br> choose+triangle<br> choose+brown<br> choose+query_attr[shape]<br> choose+square<br> | 0.22 | [Details](splits_details/15.md) |
| [16](splits_details/16.md) | 1 | 1 | 0.97 | 0.97 | 0.98 |  |  | 0.99 | [Details](splits_details/16.md) |
| [17](splits_details/17.md) | 0.99 | 1 | 0.9 | 0.91 | 0.95 |  |  | 1 | [Details](splits_details/17.md) |
| [18](splits_details/18.md) | 0.99 | 1 | 0.99 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/18.md) |
| [19](splits_details/19.md) | 0.99 | 1 | 0.98 | 1 | 0.99 |  |  | 0.94 | [Details](splits_details/19.md) |
| [20](splits_details/20.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/20.md) |
| [21](splits_details/21.md) | 1 | 1 | 1 | 1 | 1 |  | and+exists<br> | 0.94 | [Details](splits_details/21.md) |
| [22](splits_details/22.md) | 0.99 | 0.99 | 0.99 | 0.97 | 0.99 |  |  | 1 | [Details](splits_details/22.md) |
| [23](splits_details/23.md) | 1 | 1 | 0.99 | 0.8 | 0.95 |  |  | 1 | [Details](splits_details/23.md) |
| [24](splits_details/24.md) | 0.53 | 1 | 1 | 1 | 0.88 | [0.88](gpt3_experiments/24.md) |  | 1 | [Details](splits_details/24.md) |
| [25](splits_details/25.md) | 0.56 | 0.73 | 0.56 | 0.52 | 0.59 | [0.23](gpt3_experiments/25.md) | and+some<br> none+filter<br> filter+scene<br> some+filter<br> most+filter<br> exists+filter<br> all+filter<br> | 0.74 | [Details](splits_details/25.md) |
| [26](splits_details/26.md) | 1 | 1 | 0.98 | 0.95 | 0.98 |  | count+with_relation<br> | 0.52 | [Details](splits_details/26.md) |
| [27](splits_details/27.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/27.md) |
| [28](splits_details/28.md) | 0.14 | 0.32 | 0.29 | 0.27 | 0.26 | [0.01](gpt3_experiments/28.md) | none+filter<br> and+most<br> filter+scene<br> some+filter<br> most+filter<br> or+most<br> all+filter<br> | 0.41 | [Details](splits_details/28.md) |
| [29](splits_details/29.md) | 1 | 0.99 | 0.99 | 0.98 | 0.99 |  |  | 1 | [Details](splits_details/29.md) |
| [30](splits_details/30.md) | 0.99 | 1 | 1 | 1 | 1 |  | or+exists<br> | 0.94 | [Details](splits_details/30.md) |
| [31](splits_details/31.md) | 0.61 | 0.61 | 0 | 0 | 0.3 | [0.81](gpt3_experiments/31.md) | choose+2<br> choose+count<br> \<s>+count<br> choose+3<br> choose+4<br> | 0.3 | [Details](splits_details/31.md) |
| [32](splits_details/32.md) | 1 | 1 | 1 | 0.99 | 1 |  |  | 1 | [Details](splits_details/32.md) |
| [33](splits_details/33.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/33.md) |
| [34](splits_details/34.md) | 0.39 | 0.41 | 0.28 | 0.33 | 0.35 | [0.38](gpt3_experiments/34.md) | all+with_relation<br> with_relation+scene<br> exists+with_relation<br> none+with_relation<br> most+with_relation<br> some+with_relation<br> | 0.55 | [Details](splits_details/34.md) |
| [35](splits_details/35.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/35.md) |
| [36](splits_details/36.md) | 1 | 1 | 0.95 | 0.97 | 0.98 |  |  | 1 | [Details](splits_details/36.md) |
| [37](splits_details/37.md) | 1 | 1 | 0.99 | 1 | 1 |  |  | 1 | [Details](splits_details/37.md) |
| [38](splits_details/38.md) | 1 | 1 | 0.99 | 0.99 | 1 |  | or+all<br> or+none<br> or+most<br> or+some<br> | 0.88 | [Details](splits_details/38.md) |
| [39](splits_details/39.md) | 0.99 | 0.99 | 0.98 | 0.97 | 0.98 |  |  | 1 | [Details](splits_details/39.md) |
| [40](splits_details/40.md) | 0.98 | 0.99 | 0.91 | 0.92 | 0.95 |  |  | 1 | [Details](splits_details/40.md) |
| [41](splits_details/41.md) | 1 | 1 | 0.99 | 0.99 | 1 |  | or+eq<br> | 0.94 | [Details](splits_details/41.md) |
| [42](splits_details/42.md) | 1 | 1 | 1 | 1 | 1 | [0.63](gpt3_experiments/42.md) | or+gt<br> or+lt<br> | 0.91 | [Details](splits_details/42.md) |
| [43](splits_details/43.md) | 0.03 | 0.01 | 0.4 | 0.35 | 0.2 | [0.11](gpt3_experiments/43.md) | and+some<br> and+most<br> or+all<br> and+all<br> or+none<br> and+none<br> or+most<br> or+some<br> | 0.26 | [Details](splits_details/43.md) |
| [44](splits_details/44.md) | 0.99 | 0.99 | 0.99 | 1 | 0.99 |  |  | 1 | [Details](splits_details/44.md) |
| [45](splits_details/45.md) | 0.28 | 0.28 | 0.95 | 0.92 | 0.61 | [0.61](gpt3_experiments/45.md) | and+lt<br> or+gt<br> and+gt<br> or+lt<br> | 0.77 | [Details](splits_details/45.md) |
| [46](splits_details/46.md) | 1 | 1 | 0.95 | 0.87 | 0.95 |  | exists+with_relation<br> | 0.91 | [Details](splits_details/46.md) |
| [47](splits_details/47.md) | 0.99 | 1 | 0.99 | 1 | 0.99 |  |  | 1 | [Details](splits_details/47.md) |
| [48](splits_details/48.md) | 0 | 0 | 0 | 0 | 0 | [0.85](gpt3_experiments/48.md) | \<s>+query_attr[shape]<br> \<s>+query_attr[color]<br> | 0.35 | [Details](splits_details/48.md) |
| [49](splits_details/49.md) | 1 | 1 | 0.99 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/49.md) |
| [50](splits_details/50.md) | 0.97 | 0.99 | 0.87 | 0.87 | 0.93 |  |  | 1 | [Details](splits_details/50.md) |
| [51](splits_details/51.md) | 0.64 | 0.76 | 0.57 | 0.58 | 0.64 | [0.35](gpt3_experiments/51.md) |  | 0.98 | [Details](splits_details/51.md) |
| [52](splits_details/52.md) | 1 | 0.99 | 0.99 | 0.98 | 0.99 |  |  | 1 | [Details](splits_details/52.md) |
| [53](splits_details/53.md) | 0.99 | 0.34 | 0.99 | 0.99 | 0.83 |  |  | 1 | [Details](splits_details/53.md) |
| [54](splits_details/54.md) | 1 | 1 | 0.99 | 0.98 | 0.99 |  |  | 1 | [Details](splits_details/54.md) |
| [55](splits_details/55.md) | 1 | 0.99 | 0.99 | 0.99 | 0.99 | [0.16](gpt3_experiments/55.md) | exists+filter<br> | 0.89 | [Details](splits_details/55.md) |
| [56](splits_details/56.md) | 0.99 | 0.99 | 1 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/56.md) |
| [57](splits_details/57.md) | 0.99 | 1 | 0.99 | 0.69 | 0.92 |  | eq+count<br> eq+3<br> eq+2<br> eq+4<br> | 0.59 | [Details](splits_details/57.md) |
| [58](splits_details/58.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/58.md) |
| [59](splits_details/59.md) | 1 | 1 | 0.99 | 1 | 1 |  |  | 1 | [Details](splits_details/59.md) |
| [60](splits_details/60.md) | 0.96 | 0.99 | 0.95 | 0.93 | 0.96 |  |  | 1 | [Details](splits_details/60.md) |
| [61](splits_details/61.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/61.md) |
| [62](splits_details/62.md) | 1 | 1 | 0.99 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/62.md) |
| [63](splits_details/63.md) | 1 | 1 | 1 | 1 | 1 |  |  | 0.91 | [Details](splits_details/63.md) |
| [64](splits_details/64.md) | 1 | 0.99 | 1 | 0.99 | 1 |  | eq+4<br> eq+2<br> eq+3<br> | 0.84 | [Details](splits_details/64.md) |
| [65](splits_details/65.md) | 0.98 | 0.99 | 0.91 | 0.89 | 0.94 |  |  | 0.99 | [Details](splits_details/65.md) |
| [66](splits_details/66.md) | 0.61 | 0.89 | 0.75 | 0.25 | 0.62 | [0.44](gpt3_experiments/66.md) | choose+round<br> choose+white<br> choose+query_attr[color]<br> choose+black<br> choose+gray<br> choose+triangle<br> choose+brown<br> choose+query_attr[shape]<br> choose+square<br> | 0.16 | [Details](splits_details/66.md) |
| [67](splits_details/67.md) | 1 | 1 | 0.98 | 0.97 | 0.98 |  |  | 1 | [Details](splits_details/67.md) |
| [68](splits_details/68.md) | 1 | 0 | 1 | 0.99 | 0.75 | [0.25](gpt3_experiments/68.md) |  | 1 | [Details](splits_details/68.md) |
| [69](splits_details/69.md) | 1 | 1 | 1 | 1 | 1 | [0.63](gpt3_experiments/69.md) |  | 0.96 | [Details](splits_details/69.md) |
| [70](splits_details/70.md) | 1 | 1 | 0.99 | 0.99 | 0.99 |  |  | 0.82 | [Details](splits_details/70.md) |
| [71](splits_details/71.md) | 1 | 0.99 | 0.99 | 1 | 0.99 |  |  | 1 | [Details](splits_details/71.md) |
| [72](splits_details/72.md) | 0.99 | 1 | 0.93 | 0.94 | 0.97 |  | query_attr[shape]+filter<br> query_attr[color]+filter<br> | 0.89 | [Details](splits_details/72.md) |
| [73](splits_details/73.md) | 0.99 | 1 | 0.92 | 0.93 | 0.96 |  |  | 1 | [Details](splits_details/73.md) |
| [74](splits_details/74.md) | 0.99 | 0.99 | 0.99 | 1 | 0.99 |  |  | 1 | [Details](splits_details/74.md) |
| [75](splits_details/75.md) | 1 | 1 | 0.98 | 0.98 | 0.99 |  |  | 1 | [Details](splits_details/75.md) |
| [76](splits_details/76.md) | 0 | 0.97 | 0.68 | 0.95 | 0.65 | [0.27](gpt3_experiments/76.md) | \<s>+some<br> \<s>+most<br> \<s>+none<br> \<s>+all<br> | 0.92 | [Details](splits_details/76.md) |
| [77](splits_details/77.md) | 0.99 | 1 | 0.99 | 0.99 | 0.99 |  | and+eq<br> | 0.94 | [Details](splits_details/77.md) |
| [78](splits_details/78.md) | 1 | 1 | 1 | 1 | 1 | [0.58](gpt3_experiments/78.md) |  | 1 | [Details](splits_details/78.md) |
| [79](splits_details/79.md) | 0.99 | 1 | 0.94 | 0.98 | 0.98 |  |  | 1 | [Details](splits_details/79.md) |
| [80](splits_details/80.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/80.md) |
| [81](splits_details/81.md) | 0.99 | 1 | 1 | 0.99 | 1 |  |  | 1 | [Details](splits_details/81.md) |
| [82](splits_details/82.md) | 0.99 | 0.99 | 1 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/82.md) |
| [83](splits_details/83.md) | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/83.md) |
| [84](splits_details/84.md) | 0.99 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/84.md) |
| [85](splits_details/85.md) | 1 | 1 | 0.99 | 0.98 | 0.99 |  |  | 1 | [Details](splits_details/85.md) |
| [86](splits_details/86.md) | 0.99 | 0.99 | 0.98 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/86.md) |
| [87](splits_details/87.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/87.md) |
| [88](splits_details/88.md) | 1 | 1 | 0.99 | 1 | 1 |  |  | 1 | [Details](splits_details/88.md) |
| [89](splits_details/89.md) | 0.31 | 0.31 | 1 | 1 | 0.65 | [0.85](gpt3_experiments/89.md) | \<s>+lt<br> \<s>+gt<br> | 1 | [Details](splits_details/89.md) |
| [90](splits_details/90.md) | 0 | 1 | 1 | 0.8 | 0.7 | [0.8](gpt3_experiments/90.md) | \<s>+exists<br> | 0.92 | [Details](splits_details/90.md) |
| [91](splits_details/91.md) | 1 | 0 | 0.99 | 1 | 0.75 | [0.83](gpt3_experiments/91.md) |  | 1 | [Details](splits_details/91.md) |
| [92](splits_details/92.md) | 0.62 | 0.85 | 0.62 | 0.67 | 0.69 | [0.35](gpt3_experiments/92.md) | and+some<br> | 0.92 | [Details](splits_details/92.md) |
| [93](splits_details/93.md) | 1 | 1 | 0.99 | 0.99 | 1 |  | count+filter<br> | 0.9 | [Details](splits_details/93.md) |
| [94](splits_details/94.md) | 1 | 1 | 1 | 0.99 | 1 |  |  | 0.94 | [Details](splits_details/94.md) |
| [95](splits_details/95.md) | 0.77 | 1 | 1 | 1 | 0.94 |  |  | 1 | [Details](splits_details/95.md) |
| [96](splits_details/96.md) | 1 | 1 | 1 | 0.99 | 1 |  |  | 1 | [Details](splits_details/96.md) |
| [97](splits_details/97.md) | 1 | 1 | 0.98 | 0.98 | 0.99 |  | eq+count<br> eq+3<br> eq+2<br> eq+4<br> | 0.26 | [Details](splits_details/97.md) |
| [98](splits_details/98.md) | 1 | 0 | 0.99 | 0.98 | 0.74 |  |  | 1 | [Details](splits_details/98.md) |
| [99](splits_details/99.md) | 0 | 0 | 0 | 0 | 0 | [0.89](gpt3_experiments/99.md) | \<s>+count<br> | 0.35 | [Details](splits_details/99.md) |
| [100](splits_details/100.md) | 0 | 0 | 0 | 0.08 | 0.02 | [0.18](gpt3_experiments/100.md) | and+exists<br> exists+find<br> or+exists<br> | 0.21 | [Details](splits_details/100.md) |
| [101](splits_details/101.md) | 1 | 1 | 0.99 | 0.99 | 1 |  |  | 1 | [Details](splits_details/101.md) |
| [102](splits_details/102.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/102.md) |
| [103](splits_details/103.md) | 1 | 1 | 0.99 | 0.99 | 0.99 |  |  | 1 | [Details](splits_details/103.md) |
| [104](splits_details/104.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/104.md) |
| [105](splits_details/105.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/105.md) |
| [106](splits_details/106.md) | 1 | 1 | 1 | 0.99 | 1 |  |  | 1 | [Details](splits_details/106.md) |
| [107](splits_details/107.md) | 0.92 | 1 | 1 | 0.98 | 0.97 |  |  | 1 | [Details](splits_details/107.md) |
| [108](splits_details/108.md) | 1 | 1 | 1 | 1 | 1 | [](gpt3_experiments/108.md) |  | 0.99 | [Details](splits_details/108.md) |
| [109](splits_details/109.md) | 1 | 1 | 0.99 | 1 | 0.99 |  |  | 1 | [Details](splits_details/109.md) |
| [110](splits_details/110.md) | 0.21 | 0.17 | 0.2 | 0.13 | 0.18 | [0.33](gpt3_experiments/110.md) | with_relation+filter<br> | 0.43 | [Details](splits_details/110.md) |
| [111](splits_details/111.md) | 0.99 | 1 | 0.97 | 0.92 | 0.97 |  |  | 1 | [Details](splits_details/111.md) |
| [112](splits_details/112.md) | 1 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/112.md) |
| [113](splits_details/113.md) | 1 | 1 | 0.99 | 1 | 1 |  |  | 1 | [Details](splits_details/113.md) |
| [114](splits_details/114.md) | 1 | 1 | 1 | 0.99 | 1 |  |  | 1 | [Details](splits_details/114.md) |
| [115](splits_details/115.md) | 0.32 | 0.38 | 0.19 | 0.2 | 0.28 | [0.05](gpt3_experiments/115.md) | all+with_relation<br> with_relation+scene<br> none+with_relation<br> most+with_relation<br> some+with_relation<br> | 0.25 | [Details](splits_details/115.md) |
| [116](splits_details/116.md) | 0.99 | 1 | 0.98 | 0.97 | 0.99 |  | and+some<br> and+all<br> | 0.97 | [Details](splits_details/116.md) |
| [117](splits_details/117.md) | 0.99 | 1 | 1 | 1 | 1 |  |  | 1 | [Details](splits_details/117.md) |
| [118](splits_details/118.md) | 0 | 0.02 | 1 | 1 | 0.5 | [0.92](gpt3_experiments/118.md) | \<s>+eq<br> | 0.74 | [Details](splits_details/118.md) |
| [119](splits_details/119.md) | 0.99 | 1 | 1 | 0.95 | 0.98 |  |  | 1 | [Details](splits_details/119.md) |
| [120](splits_details/120.md) | 0.99 | 0.99 | 0.99 | 1 | 0.99 |  |  | 1 | [Details](splits_details/120.md) |
| [121](splits_details/121.md) | 1 | 1 | 0.42 | 1 | 0.85 | [0.71](gpt3_experiments/121.md) | choose+2<br> choose+count<br> choose+3<br> choose+4<br> | 0.26 | [Details](splits_details/121.md) |
| [122](splits_details/122.md) | 1 | 0.99 | 0.99 | 0.99 | 0.99 |  | and+none<br> and+some<br> and+all<br> and+most<br> | 0.85 | [Details](splits_details/122.md) |
| [123](splits_details/123.md) | 0.99 | 0.99 | 0.99 | 1 | 0.99 |  |  | 1 | [Details](splits_details/123.md) |
