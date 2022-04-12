from dataclasses import dataclass, field

@dataclass
class Orders:
    orderID: int
    customerID: int
    salespersonID: int
    pickedByPersonID: int
    contactPersonID: int
    backorderOrderID: int
    orderDate: str
    expectedDeliveryDate: str
    customerPurchaseOrderNumber: str
    isUndersupplyBackordered: bool
    comments: str
    deliveryInstructions: str
    internalComments: str
    pickingCompletedWhen: str
    lastEditedBy: int
    lastEditedWhen: str
    
    def __gt__(self,other):
        return self.orderID > other.orderID
        
    def __ge__(self,other):
        return self.orderID >= other.orderID
    
@dataclass
class Invoices:
    invoiceID: int
    customerID: int
    billToCustomerID: int
    orderID: int
    deliveryMethodID: int
    contactPersonID: int
    accountsPersonID: int
    salespersonPersonID: int
    packedByPersonID: int
    invoiceDate: str
    customerPurchaseOrderNumber: str
    isCreditNote: bool
    creditNoteReason: str
    comments: str
    deliveryInstructions: str
    internalComments: str
    totalDryItems: int
    totalChillerItems: int
    deliveryRun: str
    runPosition: str
    returnedDeliveryData: str
    confirmedDeliveryTime: str
    confirmedReceivedBy: str
    lastEditedBy: int
    lastEditedWhen: str
    
    def __gt__(self,other):
        return self.invoiceID > other.invoiceID
        
    def __ge__(self,other):
        return self.invoiceID >= other.invoiceID
    
@dataclass
class Customers:
    customerID: int
    customerName: str
    billToCustomerID: int
    customerCategoryID: int
    buyingGroupID: int
    primaryContactPersonID: int
    alternateContactPersonID: int
    deliveryMethodID: int
    deliveryCityID: int
    postalCityID: int
    creditLimit: float
    accountOpenedDate: str
    standardDiscountPercentage: float
    isStatementSent: bool
    isOnCreditHold: bool
    paymentDays: int
    phoneNumber: str
    faxNumber: str
    deliveryRun: str
    runPosition: str
    websiteURL: str
    deliveryAddressLine1: str
    deliveryAddressLine2: str
    deliveryPostalCode: str
    deliveryLocation: str
    postalAddressLine1: str
    postalAddressLine2: str
    postalPostalCode: str
    lastEditedBy: int
    validFrom: str
    validTo: str