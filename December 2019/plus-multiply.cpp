#include <iostream>
using namespace std;

int main() {
   int t,n,a;
   cin>>t;
   for(int i=0;i<t;i++){
     int ans=0,two=0,zero=0;
     cin>>n;
     for(int j=0;j<n;j++){
       cin>>a;
       if(a==2){
         two++;
       }
       if(a==0){
         zero++;
       }
     }
     two=(two*(two-1))/2;
     zero=(zero*(zero-1))/2;
     ans=two+zero;
     cout<<ans<<endl;
   }

   return 0;
}