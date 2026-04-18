#include <iostream>
using namespace std;

int main()
{
    int hr, mn, time;
    cin >> hr >> mn;
    cin >> time;
    
    if(mn + time < 60)
    {
        cout << hr << " " << mn + time;
    }

    else if(mn + time>=60)
    {
        mn = mn+time-60;
        hr++;
        while(mn>=60)
        {
            mn -= 60;
            hr++;
            if(hr>23) break;
        }
        if(hr>23)
        {
        hr = 0;
        while(mn>=60)
            {
            mn -= 60;
            hr++;
            }
        }

        cout << hr << " " << mn;
    }

    return 0;
}