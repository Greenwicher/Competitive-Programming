#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
      int ans = -1;
      int l = 0;
      for (vector<int>::size_type i = 0; i < nums.size(); ++i){
        if (nums[i] == 1){
          l += 1;
        } else {
          ans = max(l, ans);
          l = 0;
        }
      }
      ans = max(l, ans);
      return ans;
    }
};

int main(){
  int num;
  vector<int> nums;
  cout << "nums? (with exit code -1)" << endl;
  while (cin >> num){
    if (num + 1 == 0) break;
    nums.push_back(num);
  }
  Solution s;
  cout << s.findMaxConsecutiveOnes(nums) << endl;
  return 0;
}
