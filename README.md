# Monolingual Pre-trained Language Models for Tigrinya

# CHANGE PAPER LINK
This repository contains resources for the paper ["Monolingual Pre-trained Language Models for Tigrinya"](http://mt.kaist.ac.kr/files/Fitsum_etal_2021_TigrinyaPLMs.pdf) that first appeared at the WiNLP workshop, EMNLP 2021.

We pre-train three monolingual language models for Tigrinya on a newly compiled corpus, and compare the performance the models with their multilingual counterparts on two downstream tasks – part-of-speech tagging and sentiment analysis – achieving significantly better results and establishing the state-of-the-art.


## Pre-trained Language Models

The transformer language models are published on the Huggingface Hub:

- [TiRoBERTa base](https://huggingface.co/fgaim/tiroberta-base), 125M parameters.
- [TiBERT base](https://huggingface.co/fgaim/tibert-base), 110M parameters.
- [TiELECTRA small](https://huggingface.co/fgaim/tielectra-small), 14M parameters.


## Downstream Task Models

We fine-tuned the above three models on two tasks.

#### Part-of-Speech Tagging

Models fine-tuned on the Nagaoka Tigrinya Corpus (NTC) (Tedla et al. 2016).

- [TiRoBERTa POS](https://huggingface.co/fgaim/tiroberta-pos)
<!-- - [TiBERT POS](https://huggingface.co/fgaim/tibert-pos) -->
- [TiELECTRA POS](https://huggingface.co/fgaim/tielectra-small-pos)

#### Sentiment Analysis

Models fine-tuned on a dataset for Tigrinya Sentiment Analysis (Tela et al. 2020).

- [TiRoBERTa Sentiment](https://huggingface.co/fgaim/tiroberta-sentiment)
<!-- - [TiBERT Sentiment](https://huggingface.co/fgaim/tibert-sentiment) -->
- [TiELECTRA Sentiment](https://huggingface.co/fgaim/tielectra-small-sentiment)


## Results

Evaluation results on the two downstream tasks.

| Model | POS | Sentiment | #Params |
|--------|--------|--------|--------|
| TiELECTRA | 93.12 | 82.29 | 14M |
| TiBERT | 92.89 | 82.06 | 110M |
| TiRoBERTa | **95.49** | **84.76** | **125M** |

Following the original papers, `accuracy` is used to report the POS performances, while `F1` is used for Sentiment Analysis.


## Predictions

The predictions of all models for both downstream tasks can be found in the `predictions` directory.
Check the `tasks` folder for training and evaluation data.


## Tigrinya Language Modeling Dataset (TLMD)

We compiled a new dataset for Tigrinya language modeling from various sources across the web including news, blogs, and books; with a total data size of ~0.5GB and over 40 million tokens. The data can be doownload from [here](https://zenodo.org/record/5139094).


## Citation

If you use the models or the TLMD dataset in your research, please cite as follows:

```bibtex
@article{Fitsum2021TiPLMs,
  author={Fitsum Gaim and Wonsuk Yang and Jong C. Park},
  title={Monolingual Pre-trained Language Models for Tigrinya},
  publisher={WiNLP @ EMNLP 2021},
  year={2021}
}
```

> We would like to thank the authors of the labeled downstream datasets for publicly sharing their work: Yemane Tedla (POS) and Abrhalei Tela (Sentiment Analysis). If you use these datasets, please cite their respective papers.


## References

```
Tedla, Y., Yamamoto, K. and Marasinghe, A. 2016.
Tigrinya Part-of-Speech Tagging with Morphological Patterns and the New Nagaoka Tigrinya Corpus.
International Journal Of Computer Applications 146 pp. 33-41 (2016).

Tela, A., Woubie, A. and Hautamäki, V. 2020.
Transferring Monolingual Model to Low-Resource Language: The Case of Tigrinya.
ArXiv, abs/2006.07698.
```
