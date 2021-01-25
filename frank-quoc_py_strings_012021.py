# Exercise 6.5

text = "X-DSPAM-Confidence:    0.8475";
i_colon = text.find(":")
num = float(text[i_colon + 1:])
print(num)
