#include <vector>
#include <iostream>
#include <cmath>
int main(){
    using namespace std;
	int p=3,flag=0,size;
	vector<int> primes;
	primes.push_back(2);
	cout<<"Enter the position of the prime = ";
	cin>>size;

	while(primes.size()<size){
		for(auto x:primes){
			if(remainder(p,x)==0){
				flag=1;
				break;
			}
		}
		if(flag==0){
			primes.push_back(p);
		}
		flag=0;
		p++;
	}	
    for(int i=0;i<primes.size();i++)
    cout<<i+1<<"\tprime\t= "<<primes.at(i)<<endl;
	cout<<"The "<<primes.size()<<" th prime is "<<primes.back() << endl;
	return 0;

}
