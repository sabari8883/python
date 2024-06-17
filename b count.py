# Sample input
input_text = '''The apple doesn't fall. ...
All that glitters are not gold. ...
A picture is worth a thousand words. ... Beggers can't be choosers. ...
A bird in the hand. ...
Better safe than sorry. ...
An apple a day keeps doctor away. ...
Blood is thicker than water. ...'''

# Split the input text by lines
lines = input_text.strip().split('\n')

# Count the total number of lines
total_lines = len(lines)

# Initialize the count of sentences starting with 'B'
count_B = 0

# Iterate over each line and check if it starts with 'B'
for line in lines:
    if line.strip().startswith('B'):
        count_B += 1

# Print the results
print(f"Total number of lines: {total_lines}")
print(f"Number of sentences that start with letter B: {count_B}")
