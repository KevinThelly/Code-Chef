#include <iostream>
using namespace std;

int main() {
  long t,n;
  long a;
  cin>>t;
  for(int i=0;i<t;i++){
    cin>>n;
    if(n==0){
        cout<<0<<endl;
        continue;
    }
    long sum=0;
    long k=n;
    while(k!=0){
      sum=sum+k%10;
      k=k/10;
    }
    a=n*10 + (10-(sum%10));
    cout<<a<<endl;
  }
  return 0;
}