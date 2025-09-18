text = "X-DSPAM-Confidence:    0.8475"

stpos = text.find(':')
res_str = text[stpos + 1:]

res_str = res_str.lstrip()

res_no = float(res_str)
print(res_no)