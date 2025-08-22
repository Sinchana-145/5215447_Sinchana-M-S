def reverse(llist):
    curr =llist
    new = None
    while curr:
        curr.prev,curr.next=curr.next,curr.prev 
        new=curr
        curr=curr.prev
    return new         
    # Write your code here

