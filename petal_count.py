"""

"Not every love story has a happy ending!"- Little Jhool was certainly a con man, fooling people by telling them about their future, [The first problem!] but he loved his girl - truly! But, Big Jhool, his girlfriend, was shocked and had broken up with him after getting to know that Little Jhool was a con man. Now, our hero of this problem set, little Jhool is upset, and he's unable to get over her (Or, back with her, for that matter!) and he's sure that somewhere deep down she still loves him!

And to verify her love for him, he's using the good, old, tested formula by the lovers of tearing off the petals of a flower one by one, and saying, "She loves me!", "She loves me not!" Now, he's standing in the garden of your house, and plucking off the petals of as many flowers as he sees everyday. Obviously, he's so obsessed with his ex, that he wants to stop at "She loves me!" and not very surprisingly, start off with "She loves me!" as well!**

You're his neighbor, and you cannot bear him cry when the answer comes out to be "She loves me not!", so you decide to help him. Given n roses in his garden, you want to pick up a bouquet with maximum number of total petals (To keep him busy!) so that the result would be in little Jhool's favor ("She loves me!") and he wouldn't cry because of his lost love. A bouquet may even consist of a single flower, but you just have to make him not cry!

Find the maximum number of rose petals possible in the bouquet of flowers.

Input format:

The first line contains n, the number of roses in your garden. The second line will contain n different integers separated by space, which denote the number of petals on the i-th rose.

Output format:

You have to print the maximum number of petals in the bouquet of rose, which would result in "She loves me!". If there is no such bouquet possible, sadly, print ":(" instead.

Constraints:

There will be no more than 100 roses in a bouquet, and no less than 1. The number of petals in a bouquet will also be less than 100 and greater or equal to 1.

Example:

Input:

4

2 3 5 4

Output: 11



"""
name = input()                 
name = name.split(" ");
a = 0;
c = len(name)-1;
odd = [];
for i in range (1,len(name)):
	b = int(name[i]);
	a = a + b;
	if(b%2 == 0):
		c-=1;
	else:
		odd.append(b)

if(c==0):
    n = ":("
    print(n)
else:
    n  = a - min(odd);
    print(n)
  