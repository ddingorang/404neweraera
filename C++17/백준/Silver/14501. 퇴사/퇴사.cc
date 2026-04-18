#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

static vector<int> task;
static vector<int> pay;
static vector<int> dp;

int main() {
	int n;
	cin >> n;
	
	task.resize(n+1);
	pay.resize(n+1);
	dp.resize(n+2);

	for (int i = 1; i <= n; i++) {
		cin >> task[i] >> pay[i];
	}

	for (int j = n; j > 0; j--) {
		if (j + task[j] > n + 1) {
			dp[j] = dp[j + 1];
		}
		else {
			dp[j] = max(dp[j + 1], pay[j] + dp[j + task[j]]);
		}
	}

	cout << dp[1];

}