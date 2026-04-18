#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    
    int n;
    cin >> n;

    int *arr = new int[n];
    for(int i=0;i<n;i++)
    {
        cin >> arr[i];
    }
    int min = arr[0];
    int max = arr[0];

    for(int i=0;i<n;i++)
    {
        if(arr[i]<min) min = arr[i];     
    }

    for(int i=0;i<n;i++)
    {
        if(arr[i]>max) max = arr[i];
    }
    cout << min << " " << max;

    return 0;
}
