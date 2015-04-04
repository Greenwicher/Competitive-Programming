// version 1
#include<iostream>
#include<set>

using namespace std;

int main()
{
  int n,ans=0,num=0; // ans represents the size of the tree height while num represents the size of nodes visited currently
  cin>>n;
  int p[n+1];
  set<int> t1;
  for(int i=1;i<n+1;++i){
    cin>>p[i];
    if(p[i]==-1){
      t1.insert(i); // first layer of the tree
      ++num;
    }
  }
  ++ans;

  while(num<n){
    set<int> t2;
    // construct the next layer of the tree
    for(int i=1;i<n+1;++i){
      if(t1.find(p[i])!=t1.end()){
        t2.insert(i);
        ++num;
      }
    }
    ++ans;
    t1.clear();
    t1 = t2;
    //cout<<"The layer "<<ans<<" is: ";
    //copy(t1.begin(),t1.end(),ostream_iterator<int>(cout," "));
    cout<<endl;
  }

  cout<<ans<<endl;
}

/*
// version 2
// trace back to the origin from the bottom of the tree
#include <stdio.h>
int n,i,j,k,r,p[2020];
int main() {
  scanf("%d",&n);
  for (i=1; i<=n; i++) scanf("%d",&p[i]);
  for (i=1; i<=n; i++) {
    for (j=i, k=0; j!=-1; j=p[j], k++);
    if (k>r) r=k;
  }
  printf("%d\n",r);
  return 0;
}
*/

/*
// version 3
// similar with version 2
#include<stdio.h>
int a[2001];
int f(int p){
        if(a[p]==-1) return 1;
        return f(a[p])+1;
}
int main(){
        int n,i,best;
        scanf("%d",&n);
        for(i=1;i<=n;i++){
                scanf("%d",&a[i]);
        }
        best=0;
        for(i=1;i<=n;i++){
                if(f(i)>best) best=f(i);
        }
        printf("%d\n",best);
}
*/
