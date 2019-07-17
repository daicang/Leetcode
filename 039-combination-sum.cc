#include "leetcode.hh"

class Solution {
public:
    void dfs(vector<vector<int>>& results, vector<int>& progress, vector<int>& candidates, int start, int target) {
        if (target == 0) {
            results.emplace_back(progress);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            int curr = candidates[i];
            if (curr > target) {
                break;
            }
            progress.push_back(curr);
            dfs(results, progress, candidates, i, target-curr);
            progress.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> progress;
        vector<vector<int>> result;

        sort(candidates.begin(), candidates.end());

        dfs(result, progress, candidates, 0, target);
        return result;
    }
};

