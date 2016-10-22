//version 1
#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;
int n,m,k;
char museum[1001][1001];
int region[1001][1001];
int search(int x, int y, int i)
{
  if (museum[x][y]=='*') return 1;
  if (region[x][y]) return 0;
  region[x][y] = i;
  return search(x,y-1,i)+search(x,y+1,i)+search(x-1,y,i)+search(x+1,y,i);
}

int main()
{
  cin>>n>>m>>k;
  int region_id=0;
  vector<int> ans;
  ans.push_back(0);
  for(int i=1;i<=n;i++) scanf("%s", museum[i]+1);
  for(int i=0;i<k;++i){
    int x,y;
    scanf("%d%d",&x,&y);
    if (!region[x][y]){
        region_id++;
        ans.push_back(search(x,y,region_id));
    }
    printf("%d\n",ans[region[x][y]]);
  }
}
