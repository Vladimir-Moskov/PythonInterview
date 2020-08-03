# AlgorithmsDynamic Programming

##################################################################################################
# https://www.hackerrank.com/challenges/coin-change/problem
# The Coin Change Problem

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#


def getWays(needed_amount, couns_set):
    counter = [0] * (needed_amount + 1)
    for coin in couns_set:
        start = coin
        if start <= needed_amount:
            counter[start] += 1
            start += 1
        while start <= needed_amount:
            prev = start - coin
            counter[start] += counter[prev]
            start += 1
    return counter[-1]


def getWays_better(n, c):
    n_perms = [1]+[0]*n
    for coin in c:
        for i in range(coin, n+1):
            n_perms[i] += n_perms[i-coin]
    return n_perms[n]

# print(getWays(4, [1, 2, 3]))  # 4
# print(getWays(10, [2, 5, 3, 6]))  # 5

##################################################################################################
# https://www.hackerrank.com/challenges/hr-city/problem
# HackerRank City


def hackerrankCity(valueIn):
    result = 0
    n = len(valueIn)
    numArr = [1]
    pointArr = [0]
    res = [0]
    distance = 0  # Cross distance between furthest points
    for i in range(1, n + 1):
        a = valueIn[i - 1]
        num = numArr[i - 1]
        pointer = pointArr[i - 1]
        numArr.append((numArr[i - 1] * 4 + 2) % 1000000007)
        pointArr.append((pointer * 4 + (2 + 3 * num) * distance + a * (3 + 6 * num + 2 * num)) % 1000000007)
        res.append((res[i - 1] * 4 + pointer * (numArr[i] - num) * 4 + (
                    6 * num * 2 + 1) * a + num * num * 16 * a) % 1000000007)
        distance = (distance * 2 + 3 * a) % 1000000007
    # print(numArr)
    # print(pointArr)
    result = res[-1] % 1000000007
    return result


# print(hackerrankCity([2, 1]))

##################################################################################################
# https://www.hackerrank.com/challenges/maxsubarray/problem
# The Maximum Subarray


def maxSubarray(arr):
    # calculate max subsequence sum
    min_val = -10000
    sum_val = 0
    only_negative = True
    for val in arr:
        if val > 0:
            sum_val += val
            only_negative = False
        else:
            min_val = max(min_val, val)
    if only_negative:
        sum_val = min_val

    # maximum subarray sum
    result = 0
    cur_max = arr[0]
    prev_max = cur_max
    for i in range(1, len(arr)):
        val = arr[i]
        if cur_max < 0:
            cur_max = max(cur_max, val)
        elif val >= 0:
            cur_max += val
        else:
            prev_max = max(cur_max, prev_max)
            cur_max += val

    result = max(cur_max, prev_max)

    return [result, sum_val]

# print(maxSubarray([1, 2, 3, 4]))  # 10, 10
# print(maxSubarray([2, -1, 2, 3, 4, -5]))  # 10, 11
# print(maxSubarray([-2, -3, -1, -4, -6]))  # -1, -1
# print(maxSubarray([-1, 2, 3, -4, 5, 10]))  # 16, 20


def max_sum_subsequence(a, n):
    m = a[0]
    t = 0
    for i in range(n):
        m = max(m, a[i])
        if a[i] >= 0:
            t += a[i]
    return t if m >= 0 else m


def max_sum_subarray(a, n):
    f = a[0]
    ans = f
    for i in range(1, n):
        f = max(a[i], f + a[i])
        ans = max(ans, f)
    return ans

##################################################################################################
# https://www.hackerrank.com/challenges/stockmax/problem
# Stock Maximize


def stockmax(prices):
    result = 0
    max_back_ar = [0] * len(prices)
    for i in range(len(prices) - 1, -1, -1):
        if i < len(prices) - 1:
            max_back_ar[i] = i if prices[i] > prices[max_back_ar[i+1]] else max_back_ar[i + 1]
        else:
            max_back_ar[i] = i

    start = 0
    end = -1
    while end < len(prices) - 1:
        end = max_back_ar[end + 1]
        max_val = prices[end]
        while start < end:
            result += max_val - prices[start]
            start += 1
        start = end + 1

    return result

# print(stockmax([1, 2])) # 1
# # print(stockmax([2, 1])) # 0
# # print(stockmax([1, 3, 1, 2])) # 3
# # print(stockmax([5, 3, 2])) # 0
# # print(stockmax([1, 2, 100])) # 197


##################################################################################################
# https://www.hackerrank.com/challenges/lego-blocks/problem
# Lego Blocks

max_width = 4


def generate_all(m_width):
    next_add = [[i] for i in range(1, max_width + 1)]
    result = []
    while next_add:
        next_temp = []
        for val in next_add:
            sum_v = sum(val)
            if sum_v == m_width:
                result.append(val)
            else:
                for i in range(1, max_width + 1):
                    if sum_v + i > max_width:
                        break
                    else:
                        new_val = val[:]
                        new_val.append(i)
                        next_temp.append(new_val)
        next_add = next_temp

    return result


