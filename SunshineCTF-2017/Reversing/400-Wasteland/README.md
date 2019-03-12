# [Reversing 200] Wasteland

## Setup

Have this challenge running on a server, in the same directory as "0", "1", "2", "3", "4", and "flag". Needs to be compiled with pwnableharness. Give the players a copy of wasteland.asm only.

## Solution

This challenge is an 8 part reversing challenge. Players only recieve an assembly file of the main function that is just the 32 and 64 bit versions splice together.
Documented reversing work can be found in writeup.md. Here are the intended solutions.

```
North answers: "" + "10" & "38" + "9216"

East answers: "" + "" + "56991" & "57023"

West answers: "64" & "-1153"

South answers: "nan" & "Chalk" + output of hash (for chalk it's 217455688)

End String: 1dt6SE89dNEOnAdBzxtNllxgfH3VJCyJRWm9tDnanQJMkzSF2CKSKSTSkZDvTSkZDvheYsdA9ueFUJPeOzcTwoSPq5OpuLrhAzD35myz3XV38K2aQlqv1vZIfJNcM1HyiaLk88CO4MdeXbQIJdThWqicmv1pKjo3V5gGON0jcRQJGpcedJNEQPc2rY

flag: sun{w@5t4land_i5 @_dang3r0u5_p1@c3}
```
