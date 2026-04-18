#include <iostream>
using namespace std;

int main()
{
	int a;
	int b;
	cin >> a >> b;
	int one = b % 10;
	cout << a* one << endl;
	int two = b % 100 - one;
	cout << a * two /10 << endl;
	int three = b % 1000 - one - two;
	cout << a * three / 100 << endl;
	cout << a * b << endl;

	return 0;

}