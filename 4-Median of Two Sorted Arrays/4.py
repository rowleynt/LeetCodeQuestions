class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)
        if len(merged) % 2 != 0:
            return merged[len(merged)//2]
        else:
            return self.avg(merged[len(merged)//2], merged[(len(merged)//2) - 1])
            
    def merge(self, lst1, lst2):
        merged = []
        i, j = 0, 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                merged.append(lst1[i])
                i += 1
            else:
                merged.append(lst2[j])
                j += 1
        while i < len(lst1):
            merged.append(lst1[i])
            i += 1
        while j < len(lst2):
            merged.append(lst2[j])
            j += 1
        return merged

    def avg(self, n, m):
        return (n + m) / 2