class Solution:
    def finalPrices(self, prices):
        newprice = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            newprice.append(prices[i] - discount)

        return newprice
                