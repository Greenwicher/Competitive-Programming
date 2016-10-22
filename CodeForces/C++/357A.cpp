#include<iostream>

using namespace std;

int main()
{
  int m,x,y,sum=0;
  cin>>m;
  int c[m];
  for(int i=0;i<m;++i){
    cin>>c[i];
    sum+=c[i];
  }
  cin>>x>>y;
  int beginner = 0;
  for(int i=0;i<m;++i){
    beginner+=c[i];
    if((x<=beginner) && (beginner<=y) && (x<=sum-beginner) && (sum-beginner<=y)){
      cout<<i+2<<endl;
      return 0;
    }
  }
  cout<<0<<endl;
  return 0;
}
