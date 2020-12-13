
class Solution:
    def __init__(self):
        self.target_n = 0
        self.target_list = []
        self.answer = []

    def shuffle(self, nums, n):
        target_n = n
        target_list = nums

        for i in range(0, target_n):
            print(target_list[i],target_list[target_n])
            self.answer.append(target_list[i])
            self.answer.append(target_list[target_n])
            target_n += 1
        return self.answer


List = [2,5,1,3,4,7]
n = 3
sol1 = Solution()
answer = sol1.shuffle(List,n)
print(answer)