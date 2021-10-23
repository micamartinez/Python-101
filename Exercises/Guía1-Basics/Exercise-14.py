'''In a certain company, its employees are evaluated at the end of
every year. The points they can get in the assessment start at 0.0 and can
increase, translating into better benefits. The points they can get
can be 0.0, 0.4, 0.6 or more, there are not intermediate values between the
scores mentioned. Below there is a table with the levels
corresponding to each score. The amount of money earned at each level
is 100000 multiplied by the level score.
Level Score
Unacceptable 0.0
Acceptable 0.4
Meritorious 0.6 or more
Create a program that reads the user's score and indicates their performance level,
as well as the amount of money that the user will receive.'''

points = float(input('Enter the points: '))
unacceptable = 0.0
acceptable = 0.4
meritorious = 0.6
bonus = 100000

if points == unacceptable:
    bonus *= points 
    print(f'Your performance is unacceptable, you will receive {bonus} pesos.')
elif points == acceptable:
    bonus *= points
    print(f'Your performance is acceptable, you will receive {bonus} pesos.')
elif points >= meritorious:
    bonus *= points
    print(f'Your performance is meritorious, you will receive {bonus} pesos.')
else:
    print('You have not entered a correct score')
