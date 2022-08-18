# Sense Disambiguator

## Investigating word sense differences by context
## Note, all texts used as examples are scraped from Project Gutenburg. No commercial designs are intended, rather they represent access to a single object which can be treated as a corpus. 

[My_github_repo](https://github.com/dlmee/Ling508_MilestoneProject_DMee)

This repository is the culmination of a 7 week project for a graduate level course. In the course, I develop an app that sets use cases, is designed using UML (see documents directory), scrapes data from the internet, populates an SQL database, and uses a flask api. The project I have designed is intended to explore the way in which we refine data influences the quality and by extension the ways in which we can more effectively manipulate that data. 

Already having completed this project, there are some things that I would design from the ground up differently. Most significantly the runtime for building the mysql database is quite hefty. A lot is happening under the hood! Once a database is populated, the use case of finding the different senses of a word is quite fast. How effective these use cases are, bears future investigation. One significant factor is simply that these databases are rather small. While this model does not stack databases, I envision this as a meaningful future upgrade. Rather than looking at one text, what happens when we look at every work from an author? Here, I imagine, is where statistical methods would be compelling. 

Please note, in order to use this you will need to take the following steps. 

* Clone the git repository. 
* run a local server `python -m http.server`
* docker-compose up
* go to http://localhost:5000
* Follow the directions there, or reference the hyperlinked http://localhost:5000
* Send a post request via the generate a database section. 
* You may now search the senses of a given word. 

