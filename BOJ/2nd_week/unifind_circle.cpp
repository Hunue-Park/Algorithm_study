#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
using namespace std;

#define int int64_t

struct UnionFind {
	vector<int> parent, rank, cnt;
	UnionFind(int n) : parent(n), rank(n, 1), cnt(n, 1) {
		iota(parent.begin(), parent.end(), 0); // 트리 초기화 하는 부분. 부모 노드값을 자기자신으로 
	}
	int Find(int x) {
		return x == parent[x] ? x : parent[x] = Find(parent[x]);
	}
	bool Union(int a, int b) {
		a = Find(a), b = Find(b);
		if (a == b) return 0;
		if (rank[a] < rank[b]) swap(a, b);
		parent[b] = a;
		rank[a] += rank[a] == rank[b];
		cnt[a] += cnt[b];
		return 1;
	}
};

int32_t main() {
	fastio;
	//input
	int n; cin >> n;
	vector<int> L(n), R(n), v;
	for (int i = 0; i < n; i++) {
		int x, r; cin >> x >> r;
		L[i] = x - r, R[i] = x + r;
		v.push_back(L[i]);
		v.push_back(R[i]);
	}
	
	//coordinate compression
	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.end());

	//sol, V-E+F = C
	UnionFind UF(v.size());
	int V = v.size(), E = 2 * n, C = 0;
	for (int i = 0; i < n; i++) {
		int l = lower_bound(v.begin(), v.end(), L[i]) - v.begin();
		int r = lower_bound(v.begin(), v.end(), R[i]) - v.begin();
		UF.Union(l, r);
	}
	for (int i = 0; i < v.size(); i++) {
		if (i == UF.Find(i)) C++;
	}
	cout << C + 1 - V + E << '\n';
}