{"filter":false,"title":"lab08.py","tooltip":"/lab08.py","undoManager":{"mark":62,"position":62,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":66}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":39},"action":"insert","lines":["Exercise 1: Working with a while loop"],"id":67}],[{"start":{"row":0,"column":39},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":68}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":86},"action":"insert","lines":["print(\"Welcome to Guess the Number!\")","print(\"The rules are simple. I will think of a number, and you will try to guess it.\")"],"id":69}],[{"start":{"row":2,"column":86},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":70},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":13},"action":"insert","lines":["import random"],"id":71}],[{"start":{"row":4,"column":13},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":72},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":29},"action":"insert","lines":["number = random.randint(1,10)"],"id":73}],[{"start":{"row":6,"column":29},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":74},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":20},"action":"insert","lines":["isGuessRight = False"],"id":75}],[{"start":{"row":8,"column":20},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":76},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":16,"column":79},"action":"insert","lines":["while isGuessRight != True:","    guess = input(\"Guess a number between 1 and 10: \")","    if int(guess) == number:","        print(\"You guessed {}. That is correct! You win!\".format(guess))","        isGuessRight = True","    else:","        print(\"You guessed {}. Sorry, that isn’t it. Try again.\".format(guess))"],"id":77}],[{"start":{"row":10,"column":19},"end":{"row":10,"column":26},"action":"remove","lines":["!= True"],"id":78},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"remove","lines":[" "]}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["!"],"id":79}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"remove","lines":["!"],"id":80},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["\\"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["n"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"remove","lines":["o"],"id":81},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"remove","lines":["n"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"remove","lines":["\\"]}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["n"],"id":82},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["o"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":[" "],"id":83}],[{"start":{"row":6,"column":29},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":84},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["p"]},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["r"]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["i"]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":["n"]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":7},"action":"insert","lines":["()"],"id":85}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["n"],"id":86},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["y"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["m"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["b"]}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"remove","lines":["b"],"id":87},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["m"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"remove","lines":["y"]}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["u"],"id":88},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["m"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["b"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["e"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["\""],"id":89},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["\""]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["f"],"id":90}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["s"],"id":91},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["p"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["o"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["i"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["l"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["e"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["r"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":[":"]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":[" "],"id":92},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["a"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"remove","lines":["a"],"id":93}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["n"],"id":94}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"remove","lines":["n"],"id":95}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["t"],"id":96},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["h"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":[" "],"id":97},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["n"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["u"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["m"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["b"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["e"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":[" "],"id":98},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["i"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":[" "],"id":99},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["{"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["n"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["u"]},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["m"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["b"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["e"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["r"]},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["{"]}],[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"remove","lines":["{"],"id":100}],[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["}"],"id":101}],[{"start":{"row":7,"column":40},"end":{"row":7,"column":46},"action":"remove","lines":["number"],"id":102}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["g"],"id":103},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["u"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["s"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["f"],"id":104}],[{"start":{"row":14,"column":63},"end":{"row":14,"column":77},"action":"remove","lines":[".format(guess)"],"id":105}],[{"start":{"row":17,"column":64},"end":{"row":17,"column":78},"action":"remove","lines":[".format(guess)"],"id":106}],[{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["f"],"id":107}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["g"],"id":108},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["u"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["e"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["s"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":54},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":109},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":36},"action":"remove","lines":["print(f\"You guessed {guess}."],"id":110}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":32},"action":"insert","lines":["print(f\"You guessed {guess}."],"id":111}],[{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"remove","lines":["."],"id":112}],[{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":[")"],"id":113}],[{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"remove","lines":[")"],"id":114}],[{"start":{"row":13,"column":31},"end":{"row":13,"column":33},"action":"insert","lines":["\"\""],"id":115}],[{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"remove","lines":["\""],"id":116}],[{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":[")"],"id":117}],[{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["p"],"id":118},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["r"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["i"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["n"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["t"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["("]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["\""]}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"remove","lines":["f"],"id":119}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":36},"action":"remove","lines":["You guessed {guess}. "],"id":120}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"remove","lines":[" "],"id":121}],[{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":[","],"id":122}],[{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"insert","lines":[" "],"id":123},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"insert","lines":["e"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"insert","lines":["n"]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":["d"]}],[{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"insert","lines":[" "],"id":124},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"insert","lines":["="]}],[{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"insert","lines":[" "],"id":125}],[{"start":{"row":13,"column":40},"end":{"row":13,"column":42},"action":"insert","lines":["\"\""],"id":126}],[{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["."],"id":127}],[{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":[" "],"id":128}]]},"ace":{"folds":[],"scrolltop":55,"scrollleft":0,"selection":{"start":{"row":18,"column":49},"end":{"row":18,"column":49},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1699019246677,"hash":"6079aae73cee845e8d19cf9b7dcbef2d52843efc"}