#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    int index=1;
    int arr[9];
    for(int i=0;i<9;i++)
    {
        cin >> arr[i];
    }
    //int min = arr[0];
    int max = arr[0];

    /*for(int i=0;i<9;i++)
    {
        if(arr[i]<min) min = arr[i];     
    }*/

    for(int i=0;i<9;i++)
    {
        if(arr[i]>max) 
        {
            max = arr[i];
            index = i+1;
        }
    }
    cout << max << '\n';
    cout << index;
}
