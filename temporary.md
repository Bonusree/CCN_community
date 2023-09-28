<details>
    <summary>Problem A</summary>

```c++

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

<details>
    <summary>Problem B</summary>

```c++
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
    vector<string>clr={ "blue", "green", "yellow", "red", "purple", "orange", "pink", "grey", "cyan", "brown", "ash", "silver", "gold", "white", "black" };
    // sort(all(clr));
    t_c{
        string s; cin>>s;
        map<char,int>c1,c2;
        for(auto x:s){
            c1[x]++;
        }
        int ans=0;
        for(int st=1; st<(1<<15); st++){
            c2=c1;
            bool ok=1;
            for(int i=0; i<15 and ok; i++){
                if(st&(1<<i)){
                    for(auto x:clr[i]){
                        if(c2.find(x)==c2.end() or c2[x]<=0){
                            ok=0;break;
                        }
                        c2[x]--;
                    }
                }
            }
            if(ok){
                ans = max(ans,__builtin_popcount(st));
            }
        } 
        cout<<ans<<endl;
    }
}
```
</details>

<details>
    <summary>Problem C</summary>

```c++
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

#define mod 1000000007
//........constant........///
const ll N = 1e6+5;
void file(){
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
}
ll prime_size=5005;
vi primes;
vector<bool> mark(prime_size+5);
void sieve(){
    ll i,j;
    mark[0]=mark[1]=1;
    for(i=4; i<prime_size; i+=2)mark[i]=1;
    for(i=3; i*i<=prime_size; i+=2){
        if(!mark[i]){
            for(j=i*i; j<=prime_size; j+=i*2)mark[j]=1;
        }
    }
    primes.pb(2);
    for(i=3; i<=prime_size; i+=2)if(!mark[i])primes.pb(i);
}
ll mem[5005],n,m;
ll dp(int p){
    // cout<<p<<" "<<ct<<endl;
    if(p<=0)return 1ll;
    ll &ret = mem[p];
    if(~ret)return ret;
    ret = dp(p-1);
    for(auto it:primes){
        if(it+1<=m and it<=p){
            ret = (ret+dp(p-(it+1)))%mod;
        }
    }
    // cout<<p<<" "<<ret<<endl;
    return ret%mod;
}
int main(){
    FIO;
    sieve();
    // for(int i=0;i<5; i++)cout<<primes[i]<<endl;
    // file();
    // cout<<primes.size()<<endl;
    t_c{
        cin>>n>>m;
        for(int i=0; i<=n; i++)mem[i]=-1;
        ll ret = dp(n)%mod;
        if(ret<0){
            ret=(ret+mod)%mod;
        }
        cout<<ret<<endl;
    }
}
```
</details>

<details>
    <summary>Problem D</summary>

Not solve yet.
</details>

<details>
    <summary>Problem E</summary>

```c++
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

