import os
from tabulate import tabulate
from sklearn.metrics import accuracy_score, precision_recall_fscore_support as prfs
import warnings
warnings.simplefilter("ignore")


MODELS = (
    'mbert',
    'mbert-sera',
    'xlmr',
    'xlmr-sera',
    'tielectra',
    'tibert',
    'tiroberta'
)


def eval_pos():
    """Evaluate Part-of-Speech tagging predictions"""
    testpath = 'pos/ground_truth.txt'
    y_true = [line.split() for line in open(testpath).read().splitlines()]

    def trim_lol(ytrue, ypred):
        """Truncate truth sequences to match the max-length of predictions"""
        return [t[:len(p)] for t, p in zip(ytrue, ypred)]

    def flatten(sequences):
        """Flatten a list of sequences"""
        return [e for l in sequences for e in l]

    model_scores = list()
    for model in MODELS:
        predpath = os.path.join('pos', f'{model}_preds.txt')
        if not os.path.exists(predpath):
            print(f'Predictions for {model} not found!')
            continue
        y_pred = [line.split() for line in open(predpath).read().splitlines()]
        _y_true = flatten(trim_lol(y_true, y_pred))
        _y_pred = flatten(y_pred)

        acc = accuracy_score(_y_true, _y_pred)
        precision, recall, f1, _ = prfs(_y_true, _y_pred, average="weighted")
        model_scores.append({"model": model, "accuracy": acc,
                             "f1": f1, "precision": precision, "recall": recall})
    headers = ["Model", "Precision", "Recall", "F1", "♤Accuracy"]
    print('Part-of-Speech Tagging'.center(50))
    print(tablulate_results(model_scores, headers))
    return model_scores


def eval_sentiment():
    """Evaluate Sentiment Analysis Predictions"""
    testpath = 'sentiment/ground_truth.txt'
    y_true = [int(lbl) for lbl in open(testpath).read().splitlines()]

    model_scores = list()
    for model in MODELS:
        predpath = os.path.join('sentiment', f'{model}_preds.txt')
        if not os.path.exists(predpath):
            print(f'Predictions for {model} not found!')
            continue
        y_pred = [int(lbl) for lbl in open(predpath).read().splitlines()]
        acc = accuracy_score(y_true, y_pred)
        precision, recall, f1, _ = prfs(y_true, y_pred, average="binary")
        model_scores.append({"model": model, "accuracy": acc, "f1": f1,
                             "precision": precision, "recall": recall})
    headers = ["Model", "Precision", "Recall", "♤F1", "Accuracy"]
    print('Sentiment Analysis'.center(50))
    print(tablulate_results(model_scores, headers))
    return model_scores


def fmt(val):
    return f"{round(val*100, 2):.02f}"


def tablulate_results(model_scores, headers):
    cells = list()
    for row in model_scores:
        cells.append(
            [row['model'],
             fmt(row['precision']), fmt(row['recall']), fmt(row['f1']),
             fmt(row['accuracy'])]
        )
    return tabulate(cells, headers=headers)


if __name__ == '__main__':
    eval_pos()
    print()
    eval_sentiment()
    print()
    print("♤ indicats the metric reported on thes paper.")
