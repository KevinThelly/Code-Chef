#include <iostream>
using namespace std;

void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
}

int partition (int arr[], int low, int high,int d[]) 
{ 
    int pivot = arr[high];    // pivot 
    int i = (low - 1);  // Index of smaller element 
  
    for (int j = low; j <= high- 1; j++) 
    { 
        // If current element is smaller than or 
        // equal to pivot 
        if (arr[j] <= pivot) 
        { 
            i++;    // increment index of smaller element 
            swap(&arr[i], &arr[j]);
            swap(&d[i],&d[j]);
        } 
    } 
    swap(&arr[i + 1], &arr[high]); 
    swap(&d[i + 1], &d[high]); 
    return (i + 1); 
} 
  


void quickSort(int arr[], int low, int high,int d[]) 
{ 
    if (low < high) 
    { 
        /* pi is partitioning index, arr[p] is now 
           at right place */
        int pi = partition(arr, low, high,d); 
  
        // Separately sort elements before 
        // partition and after partition 
        quickSort(arr, low, pi - 1,d); 
        quickSort(arr, pi + 1, high,d); 
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
    quickSort(v,0,n,days);
    
    int same=days[n];
    int j=n-1;
    while(same==days[j]){
      j=j-1;
    }

    int best=v[n]+v[j];
    cout<<best<<endl;
  }
  return 0;
}