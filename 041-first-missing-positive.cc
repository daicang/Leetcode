#include "leetcode.hh"



class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        bool has_1 = false;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                has_1 = true;
            } else if (nums[i] < 1 || nums[i] > nums.size()) {
                nums[i] = 1;
            }
        }
        if (!has_1) {
            return 1;
        }

        for (int i = 0; i < nums.size(); i++) {
            int idx = abs(nums[i])-1;
            if (nums[idx] > 0) {
                nums[idx] = -nums[idx];
            }
        }

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                return i+1;
            }
        }
        return nums.size() + 1;
    }
};