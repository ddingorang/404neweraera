#include <iostream>
using namespace std;

int hour(int a, int b)
{
	if (a == 0 && b < 45)
		return a + 23;
	else if (b < 45)
		return a-1;
	else
		return a;
}

int min(int k)
{
	if (k < 45)
		return 60 - (45 - k);
	else
		return k - 45;
}


int main()
{
	int h, m;
	cin >> h >> m;
	hour(h, m);
	min(m);
	

	cout << hour(h,m) << " " << min(m) << endl;

	return 0;
}
