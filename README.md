# CS533_proj1
CS533 MDP planner

The input format for the MDP should be a text file with the following format:
-First line gives two integers n and m specifying the number of states and actions respectively.
-After the first line there will be a blank line and then a sequence of m n × n matrices (each
separated by a blank line) that give the transition function for each action. Specifically, the
i’th matrix gives the transition function for the i’th action. Entry j, k in that matrix (j is the
row and k is the column) gives the probability of a transition from state j to state k given
action i. The rows, thus, will sum to 1.

After the final transition matrix there will be a blank line followed by row of n real numbers.
The i’th real number specifies the reward for the i’th state.
An example of the format is below:

3 2

0.2 0.8 0.0
0.0 0.2 0.8
1.0 0.0 0.0

0.9 0.05 0.05
0.05 0.9 0.05
0.05 0.05 0.9
-1.0 -1.0 0.0

The MDP has 3 states and 2 actions. We see that in state 1 if we take action 1 then there is 0.2
probability of remaining in state 1 and 0.8 probability of a transition to state 2 (zero probability
of going to state 3). The reward is negative, except for when the system is in state 3.

So the goal should be to get to state 3 and stay there as much as possible. This will generally involve taking
action 1 if not in state 3 and then taking action 2 when in state 3. (see if you can understand why
that is the best policy and test that your algorithm can figure that out)
The output format could be two n × H-dimensional matrices, one for the non-stationary value
function (column i gives the value function with i steps-to-go) and one for the policy (column i
gives the policy for i steps-to-go)

## States
Nothing more than just a value in some range for looking up in our transition table. There is a state class but it doesnt do 
anything right now.

## Actions
Actions just represent a different index in our transition table

## Rewards
State => Reward. That simple.

## Transition
A simple action + state => new state function. Right now we are just working from tuples of things so it isnt anything 
more complicated than a bunch of integers getting passed around, in future projects it may be desirable to abstract this another level. 
It isnt done yet but maybe if I get bored in class or something I can do that.
