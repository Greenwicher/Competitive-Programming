// version 1
#include<iostream>
using namespace std;

int main()
{
  int n,t[26]={0},flag=1;
  string s;

  cin>>n;cin>>s;
  for(int i=0;i<n;++i){
    t[tolower(s[i])-97]+=1;
  }
  for(int i=0;i<26;++i){
    flag*=t[i];
  }
  string ans = flag!=0?"YES":"NO";
  cout<<ans<<endl;
}
