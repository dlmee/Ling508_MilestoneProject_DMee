# Ling508_MilestoneProject_DMee

## Week 5 Submission

[My_github_repo](https://github.com/dlmee/Ling508_MilestoneProject_DMee)

Unfortunately I did not get quite as far as I would like. I am currently in the middle of implementing my service layer.
The main problem is that I need to build my SenseDisambiguater class, that is then called by the service layer, and while the service layer is operating as intended, it's just a matter of finishing my build. 

I will finish this as soon as possible! 

Please do note what has been accomplished. 
* I have fleshed out my interactions between my sql database and the program itself. collectdata.py should be run one time. A server will need to be open for this part only.
* services then calls back this data from my sql server (running on 8.0)
* model and app are separated as modules. 
* mysql_implementation is no longer necessary. I'm keeping it for personal reference. 
* I have implemented the abstract layer repository.py

...I also learned that my init.sql file only runs on the first instantiation. After that, I need to docker-compose down -v if I want to rebuild my database.

## Update 8/8/22!

I have reached my goal for week 5 and implemented a service layer, that returns to me the Senses class for each sense found of a particular word in a context. I definitely want more data, and need to refine and expand (next step, returning context sentences to various senses). But at least I made it this far!



