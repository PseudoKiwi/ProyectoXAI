# Representational comparison against Teacher $P_{avg}$ (IMDB)

Cosine similarity, Frobenius distance, Jensen–Shannon divergence, participation ratio, and
entropy-based effective rank between each model's attention map and the teacher's averaged
attention $P_{avg}$, across layers $i$. Source: `imdb/model_representational_comparisons.ipynb`
(cells 23-41, 67-68). Rollout-based comparisons and student-student comparisons are excluded.
For Teacher $P_{avg}$ itself, cosine/Frobenius/JS are not applicable (self-reference).

| Model | Layer $i$ | Cosine Similarity | Frobenius Distance | $D_{JS}$ | PR | ER |
|---|---|---|---|---|---|---|
| Teacher $P_{avg}$ | 0 | – | – | – | 3.2614 | 309.3200 |
| Teacher $P_{avg}$ | 1 | – | – | – | 1.0108 | 42.2246 |
| Teacher $P_{avg}$ | 2 | – | – | – | 1.0004 | 5.2036 |
| Teacher $P_{avg}$ | 3 | – | – | – | 1.0006 | 6.9923 |
| Teacher $P_{avg}$ | 4 | – | – | – | 1.0036 | 20.3665 |
| Teacher $P_{avg}$ | 5 | – | – | – | 1.0055 | 26.3498 |
| Teacher $P_{avg}$ | 6 | – | – | – | 1.0146 | 66.2817 |
| Teacher $P_{avg}$ | 7 | – | – | – | 1.0166 | 84.2087 |
| Teacher $P_{avg}$ | 8 | – | – | – | 1.0125 | 64.0569 |
| Teacher $P_{avg}$ | 9 | – | – | – | 1.0088 | 45.5237 |
| Teacher $P_{avg}$ | 10 | – | – | – | 1.0157 | 129.1486 |
| Baseline | 0 | 0.9330 | 1.2648 | 0.0113 | 2.5549 | 60.2092 |
| Baseline | 1 | 0.1735 | 19.1492 | 0.2123 | 5.0774 | 329.3674 |
| Baseline | 2 | 0.2869 | 36.2836 | 0.4274 | 3.3728 | 277.4744 |
| Baseline | 3 | 0.2283 | 39.1174 | 0.4926 | 2.9389 | 327.7114 |
| Baseline | 4 | 0.1538 | 26.4354 | 0.3781 | 4.9588 | 314.5093 |
| Baseline | 5 | 0.1816 | 22.5318 | 0.3530 | 5.5681 | 355.8278 |
| Baseline | 6 | 0.1659 | 18.1655 | 0.3508 | 7.3205 | 401.9564 |
| Baseline | 7 | 0.1328 | 18.0399 | 0.3685 | 13.7235 | 505.1129 |
| Baseline | 8 | 0.1421 | 19.6057 | 0.4292 | 11.5000 | 506.7776 |
| Baseline | 9 | 0.1561 | 20.3702 | 0.4189 | 8.9309 | 460.2339 |
| Baseline | 10 | 0.1350 | 21.3099 | 0.4103 | 9.6827 | 491.4134 |
| Bad Student | 0 | 0.9230 | 1.3557 | 0.0175 | 2.6227 | 116.9154 |
| Bad Student | 1 | 0.4703 | 17.8870 | 0.1494 | 2.1159 | 113.0881 |
| Bad Student | 2 | 0.4170 | 35.6589 | 0.3897 | 2.9802 | 298.3092 |
| Bad Student | 3 | 0.4325 | 38.2045 | 0.4376 | 3.3415 | 398.4451 |
| Bad Student | 4 | 0.3698 | 25.4998 | 0.3068 | 4.3946 | 437.0775 |
| Bad Student | 5 | 0.1938 | 22.4848 | 0.2957 | 17.1514 | 507.4962 |
| Bad Student | 6 | 0.2751 | 17.6709 | 0.2673 | 11.4469 | 497.0960 |
| Bad Student | 7 | 0.2604 | 17.3913 | 0.2703 | 13.4005 | 554.8601 |
| Bad Student | 8 | 0.1849 | 19.4096 | 0.3258 | 15.9452 | 521.6653 |
| Bad Student | 9 | 0.1498 | 20.4235 | 0.3417 | 11.6455 | 514.2999 |
| Bad Student | 10 | 0.2709 | 20.6607 | 0.3027 | 8.6083 | 508.4857 |
| Student | 0 | 0.9367 | 1.2356 | 0.0109 | 2.4500 | 95.6168 |
| Student | 1 | 0.6479 | 16.7155 | 0.1246 | 1.7020 | 101.7911 |
| Student | 2 | 0.4552 | 35.4357 | 0.3784 | 2.4488 | 229.5724 |
| Student | 3 | 0.5018 | 37.8417 | 0.4331 | 2.4829 | 303.6320 |
| Student | 4 | 0.4191 | 25.0765 | 0.2973 | 4.2740 | 516.8293 |
| Student | 5 | 0.3938 | 21.5096 | 0.2773 | 5.9007 | 469.7536 |
| Student | 6 | 0.2971 | 17.5652 | 0.2623 | 10.6305 | 486.0109 |
| Student | 7 | 0.4788 | 16.0823 | 0.2361 | 7.5018 | 505.2451 |
| Student | 8 | 0.3150 | 18.8159 | 0.3088 | 5.4860 | 431.2502 |
| Student | 9 | 0.1995 | 20.1939 | 0.3365 | 15.7668 | 549.1013 |
| Student | 10 | 0.2340 | 20.8501 | 0.3083 | 17.0195 | 550.5553 |
| Student Local | 0 | 0.9233 | 1.3529 | 0.0190 | 2.7344 | 107.2645 |
| Student Local | 1 | 0.3579 | 18.3989 | 0.1576 | 5.0372 | 399.0545 |
| Student Local | 2 | 0.6293 | 33.9489 | 0.3418 | 1.6490 | 179.7954 |
| Student Local | 3 | 0.6865 | 36.4605 | 0.3862 | 1.9987 | 360.5123 |
| Student Local | 4 | 0.6536 | 22.9474 | 0.2547 | 2.3916 | 484.5589 |
| Student Local | 5 | 0.3026 | 21.9667 | 0.2928 | 7.6533 | 489.4684 |
| Student Local | 6 | 0.3121 | 17.4682 | 0.2563 | 13.5697 | 514.5392 |
| Student Local | 7 | 0.3814 | 16.8076 | 0.2508 | 7.1345 | 488.0495 |
| Student Local | 8 | 0.1948 | 19.3582 | 0.3221 | 14.8760 | 501.1661 |
| Student Local | 9 | 0.2338 | 20.0093 | 0.3239 | 11.4031 | 551.3256 |
| Student Local | 10 | 0.1641 | 21.1837 | 0.3232 | 12.5393 | 527.9537 |
