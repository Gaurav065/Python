class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		hi=0
		low = n-1
		while(low<=hi):
			mid = low+(hi-low)//2
			if(arr[mid]==k):
				return mid
			elif(arr[mid]<k):
				low=mid+1
			else:
				hi = mid-1
		return -1

if __name__=='__main__':
	t= int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int, input().strip().split(' ')))
		k = int(input())
		ob = Solution()
		print(ob.binarysearch(arr,n,k))

			
