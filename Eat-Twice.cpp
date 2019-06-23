#include <iostream>
using namespace std;

void selectionSort(int a[], int n,int d[]) {
   int i, j, min, temp,temp2;
   for (i = 0; i < n - 1; i++) {
      min = i;
      for (j = i + 1; j < n; j++)
         if (a[j] < a[min])
            min = j;
      temp = a[i];
      a[i] = a[min];
      a[min] = temp;

      temp2=d[i];
      d[i]=d[min];
      d[min]=temp2;
   }
}

int main() {
  int t;
  cin>>t;

  for(int i=0;i<t;i++) {
    int n,d;
    cin>>n>>d;
    int days[n],v[n];

    for(int j=0;j<n;j++) {
      cin>>days[j]>>v[j];      
    }
    selectionSort(v,n,days);
    
    int same=days[n-1];
    int j=n-2;
    while(same==days[j]){
      j=j-1;
    }
    int best=v[n-1]+v[j];
    cout<<best<<endl;
  }
  return 0;
}