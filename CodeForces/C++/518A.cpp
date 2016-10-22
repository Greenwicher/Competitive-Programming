#include<iostream>

using namespace std;

int main()
{
  string s,t,ans1="",ans2="";
  cin>>s>>t;
  int k=0;
  while((k<s.size())&&(s[k]==t[k])){ans1+=s[k];ans2+=t[k];++k;}
  if((int)t[k]-(int)s[k]>1){
    ans1+=(char)(1+(int)s[k]);
  }else{
    ans1+=s[k];
    ans2+=t[k];
  }
  ++k;
  while(k<s.size()){
    if (s[k]!='z'){
      ans1+=(char)(1+(int)s[k]);
    }else{
      ans1+=s[k];
    }
    if (t[k]!='a'){
      ans2+=(char)((int)t[k]-1);
    }else{
      ans2+=t[k];
    }
    ++k;
  }

  if (ans1!=s){
    cout<<ans1<<endl;
  }
  else if(ans2!=t){
    cout<<ans2<<endl;
  }
  else
  {
    cout<<"No such string"<<endl;
  }

}


/* version 2
#include <iostream>
#include <string>

int main(){
  std::string s,t;std::cin>>s>>t;
  for(int i=s.size()-1;s[i]=='z'||(++s[i],0);--i)s[i]='a';
  std::cout<<(s!=t?s:"No such string")<<'\n';
}
*/

/* version 3
#include<iostream>
using namespace std;
int main()
{
    string s,t;
    cin>>s>>t;
  for(int i=s.length()-1;i>=0;i--){if(s[i]=='z')s[i]='a';else {s[i]++;break;}}
  (s<t)?cout<<s:cout<<"No such string";
}
 */
