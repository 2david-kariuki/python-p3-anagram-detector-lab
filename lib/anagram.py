class Anagram:
    def __init__(self, word):
        self.base_word = word.lower()

    def match(self, candidates):
        # Filter the list to only include valid anagrams
        return [
            candidate for candidate in candidates
            if sorted(candidate.lower()) == sorted(self.base_word) and candidate.lower() != self.base_word
        ]
