def getTaxAmount(total):
    taxAmount = round(total * .06, 2)
    return taxAmount
def getPostTax(total, taxAmount):
    postTax = round(total + taxAmount,2)
    return postTax