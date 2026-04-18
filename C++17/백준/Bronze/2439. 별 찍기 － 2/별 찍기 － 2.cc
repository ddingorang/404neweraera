#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for(int k = 1;k<n+1;k++)
    {
        int i=k;
        int j=n-k;
        while(j>0)
        {
            cout << " ";
            j--;
        }
        while(i>0)
        {
            cout << "*";
            i--;
        }
        cout << '\n';

    }
    

}