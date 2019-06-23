#include <iostream>
using namespace std;

int main() {
  int t;
  cin>>t;
  for(int i=0;i<t;i++) {
    int n,score;
    int j=0;
    cin>>n;
    score=n;
    string s,u;
    cin>>s;  
    cin>>u;
    while(j<n) {
      if(u[j]=='N'){
        score=score-1;
        j=j+1;
        continue;
      }
      if((s[j]!=u[j])&&(j==n-1)){
        score=score-1;
        j=j+1;
        continue;
      }
      if(s[j]!=u[j]){
        score=score-2;
        j=j+2;
        continue;
      }
      j=j+1;
    }
  cout<<score<<endl;
  }
}