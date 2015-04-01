#include<iostream>

using namespace std;

int main()
{
  int n,k=0,mint=INT_MAX,mins=0;
  cin>>n;

  for(int i=0;i<n;++i){
    int t;
    cin>>t;
    if (t<mint){
      mint=t;
      k=i+1;
      mins=1;
    }
    else if (t==mint){
      ++mins;
    }
  }

  if (mins==1){
    cout<<k<<endl;
  }else{
    cout<<"Still Rozdil"<<endl;
  }

}
