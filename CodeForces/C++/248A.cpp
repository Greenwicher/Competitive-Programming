// version 1
#include<iostream>

using namespace std;

int main()
{
  int n,a=0,b=0;
  cin>>n;
  for(int i=0;i<n;++i){
    int l,r;
    cin>>l>>r;
    a+=1*(l==0);
    b+=1*(r==0);
  }
  cout<<min(a,n-a)+min(b,n-b)<<endl;
}

/*
// version 2
// no need to check "l==0", since r and l are already boolean
#include<iostream>
using namespace std;
int n,a,b,c,d;
int main() {
    cin >> n;
    for (int i=0; i<n; i++) {cin >> c >> d; a+=c; b+=d;}
    cout << min(a,n-a) + min(b,n-b);
}
*/
