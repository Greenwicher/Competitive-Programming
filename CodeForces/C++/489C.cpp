// version 1
#include<iostream>
#include<sstream>
#include<algorithm>
using namespace std;

string construct(int m,int s)
{
  string minimum="",maximum="",tmp="";

  // construct maximum
  maximum += string(s/9,'9');
  if(s/9<m){
    maximum += (char)((int)('0')+s%9)+string(m-s/9-1,'0');
  }

  // construct minimum
  tmp = maximum;
  reverse(tmp.begin(),tmp.end());
  if((tmp[0]=='0') and (m>1)){
    tmp[0]='1';
    for(int i=1;i<m;++i){
      if(tmp[i]!='0'){
        tmp[i]=(char)((int)tmp[i]-1);
        break;
      }
    }
  }
  minimum = tmp;

  return minimum+" "+maximum;
}

int main()
{
  int m,s;
  cin>>m>>s;
  cout<<((((s>0) and (float)(s)/(float)(m)<=9.0) or ((s==0) and (m==1)))?construct(m,s):"-1 -1")<<endl;
}

/*
// version 2
// quick way to convert digits into string "int + '0'"
#import<iostream>
using namespace std;
int m,s,t,i;
string x,y;
int main() {
        cin>>m>>s;
        if (s==0) {cout<<(m==1 ? "0 0":"-1 -1"); return 0;}
        for (i=0; i<m; i++) {
                t = min(s, 9);
                y += t + '0';
                s -= t;
        }
        if (s>0) {cout<<"-1 -1"; return 0;}
        for (i=m-1; i>=0; i--) x += y[i];
        for (i=0; x[i]=='0'; i++);
        x[i]--, x[0]++;
        cout<<x<<' '<<y;
}
*/
