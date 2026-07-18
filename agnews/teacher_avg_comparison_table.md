# Representational comparison against Teacher $P_{avg}$ (AG News)

Cosine similarity, Frobenius distance, Jensen–Shannon divergence, participation ratio, and
entropy-based effective rank between each model's attention map and the teacher's averaged
attention $P_{avg}$, across layers $i$. Source: `agnews/model_representational_comparisons.ipynb`
(cells 21-39, 65-66). Pure Student (S3) rows are sourced from
`agnews/pure_s_representational_comparisons.ipynb` (cells 22-26). Rollout-based comparisons and
student-student comparisons are excluded. For Teacher $P_{avg}$ itself, cosine/Frobenius/JS are
not applicable (self-reference).

| Model | Layer $i$ | Cosine Similarity | Frobenius Distance | $D_{JS}$ | PR | ER |
|---|---|---|---|---|---|---|
| Teacher $P_{avg}$ | 0 | – | – | – | 1.3684 | 23.9915 |
| Teacher $P_{avg}$ | 1 | – | – | – | 1.0057 | 4.3148 |
| Teacher $P_{avg}$ | 2 | – | – | – | 1.0001 | 1.3737 |
| Teacher $P_{avg}$ | 3 | – | – | – | 1.0002 | 1.6388 |
| Teacher $P_{avg}$ | 4 | – | – | – | 1.0061 | 2.8218 |
| Teacher $P_{avg}$ | 5 | – | – | – | 1.0032 | 2.7772 |
| Teacher $P_{avg}$ | 6 | – | – | – | 1.0068 | 4.3390 |
| Teacher $P_{avg}$ | 7 | – | – | – | 1.0085 | 5.0505 |
| Teacher $P_{avg}$ | 8 | – | – | – | 1.0084 | 4.5117 |
| Teacher $P_{avg}$ | 9 | – | – | – | 1.0080 | 3.7821 |
| Teacher $P_{avg}$ | 10 | – | – | – | 1.0074 | 6.4643 |
| Baseline | 0 | 0.9809 | 1.0771 | 0.0051 | 1.2853 | 12.7342 |
| Baseline | 1 | 0.3683 | 19.9431 | 0.1724 | 1.6138 | 32.6731 |
| Baseline | 2 | 0.4252 | 39.2226 | 0.4495 | 1.6046 | 29.0413 |
| Baseline | 3 | 0.4354 | 37.7779 | 0.4159 | 1.8960 | 39.9879 |
| Baseline | 4 | 0.5175 | 21.4166 | 0.2499 | 1.8527 | 42.4396 |
| Baseline | 5 | 0.3318 | 21.2386 | 0.2960 | 2.6647 | 52.1225 |
| Baseline | 6 | 0.2992 | 18.2787 | 0.2725 | 2.4010 | 58.8791 |
| Baseline | 7 | 0.2722 | 18.0496 | 0.3123 | 3.3806 | 61.7950 |
| Baseline | 8 | 0.4182 | 17.3306 | 0.2844 | 2.5965 | 61.5513 |
| Baseline | 9 | 0.2517 | 19.0009 | 0.3413 | 4.3214 | 61.5604 |
| Baseline | 10 | 0.3111 | 19.3262 | 0.3002 | 3.2535 | 66.3146 |
| Bad Student | 0 | 0.9648 | 1.4618 | 0.0066 | 1.3028 | 13.9221 |
| Bad Student | 1 | 0.6935 | 17.2232 | 0.1075 | 1.3200 | 14.8970 |
| Bad Student | 2 | 0.3180 | 40.1567 | 0.4789 | 1.4353 | 13.5215 |
| Bad Student | 3 | 0.3881 | 38.5100 | 0.4313 | 1.3701 | 18.9595 |
| Bad Student | 4 | 0.3454 | 22.9589 | 0.2303 | 1.3707 | 19.9379 |
| Bad Student | 5 | 0.3981 | 20.9162 | 0.2270 | 1.4088 | 23.8049 |
| Bad Student | 6 | 0.3415 | 18.0080 | 0.2188 | 1.4703 | 31.1215 |
| Bad Student | 7 | 0.3428 | 17.5153 | 0.2292 | 1.5345 | 31.8107 |
| Bad Student | 8 | 0.2777 | 18.3096 | 0.2612 | 1.4802 | 30.7218 |
| Bad Student | 9 | 0.3962 | 17.9335 | 0.2443 | 1.4458 | 30.2790 |
| Bad Student | 10 | 0.2778 | 19.5172 | 0.2373 | 1.5565 | 27.8402 |
| Student | 0 | 0.9679 | 1.3891 | 0.0057 | 1.3687 | 15.8043 |
| Student | 1 | 0.3014 | 20.3883 | 0.1766 | 1.5915 | 23.8379 |
| Student | 2 | 0.2305 | 40.6441 | 0.5027 | 1.7232 | 30.9630 |
| Student | 3 | 0.2217 | 39.4793 | 0.4742 | 1.9060 | 31.5937 |
| Student | 4 | 0.2904 | 23.2627 | 0.2263 | 1.7582 | 46.6758 |
| Student | 5 | 0.2800 | 21.6180 | 0.2306 | 1.8667 | 49.9781 |
| Student | 6 | 0.3367 | 18.0257 | 0.2068 | 1.8724 | 51.0656 |
| Student | 7 | 0.3333 | 17.5710 | 0.2214 | 1.7841 | 46.5666 |
| Student | 8 | 0.2723 | 18.3381 | 0.2502 | 1.7318 | 44.4572 |
| Student | 9 | 0.3168 | 18.4177 | 0.2513 | 1.7725 | 44.9762 |
| Student | 10 | 0.2262 | 19.8217 | 0.2597 | 1.7335 | 39.9030 |
| Student Local | 0 | 0.9748 | 1.2184 | 0.0062 | 1.3634 | 17.7493 |
| Student Local | 1 | 0.3689 | 19.9509 | 0.1694 | 1.5816 | 24.5985 |
| Student Local | 2 | 0.3674 | 39.6411 | 0.4675 | 2.0111 | 39.1457 |
| Student Local | 3 | 0.2284 | 39.4505 | 0.4657 | 2.0625 | 51.3232 |
| Student Local | 4 | 0.3445 | 22.9105 | 0.2212 | 1.8815 | 54.5964 |
| Student Local | 5 | 0.2970 | 21.5041 | 0.2412 | 1.8840 | 55.8362 |
| Student Local | 6 | 0.2977 | 18.2689 | 0.2201 | 2.0158 | 57.6873 |
| Student Local | 7 | 0.2775 | 17.9090 | 0.2486 | 1.6417 | 47.3015 |
| Student Local | 8 | 0.3127 | 18.0979 | 0.2427 | 1.5854 | 40.2886 |
| Student Local | 9 | 0.2929 | 18.5798 | 0.2603 | 1.9755 | 51.9470 |
| Student Local | 10 | 0.2640 | 19.6215 | 0.2528 | 1.7652 | 42.6021 |
| Pure Student | 0 | 0.9654 | 1.4653 | 0.0099 | 1.3602 | 16.7108 |
| Pure Student | 1 | 0.7895 | 15.9952 | 0.0874 | 1.2391 | 13.1758 |
| Pure Student | 2 | 0.7540 | 28.2156 | 0.2248 | 1.1410 | 7.3812 |
| Pure Student | 3 | 0.7656 | 32.7230 | 0.2982 | 1.1839 | 12.1525 |
| Pure Student | 4 | 0.6373 | 17.5895 | 0.1389 | 1.2812 | 20.6470 |
| Pure Student | 5 | 0.6795 | 17.7023 | 0.1806 | 1.3476 | 25.9201 |
| Pure Student | 6 | 0.5321 | 15.9558 | 0.1768 | 1.5875 | 34.1161 |
| Pure Student | 7 | 0.5364 | 15.7315 | 0.2016 | 1.7431 | 42.6126 |
| Pure Student | 8 | 0.6566 | 15.8977 | 0.1933 | 1.4694 | 36.6744 |
| Pure Student | 9 | 0.5440 | 17.0116 | 0.2190 | 1.6544 | 35.6647 |
| Pure Student | 10 | 0.5036 | 18.1459 | 0.2170 | 1.8504 | 41.3742 |
