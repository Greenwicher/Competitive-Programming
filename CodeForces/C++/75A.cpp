#include<iostream>
//#include<math.h>

using namespace std;

int q(int n)
{
  //int p = 0;
  int p = 1;
  int ans = 0;
  while(n!=0){
    if(n%10!=0){
      //ans+=(n%10)*pow(10,p);
      ans+=(n%10)*p;
      p*=10;
    }
    n/=10;
  }
  return ans;
}

int main()
{
  int a,b,c;
  cin>>a>>b;
  c = a + b;
  //cout<<q(a)<<endl;
  //cout<<q(c)<<endl;
  if (q(a) + q(b) == q(c)){
    cout<<"YES"<<endl;
  }
  else{
    cout<<"NO"<<endl;
  }
}
