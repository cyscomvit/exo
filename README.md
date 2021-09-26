<div align="center">
  <br />
  <p>
    <a href="https://pypi.org/project/exopassword/"><img src="https://i.imgur.com/JH1vZcV.png" width="500" alt="exopassword" /></a>
  </p>
  <br />
  <p>
    <a href="https://pypi.org/project/exopassword/"><img src="https://img.shields.io/pypi/v/exopassword?color=blue" alt="PyPi version" /></a>
    <a href="https://github.com/owaspvit/exo/actions"><img src="https://github.com/owaspvit/exo/actions/workflows/python-package.yml/badge.svg" alt="Python Package Test" /></a>
    <a href="https://pypi.org/project/exopassword/"><img src="https://img.shields.io/pypi/format/exopassword" alt="format" /></a>
    <a href="https://github.com/owaspvit/exo/blob/main/LICENSE"><img src="https://img.shields.io/github/license/owaspvit/exo?color=red" alt="LICENSE" /></a>
    <a href="https://pepy.tech/project/exopassword"><img src="https://pepy.tech/badge/exopassword" alt="Downloads" /></a>
    <a href="https://pepy.tech/project/exopassword"><img src="https://pepy.tech/badge/exopassword/week" alt="Downloads/week" /></a>
    <a href="https://github.com/owaspvit/exo/issues"><img src="https://camo.githubusercontent.com/f5054ffcd4245c10d3ec85ef059e07aacf787b560f83ad4aec2236364437d097/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174" alt="Contributions" /></a>
  </p>
</div>

## About

ExoPassword is a Password Strength Analyzing module that combines Machine Learning, rule-based scoring, and breach detection to provide detailed insight regarding your passwords.

- Supports password strength evaluation by 4 Machine Learning models
- Rule based password scoring
- Password breach status and breach count

## Installation

**Python3 is required.**  
Open `terminal` and execute:
```shell
pip install exopassword
```

## Development Installation
Open `terminal` and execute:
```shell
git clone https://github.com/owaspvit/exo.git
cd exo
pip install --editable .
```

### Other Requirements

- [Enzoic API Key](https://www.enzoic.com/free-trial-2/)

## Example Usage

```Python
from exo.exocore import ExoCore

API_KEY = "" #Enzoic API Key here
SECRET_KEY = "" #Enzoic Secret Key here
exo = ExoCore(API_KEY, SECRET_KEY)

result = exo.results("abc123@12")

print(result)
```

#### Output

```Python
{
 "password": "abc123@12",
 "score": 80,
 "DecisionTree": {
  "score": 1,
  "response": "Moderate"
 },
 "LogisticRegression": {
  "score": 1,
  "response": "Moderate"
 },
 "NaiveBayes": {
  "score": 1,
  "response": "Moderate"
 },
 "NeuralNetwork": {
  "score": 2,
  "response": "Strong"
 },
 "Breached": True,
 "BreachCount": 11
}
```

## Machine Learning Models Information

<table>
  <tr>
    <th>Model</th>
    <th>Training Accuracy</th>
    <th>Testing Accuracy</th>
  </tr>
  <tr>
    <td>Decision Tree</td>
    <td>0.981</td>
    <td>0.926</td>
  </tr>
  <tr>
    <td>Logistic Regression</td>
    <td>0.819</td>
    <td>0.818</td>
  </tr>
  <tr>
    <td>Naive Bayes</td>
    <td>0.812</td>
    <td>0.812</td>
  </tr>
  <tr>
    <td>Neural Network</td>
    <td>0.991</td>
    <td>0.989</td>
  </tr>
</table>

## Links

- [Dataset](https://github.com/apratimshukla6/ExoPassword/blob/master/data.csv)
- [Demo](https://exo.owaspvit.com)

## Contributing

Before creating an issue, please ensure that it hasn't already been reported/suggested.

The issue tracker is only for bug reports and enhancement suggestions. If you have a question, please ask it in the [Discord server](https://discord.gg/aMgWPApkyS) instead of opening an issue – you will get redirected there anyway.

If you wish to contribute to the ExoPassword codebase or documentation, feel free to fork the repository and submit a pull request.

## Help

If you don't understand something in the documentation, you are experiencing problems, or you just need a gentle
nudge in the right direction, please don't hesitate to join our [Discord Server](https://discord.gg/aMgWPApkyS).
