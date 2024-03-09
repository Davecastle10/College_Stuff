# Transactions (in Databases and elsewhere)
When you have a multistepproblem, we can maintain integrity by using transactions.

```
START TRANSACTION  
    DAVE_BALANCE = DAVE-BALANCE - £10  
    DAVE_INVENTORY = DAVE_INVENTORY + NUTS  
    JOSH_BALANCE = JOSH_BALANCE + £10  
    JOSH_INVENTORY = JOSH_INVENTORY - NUTS  
END TRANSACTION
```  

## Transactions need to be **ACID**
**A** = Atomicity  
- Inseperable, making the indiviadual parts as small/seperate as possible

**C** = Consistency 
- *i.e* total money is the sme before and after  

**I** = Isolation  
- freeze as little as possible, but affect nothing oustide of the frozen transaction resources, *i.e* only resources taking part of the transaction can interacty with the transaction, without influencing things outside the transcation.

**D** = Durability  
- it stays done, *i.e* transaction reccords saved to a persistant data storgae

If a transaction is not completed in its enitirety, we **roll-back** to the previous state. *e.g.* Dave gets his money back and josh gets his nuts back.  

We either **commit** or **roll-back** trabsactions *i.e* it's either done or not done.  
