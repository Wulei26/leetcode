#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    int lower_bound(vector<int>& nums, int left, int right, int target) {
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        // 首先对数组进行排序
        sort(nums.begin(), nums.end());
        long long ans = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            int low_target = lower - v;
            int high_target = upper - v + 1;              
            int l_index = lower_bound(nums, 0, i, low_target);   // 第一个 >= lower-v 的位置
            int r_index = lower_bound(nums, 0, i, high_target);  // 第一个 >= upper-v+1 的位置          
            r_index--;        
            ans += (r_index - l_index + 1); 

        }
        return ans;
    }
};