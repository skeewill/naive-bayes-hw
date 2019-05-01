# naive-bayes-hw

### Part I

Coding.

Remember the Bayes Dice app we build many weeks ago? Let's revisit that app, but with a twist.

You have 3 coins with the following probabilities. P(H|1) = 0.3, P(H|2) = 0.45, P(H|3) = 0.75.

That is read as the probability of heads for coin 1 is 30%, etc.

Write a small app, using Object Oriented Python, that allows you to randomly select a coin (without looking) and then repeatedly flip it about 10 times or so until you are fairly certain as to the type of coin you selected.

### Part II

Questions.

In general, what makes the Naive Bayes Classifier so `naive`?

What is the difference between the Bernoulli, Gaussian and Multinomial Naive Bayes Classifiers?

Can you use the Naive Bayes Classifier if your features are not independent?

### Part III

Models.

Take this data. https://github.com/gSchool/dsi-logistic-regression/blob/g79/data/grad.csv

Predict whether someone will get into grad school. Use the following models.

- Logistic Regression
- Random Forest
- Naive Bayes (you will need to figure out what type works best for this data)

Which model performed the best?

### Part IV

Text Classification.

Remember this assignment.

https://github.com/data-science-ml/tweets-nlp-assignment/blob/master/nlp-assignment.md

Take the above tweets and turn them into a bag of words. Use a Naive Bayes classifier to figure out if a particular tweet is Neutral, Negative or Positive. Remember to split your data.

What is the accuracy of your model?

Compare this model to a KNN model (neighbors == 3) where each tweet is a 300 dimensional vector.

Which model performs better?
