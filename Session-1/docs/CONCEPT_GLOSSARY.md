<p align="center">
  <img src="../assets/ormedian_logo.png" alt="Ormedian" width="300" />
</p>

# Week 1 concept glossary

The definitions below are deliberately practical. The learner should be able to attach each term to a line of code or a step in the project.

## Artificial intelligence

A broad field concerned with systems that perform tasks associated with reasoning, perception, language, planning or decision-making. Not every AI system learns from data; some use explicit rules, search or optimisation.

## Machine learning

A way of creating behaviour by learning patterns from examples or experience rather than specifying every decision rule directly.

In this project, the model learns associations between message text and intent labels.

## Deep learning

A subfield of machine learning based on neural networks with several layers. Deep learning is especially powerful for images, speech and language, but it is not automatically the best first solution to every problem.

## Generative AI

Models that create new outputs such as text, code, images, audio or video. Many modern generative systems use deep learning. Classification, which predicts a fixed category, is different from generation.

## Supervised learning

Learning from examples that include correct answers. Each support message in this dataset has an intent label.

## Unsupervised learning

Finding structure in data without supplied labels. Examples include clustering similar messages or finding lower-dimensional representations.

## Reinforcement learning

Learning behaviour through interaction, reward and penalty. An agent chooses actions and receives feedback over time. It is not used in Session 1.

## Example or observation

One case in a dataset. Here, one row containing a support message and its label.

## Feature

Information supplied to the model as input. The primary feature here is the message text after TF-IDF conversion.

A feature should be available when a real prediction is made.

## Label or target

The correct answer the model is trained to predict. Here, one of six intent names.

## Prediction

The model's answer for a new input. A prediction may be correct or incorrect and may be accompanied by a score or probability.

## Parameter

A value learned by the model during training. Logistic regression learns weights for text features and classes.

## Hyperparameter

A setting chosen by the engineer rather than learned directly. Examples include `ngram_range`, regularisation strength and random seed.

## Classification

Predicting a category, such as `technical_support` or `refund_request`.

## Regression

Predicting a number, such as delivery time, temperature or price.

## Training

The process of fitting model parameters using the training examples.

## Training set

Examples used to fit the model. Performance on this set does not provide an honest measure of future behaviour because the model has already seen it.

## Validation set

Held-out examples used to compare model choices during development. It guides decisions such as unigram versus bigram features.

## Test set

Examples reserved for the final, honest evaluation. It should not be consulted repeatedly while tuning the model.

## Generalisation

The ability to perform well on relevant examples that were not used for training.

## Baseline

A simple reference strategy. The majority baseline predicts the most frequent training label for every input. A more complex model should justify itself by improving on a credible baseline.

## TF-IDF

Term frequency-inverse document frequency. It converts text into numerical features. Terms that are distinctive within a document receive more influence than terms that occur across many documents.

## Sparse matrix

A numerical matrix in which most entries are zero. Text vocabularies can contain many terms, while each short message uses only a few of them, so sparse storage is efficient.

## Logistic regression

A linear classification algorithm that learns feature weights for one or more classes. Despite the word "regression" in its name, it is widely used for classification.

## Loss function

A mathematical training signal that measures how wrong model outputs are. The optimisation procedure tries to reduce loss.

## Metric

A quantity used to judge performance in terms meaningful to the task. Accuracy, precision, recall and F1 are evaluation metrics.

## Accuracy

The proportion of predictions that are correct:

```text
correct predictions / all predictions
```

Accuracy can be misleading when one class is much more common than the others.

## True positive

A positive case that the model correctly predicts as positive.

## False positive

A negative case incorrectly predicted as positive. This is a false alarm.

## False negative

A positive case incorrectly predicted as negative. This is a missed case.

## True negative

A negative case correctly predicted as negative.

For multi-class classification, these ideas are calculated one class at a time.

## Precision

Of all examples predicted as a particular class, the proportion that truly belongs to that class.

High precision means fewer false alarms.

## Recall

Of all examples that truly belong to a class, the proportion the model correctly finds.

High recall means fewer missed cases.

## F1 score

The harmonic mean of precision and recall. It is high only when both are reasonably high.

## Macro F1

Calculate F1 separately for every class, then take the unweighted mean. Each class contributes equally, even if some classes are rare.

## Weighted F1

Calculate F1 per class, then average using class frequency. Common classes contribute more to the result.

## Confusion matrix

A table comparing true labels with predicted labels. The diagonal shows correct predictions; off-diagonal cells show specific confusions.

## Underfitting

The model is too limited to capture useful patterns. Training and validation performance are both poor.

## Overfitting

The model fits training examples very closely but performs worse on unseen examples. It has learned details that do not generalise.

## Data leakage

Information unavailable at real prediction time enters training or evaluation. Examples include using a label-derived field, fitting preprocessing on all data before splitting, or placing duplicates in train and test.

Leakage makes metrics look better than real-world performance.

## Class imbalance

Some labels appear far more often than others. A model can obtain high accuracy by favouring common classes while failing on rare but important classes.

## Error analysis

Reading and grouping wrong predictions to understand failure patterns. Error analysis can reveal ambiguous labels, missing data coverage, weak features or an ill-defined task.

## Reproducibility

The ability to rerun an experiment with the same code, data, configuration and split and obtain the same or appropriately similar result.

## Random seed

A fixed value used to make pseudo-random operations repeatable. A seed improves reproducibility but does not guarantee correctness.

## Artefact

A file produced by a run, such as a saved model, metrics JSON, predictions CSV or confusion-matrix image.

## Model card

A short document describing a model's purpose, data, evaluation, limitations and responsible-use considerations.
