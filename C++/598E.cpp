#include<iostream>
using namespace std;
int t,n,m,k;
int INF = 1e99;
int f[31][31][51] = {{{-1}}};

// dynamic programming with memoization
int dp(int n, int m, int k){
  if(k>n*m || n<=0 || m<=0 || k<=0){
    return INF;
  }else if(k == n*m){
    return 0;
  }else if(n==1 || m==1){
    return 1;
  }else if(f[n][m][k] != -1){
    return f[n][m][k];
  }else{
    double cost = INF;
    double n2 = n*n;
    double m2 = m*m;
    for(int i=1;i<n;++i){
      cost = min(min(f[i][m][k]+m2, dp(n-i,m,k-i*m)+m2), cost);
    }
    for(int j=1;j<m;++j){
      cost = min(min(f[n][j][k]+n2, dp(n,m-j,k-n*j)+n2), cost);
    }
    return cost;
  }
}

int main(){

  for(int i=0;i<31;++i){
    for(int j=0;j<31;++j){
      for(int k=0;k<51;++k){
        f[i][j][k] = -1;
      }
    }
  }

  // pre-processing
  for(int i=1;i<31;++i){
    for(int j=1;j<31;++j){
      for(int k=1;k<51;++k){
        f[i][j][k] = dp(i,j,k);
      }
    }
  }
  // output solutions
  cin>>t;
  for(int i=0;i<t;++i){
    cin>>n>>m>>k;
    cout<<f[n][m][k]<<endl;
  }
}
