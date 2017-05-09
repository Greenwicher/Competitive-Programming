#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// int arrayPairSum(int* nums, int numsSize) {
//   sort(nums, nums + numsSize);
//   int ans = 0;
//   for (int i = 0; i < numsSize; i = i + 2){
//     ans += nums[i];
//   }
//   return ans;
// }

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
      int ans = 0;
      vector<int>::size_type size = nums.size();
      sort(nums.begin(), nums.end());
      for (int i = 0; i < size; i = i + 2){
        ans += nums[i];
      }
      return ans;
    }
};

int main(){
  int numsSize;
  cout << "numsSize?" << endl;
  cin >> numsSize;
  // int nums[numsSize];
  vector<int> nums;
  cout << "nums?" << endl;
  // for(int i = 0; i < numsSize; ++i){
  //   cin >> nums[i];
  // }
  for (int i = 0; i < numsSize; ++i){
    int t;
    cin >> t;
    nums.push_back(t);
  }
  Solution s;
  cout << "ans = " << s.arrayPairSum(nums) << endl;
  return 0;
}
