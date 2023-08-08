class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # get the lowest length of one of the words so
        # we know where to stop
        lowest_count = sorted([len(n) for n in strs])[0]

        if lowest_count == 0:
            return ""

        # start with initial letter
        test_letter = strs[0][0]
        prefix = ""
        end = False

        for i in range(0, lowest_count):

            test_letter = strs[0][i]
            #print(test_letter)

            for word in strs:

                if word[i] != test_letter:

                    end = True
                    break

            # if there wasn't a match, quit
            if end:

                break

            prefix = f"{prefix}{test_letter}"

        return prefix