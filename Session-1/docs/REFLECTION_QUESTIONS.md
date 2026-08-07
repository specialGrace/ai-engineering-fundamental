# Week 1 reflection questions

Answer in your own words. Use a small example whenever possible.

## Core questions

1. What is the difference between artificial intelligence, machine learning and deep learning?
The difference between AI, ml and dl is that AI is the big idea, ML is one method to build AI, deep learning is one advanced type of ML
2. How does traditional rule-based programming differ from supervised machine learning?
3. In the support-intent dataset, what are the example, feature, label and prediction?
4. Why is this task classification rather than regression?
5. Why is it supervised learning?
6. Why should test data not be used during training or daily tuning?
7. What is the role of the validation set?
8. What is a baseline, and why did we build one before logistic regression?
9. What does TF-IDF do to the text?
   It convert text to numerical features
10. Why is logistic regression able to classify text after TF-IDF?
11. Why can accuracy be misleading?
12. Explain precision using a support-ticket example.
13. Explain recall using a support-ticket example.
14. Why might macro F1 be useful when class frequencies differ?
15. How do you read the diagonal and off-diagonal cells of a confusion matrix?
16. What does underfitting look like in training and validation results?
17. What does overfitting look like?
18. What is data leakage? Give two examples.
19. What should an error analysis contain?
20. Why should an experiment change one main variable at a time?

## Applied questions

21. A model gets 95% accuracy on data with 95 normal messages and 5 urgent messages, but it misses every urgent message. Is it useful? Explain.
22. A column called `final_queue` was assigned by a human after reading each ticket. Why might it be a dangerous training feature?
23. The same message appears in both the training and test sets. What is wrong with the evaluation?
24. Training macro F1 is 0.99 and validation macro F1 is 0.55. What is one likely explanation?
25. Both training and validation macro F1 are 0.30. What might this suggest?
26. A bigram experiment lowers validation macro F1 by 0.02. Was the experiment a failure? Explain.
27. Which mistake is more costly for the imagined support workflow: a false technical-support alert or a missed technical-support message? What information would you need to decide?
28. A message says, "Cancel the order and refund the charge." Why is a single-label dataset limited for this case?
29. What new data would you collect after seeing repeated confusion between `refund_request` and `invoice_status`?
30. What evidence would you require before deploying this classifier to route real support messages automatically?

## Personal reflection

31. What concept was easiest to understand?
32. What concept remains unclear?
33. Which error taught you the most?
34. What did you initially believe about AI that changed during this session?
35. What will you do differently in the next experiment?
