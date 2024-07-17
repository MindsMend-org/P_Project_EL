# No Coding Demo
https://colab.research.google.com/drive/1e9XPbAb0wBpAaOTWUsEdDjl1kN48mzOQ?usp=sharing


## P_Project_EL (WIP/TBC)  
run nda.py set to predict 2 numbers, the signal is so diluted with only a fraction of training. [I Truly Hope One Day] I will see this project to ABSOLUTE level.

## Binary Representation:
![BINREP](x_demo_results/binrep.gif)

## K-cluster:
![K-](x_demo_results/k-cluster.png)

## Interpreter [NotRF]:
![NRF](x_demo_results/interpreter.png)


## Overview
**Simple / Innovative Technology / AI / To Predict The Future.**

What this project opens up as a possibility, is truly staggering. Imagine being able to make accurate predictions of any future event at any temporal distance. The project explores the possibility of making predictions across various domains, including financial markets, lotteries, and real-time events like roulette spins. (WIP/TBC)

## Motivation
The motivation behind this project is to challenge the conventional understanding of time and events. It explores the idea that everything may already be determined, and our perception merely observes the unfolding of pre-existing events, akin to a needle tracing a record.

Impossible it would seem, but what if the real truth is everything is written? Could this be a possibility? Akashic Records, Remote Viewing, NDEs all show a glimmer. The glimmer leads to attention, and attention is ALL.

### The Dataset Challenge [Time & xPU-Power] 
These models have only seen 150,000 datasets from the min tot of 2,658,391,066 

a minimum of 2,658,391,066 datasets needed that is just 1 dataset per possibility! 

each dataset is 2 similar images one for input1 and one for input2

2 images size 13.2 KB = 13,532 bytes
```python
# Given data
num_combinations = 2_658_391_066
storage_per_combination_bytes = 13_532

# Calculate total storage in bytes
total_storage_bytes = num_combinations * storage_per_combination_bytes

# Convert bytes to gigabytes
total_storage_gb = total_storage_bytes / (1024 * 1024 * 1024)
total_storage_gb
```
Result
33502.79098852724
approximately 33,502.79 GB

1 TB = 1,024 GB
approximately 32.72 TB



## Description
This part of the project attempts to predict future UK lotteries using data generated before the event. The data will be added days before the event. (WIP/TBC)

## Current Progress
Predicting 5 numbers and getting 2/3 correct repeatedly shows a level of consistency that is remarkable, even with these under-trained models.

It is time to seek attention to this project to potentially verify this is a real effect/phenomenon.

