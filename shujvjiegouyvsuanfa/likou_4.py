class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        numl_len = len(nums1)
        num2_len = len(nums2)

        total_len = numl_len+num2_len
        res01 = None
        res02 = None


        if numl_len%2 == 0 and num2_len%2==0:
            mid_01 = numl_len//2
            mid_02 = num2_len//2
            tmp = []
            tmp.extend(nums1[mid_01:mid_01+2])
            tmp.extend(nums2[mid_02:mid_02+2])
            sorted(tmp)
            res01 = tmp[-1]
            res02 = tmp[-2]
        elif numl_len%2 != 0 and num2_len%2!=0:







            mid_idx_1 = (numl_len+num2_len)//2
            mid_idx_2 = mid_idx_1+1


            a = numl_len//2
            b = num2_len//2


            c = a+b

            if c==mid_idx_1:
                if nums1[a]>nums2[b]:
                    res01 = nums1[a]
                    if nums1[a+1]>nums2[b]:
                        res02 = nums1[a+1]
                    else:
                        res02 = nums2[b]
                else:
                    res01 = nums2[b]
                    if nums1[a]>nums2[b+1]:
                        res02 = nums1[a]
                    else:
                        res02 = nums2[b+1]


        else:
            mid_idx_1 = (numl_len+num2_len)//2+1
            a = numl_len // 2
            b = num2_len // 2
            c = a+b

            if c==mid_idx_1:
                if nums1[a]>nums2[b]:
                    res01 = nums1[a]
                    if nums1[a+1]>nums2[b]:
                        res02 = nums1[a+1]
                    else:
                        res02 = nums2[b]
                else:
                    res01 = nums2[b]
                    if nums1[a]>nums2[b+1]:
                        res02 = nums1[a]
                    else:
                        res02 = nums2[b+1]



class Solution02(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numl_len = len(nums1)
        num2_len = len(nums2)

        total_len = numl_len+num2_len


        if total_len%2==0:  # 中位数为2个平均值
            idx_1 = total_len//2
            idx_2 = total_len//2+1


            num_mid_1 = nums1[numl_len//2]


class Solution03(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numl_len = len(nums1)
        num2_len = len(nums2)

        total_len = numl_len+num2_len


        def search(A,B,K):
            if K==0:
                if A[0]>B[0]:
                    return B[0]
                else:
                    return A[0]

            if len(A)==0:
                return B[K]
            if len(B)==0:
                return A[K]



            mid_a = A[len(A)//2]
            mid_b = B[len(B)//2]

            if mid_a>mid_b:
                return search(A,B[len(B)//2+1:],K-len(B)//2)
            else:
                return search(A[len(A)//2+1:], B, K - len(A) // 2)

        def search2(A, B, K):

            if len(A) == 0:
                return (B[K]+B[K+1])/2
            if len(B) == 0:
                return (A[K]+A[K+1])/2
            if K == 0:
                if A[0] > B[0]:
                    if A[0]>B[1]:
                        return (B[0]+B[1])/2
                    else:
                        return (A[0]+B[0])/2
                else:
                    if A[1]>B[1]:
                        return (A[0]+B[1])/2
                    else:
                        return (A[0]+A[1])/2

            mid_a = A[len(A) // 2]
            mid_b = B[len(B) // 2]

            if mid_a > mid_b:
                return search2(A, B[len(B) // 2 + 1:], K - len(B) // 2)
            else:
                return search2(A[len(A) // 2 + 1:], B, K - len(A) // 2)

        if total_len%2!=0:
            return float(search(nums1,nums2,int((total_len+1)/2)))

        return float(search2(nums1,nums2,total_len//2))

nums1 = [1, 3]
nums2 = [2]

print(Solution03().findMedianSortedArrays(nums1,nums2))









