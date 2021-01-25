text = "X-DSPAM-Confidence:    0.8475";
strLen = len(text)
colPos = text.find(':')
strNum = text[colPos+1:strLen]
print(float(strNum))
