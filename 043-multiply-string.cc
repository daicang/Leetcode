#include "leetcode.hh"

class Solution {
public:
    string multiply(string num1, string num2) {
        int s1 = num1.size();
        int s2 = num2.size();
        int size = s1 + s2;
        int *arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = 0;
        }

        for (int i = s1-1; i >= 0; i--) {
            for (int j = s2-1; j >= 0; j--) {
                int val = (num1[i] - '0') * (num2[j] - '0');
                int idx = i + j + 1;
                val += arr[idx];
                arr[idx] = val % 10;
                arr[idx-1] += val / 10;
            }
        }

        string result;
        bool zero = true;
        for (int i = 0; i < size; i++) {
            if (zero && arr[i] != 0) {
                zero = false;
            }
            if (!zero) {
                result += arr[i] + '0';
            }
        }
        delete[] arr;

        if (zero) {
            return string("0");
        }
        return result;
    }
};

int main() {
    Solution s = Solution();
    cout << s.multiply("123", "456") << endl;
    return 0;
}