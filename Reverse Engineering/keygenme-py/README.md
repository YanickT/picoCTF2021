#keygenme-py (30 Points)

##Description
None

##Hints
None

##Solution
Checking the code, the key can be recived step by step:
At first `hashlib.sha256(username_trial).hexdigest()` is needed.
This can easily done with python and the result reads:
`09820d032d73c31bd8f4a0532062a239d828a4da0951aeb66da928e843597e35`.

1. key_part_static1_trial = picoCTF{1n_7h3_|<3y_of_
2. The dynamic part is given by the ifs: 0d208392
3. Finally, we add the } to the end and get
`picoCTF{1n_7h3_|<3y_of_0d208392}`