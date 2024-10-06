class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        size1 = len(sentence1)
        size2 = len(sentence2)

        # return right away if the sentences are the same
        if sentence1 == sentence2:
            return True
        # switch the longer sentence to be 1
        elif size1 < size2:
            sentence1, sentence2 = sentence2, sentence1
            size1, size2 = size2, size1
        
        # find longest prefix
        long_prefix = 0
        if sentence1[0] == sentence2[0]:
            for i in range(1, size2):
                if sentence1[i] != sentence2[i]:
                    long_prefix = i
                    break

            if long_prefix == 0 and sentence1[size2] == " ":
                long_prefix = size2 # max size

        # finx longest suffix
        long_suffix = 0
        if sentence1[-1] == sentence2[-1]:
            for i in range(2, size2 + 1):
                if sentence1[-i] != sentence2[-i]:
                    long_suffix = i - 1
                    break   

            if long_suffix == 0 and sentence1[-size2 - 1] == " ":
                long_suffix = size2 # max size
        
        common_lim = min(long_prefix, long_suffix)
        # find longest common of prefix and suffix (if exists)
        if sentence1[common_lim - 1] == sentence1[-common_lim]:
            long_common = 1

            while long_common <= common_lim and sentence1[common_lim - 1 - long_common] == sentence1[-common_lim + long_common]:
                long_common += 1
            
            if long_prefix + long_suffix - long_common == size2:
                return True
        
        # print(long_prefix)
        # print(long_suffix)
        # print(long_common)
        # print(size2)

        if long_prefix == size2 or long_suffix == size2:
            return True # smaller sentence fills either end of longer sentence
        elif long_prefix + long_suffix - 1 == size2:
            return True # the middle of smaller sentence can be inserted to form longer sentence
        
        return False

        