buttons = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution:
    def letterCombinations(self, digits: str, l: List[str] = []) -> List[str]:
        if digits == "":
            return l

        big_list = []
        letter_combo = list(buttons[digits[0]])
        if len(l) == 0:
            big_list = letter_combo
        else:
            for i in l:
                letter_list = []
                for letter in list(buttons[digits[0]]):
                    letter_list.append(i + letter)
                big_list.extend(letter_list)

        return self.letterCombinations(digits[1:], big_list)