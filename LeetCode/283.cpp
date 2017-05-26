#include <iostream>
#include <vector>

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int>::size_type i = 0;
        while (i < nums.size()){
            if (nums[i] == 0){
                vector<int>::size_type j = i + 1;
                while ((j < nums.size()) and (nums[j] == 0)) j++;
                if (j != nums.size()){
                    int tmp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = tmp;
                }
            }
            i += 1;
        }
    }
};