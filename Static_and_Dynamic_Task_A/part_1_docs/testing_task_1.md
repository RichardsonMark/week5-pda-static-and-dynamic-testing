### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# this function has an error when checking the value of the card. should have double equals ==, not single =. 
# The else statement should also have a colon after it, as such... else:
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# this function has a spelling error when defining the function. should read def, not dif
# there should also be a comma between card1 and card2
# lines 2,3 and4 should be indented one more step
# card on line 3 should say card1
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# this function has an error when defining the initial value of 'total'. should be given an initial empty/0 value
# the indentation of the lines of code needs realigned. first 4 lines needs indented one place, last line will be in correct place when the others are indented
# on the last line, need to add a space before second double quote to allow proper sentence/string 
# and also convert 'total' to a string so that we can append/concatenate to the rest of the string
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
