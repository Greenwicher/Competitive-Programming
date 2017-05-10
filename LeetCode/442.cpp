#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Version 1, Reverse the number of index every time we meet the index
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
      vector<int> ans;
      for(vector<int>::size_type i = 0; i < nums.size(); ++i){
        if (nums[abs(nums[i])-1] < 0)
          ans.push_back(abs(nums[i]));
        else
          nums[abs(nums[i])-1] *= -1;
      }
      return ans;
    }
};

// Version 2, Put x in nums[x-1], then check each nums[x] == x + 1
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        int i = 0;
        while (i < nums.size()) {
            if (nums[i] != nums[nums[i]-1]) swap(nums[i], nums[nums[i]-1]);
            else i++;
        }
        for (i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) res.push_back(nums[i]);
        }
        return res;
    }
};


int main(){
  cout << "nums? (with exit code -1)" << endl;
  int num;
  vector<int> nums;
  while(cin >> num){
    if (num + 1 == 0)
      break;
    nums.push_back(num);
  }
  Solution s;
  vector<int> ans = s.findDuplicates(nums);
  for (vector<int>::size_type i = 0; i < ans.size(); ++i){
    cout << ans[i] << " ";
  }
  cout << endl;
  return 0;
}
