#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int ans = 0, stop = 0;
        for (vector<int>::size_type i = 0; i < timeSeries.size(); ++i){
            ans += duration - max(stop - timeSeries[i], 0);
            stop = timeSeries[i] + duration;
        }
        return ans;
    }
};