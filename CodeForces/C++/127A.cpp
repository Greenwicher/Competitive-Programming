#include<iostream>
#include<math.h>

using namespace std;

int main()
{
  int n;
  double k;
  cin>>n>>k;
  double d=0.0,x1,y1;
  cin>>x1>>y1;

  for(int i=0;i<n-1;++i){
    double x2,y2;
    cin>>x2>>y2;
    d+=sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
    x1=x2;
    y1=y2;
  }
  double ans = d*k/50.0;
  cout.precision(15);
  cout<<ans<<endl;
}
