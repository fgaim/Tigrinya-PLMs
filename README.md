# Monolingual Pre-trained Language Models for Tigrinya

This repository contains resources for the paper ["Monolingual Pre-trained Language Models for Tigrinya"](paper/Gaim_etal_2021_TigrinyaPLMs.pdf) that first appeared at the fifth WiNLP Workshop held in conjunction with EMNLP 2021 on November 11, 2021, in Punta Cana, Dominican Republic.

**Abstract**

> Pre-trained language models (PLMs) are driving much of the recent progress in natural language processing. However, due to the resource-intensive nature of the models, under-represented languages without sizable curated data have not seen significant progress. Multilingual PLMs have been introduced with the potential to generalize across many languages, but their performance trails compared to their monolingual counterparts and depends on the characteristics of the target language. In the case of the Tigrinya language, recent studies report a sub-optimal performance when applying the current multilingual models. This may be due to its writing system and unique linguistic characteristics, especially when compared to the Indo-European and other typologically distant languages that were used to train the models. In this work, we pre-train three monolingual PLMs for Tigrinya on a newly compiled corpus, and we compare the models with their multilingual counterparts on two downstream tasks, part-of-speech tagging and sentiment analysis, achieving significantly better results and establishing the state-of-the-art.

## Pre-trained Language Models

The transformer language models are published on the Huggingface Hub:

- [TiRoBERTa base](https://huggingface.co/fgaim/tiroberta-base), 125M parameters.
- [TiBERT base](https://huggingface.co/fgaim/tibert-base), 110M parameters.
- [TiELECTRA small](https://huggingface.co/fgaim/tielectra-small), 14M parameters.

## Downstream Task Models

We fine-tuned the above three models on two tasks.

### Part-of-Speech Tagging

Models fine-tuned on the Nagaoka Tigrinya Corpus (NTC) (Tedla et al. 2016).

- [TiRoBERTa POS](https://huggingface.co/fgaim/tiroberta-pos)
<!-- - [TiBERT POS](https://huggingface.co/fgaim/tibert-pos) -->
- [TiELECTRA POS](https://huggingface.co/fgaim/tielectra-small-pos)

### Sentiment Analysis

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

We compiled a new dataset for Tigrinya language modeling from various sources across the web including news, blogs, and books; with a total data size of ~0.5GB and over 40 million tokens. The data can be downloaded from [here](https://zenodo.org/record/5139094).

## Citation

If you use the models or the TLMD dataset in your research, please cite as follows:

```bibtex
@inproceedings{gaim-etal-2021-tiplms,
  title     = {{Monolingual Pre-trained Language Models for Tigrinya}},
  author    = {Fitsum Gaim and Wonsuk Yang and Jong C. Park},
  booktitle = {5th WiNLP workshop co-located with the 2021 Conference on Empirical Methods in Natural Language Processing ({EMNLP})},
  month     = {November},
  year      = {2021}
}
```

## References

We would like to thank the authors of the labeled downstream datasets for publicly sharing their work: Yemane Tedla (POS) and Abrhalei Tela (Sentiment Analysis). If you use these datasets, please cite their respective papers.

```text
Tedla, Y., Yamamoto, K. and Marasinghe, A. 2016.
Tigrinya Part-of-Speech Tagging with Morphological Patterns and the New Nagaoka Tigrinya Corpus.
International Journal Of Computer Applications 146 pp. 33-41 (2016).

Tela, A., Woubie, A. and Hautamäki, V. 2020.
Transferring Monolingual Model to Low-Resource Language: The Case of Tigrinya.
ArXiv, abs/2006.07698.
```
