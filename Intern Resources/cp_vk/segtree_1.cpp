#include<bits/stdc++.h>
using namespace std;
 
 
struct SegTree
{
	vector<int> tree;
	SegTree(int N)
	{
		tree.resize(4*N+5);
	}
	int merge(int a, int b)
	{
		return a + b;
	}
	void build(vector<int> &A, int v, int lx, int rx)
	{
		if(lx == rx)
		{
			tree[v] = A[lx];
			return;
		}
		int mid = (lx + rx)/2;
		build(A, 2*v+1, lx, mid);
		build(A, 2*v+2, mid+1, rx);
		tree[v] = merge(tree[2*v+1], tree[2*v+2]);
	}






 


	void point_update(int v, int lx, int rx, int pos, int val)
	{
		if(lx == rx)
		{
			tree[v] = val;
			return;
		}
		int mid = (lx + rx)/2;
		if(pos <= mid) 
			point_update(2*v+1, lx, mid, pos, val);
		else
			point_update(2*v+2, mid+1, rx, pos, val);
 
		tree[v] = merge(tree[2*v+1], tree[2*v+2]);
	}








 	int range_query(int v, int lx, int rx, int ql, int qr)
	{
		//lx <= ql <= qr <= rx
		if(lx == ql && rx == qr)
		{
			return tree[v];
		}
		int mid = (lx + rx)/2;
 
		int left_ans = 0, right_ans = 0;
		if(mid >= ql)
			left_ans = range_query(2*v+1, lx, mid, ql, min(qr, mid));
		if(qr > mid)
			right_ans = range_query(2*v+2, mid+1, rx, max(mid+1, ql), qr);
 
		return merge(left_ans, right_ans);
	}






};
 
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
 
	int N;
	cin >> N;
	vector<int> A(N);
 
	for(int i=0; i<N; i++)
	{
		cin >> A[i];
	}
 
	SegTree S(N);
 
	S.build(A, 0, 0, N-1);
 
	int Q;
	cin >> Q;
	for(int i=0; i<Q; i++)
	{
		int type;
		cin >> type;
 
		if(type == 1)
		{
			int pos, val;
			cin >> pos >> val;
			pos--;
			S.point_update(0, 0, N-1, pos, val);
		}
		else
		{
			int ql, qr;
			cin >> ql >> qr;
			ql--; qr--;
			cout << S.range_query(0, 0, N-1, ql, qr) << "\n";
		}
	}
 
	return 0;
}
