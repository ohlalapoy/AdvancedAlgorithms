class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        xor_list = []
        for i in range(0,len(nums)): #find the duplicate numbers in list
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    xor_list.append(nums[j])
                    # XOR คือ ค่า ต่างกัน ได้ 1 | ค่าเหมือนกันให้ 0
                else: 
                    xor_list.append(0)
        #return xor_list
        #print(f"xor_list is: {xor_list}")

        xor_results = 0        
        for num in xor_list:
            xor_results ^= num
        return xor_results

                    
        #return xor_list 
number =[1,2,1,3]
test =  Solution()
print(test.duplicateNumbersXOR(number))       

### Runtime O(n^2) optimize laterrrr !!
