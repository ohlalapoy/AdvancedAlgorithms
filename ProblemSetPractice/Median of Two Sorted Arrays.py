import statistics as st

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_num = nums1+nums2
        #print(new_num)
        Num_all = sorted(new_num)

        return st.median(Num_all)

nums1 = [1,2]
nums2 = [3,4]
test = Solution()
print(test.findMedianSortedArrays(nums1,nums2))