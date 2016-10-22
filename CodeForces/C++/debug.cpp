#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
  string s;
  cin>>s;
  for(int i=s.size()-1;s[i]=='z'||(++s[i],1);--i){
    cout<<"i is "<<i<<endl;
    s[i]='a';
    cout<<s[i]<<endl;
  }
  cout<<"The string s is "<<s<<endl;

}
