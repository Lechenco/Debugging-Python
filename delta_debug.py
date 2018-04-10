import re

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""
    
    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag == False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
            
    assert out.find("<") == -1
    return out
            

def test(s):
    #Return "FAIL" if assertion fails, otherwise return "PASS"
    
    print (s, len(s))
    try:
        result = remove_html_markup(s)
        print("PASS")
        return "PASS"
    except AssertionError:
        print("FAIL")
        return "FAIL"
    


def ddmin(s):
    assert test(s) == "FAIL"

    n = 2     # Initial granularity
    while len(s) >= 2:
        start = 0
        subset_length = int(len(s) / n)
        some_complement_is_failing = False

        while start < len(s):
            complement = s[:start] + s[start + subset_length:]

            if test(complement) == "FAIL":
                s = complement
                n = max(n - 1, 2)
                some_complement_is_failing = True
                break
                
            start += subset_length

        if not some_complement_is_failing:
            n = min(n*2, len(s))
            if(n == len(s)):
                break
            

    return s

# UNCOMMENT TO TEST
html_input = '"<b>foo</b>"'
print (ddmin(html_input))