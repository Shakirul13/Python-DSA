s1="success"
s2="anhiebdkb"      
def vowel(s):     
        vowels=set("aeiou")
        n=len(s)
        freq_map={}
        for ch in s:
            freq_map[ch]=freq_map.get(ch,0)+1
        vowel=[freq for ch,freq in freq_map.items() if ch in vowels]
        consonant=[freq for ch,freq in freq_map.items() if ch not in vowels]
        max_vowel=max(vowel,default=0)
        max_consonant=max(consonant,default=0)
        return max_vowel+max_consonant
print(vowel(s1))
print(vowel(s2))
