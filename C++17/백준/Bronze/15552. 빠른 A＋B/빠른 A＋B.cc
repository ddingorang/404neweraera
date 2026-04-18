#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    int j;
    cin >> j;
    
    for(int i=0;i<j;i++)
    {
        int k, l;
        cin >> k;
        cin >> l;
        
        cout << k+l << '\n';
    }
}
