class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        last = self.initializeList(-1, 26)
        last2 = self.initializeList(-1, 26)

        result = 0

        for i, char in enumerate(s):
            idx = self.calculateIndex(char)
            result = self.calculateContribution(i, last[idx], idx, last, last2, MOD, result)
            self.updatePositions(idx, i, last, last2)

        for i in range(26):
            result = self.finalizeContribution(n, last, last2, i, MOD, result)

        return result

    def initializeList(self, value: int, count: int) -> list[int]:
        return [value] * count

    def calculateIndex(self, character: str) -> int:
        # Map uppercase A-Z to 0-25
        return ord(character) - ord('A')

    def calculateContribution(
        self,
        currentIndex: int,
        lastIndex: int,
        charIndex: int,
        lastPositions: list[int],
        lastPositions2: list[int],
        modulus: int,
        currentResult: int,
    ) -> int:
        contribution = (currentIndex - lastIndex) * (lastIndex - lastPositions2[charIndex])
        return (currentResult + contribution) % modulus

    def updatePositions(
        self,
        charIndex: int,
        currentIndex: int,
        lastPositions: list[int],
        lastPositions2: list[int],
    ) -> None:
        lastPositions2[charIndex] = lastPositions[charIndex]
        lastPositions[charIndex] = currentIndex

    def finalizeContribution(
        self,
        totalLength: int,
        lastPositions: list[int],
        lastPositions2: list[int],
        index: int,
        modulus: int,
        currentResult: int,
    ) -> int:
        contribution = (totalLength - lastPositions[index]) * (lastPositions[index] - lastPositions2[index])
        return (currentResult + contribution) % modulus