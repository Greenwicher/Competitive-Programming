#include<iostream>

using namespace std;

int main()
{
  int n;
  cin>>n;

  int r[n],c[n];
  for(int i=0;i<n;++i){
    r[i]=0;
    c[i]=0;
  }

  for(int i=0;i<n;++i){
    for(int j=0;j<n;++j){
      int s;
      cin>>s;
      r[i]+=s;
      c[j]+=s;
    }
  }

  int ans=0;
  for(int i=0;i<n;++i){
    for(int j=0;j<n;++j){
      if (c[j]>r[i]){
        ++ans;
      }
    }
  }

  cout<<ans<<endl;

}
