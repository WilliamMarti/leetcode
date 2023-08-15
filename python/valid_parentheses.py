class Solution:
    def isValid(self, s: str) -> bool:

        # quick win
        # odd number of chars, must be invald
        if len(s) % 2 == 1:

            return False

        pairs = ["()", "{}", "[]"]

        replacement = True

        while replacement:

            replacement = False

            for pair in pairs:

                if pair in s:
                    s = s.replace(pair, "")
                    print(s)
                    replacement = True

        if len(s) == 0:

            return True

        else:

            return False