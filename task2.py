# you are given a list of N transfers(numbered from 0 to N-1) between two banks: bank A & bank B. the Kth transfer is described by two values:
# R[K](either "A" or "B") representing the recipient ( the bank the transfer is sent to);
# V[K] denoting the value sent via the transfer.
# All transfers are complted in the order they appear on the list. the banks do not want to go into debt( in other words, their account balance may not drop below 0).
# What minimum initail account balance each bank must have to ensure that all transfers can be completed?
# write a function:
# def solution(R,V)
# that, given two non-empty zero-indexed arrays R and V consisting of N integers, returns the minimum initial account balance each bank must have to ensure that all transfers can be completed.
# for example, given R = [BAABA] and V = [2,4,1,1,2], the function should return [2,4].
# given R="ABAB" and V = [10,5,10,15], the function should return [0,15].
# Write an efficient algorithm for the following assumptions:
# string R and array V are bith of length N
# N is an integer within the range [1..100,000]
# each element of arrays R is a string that can have one of the following values: "A", "B"
# each element of arrays V is an integer within the range [1..10,000]

# find the number of transfers
def solution(R,V):
    # write your code in Python 3.6
    # given two non-empty zero-indexed arrays R and V consisting of N integers, returns the minimum initial account balance each bank must have to ensure that all transfers can be completed.
    # for example, given R = [BAABA] and V = [2,4,1,1,2], the function should return [2,4].
    # given R="ABAB" and V = [10,5,10,15], the function should return [0,15].
    # Write an efficient algorithm for the following assumptions:
    # string R and array V are bith of length N
    # N is an integer within the range [1..100,000]
    # each element of arrays R is a string that can have one of the following values: "A", "B"
    # each element of arrays V is an integer within the range [1..10,000]
    # find the number of transfers
    transfers = len(R)
    # find the number of transfers to bank A
    transfers_to_bank_A = 0
    # find the number of transfers to bank B
    transfers_to_bank_B = 0
    # find the number of transfers from bank A
    transfers_from_bank_A = 0
    # find the number of transfers from bank B
    transfers_from_bank_B = 0
    # find the number of transfers to bank A
    for i in range(transfers):
        if R[i] == "A":
            transfers_to_bank_A += 1
    # find the number of transfers to bank B
    for i in range(transfers):
        if R[i] == "B":
            transfers_to_bank_B += 1
    # find the number of transfers from bank A
    transfers_from_bank_A = transfers - transfers_to_bank_A
    # find the number of transfers from bank B
    transfers_from_bank_B = transfers - transfers_to_bank_B
    # find the minimum initial account balance each bank must have to ensure that all transfers can be completed.
    # find the minimum initial account balance for bank A
    min_account_balance_bank_A = 0
    # find the minimum initial account balance for bank B
    min_account_balance_bank_B = 0
    # find the minimum initial account balance for bank A
    for i in range(transfers):
        if R[i] == "A":
            min_account_balance_bank_A += V[i]
        else:
            min_account_balance_bank_A -= V[i]
    # find the minimum initial account balance for bank B
    for i in range(transfers):
        if R[i] == "B":
            min_account_balance_bank_B += V[i]
        else:
            min_account_balance_bank_B -= V[i]
    # find the minimum initial account balance for bank A
    if min_account_balance_bank_A < 0:
        min_account_balance_bank_A = 0
    # find the minimum initial account balance for bank B
    if min_account_balance_bank_B < 0:
        min_account_balance_bank_B = 0
    # return the minimum initial account balance each bank must have to ensure that all transfers can be completed.
    return [min_account_balance_bank_A, min_account_balance_bank_B]
    

  