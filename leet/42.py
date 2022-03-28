# trapping rain water

class Solution:
    def trap_twoPointer(self, height):
        if not height:
            return 0
        volume = 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[right]
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume