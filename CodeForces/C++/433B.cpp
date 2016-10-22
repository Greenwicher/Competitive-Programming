// version 1
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
  int n,m,type,l,r;
  cin>>n;
  int v[n];
  long long a[n+1],b[n+1];
  a[0]=0;b[0]=0;

  for(int i=1;i<n+1;++i){
    cin>>v[i];
    a[i]=a[i-1]+v[i];
  }

  sort(v+1,v+n+1);
  for(int i=1;i<n+1;++i){
    b[i]=b[i-1]+v[i];
  }

  cin>>m;
  for(int i=0;i<m;++i){
    cin>>type>>l>>r;
    if(type==1){
      cout<<a[r]-a[l-1]<<endl;
    }else{
      cout<<b[r]-b[l-1]<<endl;
    }
  }
}

/*
// version 2 elegant for loop
#include<bits/stdc++.h>
using namespace std;
long long n, a[100005],x, b[100005],i=1,m,z,y;
int main()
{
    ios_base::sync_with_stdio(false);
    for (cin >> n; i <= n; cin >> a[i], b[i] = a[i], ++i);
    sort(b+1, b + n+1);
    for (i = 2; i <= n; b[i] += b[i - 1], a[i] += a[i - 1], ++i);
    for (cin >> m; m--; cin >> z >> x >> y, cout << ((z == 1) ? a[y] - a[x - 1] : b[y] - b[x - 1])<<endl);
    return 0;
}
*/
