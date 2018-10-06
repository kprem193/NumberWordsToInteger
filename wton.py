def text2int(textnum, numwords={}):
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, (idx + 2) * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


check = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
    "ninety", "hundred", "thousand", "million", "billion", "trillion"
]

text = "Twenty two thousand pound"
text = text.lower()  # to make the code work even if user write some uppercase characters
a = text.split(" ")
f1 = 0
j = 1

if a[-1] == "cent" or a[-1] == "cents":
    f1 = 1
    text = text[:len(text) - (len(a[-1]) + 1)]
    for i in check:
        if i == a[-3]:
            j = 2
            break

    if j == 2:
        text1 = a[-3] + " " + a[-2]
        text = text[:len(text) - (len(a[-2]) + len(a[-3]) + 1)]
    if j == 1:
        text1 = a[-2]
        text = text[:len(text) - (len(a[-2]) + 1)]
    text = text[:len(text) - 1]

a = text.split(" ")
f = 0
for i in check:
    if i == a[-1]:
        f = 1

currency = ""
if f != 1:
    text = text[:len(text) - (len(a[-1]) + 1)]
    if a[-1] == "dollar" or a[-1] == "dollars":
        currency = "$"
    if a[-1] == "euro" or a[-1] == "euros":
        currency = u"\u20ac"
    if a[-1] == "pound" or a[-1] == "pounds":
        currency = u"\u00A3"

    final = str(text2int(text)) + currency
    print(final)
else:
    final = str(text2int(text)) + "." + str(text2int(text1)) + currency
    print(final)
