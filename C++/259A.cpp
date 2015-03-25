#include<iostream>

using namespace std;

int main()
{
  string a = "WBWBWBWB";
  string b = "BWBWBWBW";
  bool t = true;
  for(int i=0;i<8;++i){
    string c;
    cin>>c;
    if ((c!=a) && (c!=b)){
        t = false;
      }
  }
  string ans;
  ans = t?"YES":"NO";
  cout<<ans<<endl;
}
