class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        Check if n new flowers can be planted in the flowerbed
        without placing two flowers next to each other.

        :type flowerbed: List[int]  (0 = empty plot, 1 = planted plot)
        :type n: int                (number of flowers we want to plant)
        :rtype: bool

        Time Complexity:  O(n) - one pass through the list
        Space Complexity: O(n) - a padded copy of the list is created
        """

        # Pad both ends with 0 so the first and last plots can be treated
        # like any other plot (no special edge-case checks needed).
        # Example: [1,0,0,0,1] -> [0,1,0,0,0,1,0]
        f = [0] + flowerbed + [0]

        # Loop over the real plots only: skip the padding at index 0
        # and at the last index.
        for i in range(1, len(f) - 1):

            # A flower can be planted at i only if the left neighbour,
            # the current plot, and the right neighbour are all empty.
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:

                # Plant a flower here. Marking it as 1 makes sure the
                # next plot sees it as occupied and won't plant beside it.
                f[i] = 1

                # One flower placed, so one fewer left to plant.
                n = n - 1

        # If n is 0 or less, we planted at least as many flowers as needed.
        return n <= 0