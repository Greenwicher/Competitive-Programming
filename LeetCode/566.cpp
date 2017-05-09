#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > matrixReshape(vector<vector<int> >& nums, int r, int c) {
      vector<vector<int> >::size_type _r = nums.size();
      vector<int>::size_type _c = nums[0].size();
      if (_r * _c == r * c) {
        vector<vector<int> > ans(r, vector<int>(c));
        for(int i = 0; i < r; ++i){
          for(int j = 0; j < c; ++j){
            int id = j + i * c;
            ans[i][j] = nums[int(id / _c)][id % _c];
          }
        }
        return ans;
      }
      else{
        return nums;
      }
    }
};


int main(){
  int _r, _c, r, c;
  cout << "_r and _c?" << endl;
  cin >> _r >> _c;
  cout << "matrix?" << endl;
  vector<vector<int> > nums(_r, vector<int>(_c));
  for (int i = 0; i < _r; ++i){
    for (int j = 0; j < _c; ++j){
      cin >> nums[i][j];
    }
  }
  cout << "r and c?" << endl;
  cin >> r >> c;
  Solution s;
  vector<vector<int> > ans = s.matrixReshape(nums, r, c);
  cout << "matrix after reshape:" << endl;
  r = ans.size();
  c = ans[0].size();
  for (int i = 0; i < r; ++i){
    for (int j = 0; j < c; ++ j){
      cout << ans[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
