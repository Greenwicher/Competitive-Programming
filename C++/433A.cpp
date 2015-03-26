#include<iostream>

using namespace std;

int main()
{
  int n,a=0,b=0;
  cin>>n;
  for(int i=0;i<n;++i){
    int w;
    cin>>w;
    if (w==100){
      ++a;
    }else{
      ++b;
    }
  }
  if((a%2==0 && b%2==0) || (b%2==1 && (a>=2 && a%2==0))){
    cout<<"YES"<<endl;
  }else{
    cout<<"NO"<<endl;
  }
}
