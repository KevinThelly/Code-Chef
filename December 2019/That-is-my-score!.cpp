#include <iostream>
using namespace std;

int main() {
   int t,s,sub,total=0,num,score;
  //  int flag[9]={};
   cin>>t;
   for(int i=0;i<t;i++){
     total=0;
     int flag[9]={};
     cin>>sub;
     for(int j=0;j<sub;j++){
       cin>>num>>score;
       if(num>0 && num<9){
         if(flag[num]==0){
           total=total + score; 
           flag[num]=score;
           cout<<num<<":score:"<<score<<endl;
         }        
         else if(flag[num]<score){
           total=total-flag[num];
           total=total+score;
           flag[num]=score;
           cout<<num<<":score:"<<score<<endl;
         }
       }
     }
     cout<<total<<endl;

   }
 return 0;


}