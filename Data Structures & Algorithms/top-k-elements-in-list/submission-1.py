class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new=Counter(nums)
        c=new.most_common(k)
        l=[]
        for i in c:
            l.append(i[0])
        return l