#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    int n, k;
    cin >> n;
    k=n;
    int left, right;
    int newright, newnum;
    int count=0;
    
    for(;;)
    {
        left = n/10;
        right = n%10;
        newright = (left + right)%10;
        newnum = right*10 + newright;
        count++;
        if(newnum==k) break;
        n=newnum;
    }
    
    cout << count;
    
    
}
