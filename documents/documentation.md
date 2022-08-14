# Sense Disambiguator

Dillon Mee
Ling 508
Summer, 2022

## Find Sense

The purpose of this program is to be able to find different senses of a word given a particular context. From the outset, I would like to establish that the nuance of this process certainly bears more depth of code and greater scope of data.

The goal is to create a database, then leverage that database to find different senses of a word, as identified by different word vectors.

The underlying assumption is that given a large enough corpus a single word will have several different groupings of vectors all hidden under a single word. These groupings can presumably be discovered by identifying the similarity and difference between the components of a vector.

Using the "Find a sense interface" a user can put in a word such as `tired`, and will receive four things in return as JSON string. The sense, which will be a number. Combined with the surface form (also included in the response) and the sense intiger, we receive a unique sense. Additionally there is a vector with the words which constitute that unique sense, and finally example sentences that are found using the word as a key and the vector as a way to filter out sentences that use another sense. 

An example of what this would look like is below, with whitespace truncation for ease of reading. One sense is shown here, but a call may yield multiple senses. 

Searching for a word that is not in the database will result in a 500 internal servor error. Using the UI this will simply return no result. 

``` 
    "examples": ["And so the day went on  and the evening came  and in the middle of a great desolate heath he began to feel tired  and sat down under an ancient hawthorn  through which every now and then a lone wind that seemed to come from nowhere and to go nowhither sighed and hissed"],
    "sense": 1,
    "surface": "tired",
    "vector": [
      ["desolate", 1],
      ["heath",1],
      ["hawthorn",1],
      ["lone",1],
      ["nowhere",1],
      ["nowhither",1],
      ["sighed",1],
      ["hissed",1]]
```

The API can be called directly using the endpoint [http:/localhost:5000/find_sense](). This can be done using a service such as Postman and must have a key value pair in which the key is 'word'. 

In such a case, please ensure that `"Content-Type: application/json" ` is part of the request. 

A curl command would look like:

`curl -X POST "http://localhost:5000/find_sense" -H "Content-Type: application/json" -d '{"word":"tired"}'`

## Database Generation

The docker-compose.yml file has everything necessary to not only run the API, but also generate an example database: 'mcdonald'. This database is built using a localserver, and as such if you need to build the database, then you will need to have the main directory of this folder running on a local server which is as easy as `python -m http.server`. 

You may then call the database generation with a GET request by visiting [http:/localhost:5000//generatedb](). This process then calls a method from ther Service layer. This layer is currently hardwired to the sample database, but could easily be modified to accept any URL or file path. Note, however, that due to the variability of webscraping, this might still require a little back-end development. 

It was a design choice to let the user become part of the database generation process. I want the user to be aware that it is the particular database that is yielding those particular senses, and that a different database might yield other senses. I see this as an interesting area of research, how different speaker groups or speakers might begin to yield different senses of words, but that is outside the scope of this documentation. Additionally letting the database generation be called, reduced the load time, and let the flask environment be changed, while simply calling an already generated database. 
