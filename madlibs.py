'''
Madlibs using string concatenation

'''

# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "Add me on  _____ "
# instagrammer = "Kabir Srivastava" # some string variable

# # a few ways to do this

# print("Add me on " + instagrammer) 
# First way is: Using the string  "Add me on", concatenate it with instagrammer by adding a plus sign.
 
# print("Add me on {}".format(instagrammer))
# The  second way is: string "Add me on" and then have these curly braces. Call string dot format (instagrammer), 
# It will put the value of instagrammer is into where the curly braces are in that string.

# print(f"Add me on {instagrammer}")
 
# The third metnod F-string. And after string "Add me on" and then the curly braces.  
# And then directly in the curly braces,add the variable name instagrammer. 



#inputs
nounVariable1 = input("Enter a Noun: ")
nounVariable2 = input("Enter another Noun: ")
nounVariable3 = input("Enter last Noun: ")


adjectiveVariable1 = input("Enter an Adjective: ")
adjectiveVariable2 = input("Enter another Adjective: ")

verb1 = input("Enter a Verb: ")
verb2 = input("Enter another Verb: ")
verb3 = input("Enter third Verb: ")

famousCelebrity = input("Enter a name of celebrity: ")


#The Madlib Sentence using f-string
madLibSentence = f"Look at the {nounVariable1} and the {nounVariable2}. Please feel free to pet the {nounVariable3}! \
The {nounVariable3} is {adjectiveVariable1} and {adjectiveVariable2} thus motivating, the determined wrestler aka {famousCelebrity}, {verb2}, and {verb3} his way to slow victory."

print(madLibSentence)