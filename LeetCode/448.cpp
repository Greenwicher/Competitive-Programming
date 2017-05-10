#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> ans;
        for (vector<int>::size_type i = 0; i < nums.size(); ++i){
            if (nums[abs(nums[i])-1] > 0)
                nums[abs(nums[i])-1] *= -1;
        }
        for (vector<int>::size_type i = 0; i < nums.size(); ++i)
            if (nums[i] > 0) ans.push_back(i+1);
        return ans;
    }
};


int main(){
    vector<int> nums;
    cout << "nums? (with exit code -1)" << endl;
    int num;
    while (cin >> num){
        if (num + 1 == 0)
            break;
        nums.push_back(num);
    }
    Solution s;
    vector<int> ans = s.findDisappearedNumbers(nums);
    for (vector<int>::size_type i = 0; i < ans.size(); ++i){
        cout << ans[i] << " ";
    }
    cout << endl;
}
