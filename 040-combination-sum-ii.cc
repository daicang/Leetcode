#include "leetcode.hh"

class Solution {
public:
    void dfs(vector<vector<int>>& results, vector<int>& progress,
             vector<int>& candidates, int start, int target, map<int, int>& counter) {
        if (target == 0) {
            results.emplace_back(progress);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            int curr = candidates[i];
            if (curr > target) {
                break;
            }

            for (int j = 1; j <= counter[curr]; j++) {
                for (int k = 0; k < j; k++) {
                    progress.push_back(curr);
                }
                dfs(results, progress, candidates, i+1, target-curr*j, counter);
                for (int k = 0; k < j; k++) {
                    progress.pop_back();
                }
            }
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> progress;
        vector<vector<int>> result;
        map<int, int> counter;

        sort(candidates.begin(), candidates.end());

        for (int i = 0; i < candidates.size(); i++) {
            if (counter.find(candidates[i]) == counter.end()) {
                counter[candidates[i]] = 1;
            } else {
                counter[candidates[i]]++;
            }
        }

        candidates.erase(unique(candidates.begin(), candidates.end()), candidates.end());

        dfs(result, progress, candidates, 0, target, counter);
        return result;
    }
};


int main() {
    auto s = Solution();
    // 1,1,6
    vector<int> vec {10,1,2,7,6,1,5};
    auto result = s.combinationSum2(vec, 8);
    print_2d_vec(result);
    return 0;
}
