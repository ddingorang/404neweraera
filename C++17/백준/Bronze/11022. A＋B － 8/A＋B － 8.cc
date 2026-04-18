#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int *arr = new int[2*n];
    for(int k = 0;k<n;k++)
    {
        cin >> arr[2*k] >> arr[2*k+1];
    }
    for(int i=0;i<n;i++)
    {
        cout << "Case #" << i+1 << ": " << 
        arr[2*i] << " + " << arr[2*i+1] << " = " << 
        arr[2*i]+arr[2*i+1] << '\n';
    }

}