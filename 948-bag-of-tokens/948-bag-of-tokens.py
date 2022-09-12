class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # * Sort in ascending order.
        tokens.sort()
        cur_score = max_score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                cur_score += 1
                max_score = max(max_score, cur_score)
                left += 1
            elif cur_score >= 1:
                cur_score -= 1
                power += tokens[right]
                right -= 1
            else:
                break

        return max_score