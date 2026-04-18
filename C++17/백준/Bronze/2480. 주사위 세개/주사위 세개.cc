#include <iostream>
using namespace std;

int main()
{
    int one, two, three;
    int sum;
    cin >> one >> two >> three;

    if(one==two && two==three)
    {
        sum = 10000 + one * 1000;
        cout << sum;
    }
    else if(one==two && two != three)
    {
        sum = 1000 + one * 100;
        cout << sum;
    }
    else if(one==three && two != three)
    {
        sum = 1000 + one * 100;
        cout << sum;
    }
    else if(two==three && one != three)
    {
        sum = 1000 + two * 100;
        cout << sum;
    }

    else
    {
        int max = one;
        if(max < two || max < three) {
            max = two;
            if(max < three) {
                max = three;
            }
        }
        sum = max * 100;
        cout << sum;
    }
}