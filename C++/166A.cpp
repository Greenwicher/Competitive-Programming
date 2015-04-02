// version 1
#include<iostream>

using namespace std;

int main()
{
  int n,k;
  cin>>n>>k;
  int a[n][2];
  for(int i=0;i<n;++i){ cin>>a[i][0]>>a[i][1]; }

  // sorting based on # of solved prolbems and penalty time
  for(int i=0;i<n-1;++i){
    int maxp=a[i][0],mint=a[i][1];
    int k=i;
    for(int j=i+1;j<n;++j){
      if(a[j][0]>maxp){
        maxp=a[j][0];
        mint=a[j][1];
        k=j;
      }
      else if((a[j][0]==maxp) and (a[j][1]<mint)){
          mint=a[j][1];
          k=j;
      }
    }
    int p=a[i][0],t=a[i][1];
    a[i][0]=a[k][0];a[i][1]=a[k][1];
    a[k][0]=p;a[k][1]=t;
  }

  // counting the # of kth palces
  int p=a[k-1][0],t=a[k-1][1];
  int i=k-2,j=k;
  while((i>-1) and (a[i][0]==p) and (a[i][1]==t)){--i;}
  while((j<n) and (a[j][0]==p) and (a[j][1]==t)){++j;}
  cout<<j-i-1<<endl;
}

/* //version 2
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
        int n,k;
        cin>>n>>k;
        pair<int,int>a[50];
        for(int i=0;i<n;i++)
        {
                cin>>a[i].first>>a[i].second;
                a[i].first*=-1;
        }
        sort(a,a+n);
        cout<<count(a,a+n,a[k-1])<<endl;
        return 0;
}
*/
