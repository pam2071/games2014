#NotSoTrivial.py
#A trivia game that asks multiple choice questions and tells the user if they ar right or wrong.
#It will have five questions.

#Welcome Screen
print "Welcome to the 2014 Fellows Code For Progress Trivial Game"

#Section 1.  The First Question

print "1. Ohio passed legislation to eliminate the practice of shackling prisoners under the age of 14 in what year? "
print "\n (a) 2012 \t (b) 1957 \t  (c) 1921"

answer = raw_input("Your answer: ") #Asks the user for their reponse and saves it as answer
if answer=="a": #Checks to see if answer is correct.  If it is, say that's Correct! If it isn't, say so.
	print "Right!"
else:
	print "Wrong! \n"

print "2. What does it cost Taxpayers each year to keep a Walmart SuperCenter open in your City?  "
print "\n (a) $2M \t (b) $900K \t  (c) $100K"

answer = raw_input("Your answer: ") #Asks the user for their reponse and saves it as answer
if answer=="b": #Checks to see if answer is correct.  If it is, say that's Correct! If it isn't, say so.
	print "Right!"
else:
	print "Wrong! \n"

	
print "3. What is the percentage of 1.3 million Walmart Associates that qualify or are eligible to for Government Assistance? "
print "\n (a) 3 \t (b) 25 \t  (c) 80"

answer = raw_input("Your answer: ") #Asks the user for their reponse and saves it as answer
if answer=="c": #Checks to see if answer is correct.  If it is, say that's Correct! If it isn't, say so.
	print "Right!"
else:
	print "Wrong! \n"