#define mod 1000000007
//........constant........///
const ll N = 1e6+5;
void file(){
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
}
ll prime_size=1e7+1;
vi primes;
vector<bool> mark(prime_size+4);
void sieve(){
    ll i,j;
    mark[0]=mark[1]=1;
    for(i=4; i<prime_size; i+=2)mark[i]=1;
    for(i=3; i*i<=prime_size; i+=2){
        if(!mark[i]){
            for(j=i*i; j<=prime_size; j+=i*2)mark[j]=1;
        }
    }
    primes.pb(2);
    for(i=3; i<=prime_size; i+=2)if(!mark[i])primes.pb(i);
}
#define lft nd*2
#define rgt nd*2+1
#define mid (b+e)/2
class segtree{
    public:
    int n;
    vector<int> mn,mx;
    int lt1,lt2;
    segtree(int _n){
        n=_n;
        lt1=n+1, lt2=0;
        mn = vi(4*n,lt1);
        mx = vi(4*n,lt2);
    }
    void uthaw(int nd){
        mn[nd]=min(mn[lft],mn[rgt]);
        mx[nd]=max(mx[lft],mx[rgt]);
    }
    void update(int nd, int b, int e, int l, int r, int x){
        if(b>e or e<l or r<b)return;
        if(l<=b and e<=r){
            if(!x)mn[nd]=lt1,mx[nd]=lt2;
            else mn[nd]=x,mx[nd]=x;
            return;
        }
        update(lft,b,mid,l,r,x);
        update(rgt,mid+1,e,l,r,x);
        uthaw(nd);
    }
    int mn_query(int nd, int b, int e, int l, int r){
        if(b>e or e<l or r<b)return lt1;
        if(l<=b and e<=r){
            return mn[nd];
        }
        int p1 = mn_query(lft,b,mid,l,r);
        int p2 = mn_query(rgt,mid+1,e,l,r);
        return min(p1,p2);
    }
    int mx_query(int nd, int b, int e, int l, int r){
        if(b>e or e<l or r<b)return lt2;
        if(l<=b and e<=r){
            return mx[nd];
        }
        int p1 = mx_query(lft,b,mid,l,r);
        int p2 = mx_query(rgt,mid+1,e,l,r);
        return max(p1,p2);
    }
};
int main(){
    FIO;
    sieve();
    // cout<<primes.size()<<endl;
    t_c{
        int n,m; cin>>n>>m;
        vi v(n+1);
        segtree obj(n);
        for(int i=1; i<=n; i++){
            cin>>v[i];
            if(!mark[v[i]]){
                obj.update(1,1,n,i,i,i);
            }
        }
        while(m--){
            int tp; cin>>tp;
            if(tp==1){
                int x; cin>>x;
                int p1=max(x,obj.mn_query(1,1,n,x+1,n)-1);
                int p2=min(x,obj.mx_query(1,1,n,1,x-1)+1);
                // cout<<p1<<" "<<p2<<endl;
                cout<<p1-p2<<endl;
            }
            else{
                int x,y;
                cin>>x>>y;
                if(!mark[y]){
                    obj.update(1,1,n,x,x,x);
                }
                else{
                    obj.update(1,1,n,x,x,0);
                }
            }
        }
    }
}
```
</details>

<details>
    <summary>Problem F</summary>

```c++
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

#define mod 1000000007
//........constant........///
const ll N = 1e6+5;
void file(){
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
}
ll prime_size=1e5+5;
vi mark(prime_size+5);
void sieve(){
    ll i,j;
    for(i=1; i<prime_size; i++)mark[i]=i;
    for(i=4; i<prime_size; i+=2)mark[i]=2;
    for(i=3; i*i<=prime_size; i+=2){
        if(i==mark[i]){
            for(j=i*i; j<=prime_size; j+=i){
                if(j==mark[j])mark[j]=i;
            }
        }
    }
}
class DSU{
    public:
    vi par,sz;
    int n;
    DSU(int _n){
        n=_n;
        par.resize(n+1);
        sz.resize(n+1);
        for(int i=1; i<=n; i++)par[i]=i,sz[i]=1;
    }
    int Find(int a){
        if(a==par[a])return par[a];
        return par[a] = Find(par[a]);
    }
    void Union(int a, int b){
        a = Find(a);b = Find(b);
        if(a==b)return;
        if(sz[a]>=sz[b]){
            sz[a]+=sz[b];
            par[b]=a;
        }
        else{
            par[a]=b;
            sz[b]+=sz[a];
        }
    }
};
int main(){
    FIO;
    sieve();
    int n; cin>>n;
    vi v(n+1);
    DSU ob(n);
    vi pos(prime_size+5);
    for(int i=1; i<=n; i++){
        cin>>v[i];
        int t1=v[i];
        while(t1>1){
            int cur=mark[t1];
            while(t1%cur==0)t1/=cur;
            if(!pos[cur]){
                pos[cur]=i;
            }
            else{
                ob.Union(pos[cur],i);
            }
        }
    }
    set<int>grps;
    for(int i=1; i<=n; i++){
        grps.insert(ob.Find(i));
    }
    cout<<grps.size()<<endl;
}
```
</details>