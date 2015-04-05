#include<iostream>
#include<vector>
#include<sstream>

using namespace std;

vector<int> find(string s){
  vector<int> sol;
  int r[6] = {1,2,3,4,6,12};

  for(int i=0;i<6;++i){
    int a,b;
    a=r[i];b=12/a;
    for(int j=1;j<=b;++j){
      int flag=0;
      for(int k=1;k<=a;++k){
        flag+=1*(s[(j-1)+(k-1)*b]=='X');
      }
      if(flag==a){
        sol.push_back(a);
        break;
      }
    }
  }
  return sol;
}

int main()
{
  int t;
  cin>>t;
  for(int i=0;i<t;++i){
    string s,ans="";
    cin>>s;
    vector<int> sol;
    sol=find(s);
    for(int j=0;j<sol.size();++j){
      ostringstream a,b;
      a<<sol[j];b<<12/sol[j];
      ans+=" "+a.str()+"x"+b.str();
    }
    cout<<sol.size()<<ans<<endl;
  }
}

/*
// version 2
// learn to use macro and elegant coding style
#include<iostream>
#include<cstdio>
#include<cassert>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#pragma comment(linker, "/STACK:640000000")
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define ll long long
#define bit __builtin_popcountll
#define sqr(x) (x) * (x)
#define forit(it,S) for(__typeof((S).begin()) it = (S).begin(); it != (S).end(); it++)
using namespace std;
typedef pair<int, int> pii;
const double eps = 1e-9;
const double pi = acos(-1.0);
int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    int t; cin >> t;
    while(t--) {
        string s; cin >> s;
        vector<int> v;
        for (int i = 1; i <= 12; i++) if (12 % i == 0) {
            bool yes = false;
            int a = i;
            int b = 12 / i;
            for (int j = 0; j < b; j++) {
                bool ok = true;
                for (int k = 0; k < a; k++) {
                    ok &= s[k * b + j] == 'X';
                }
                if (ok) yes = true;
            }
            if (yes) v.pb(i);
        }
        cout << sz(v);
        for (int i = 0; i < sz(v); i++) {
            cout << " ";
            cout << v[i] << "x" << 12 / v[i];
        }
        cout << endl;
    }
    return 0;
}
*/
