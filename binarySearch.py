def binary_search(dizi, left, right, key):


    while left <= right:

        mid = left + (right - left) // 2


        if dizi[mid] == key:
            return mid


        elif dizi[mid] < key:
            left = mid + 1


        else:
            right = mid - 1

    return -1


if __name__ == '__main__':

   dizi= [1, 2, 3, 10, 20, 40, 111, 244, 14444, 800000]
   key = 244
   result = binary_search(dizi, 0, len(dizi) - 1, key)
   if result != -1:
       print("Bulunduğu konum:", result)
   else:
        print("Değer  dizide yok")