def is_valid(base_ar, top_ar, m_width):
    distance = [0] * (m_width - 1)
    current = 0
    for i in range(len(base_ar) - 1):
        val = base_ar[i]
        current += val
        distance[current - 1] = 1
    current = 0
    for i in range(len(top_ar) - 1):
        val = top_ar[i]
        current += val
        if current < (len(distance) + 1) and distance[current - 1] == 1:
            return False

    return True


def ar_to_key(array_val, m_width):
    result = 0
    for val in array_val:
        result += val * (10 ** m_width)
        m_width -= 1
    return result


def legoBlocks(n_height, m_width):
    result = 0
    all_options = generate_all(m_width)
    valid_dic = {}
    for i in range(len(all_options)):
        val_bot = all_options[i]
        count = 0
        ref = []
        for val_top in all_options:
            if is_valid(val_bot, val_top, m_width):
                count += 1
                ref.append(val_bot)
        valid_dic[ar_to_key(val_bot)] = ref

    for val in all_options:
        count = 1
        for i in range(n_height):
            count = count * 1


    return result


def legoBlocks(wall_height, wall_width):
    mod = 10 ** 9 + 7
    wall_height = wall_height % mod
    wall_width = wall_width % mod
    f = []
    f.append(0)
    f.append(1)
    if wall_width > 1:
        f.append(2)
    if wall_width > 2:
        f.append(4)
    if wall_width > 3:
        f.append(8)

    if wall_width > 4:
        for i in range(5, wall_width + 1):  # stop at index wall_width - 1
            f.append((f[i - 1] + f[i - 2] + f[i - 3] + f[i - 4]) % mod)

    # total_combos = f[-1] ** wall_height

    g = []
    for i in range(len(f)):
        g.append(f[i] ** wall_height % mod)

    # print('f')
    # for _ in range(wall_height): print(f)
    # print('---')
    # print('g')
    # print(g)
    # print('---')

    h = [0] * (wall_width + 1)
    h[1] = 1

    for i in range(2, wall_width + 1):
        h[i] = g[i]
        for j in range(1, i):
            h[i] = (h[i] - h[j] * g[i-j]) % mod
            a=1

    # print('h')
    # print(h)
    # print('---')

    return h[-1] % mod
# print(legoBlocks(2, 2))
# print(legoBlocks(3, 2))
# print(legoBlocks(2, 3))
# print(legoBlocks(4, 4))

"""
    import java.util.Scanner;
    
    class Solution{
        static final int mod=1000000007;
        static int[] f;
        static int mult(int x, int y){
        long z=x;
        z*=y;
        return (int) (z%mod);
        }
        static int pow(int x, int n){
        int r=1;
        while(n!=1){
            if((n&1)==1) r=mult(r,x);
            x=mult(x,x);
            n>>=1;
        }
        return mult(x,r);
        }
        static int add(int x, int y){
        return (x+y)%mod;
        }
        static void computeF(int highM){
        if(highM<4) highM=4;
        f=new int[highM+1];
        f[0]=1;
        f[1]=1;
        f[2]=2;
        f[3]=4;
        for(int i=4;i<=highM;++i){
            int x=0;
            for(int j=1;j<=4;++j){
            x=add(x,f[i-j]);
            }
            f[i]=x;
        }
        }
        static long solve(int n, int m){
        int[] g=new int[m+1], h=new int[m+1];
        g[1]=1;
        h[1]=0;
        for(int i=2;i<=m;++i){
            int x=0;
            for(int j=1;j<i;++j){
            x=add(x,mult(g[j],g[i-j]));
            x=add(x,mult(g[j],h[i-j]));
            }
            h[i]=x;
            g[i]=add(pow(f[i],n),mod-h[i]);
        }
        return g[m];
        }
        static void input(){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        int[] an=new int[t], am=new int[t];
        for(int i=0;i<t;++i){
            an[i]=sc.nextInt();
            am[i]=sc.nextInt();
        }
        sc.close();	
        int highM=0;
        for(int m: am){
            if(m>highM) highM=m;
        }
        computeF(highM);
        for(int i=0;i<t;++i){
            System.out.println(solve(an[i],am[i]));	    
        }
        }
        public static void main(String[] args){
        input();
        }
    }
"""

##################################################################################################
# https://www.hackerrank.com/challenges/unbounded-knapsack/problem
# Knapsack


def unboundedKnapsack(k, arr):
    result = 0
    uniq_val = set(arr)
    dp_ar = [0] * (k + 1)
    dp_ar[0] = 1
    for i in range(1, k + 1):
        for val in uniq_val:
            prev_index = i - val
            if prev_index >= 0 and dp_ar[i] == 0:
                dp_ar[i] = dp_ar[prev_index]
    last = k
    while last >= 0:
        if dp_ar[last] == 1:
            return last
        last -= 1
    return result

# print(unboundedKnapsack(12, [1, 6, 9])) # 12
# print(unboundedKnapsack(9, [3, 4, 4, 8])) # 9

##################################################################################################
# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem
# The Longest Common Subsequence


















