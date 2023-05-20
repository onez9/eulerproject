#include <bits/c++config.h>
#include <cstddef>
#include <iostream>

bool check(int n) {
    for(std::size_t i=2;i<n;++i){
        if (n%i==0) return false;
    }


    return true;
}

void func(int n) {
    using namespace std;
    int acc=0;
    int count=2;
    while (true){

        if (check(count)) {
            acc++;
            cout<<acc<<" "<<count<<endl;
            if (acc==n) break;
        }
        count++;
    }

}

int main(){
    using namespace std;
    size_t n;
    cin>>n;
    func(n);
    return 0;

}
