from collections import Counter
from statistics import mean

import jsonlines
import numpy as np
from sklearn import metrics

from NewsSentiment.SentimentClasses import SentimentClasses
from NewsSentiment.dataset import FXDataset
from NewsSentiment.fxlogger import get_logger


class Evaluator:
    def __init__(self, sorted_expected_label_values, polarity_associations, snem_name):
        self.logger = get_logger()
        self.polarity_associations = polarity_associations
        self.pos_label_value = polarity_associations["positive"]
        self.neg_label_value = polarity_associations["negative"]
        self.sorted_expected_label_values = sorted_expected_label_values
        self.pos_label_index = self.sorted_expected_label_values.index(
            self.pos_label_value
        )
        self.neg_label_index = self.sorted_expected_label_values.index(
            self.neg_label_value
        )
        self.snem_name = snem_name

    def mean_from_all_statistics(self, all_test_stats):
        # for Counters, we do not take the mean
        mean_test_stats = {}
        number_stats = len(all_test_stats)

        for key in all_test_stats[0]:
            value_type = type(all_test_stats[0][key])

            if value_type in [float, np.float64, np.float32]:
                aggr_val = 0.0
                for test_stat in all_test_stats:
                    aggr_val += test_stat[key]

                mean_test_stats[key] = aggr_val / number_stats

            elif value_type == Counter:
                aggr_val = Counter()
                for test_stat in all_test_stats:
                    aggr_val += test_stat[key]
                mean_test_stats[key] = aggr_val

        return mean_test_stats

    def calc_statistics(self, y_true, y_pred):
        """
        Calculates performance statistics by comparing k-dimensional Tensors y_true and
        y_pred. Both y_true and y_pred's shape have to be(batchsize, maxtargetsperexample)
        :param y_true:
        :param y_pred:
        :return:
        """
        assert y_true.shape == y_pred.shape, "different shapes"
        assert y_true.shape[1] == FXDataset.NUM_MAX_TARGETS_PER_ITEM

        # for now, the following doesn't keep track of which prediction or true answer
        # belongs to which examples. for other measures, this might be necessary, though
        # in that case, the code would have to be changed, e.g., by keeping the original
        # dimensions. for now, we just unpack the Tensors to so that the former
        # evaluation logic will work on them. practically, this treats each non-fillup
        # target as an example
        y_true = y_true.view(-1)
        y_pred = y_pred.view(-1)

        # in both tensors, keep only those scalars that are non-fill in y_true
        non_fillup_mask = y_true != SentimentClasses.FILLUP_POLARITY_VALUE
        y_true = y_true[non_fillup_mask]
        y_pred = y_pred[non_fillup_mask]

        # this is just the previous, single-target evaluation logic
        y_true_list = y_true.tolist()
        y_pred_list = y_pred.tolist()
        y_true_count = Counter(y_true_list)
        y_pred_count = Counter(y_pred_list)

        f1_macro = metrics.f1_score(
            y_true, y_pred, labels=self.sorted_expected_label_values, average="macro"
        )
        f1_of_classes = metrics.f1_score(
            y_true, y_pred, labels=self.sorted_expected_label_values, average=None
        )
        f1_posneg = (
            f1_of_classes[self.pos_label_index] + f1_of_classes[self.neg_label_index]
        ) / 2.0
        confusion_matrix = metrics.confusion_matrix(
            y_true, y_pred, labels=self.sorted_expected_label_values
        )
        recalls_of_classes = metrics.recall_score(
            y_true, y_pred, labels=self.sorted_expected_label_values, average=None
        )
        recall_avg = mean(recalls_of_classes)
        recall_macro = metrics.recall_score(
            y_true, y_pred, labels=self.sorted_expected_label_values, average="macro"
        )
        precision_macro = metrics.precision_score(
            y_true, y_pred, labels=self.sorted_expected_label_values, average="macro"
        )
        accuracy = metrics.accuracy_score(y_true, y_pred)

        return {
            "f1_macro": f1_macro,
            "confusion_matrix": confusion_matrix,
            "recalls_of_classes": recalls_of_classes,
            "recall_avg": recall_avg,
            "recall_macro": recall_macro,
            "precision_macro": precision_macro,
            "accuracy": accuracy,
            "f1_posneg": f1_posneg,
            "y_true_count": y_true_count,
            "y_pred_count": y_pred_count,
        }

    def print_stats(self, stats, description):
        self.logger.info(description)
        self.logger.info("{}: {})".format(self.snem_name, stats[self.snem_name]))
        self.logger.info(
            "y_true distribution: {}".format(sorted(stats["y_true_count"].items()))
        )
        self.logger.info(
            "y_pred distribution: {}".format(sorted(stats["y_pred_count"].items()))
        )
        self.logger.info(
            "> recall_avg: {:.4f}, f1_posneg: {:.4f}, acc: {:.4f}, f1_macro: {:.4f}".format(
                stats["recall_avg"],
                stats["f1_posneg"],
                stats["accuracy"],
                stats["f1_macro"],
            )
        )

    def write_error_table(self, y_true, y_pred, texts_list, filepath):
        y_true_list = y_true.tolist()
        y_pred_list = y_pred.tolist()

        with jsonlines.open(filepath, "w") as writer:
            for true_label, pred_label, text in zip(
                y_true_list, y_pred_list, texts_list
            ):
                writer.write(
                    {"true_label": true_label, "pred_label": pred_label, "text": text}
                )
