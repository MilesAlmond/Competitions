class Solution:

    def generate_chain_code(self, input):
        word_list = input.split()
        new_word_list = list()
        for word in word_list:
            new_word = ''.join(sorted(word.lower()))
            for i in range(len(word)):
                if word[i] == word[i].upper() and word[i].isalpha():
                    dummy_list = list(new_word)
                    dummy_list[i] = dummy_list[i].upper()
                    new_word = ''.join(dummy_list)
            new_word_list.append(new_word)
        for w in new_word_list:
            if not w.isalnum():
                for i in range(len(w)):
                    if not w[i].isalnum():
                        dummy_fix = list(w)
                        dummy_fix_2 = dummy_fix.copy()
                        dummy_fix.remove(w[i])
                        index_find = new_word_list.index(w)
                        dummy_fix.insert(word_list[index_find].index(w[i]),w[i])
                        new = ''.join(dummy_fix)
                new_word_list[new_word_list.index(w)] = new
        answer = " ".join(new_word_list)   
        return answer
