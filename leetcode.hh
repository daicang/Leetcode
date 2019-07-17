#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <deque>
#include <utility>
#include <map>
#include <algorithm>

using namespace std;

void print_2d_vec(vector<vector<int>> vec) {
    for (int i = 0; i < vec.size(); i++) {
        for (int j = 0; j < vec[i].size(); j++) {
            cout << vec[i][j] << " ";
        }
        cout << endl;
    }
}
