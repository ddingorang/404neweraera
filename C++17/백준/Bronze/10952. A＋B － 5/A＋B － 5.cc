#include <iostream>
using namespace std;

int main()
{
    int c = 0;
    int arr[1000];
    for(int k = 0;;k++)
    {
        cin >> arr[2*k] >> arr[2*k+1];
        if(arr[2*k]==0 && arr[2*k+1] == 0) break;
        c++;
    }
    for(int i=0;i<c;i++)
    {
        cout << arr[2*i] + arr[2*i+1] << '\n';
    }

    return 0;
}
