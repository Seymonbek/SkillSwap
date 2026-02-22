def transferTokens(user_balance, transfer_amount):
    # Calculate the tax
    tax = transfer_amount * 0.05
    net_transfer = transfer_amount - tax

    # Check for negative balance
    if user_balance < net_transfer:
        raise ValueError("Insufficient balance, transfer would cause a negative balance.")

    # Atomic transaction start (pseudo-code)
    try:
        # Begin transaction
        start_transaction()

        # Update balances
        user_balance -= net_transfer
        # Assuming we have a function to update user balance in the database
        update_user_balance(user_balance)

        # Transaction commit
        commit_transaction()
    except Exception as e:
        # Rollback in case of error
        rollback_transaction()
        raise e

    return user_balance
