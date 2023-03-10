# MangaRecommendationEngine
 Get a manga (japanese comics) recommendation based on a series description.

# Table of contents

 - [Introduction](#introduction)

 - [Data Mining](#data-mining)
        
 - [Data Cleaning](#data-cleaning)
    
 - [Recommendation](#recommendation)


## Introduction

Japanese comics, commonly known as Manga, have become one of the most popular forms of literature. However, due to the vast amount of
different titles, more often than not, finding a new series to binge read can be challenging.

Using data gathered form the Anilist API ('https://graphql.anilist.co'), in combination with a simple natural language processing
model, we can give recommendations to readers.

In this repository, you can find, download, recreate and optimize the process of recommending manga series  title based on the series
description information.

### Data Mining

The data used for this project was obtained through the GraphQL API of Anilist ('https://graphql.anilist.co'). You can find more about it in this link: https://anilist.gitbook.io/anilist-apiv2-docs/

The query used to draw data is located in the **query.py** script.

### Data Cleaning

In order to bring our data in the correct form, the description text of each title needed to be cleaned of special characters
and irrelevant patterns that did not provide meaninful information about the content of the series. Additionaly, using descriptive statistics we got an insightful look at some of the series features recorded in the dataframe (relevant code: **eda notebook**).

### Recommendation

Finally, after creating a recommendation function that takes as input the data frame, and a manga title of our choosing (the title must be in romaji, and exist into the dataframe), 5 recommended titles are produced. Measure of similarity is the cosine similarity algorithm (https://en.wikipedia.org/wiki/Cosine_similarity) (relevant code: **recommendation notebook**).