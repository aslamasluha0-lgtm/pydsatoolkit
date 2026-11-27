class Solution(object):

    def reverseVowels(self, s):
        # Convert the string into a list because strings are immutable in Python.
        # Lists are mutable, so we can swap characters.
        s = list(s)

        # Initialize two pointers.
        # left starts at the beginning of the string.
        # right starts at the end of the string.
        left, right = 0, len(s) - 1

        # Create a set containing all vowels (both lowercase and uppercase).
        vowels = {"a", "e", "i", "o", "u",
                  "A", "E", "I", "O", "U"}

        # Continue until the two pointers meet or cross each other.
        while left < right:

            # Check whether the character at the left pointer is NOT a vowel.
            if s[left] not in vowels:

                # If it is not a vowel, move the left pointer one step forward.
                left = left + 1

            # Check whether the character at the right pointer is NOT a vowel.
            elif s[right] not in vowels:

                # If it is not a vowel, move the right pointer one step backward.
                right = right - 1

            else:
                # Both characters are vowels.
                # Swap the vowels at the left and right positions.
                s[left], s[right] = s[right], s[left]

                # Move the left pointer forward after swapping.
                left = left + 1

                # Move the right pointer backward after swapping.
                right = right - 1

        # Convert the list back into a string and return it.
        return "".join(s)