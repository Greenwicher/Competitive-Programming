/*
// version 1
// Time limit exceeded on test 9
#include<iostream>
#include<vector>
using namespace std;

int main()
{
  int n;
  cin>>n;
  long long a[n+1];a[0]=0;
  for(int i=1;i<=n;++i){
    int tmp;
    cin>>tmp;
    a[i]=a[i-1]+tmp;
  }

  if(a[n]%3!=0 || n<3){
    cout<<0<<endl;
  }
  else{
    long long sum;
    sum=a[n]/3;
    vector<int> l,r;
    for(int i=2;i<n;++i){
      if(a[i-1]==sum){
        l.push_back(i);
      }
      if (a[i]==2*sum){
        r.push_back(i);
      }
    }
    long long ans=0; // be careful about the range of ans
    for(int i=0;i<l.size();++i){
      for(int j=r.size()-1;j>=0;--j){
        if(r[j]>=l[i]){
          ++ans;
        }else{
          break;
        }
      }
    }

    cout<<ans<<endl;
  }
}
*/

// version 2
#include<iostream>
#include<vector>
using namespace std;

int main()
{
  int n;
  cin>>n;
  long long a[n+1];a[0]=0;
  for(int i=1;i<=n;++i){
    int tmp;
    cin>>tmp;
    a[i]=a[i-1]+tmp;
  }

  if(a[n]%3!=0 || n<3){
    cout<<0<<endl;
  }
  else{
    long long sum;
    sum=a[n]/3;
    vector<int> l,r;
    for(int i=2;i<n;++i){
      if(a[i-1]==sum){
        l.push_back(i);
      }
      if (a[i]==2*sum){
        r.push_back(i);
      }
    }
    long long ans=0;
    int lp=l.size(),rp=r.size()-1,m=r.size();
    while(lp--){
      while(r[rp]>=l[lp] and rp>=0){
        rp--;
      }
      ans+=m-rp-1;
    }
    cout<<ans<<endl;
  }
}
