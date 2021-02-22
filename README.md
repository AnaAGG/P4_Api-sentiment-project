# AnaAGG-P4_Api-sentiment-project

![portada](https://www.juliedesk.com/wp-content/uploads/2017/04/Featured-quotes-focus.png)

# API description

QuoteAPI is an API to collect famous quotes from different authors throughout history. This API will collect citations from different disciplines which form the basis of the API structure and therefore of the database in mongo.


# Collection Structure


![esquema](https://github.com/AnaAGG/P4_Api-sentiment-project/blob/main/Images/Esquema.png)


# Endpoints Structure
> *"/Data"* --> to obtain all the information about authors, categories and phrases from our entire database

> *"/Authors/<Collection>"* --> to get all the authors contained in a given collection

> *"/Quotes/<Collection>"* --> to get all the phrases contained in a given collection

> *"/<Collection>/delete"* --> Delete a certain author and his / her quote from the givrn collections

> *"/<Collection>/new"* --> Insert a new author and his citation from the given collection

