#include<iostream>

using namespace std;

int f(int a, int k)
{
  int b[k+1];
  for(int i=0;i<k+1;++i){
    b[i]=0;
  }

  while(a!=0){
    if(a%10<k+1){
      b[a%10]=1;
    }
    a/=10;
  }

  for(int i=0;i<k+1;++i){
    if (b[i]==0){
      return 0;
    }
  }
  return 1;
}

int main()
{
  int n,k,ans=0;
  cin>>n>>k;

  for(int i=0;i<n;++i){
    int a;
    cin>>a;
    ans+=f(a,k);
  }

  cout<<ans<<endl;
}
