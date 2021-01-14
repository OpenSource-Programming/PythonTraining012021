# parsing strings exercise

# exact match to video
str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(':')
# print(ipos)
piece = str[ipos+2:]
# print(piece)
value = float(piece)
print(value)

# practicing concept with my own fun content
fun_string = "👁️  When I close my eyes, I cannot see."

print("\n" + fun_string + " 🚫")

loc_close = fun_string.find('close')
loc_cannot = fun_string.find('cannot')

close_str = fun_string[loc_close:loc_close+5]
cannot_str = fun_string[loc_cannot:loc_cannot+6]

open_string = fun_string.replace(close_str,"open")
open_string = open_string.replace(cannot_str,"can")

print("\n" + open_string + " 💯\n")
