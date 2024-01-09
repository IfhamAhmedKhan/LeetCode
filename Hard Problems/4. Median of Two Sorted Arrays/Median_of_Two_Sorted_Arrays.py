class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        # Find the length of the merged list
        length = len(nums1)

        # Check if the length is odd or even
        if length % 2 == 1:
            # Odd length, return the middle element
            median = nums1[length // 2]
        else:
            # Even length, return the average of two middle elements
            mid1 = length // 2
            mid2 = mid1 - 1
            median = (nums1[mid1] + nums1[mid2]) / 2.0

        return median