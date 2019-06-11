#include <iostream>
using namespace std;

int attendance(int d, string s,int c){
  int flag =0;
  int a;
  for(int i=2;i<d-2;i++){
    if(s[i]=='A'){
      if((s[i-1]=='P'||s[i-2]=='P')&&(s[i+1]=='P'||s[i+2]=='P')){
        c=c+1;
        flag=flag+1;
        a=(c*100)/d;
      }
      if(a>=75){
        return flag;
      }
    }
  }
  return -1;  
}

int main() {
  int t,d,c=0;
  int a;
  string s;
  cin>>t;
  for(int i=0;i<t;i++) {
    c=0;
    cin>>d;
    cin>>s;
    for(int i=0;i<d;i++) {
      if(s[i]=='P') {
        c++;
      }
    }
    a=(c*100)/d;
    if(a>=75){
      cout<<0<<endl;
    }
    else {
      int f=attendance(d,s,c);
      cout<<f<<endl;  
    }
  }
  return 0;
}