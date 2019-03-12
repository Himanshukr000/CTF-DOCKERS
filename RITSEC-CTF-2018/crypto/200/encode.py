ans = "if you think you are worthy of the flag first you must answer these three questions. what is you name, what is your quest, what is the air speed velocity of an unladen swallow. your flag is: african_or_european_swallow_wow_theres_a_difference ";


abcs = "abcdefghijklmnopqrstuvwxyz .,:_"
emoji = "😀🤩🤬😎😟👿😯💪🤞🤠🙄😾👻🗣🐼🐙💔✅🔥🚫💩👀🍞🎱🥇😇🤓😭🤢🤡_"

ciph = dict();
for i in range(len(abcs)):
    ciph[abcs[i]] = emoji[i];

for i in abcs:
    ans = ans.replace(i,ciph[i]);

print(ans);

