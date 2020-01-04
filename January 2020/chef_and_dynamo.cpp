#include <iostream>
using namespace std;

long unsigned int maximum(int n){
  long unsigned int sum=9;
  while(n>1){
    sum = sum*10 + 9;
    n--; 
  }
  return sum;
}

long unsigned int minimum(int n){
  long unsigned int sum=10;
  if(n==1){
    return 1;
  }

  else{
    while(n>2){
      sum=sum*10;
      n--;
    }
  }

  return sum;
}

int main() {
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    long unsigned int a,b,c,s;
    int n,val;
    cin>>n>>a;
    s = a + 2*maximum(n) + 2*minimum(n) ;
    cout<<s<<endl;
    cin>>b;
    c = maximum(n) + minimum(n) - b ;
    cout<<c<<endl;
    cin>>b;
    c = maximum(n) + minimum(n) - b ;
    cout<<c<<endl;
    cin>>val;
    if(val==-1){
      return 0;
    }
  }

}