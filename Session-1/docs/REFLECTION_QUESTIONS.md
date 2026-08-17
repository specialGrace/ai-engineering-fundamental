# Week 1 reflection questions

Answer in your own words. Use a small example whenever possible.

## Core questions

1. What is the difference between artificial intelligence, machine learning and deep learning?
The difference between AI, ml and dl is that AI is the unbrella i.e the big idea, ML is one method to build AI, deep learning is one advanced type of ML
2. How does traditional rule-based programming differ from supervised machine learning?
In traditional rule based programming we write exact rules ourself (if the message contains “refund” then label = refund).
In supervised machine learning we show the computer many examples with the correct answers and it learns the patterns by itself.
3. In the support-intent dataset, what are the example, feature, label and prediction?
Example = one full row 
Feature = the text of the message
Label = the correct intent (refund, billing, etc.)
Prediction = what the model guesses the intent is
4. Why is this task classification rather than regression?
Classification chooses one category from a fixed list (refund, technical_issu).
Regression predicts a number (like price or temperature of the weather).
Here we need a category, not a number.
5. Why is it supervised learning?
It is supervised because its been provided labels 
6. Why should test data not be used during training or daily tuning?
If we use the test data while building the model, the model can “cheat” and the final score will look better than it really is in which called leakage and that is why the test set must stay hidden until the very end.
7. What is the role of the validation set?
WE use vaidation set to judge how well the model has performed during training
8. What is a baseline, and why did we build one before logistic regression?
A baseline is a very simple model, it always guesses the most common class.
We build it first so we have a minimum score to beat. If our real model cannot beat the baseline, it is useless.
9. What does TF-IDF do to the text?
It converts text to numerical features
10. Why is logistic regression able to classify text after TF-IDF?
After TF-IDF the text becomes a list of numbers. Logistic regression can learn which numbers (words) point to which intent label.
11. Why can accuracy be misleading?
Accuracy can be misleading because it only shows the overall number of correct prediction, it doesn't show whether the model is making good predictions for less common but important cases.
12. Explain precision using a support-ticket example.
Precision = when the model says “this is a refund”, how often is it really a refund.
High precision means support agents do not waste time on wrong tickets. so precision is the percentage of which is right and which is wrong.
13. Explain recall using a support-ticket example.
Recall = of all the real refund messages, how many did the model find.
High recall means almost no refund customer is sent to the wrong team.
14. Why might macro F1 be useful when class frequencies differ?
Macro F1 gives equal importance to every class, even the rare ones and accuracy can hide bad performance on small classes.
15. How do you read the diagonal and off-diagonal cells of a confusion matrix?
Diagonal = correct predictions (true label = predicted label)
Off-diagonal = mistakes (true label was A but model predicted B)
16. What does underfitting look like in training and validation results?
Both training and validation scores are low. The model is too simple and did not learn the patterns well.
17. What does overfitting look like?
Training score is very high but validation score is much lower. The model memorised the training data instead of learning general rules.
18. What is data leakage? Give two examples.
Data leakage is when the model sees information it should not have in real life.
Examples: 
Using the true label as a feature
The same message appearing in both train and test sets
19. What should an error analysis contain?
The actual wrong messages
True label vs predicted label
Possible reason for the mistake
Idea how to improve (more data, better features, etc.)
20. Why should an experiment change one main variable at a time?
it should change one variable at a time so we know exactly what caused the change in the score. If we change many things at once, we cannot tell which change helped or hurt.

## Applied questions

21. A model gets 95% accuracy on data with 95 normal messages and 5 urgent messages, but it misses every urgent message. Is it useful? Explain.
No, it is not useful. It ignores all the urgent messages. In real support work, missing urgent tickets is dangerous.
22. A column called `final_queue` was assigned by a human after reading each ticket. Why might it be a dangerous training feature?
Because final_queue was decided by a human after reading the ticket. In real life a new ticket does not have this information yet, so the model cannot use it.
23. The same message appears in both the training and test sets. What is wrong with the evaluation?
The evaluation is too optimistic. The model has already seen that message during training, so the test score is not honest.
24. Training macro F1 is 0.99 and validation macro F1 is 0.55. What is one likely explanation?
The model is overfitting. It memorised the training data but cannot generalise to new data.
25. Both training and validation macro F1 are 0.30. What might this suggest?
The model is underfitting. It did not learn useful patterns.
26. A bigram experiment lowers validation macro F1 by 0.02. Was the experiment a failure? Explain.
Not necessarily a failure. A small drop of 0.02 on a small validation set can be noise. We should check if the difference is consistent or try again with more data.
27. Which mistake is more costly for the imagined support workflow: a false technical-support alert or a missed technical-support message? What information would you need to decide?
A missed technical-support message is usually more costly (customer is stuck with a real problem). To decide properly we need to know the real business cost of each type of mistake.
28. A message says, "Cancel the order and refund the charge." Why is a single-label dataset limited for this case?
The message has two intents at the same time (cancel + refund). A single label dataset forces us to choose only one label, so information is lost.
29. What new data would you collect after seeing repeated confusion between `refund_request` and `invoice_status`?
More real messages that contain both refund language and invoice language, so the model can learn the difference better.
30. What evidence would you require before deploying this classifier to route real support messages automatically?
Good test performance on real (not synthetic) data
Error analysis showing the remaining mistakes are acceptable
Agreement from the support team on the cost of mistakes
A plan for monitoring the model after it goes live
## Personal reflection

31. What concept was easiest to understand?
the difference between feature and label
32. What concept remains unclear?
how the messages get to the support team
33. Which error taught you the most?

34. What did you initially believe about AI that changed during this session?
I thought AI was magic, now I see it just learns patterns from data
35. What will you do differently in the next experiment?
I will look at the errors more carefully before changing the model