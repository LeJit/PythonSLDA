require("lda")
require("pracma")

sldaModel <- readRDS()
vocabModel <- readRDS()

corpus <- lexicalize(documents, lower=TRUE, vocab=vocabulary)

predictions <- slda.predict(corpus, sldaModel$topics, sldaModel$model, alpha = alpha, eta = eta)