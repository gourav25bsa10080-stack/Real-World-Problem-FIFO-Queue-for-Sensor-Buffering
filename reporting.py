# =================================================================
# Module 3: reporting.py
# Purpose: Calculates and displays final results, fulfilling the
# Reporting/Analytics (FR3) and Reliability (NFR) requirements.
# =================================================================
from quiz_data import MONEY_LADDER, QUESTIONS

def get_safe_amount(q_index):
    """Determines the guaranteed prize money based on the last completed safe haven."""
    # Safe Haven 2 requires Q7 (index 7) to be completed
    if q_index >= 7:
        return MONEY_LADDER[7] 
    # Safe Haven 1 requires Q2 (index 2) to be completed
    elif q_index >= 2:
        return MONEY_LADDER[2] 
    else:
        return 0

def display_final_result(q_index, current_prize_won):
    """Displays the final winnings and end message."""
    
    # Check if the user won the grand prize
    if q_index == len(QUESTIONS):
        final_prize = MONEY_LADDER[len(QUESTIONS)]
        print("\n\n🎉 CONGRATULATIONS! YOU HAVE WON THE GRAND PRIZE! 🎉")
    else:
        # User quit or got the question wrong, award the last safe amount
        final_prize = get_safe_amount(q_index)
        
    print("\n" + "=" * 60)
    print("              KBC GAME OVER")
    print("=" * 60)
    print(f"You answered {q_index} questions correctly.")
    print(f"** Your Total Winnings: ₹{final_prize:,} **")
    print("=" * 60)
    return final_prize