//version 1
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
  int n;
  cin>>n;
  int x[n];
  for(int i=0;i<n;++i){cin>>x[i];}
  // sorting
  sort(x,x+n);
  // constructing the piles as minumum as possible
  int p[100];
  for(int i=0;i<100;++i){p[i]=0;}
  for(int i=0;i<n;++i){
    int k=0;
    // find the appropriate pile to put box i
    while(1){
      if (x[i]>=p[k]){++p[k];break;}
      ++k;
    }
  }
  // calculate the # of piles
  int ans=0;
  for(int i=0;i<100;++i){
    ans+=1*(p[i]!=0);
  }
  cout<<ans<<endl;
}

/*
//version 2
#include<bits/stdc++.h>
using namespace std;
int n,i,k,d[105];
int main(){
cin>>n;
for(i=0;i<n;i++){
cin>>d[i];
}
sort(d,d+n);
for(i=0;i<n;i++){
if(k*d[i]+k<=i) k++;
}
cout<<k<<endl;
return 0;
}
*/


/*
// version 3
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 111;
int N;
int ar[MAXN];

int main() {
  scanf("%d", &N);
  for(int i = 0; i < N; ++i) {
    scanf("%d",ar + i);
  }
  sort(ar, ar + N);

  int ans = 1;
  for(int i = 0; i < N; ++i) {
    int val = (ar[i] + i + 1) / (ar[i] + 1);
    if (val > ans) ans = val;
  }


  printf("%d\n", ans);
  return 0;
}
*/
