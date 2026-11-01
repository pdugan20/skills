import SwiftUI

struct BudgetSummaryView: View {
    let transactions: [Transaction]
    private let calculator = BudgetCalculator(
        budgets: ["Groceries": 60_000, "Transit": 15_000, "Dining": 25_000, "Utilities": 20_000]
    )

    var body: some View {
        NavigationStack {
            List(calculator.budgets.keys.sorted(), id: \.self) { category in
                let spent = calculator.spent(in: category, year: 2026, month: 10, transactions: transactions)
                let limit = calculator.budgets[category] ?? 0
                VStack(alignment: .leading) {
                    HStack {
                        Text(category)
                        Spacer()
                        Text(calculator.formattedRemaining(in: category, year: 2026, month: 10, transactions: transactions))
                    }
                    ProgressView(value: Double(min(spent, limit)), total: Double(max(limit, 1)))
                        .tint(spent > limit ? .red : .accentColor)
                }
            }
            .navigationTitle("Budgets")
        }
    }
}
