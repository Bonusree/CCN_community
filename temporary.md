<details>
    <summary>Problem A</summary>

```
#include <bits/stdc++.h>
using namespace std;
//#include<ext/pb_ds/assoc_container.hpp>
//#include<ext/pb_ds/tree_policy.hpp>
//using namespace __gnu_pbds;
//typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds; // find_by_order, order_of_key
#define ll long long
#define vi vector<int>
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vvi vector<vi>
#define vll vector<ll>
#define vvll vector<vector<ll>>
#define vpii vector<pair<int,int>>
#define vpll vector<pair<ll,ll>>
int Set(int N, int pos) {return  N = N | (1<<pos);}
int Reset(int N, int pos) {return  N = N & ~(1<<pos);}
bool Cheek(int N, int pos) {return  (bool)(N & (1<<pos));}
#define least_one_pos(x) __builtin_ffs(x)
#define leading_zeros(x) __builtin_clz(x)
#define tailing_zeros(x) __builtin_ctz(x)
#define num_of_one(x) __builtin_popcount(x)
///............x...........///
#define all(a) a.begin(), a.end()
#define allr(a) a.rbegin(), a.rend()
#define mp(a, b) make_pair(a, b)
#define pb push_back
#define UNIQUE(X) (X).erase(unique(all(X)), (X).end())
#define ft cout << "for test"<<endl;
#define print(v) for (auto it : v)cout << it<<" ";cout << endl;
#define cinv(v) for(auto &it : v)cin>>it;
#define PI acos(-1.0)
#define FIO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define t_c int test, cs = 1;cin>>test;while (test--)
///................function.....................///

//#define mod 1000000007
//........constant........///
const ll N = 1e6+5;
void file(){
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
}
int main(){
    FIO;
    // file();
    t_c{
        ll b,y; cin>>b>>y;
        ll ans=0;
        for(ll i=1; i<=b; i++){
            ll t1=i/2;
            ll t2=i-t1;
            if(t1*t1+t2*t2+y*i<=b){
                ans=i;
            }
            else break;
        }
        ll res=1;
        while(ans-->0){
            res*=2ll;
        }
        cout<<res<<endl;
    }
}
```

</details>