- **Live Demonstration**: This project was demonstrated live on X.com (previously Twitter) from November to December 2023. @M0000000000004
- Follow me on X [https://www.x.com/@M0000000000004]
- **Published Predictions**: Predictions were published between 24 hours to 1 week prior to the lottery draw.
- **Data Storage**: Data is stored in the target date directory with the generation time as the timestamp.
- **UK Lottery Results**: All UK Lottery results take place after 19:30 (H:M) on SAT/WED.

The great thing about this project is it is real and you can run it on your system to verify before the event happens, making it impossible to cheat. I am hoping to generate a buzz around this as the implications are incomprehensible.

## Reports
- **Report Headers**: `creation_date`, `el_model`, `yp`, `indices`, `label`, `matching`, `result_date`
- **Sample Data**:
    ```
    creation_date                                           | el_model | yp | indices | label | matching | result_date
    [2][C][readings/Sat-16-09-2023/2023-09-16T16-2...]  | C        |    |         |       |         | Sat-16-09-2023
    [3][M][readings/Sat-16-09-2023/2023-09-16T17-3...]  | M        |    |         |       |         | Sat-16-09-2023
    [4][N][readings/Wed-20-09-2023/2023-09-17T15-2...]  | N        |    |         |       |         | Wed-20-09-2023
    [5][C][readings/Wed-20-09-2023/2023-09-17T15-5...]  | C        |    |         |       |         | Wed-20-09-2023
    [6][A][readings/Wed-20-09-2023/2023-09-17T18-3...]  | A        |    |         |       |         | Wed-20-09-2023
    ```

## Model Files
- **Model Size on Disk**:
    - `best_model.h5`  0.99 GB (1,073,491,968 bytes)
    - `model_architecture.json` 12.0 KB (12,288 bytes)
    - `model_weights.h5` 341 MB (357,842,944 bytes)

## Images from Model Analysis
- **Reports**:
    - `reports/report_history_14_Jul_2024_062216.csv`
    - `reports/report_history_14_Jul_2024_053258.csv`
    - `reports/report_history_14_Jul_2024_043109.csv`
    - `reports/predictions_vs_correct.png`
    - `reports/predictions_over_time.png`
    - `reports/model_prediction_percent.png`
    - `reports/model_performance.png`
    - `reports/full_lottery_percent.png`
    - `reports/combined_report_history.csv`

![Predictions vs Correct](reports/predictions_vs_correct.png)
![Predictions Over Time](reports/predictions_over_time.png)
![Model Prediction Percent](reports/model_prediction_percent.png)
![Model Performance](reports/model_performance.png)
![Full Lottery Percent](reports/full_lottery_percent.png)

## Getting up and running
### 2023-STUAX Duel Input Model download link in Models/Readme.md

You will need 
root/nda.py
root/cleaned_lottery_results.json
images from NDA_parties/images moved to root/images
model from download moved to root/model
run nda.py
python nda.py

you should see something like
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 
y_pred_pcent: 0.0014466688735410571 1.4173266235195443e-18 7.114081038273762e-19 9.143528245658672e-07 1.0 6.840401578500632e-10 2.273829693422158e-07 1.6250110371753263e-17 0.010102406144142151 1.3960114035246816e-28 7.039444027689967e-10 4.683914085035212e-06 7.894012554743313e-08 4.0204024998047316e-08 7.48965759610155e-15 1.3884098315486426e-08 1.4188431730921583e-23 5.4218870121323383e-17 1.5030423737225074e-12 1.3059840284768143e-06 1.2258847382980208e-15 1.8060672082394647e-16 1.6460673102347556e-10 0.999986469745636 0.3688414394855499 0.0016705705784261227 9.037857263635023e-18 4.1841832790141435e-17 8.234526749683737e-18 2.896977024046364e-14 1.320393039350165e-07 7.511463820850488e-29 1.578688824110941e-07 4.064017494114034e-15 1.81529125065083e-09 1.4135965731298938e-09 7.738433184413388e-16 2.145495491879569e-15 3.6037792194854035e-10 1.6338050556896633e-07 6.580886826071828e-17 0.0007704448071308434 3.7507696948324565e-10 1.407844197208512e-16 0.9910064935684204 2.212945145211891e-20 0.003965334966778755 4.849316562590073e-16 7.661354328725167e-10 1.1899898874346049e-18 8.304017196092417e-11 0.9999974370002747 0.04538793861865997 1.113329047008893e-12 4.114601838502918e-17 9.349862057543915e-14 7.318383676846452e-10 0.9999997019767761 
Predicted: [5, 24, 52, 58]
answers: 1, 8, 14, 20, 24, 40, 52
Matched: [24, 52]

### I will be updating on X.com

#### @M0000000000004

and here in /new u will be able to download the new images, place them in your root/images to predict the future UK Lotto using nda.py- yourself.

### ETA 
August, Id like to do the 2 draws every week from now to Xmas.

-

## License
This project is licensed under the MIT License for personal, educational, and non-commercial use. For commercial use, please contact Mince at mince@foldingcircles.co.uk to obtain a commercial license.

## Commercial License
Commercial use of this software requires a separate commercial license. To inquire about commercial licenses, please contact Mince at mince@foldingcircles.co.uk.

## Contributing
We welcome contributions from the community! By contributing to this project, you agree to license your contributions under the same terms as the project's open-source license and grant the original author a perpetual, worldwide, non-exclusive, royalty-free license to use, modify, distribute, and commercialize your contributions.
