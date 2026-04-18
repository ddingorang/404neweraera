#include <iostream>
using namespace std;

int main()
{
    int j;
    cin >> j;
    int sum = 0;
    
    for(int i=1; i<j+1; i++)
    {
        sum += i;
    }
    cout << sum << endl;
    
    return 0;
}