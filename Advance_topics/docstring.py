'''
A docstring is a brief text that explains what something does.
We want our methods, classes, and functions to give us more information when we 
or someone else use the help function. We can do that by adding a docstring.
It is written in triple quotes notation
'''

def to_seconds(hours,minutes,seconds):
    ''' This method converts hours, minutes and seconds to seconds'''
    return hours*3600+minutes*60+seconds


help(to_seconds)

