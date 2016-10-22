#include<iostream>

using namespace std;

int main()
{
  int n,m;
  cin>>n;
  int a[n];
  for(int i=0;i<n;++i){
    cin>>a[i];
  }
  cin>>m;
  int b[m];
  for(int i=0;i<m;++i){
    cin>>b[i];
  }

  int ans=0,maxr=-1;
  for(int i=0;i<n;++i){
    for(int j=m-1;j>-1;--j){
      if(b[j]%a[i]==0){
        if(b[j]/a[i]>maxr){
          maxr = b[j]/a[i];
          ans = 1;
        }
        else if(b[j]/a[i]==maxr){
          ans += 1;
        }
        break;
      }
    }
  }

  cout<<ans<<endl;

  return 0;
}
