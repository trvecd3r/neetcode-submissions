class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new=Counter(nums)
        l=[]
        for i in new.most_common(k):
            l.append(i[0])
        return l