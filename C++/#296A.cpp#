// version 1
// greedy
#include<iostream>
using namespace std;

int main()
{
  int n,maxn=1,a[1000]={0};
  cin>>n;
  for(int i=0;i<n;++i){
    int tmp;
    cin>>tmp;
    ++a[tmp-1];
    maxn=max(maxn,a[tmp-1]);
  }
  //  cout<<"maxn:"<<maxn<<endl;
  cout<<(((n-maxn)>=maxn-1)?"YES":"NO")<<endl;
}
