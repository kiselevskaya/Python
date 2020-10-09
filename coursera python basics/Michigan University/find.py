str = 'X-DSPAM-Confidence: 0.8475'
one = str.find(":")
two = str.find(" ", one)
three = str[two + 1:]
print float(three)
