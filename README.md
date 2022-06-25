# Learning Outcomes

## Purpose:

1) we will use prairie learn interface to select problem banks for each test. Each test will try to assess a subset of the learning outcomes. 

2) instructors will need to browse learning outcomes to see what the “coverage” is of the problem bank. Example question: “how many questions are there that require both energy and momentum”

3) once the tests are done, students will get an email of all the learning outcomes they did NOT meet (ie got questions wrong) along with links to videos/readings to learn that material. 

4) if an instructor is using a different textbook, they should still be able to use our problem bank because there will be that Rosetta Stone linking learning outcomes between textbooks. This is what @stevecollins17 will be working on. 

So if we use those codes, all the above becomes a lot easier/better than carting around strings with full sentences.  


## Instructions 

Learning Outcomes are tagged under the format (Topic.Subtopic.Subsubtopic.LearningOutcome) with each category enumerated in descending order starting from 1 referring to the list order of the Masterlist_Topics_Outcomes.yml file. 

Ex. (2.4.2.1) would refer to the second Topic, fourth Subtopic, second Subsubtopic, first Learning Outcome.  

When adding new Learning Outcomes, Topics, Subtopics or Subsubtopics be sure to add to the bottom of the respective list as to not skew all subsequent tag values. 

If a specific Subtopic does not have a Subsubtopic the tagging follows the following unique format (Topic.Subtopic.1.LearningOutcome) with the Learning Outcome enumerations begining at zero (Ex. 2.4.1.0 Would be the second Topic, fourth Subtopic, FIRST Learning Outcome. 2.4.1.1 Would be the second Topic, fourth Subtopic, Second Learning Outcome.)

The first Subtopic of each Topic and the first Subsubtopic of each Subtopic are labeled "Topic Outcomes" and "Subtopic Outcomes", respectively.  This allows for the input of Learning Objectives that pertain to the entire Topic or Subtopic under these categories. With the exception of a Subtopic with no Subsubtopics, the Learning Outcomes in this case, are simply listed under the Subtopic and the unique tagging format is used (see above). 

The Masterlist_Topics_Outcomes.yml file should be formatted as follows:

```
Topic:
	Topic Outcomes:
		- Learning Objective 
		- Learning Objective
	Subtopic (without subsubtopic):
		- Learning Objective 
		- Learning Objective
	Subtopic (with subsubtopic):
		Subtopic Outcomes: 
 			- Learning Objective
 			- Learning Objective
 		Subsubtopic: 
 			- Learning Objective
 			- Learning Objective
		
```
