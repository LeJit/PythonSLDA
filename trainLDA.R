require("lda")
corpus <- lexicalize(documents)

documents <- corpus$documents
vocabulary <- corpus$vocab

params <- sample(c(-1,1), numtopics, replace=TRUE)

#result <- slda.em(documents=documents, K = numtopics, vocab=vocabulary, num.e.iterations = e_iter, num.m.iterations= m_iter, alpha = alpha, eta = eta, as.numeric(labels), params, variance = variance, lambda = lambda, logistic = logistic, method="sLDA")
result <- tryCatch({
	slda.em(documents=documents, K = 5, vocab=vocabulary, num.e.iterations = 10, num.m.iterations= 4, alpha = 1.0, eta = 0.1, as.numeric(labels), params, variance = 0.25, lambda = 1.0, logistic = TRUE, method="sLDA")
}, warning = function(war) {
    return(war) 
}, error = function(err) {
    return(err)
}, finally = {
   
})    


topics <- result$topics
model <- result$model
