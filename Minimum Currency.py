def min_cur(n):
    arr=[2000,500,200,100,50,20,10,5,2,1]
    cur_cnt={}
    cnt=0
    total_cnt=0
    for cur in arr:
        cnt=n//cur
        total_cnt+=cnt
        if cnt>0:
            cur_cnt[cur]=cnt
        n%=cur
        if n==0:
            break
    print("\n Min cur count=",total_cnt)
    print(cur_cnt)
n=int(input('Enter amount:'))
min_cur(n)
