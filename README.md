# Old Key Pad

Some people might remember T9 phone inputs, in which the numbers 2 to 9 have associated letters, and 0 acts as a space. Key 2 has "abc", 3 has "def" etc:

<pre>

  1   2   3
     abc def

  4   5   6
 ghi jkl mno

  7   8   9
pqrs tuv wxyz
     
      0
      _
</pre>

--- 

## Note that 0 is a space, not an underscore!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To get a letter you press the button a certain number of times - pressing 2 once gives "a", twice gives "b".
The input is a list of number pairs: a key and the number of times it has been pressed. For example, "7 3" would be "r". What is the message this input produces?

### Example output in :
```bash
 data.txt
```

## Output
``` bash
--@--:~/--/--/old_keypad$ python3 key_find.py 
[6] key [3] times  = [o]
[4] key [2] times  = [h]
[0] key [1] times  = [0]
[7] key [4] times  = [s]
[6] key [3] times  = [o]
[0] key [1] times  = [0]
[8] key [1] times  = [t]
[4] key [2] times  = [h]
[3] key [2] times  = [e]
[9] key [3] times  = [y]
[0] key [1] times  = [0]
[4] key [2] times  = [h]
[2] key [1] times  = [a]
[8] key [3] times  = [v]
[3] key [2] times  = [e]
[0] key [1] times  = [0]
[4] key [3] times  = [i]
[6] key [2] times  = [n]
[8] key [1] times  = [t]
[3] key [2] times  = [e]
[7] key [3] times  = [r]
[6] key [2] times  = [n]
[3] key [2] times  = [e]
[8] key [1] times  = [t]
[0] key [1] times  = [0]
[6] key [3] times  = [o]
[6] key [2] times  = [n]
[0] key [1] times  = [0]
[2] key [3] times  = [c]
[6] key [3] times  = [o]
[6] key [1] times  = [m]
[7] key [1] times  = [p]
[8] key [2] times  = [u]
[8] key [1] times  = [t]
[3] key [2] times  = [e]
[7] key [3] times  = [r]
[7] key [4] times  = [s]
[0] key [1] times  = [0]
[6] key [2] times  = [n]
[6] key [3] times  = [o]
[9] key [1] times  = [w]
[0] key [2] times  = [Space]

```
