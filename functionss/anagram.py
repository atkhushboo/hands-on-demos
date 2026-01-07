def anagram(s_one,s_two):
    if len(s_one)==len(s_two):
        for s in s_one:
            if s in s_two:
                return True,"Its Anagram"
            return False,"Not Anagram"
    
    return "Wrong input"
print(anagram("khush","huskh"))