#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for(int k = 1;k<n+1;k++)
    {
        int i=k;
        while(i>0)
        {
            cout << "*";
            i--;
        }
        cout << '\n';

    }
    

}