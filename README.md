This Text Summarizer is a basic level Text Summarizer, which Uses Text Rank Algorithm.

What is Page Rank Algorithm?

Suppose we have 4 web pages — w1, w2, w3, and w4. These pages contain links pointing to one another. Some pages might have no link – these are called dangling pages.
Web page w1 has links directing to w2 and w4
w2 has links for w3 and w1
w4 has links only for the web page w1
w3 has no links and hence it will be called a dangling page
In order to rank these pages, we would have to compute a score called the PageRank score. This score is the probability of a user visiting that page.

Text Rank Algorithm?

Let’s understand the TextRank algorithm, now that we have a grasp on PageRank. I have listed the similarities between these two algorithms below:

In place of web pages, we use sentences
Similarity between any two sentences is used as an equivalent to the web page transition probability
The similarity scores are stored in a square matrix, similar to the matrix M used for PageRank
TextRank is an extractive and unsupervised text summarization technique. 

Steps Involved:

The first step would be to concatenate all the text contained in the articles
Then split the text into individual sentences
In the next step, we will find vector representation (word embeddings) for each and every sentence
Similarities between sentence vectors are then calculated and stored in a matrix
The similarity matrix is then converted into a graph, with sentences as vertices and similarity scores as edges, for sentence rank calculation
Finally, a certain number of top-ranked sentences form the final summary
