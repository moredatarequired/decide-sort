# Help me decide

You have dozens of options. It all seems kind of overwhelming.
What if you can just focus on two options at a time? Maybe building
a simple priority queue can help you decide.

## What this is

Enter a bunch of options -- next major project, which apartment to rent,
what do to with your windfall lottery winnings. If you can compare just two
items against each other, they can just be heap-sorted and the best option
will come out on top. You still have to make a lot of decisions, but at least
you only have two items to consider at a time.

### Be careful

Technically this won't work if you don't have stable priorites (sometimes
you think A is better than B, sometimes vice versa), or if you have cycles
(A is better than B is better than C is better than A). In pratice, the item
declared "best" in those cases will usually still be pretty good. After all,
you probably don't actually need a computer to help you decide -- this is
just a nice way to get unstuck.
