#include <iostream>

#define size 6

bool lowerDivisorExists(int j, int f) {
    for (int c = 1; c < f; c++){
        if (j%c == 0 && j/c < size) return true;
    }
    return false;
}

void show_arr(int **counters) {
    using namespace std;
    for (int i = 2; i<size; i++) {
        for (int j = 2; j < size; j++)
            cout<<counters[i][j]<<" ";
        cout<<endl;
    }

}

int getAnswer(int **counters){
    using namespace std;
    for (int i = 2; i<size; i++){
        int power = i*i; //power == i^f
        int limit = size;
        for (int f=2; power < size; f++){
            for (int j = 2; j<= limit; j++){
                if (j%f == 0){
                    int d = j/f; 
                    if (d<=size && lowerDivisorExists(j, f) ){
                        counters[power][d] = 0;
                    }
                }
            }
            limit = size*f;
            cout<<"limit: "<<limit<<endl;
            power *= i;
            cout<<"power: "<<power<<endl;
        }
    }
    show_arr(counters);
    int sum = 0;
    for (int i = 2; i<size; i++)
        for (int j = 2; j < size; j++)
            sum += counters[i][j];
    return sum;        
}


int main() {
    

    int **counters = new int*[size];
    for (int i=0;i<size;i++)
        *(counters+i)=new int[size];

    for (int i = 2; i<size; i++)
        for (int j = 2; j < size; j++)
            counters[i][j] = 1;

    using  namespace std;
    


    show_arr(counters);
    cout<<endl;
    cout<<getAnswer(counters)<<endl;


    for (int i = 0; i<size; i++)
        delete counters[i];

    return 0;
}
