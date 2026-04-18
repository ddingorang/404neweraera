#include <iostream>
using namespace std;

int **arr1;
int **arr2;
int row, column;

void newarray(int **arr) {
    for(int i=0; i<row; i++) {
        for(int j=0; j<column; j++){
            cin >> arr[i][j];
        }
    }
}

int main()
{
    cin >> row >> column;
    int **arr1 = new int*[row];
    for(int i=0; i<row; i++ ) {
        arr1[i] = new int[column];
    }
    int **arr2 = new int*[row];
    for(int j=0; j<row; j++ ) {
        arr2[j] = new int[column];
    }
    newarray(arr1);
    newarray(arr2);
    for(int k=0; k<row; k++) {
        for(int l=0; l<column; l++){
            arr2[k][l] = arr1[k][l] + arr2[k][l];
        }
    }
    for(int i=0; i<row; i++) {
        for(int j=0; j<column; j++){
            cout << arr2[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
