class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.findall(r'\w+',paragraph.lower())]
        word_map = sorted(Counter(words).items(), key=lambda x: x[1], reverse = True)
        for word, _ in word_map:
            if word not in set(banned):
                return word
