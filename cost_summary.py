"""
Construction Cost Summary Tool
Author: Your Name
Description: Accepts 5 construction line items, calculates total budget vs. 
             actual cost, and flags over-budget items.
"""

def get_cost_inputs():
    print("=" * 50)
    print(" ENTER CONSTRUCTION COST LINE ITEMS ")
    print("=" * 50)
    
    line_items = []
    
    # Loop to capture 5 specific construction cost items
    for i in range(1, 6):
        print(f"\n--- Line Item {i} ---")
        name = input("Item Description (e.g., Concrete, Framing): ").strip()
        
        while True:
            try:
                budget = float(input(f"Estimated Budget for {name} ($): "))
                actual = float(input(f"Actual Cost for {name} ($): "))
                break
            except ValueError:
                print("❌ Invalid input. Please enter numbers for budget and actual cost.")
        
        variance = actual - budget
        # Flag if the actual cost is higher than the budget
        flag = "⚠️ OVER BUDGET" if variance > 0 else "✅ UNDER/ON BUDGET"
        
        line_items.append({
            "name": name,
            "budget": budget,
            "actual": actual,
            "variance": variance,
            "flag": flag
        })
    return line_items

def generate_summary(items):
    total_budget = sum(item["budget"] for item in items)
    total_actual = sum(item["actual"] for item in items)
    total_variance = total_actual - total_budget
    
    print("\n" + "=" * 70)
    print("                      CONSTRUCTION COST SUMMARY                      ")
    print("=" * 70)
    print(f"{'Item Description':<20} | {'Budget':<10} | {'Actual':<10} | {'Variance':<10} | {'Status'}")
    print("-" * 70)
    
    for item in items:
        print(f"{item['name']:<20} | ${item['budget']:<9,.2f} | ${item['actual']:<9,.2f} | ${item['variance']:<9,.2f} | {item['flag']}")
        
    print("-" * 70)
    overall_flag = "⚠️ PROJECT OVER BUDGET" if total_variance > 0 else "✅ PROJECT WITHIN BUDGET"
    print(f"{'TOTALS':<20} | ${total_budget:<9,.2f} | ${total_actual:<9,.2f} | ${total_variance:<9,.2f} | {overall_flag}")
    print("=" * 70)

if __name__ == "__main__":
    cost_data = get_cost_inputs()
    generate_summary(cost_data)
