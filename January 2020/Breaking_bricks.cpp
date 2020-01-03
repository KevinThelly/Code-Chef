#include <iostream>
using namespace std;

int main() {
  int t,s,w[3];
  cin>>t;
  for(int i=0;i<t;i++){
    cin>>s>>w[0]>>w[1]>>w[2];
    int ans=0;

    if(w[0]+w[1]>s){
      if(w[1]+w[2]>s){
        ans=3;
      }
      else{
        ans=2;
      }
    }

    else if(w[2]+w[1]>s){
      if(w[1]+w[0]>s){
        ans=3;
      }
      else{
        ans=2;
      }
    }

    else if(w[0]+w[1]+w[2]>s){
      ans=2;
    }

    else{
      ans =1;
    }

    cout<<ans<<endl;
  }

  

}