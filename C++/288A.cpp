#include<iostream>

using namespace std;

int main()
{
  int n = 0;
  int k = 0;
  cin>>n>>k;
  if ((n>=k) && (k>1)){
    string ans = "";
    for(int i=0;i<((n-k+2)/2);++i){
      ans+="ab";
    }
    if ((n-k+2)%2==1){
      ans+="a";
    }
    for(int i=0;i<k-2;++i){
      ans+= (char)(i+99);
    }
    cout<<ans<<endl;
  }
  else if ((k==1) && (n==1)){
    cout<<"a"<<endl;
  }
  else{
    cout<<"-1"<<endl;
  }
}
