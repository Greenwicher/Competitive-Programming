/*
// version 1
//Wrong answer on test 3
//Wrong understanding of the problem, I thougt the subsegment of the sequence could also be not continuous
#include<iostream>
using namespace std;

int main()
{
  int n;
  cin>>n;
  int f[n][2],a[n],b[n];

  for(int i=0;i<n;++i){cin>>a[i];}

  f[0][0]=1;f[0][1]=0;b[0]=100001;
  for(int i=1;i<n;++i){
    f[i][0]=1;f[i][1]=0;b[i]=100001;
    int max1=0,max2=0,k1=100001;
    for(int j=0;j<i;++j){
      //f[i][0]=max(f[i][0],f[j][0]*(a[i]>a[j])+1);
      if(a[i]>a[j]){
        f[i][0]=max(f[i][0],f[j][0]+1);
      }
      if(a[i]<=a[j]){
        if(f[j][0]+1>max1){
          max1=f[j][0]+1;k1=a[j];
        }
      }
      if(a[i]>b[j]){
        if(f[j][1]+1>max2){
          max2=f[j][1]+1;
        }
      }
    }
    if(max2>max1){
      f[i][1]=max2;b[i]=a[i];
    }
    else if(max2<max1){
      f[i][1]=max1;b[i]=k1;
    }
    else if(max2==max1){
      f[i][1]=max1;b[i]=min(a[i],k1)*(max1!=0)+100001*(max1==0);
    }
    //cout<<i<<" f[i][0]="<<f[i][0]<<" a[i]=\t"<<a[i]<<endl;
    cout<<f[i][0]<<"\t"<<a[i]<<endl;
    //    cout<<i<<" f[i][1] "<<f[i][1]<<endl;
  }

  int ans=-1;int ans2=-1;
  for(int i=0;i<n;++i){
    ans=max(ans,max(f[i][0],f[i][1]));
    ans2=max(ans2,f[i][0]);
  }
  cout<<ans<<endl;
  cout<<ans2<<endl;

}
*/

/*
// version 2
#include<iostream>
using namespace std;

int main()
{
  int n;
  cin>>n;
  int f[n][2][2],a[n],ans=1;
  for(int i=0;i<n;++i){cin>>a[i];}

  //cout<<"**************"<<endl;

  f[0][0][0]=1;f[0][0][1]=0;f[0][1][0]=0;f[0][1][1]=0;
  for(int i=1;i<n;++i){
    f[i][0][0]=max(1,(f[i-1][0][0]+1)*(a[i]>a[i-1]));
    f[i][0][1]=(f[i-1][0][0]+1)*(a[i]<=a[i-1]);
    f[i][1][0]=(f[i-1][0][1]+1)*(((a[i]-a[i-2]<=1)&&(a[i-1]-a[i-3]>1)) || (a[i]-a[i-2]>1) || ((i==2)&&(a[i]>a[i-1])))*(f[i-1][0][1]!=0)*(i>=2);
    f[i][1][1]=(max(f[i-1][1][0],f[i-1][1][1])+1)*(a[i]>a[i-1])*(f[i-1][1][0]!=0 || f[i-1][1][1]!=0);
    //cout<<"i="<<i<<" "<<f[i][0][0]<<" "<<f[i][0][1]<<" "<<f[i][1][0]<<" "<<f[i][1][1]<<endl;
    for(int j=0;j<2;++j){
      for(int k=0;k<2;++k){
        ans=max(ans,f[i][j][k]);
      }
    }
  }

  cout<<ans<<endl;
}
*/

// version 3
// greedy and enumerate
#include<iostream>
#include<vector>
using namespace std;

int main()
{
  int n,ans=1;
  cin>>n;
  vector<int> a,b;
  a.push_back(-1);
  b.push_back(1);
  for(int i=1;i<n+1;++i){
    int ai;cin>>ai;
    a.push_back(ai);
    if(a[i]<=a[i-1]){
      b.push_back(i);
    }
  }
  a.push_back(100002);
  b.push_back(n+1);
  for(int i=1;i<(b.size()-1);++i){
    int k=b[i];
    if((a[k+1]-1>a[k-1])||(a[k]-1>a[k-2])){
      ans=max(ans,b[i+1]-b[i-1]);
    }
    ans=max(ans,b[i]-b[i-1]+1);
    ans=max(ans,b[i+1]-b[i]+1);
  }
  if(b.size()==2){ans=n;}
  cout<<ans<<endl;

  //for(int i=0;i<b.size();++i){cout<<b[i]<<" ";}
  //cout<<endl;

}
