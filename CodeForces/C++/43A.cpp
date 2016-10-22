#include<iostream>
using namespace std;

int main()
{
	int n = -1;
	cin>>n;
	string a = "";
	string b = "";
	int x = 0;
	int y = 0;
	for(int i=0;i<n;++i){
		string c = "";
		cin>>c;
		if (a==""){
			a=c;
		}
		else if ((c!=a) && (b=="")){
			b=c;
		}
		if (c==a){
			++x;
		}
		else{
			++y;
		}
	}
	if (x>y){
		cout<<a;
	}
	else{
		cout<<b;
	}
}
