#include <iostream>
using namespace std;

int main() {
  unsigned long t,n;
  unsigned long a;
  cin>>t;
  for(int i=0;i<t;i++){
    cin>>n;
    if(n==0){
        cout<<0<<endl;
        continue;
    }
    unsigned long sum=0;
    unsigned long k=n;
    while(k!=0){
      sum=sum+k%10;
      k=k/10;
    }
    if(sum%10!=0){
        a=n*10 + (10-(sum%10));
    }
    else{
        a=n*10;
    }
    cout<<a<<endl;
  }
  return 0;
}