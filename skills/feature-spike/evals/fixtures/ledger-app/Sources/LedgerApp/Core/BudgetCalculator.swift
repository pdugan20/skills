import Foundation

/// Totals spending against monthly category budgets.
@MainActor
struct BudgetCalculator {
    var budgets: [String: Int]

    func spent(in category: String, year: Int, month: Int, transactions: [Transaction]) -> Int {
        let calendar = AppEnvironment.shared.calendar
        return transactions
            .filter { transaction in
                let parts = calendar.dateComponents([.year, .month], from: transaction.date)
                return transaction.category == category && parts.year == year && parts.month == month
            }
            .reduce(0) { $0 + $1.amountCents }
    }

    func remaining(in category: String, year: Int, month: Int, transactions: [Transaction]) -> Int {
        (budgets[category] ?? 0) - spent(in: category, year: year, month: month, transactions: transactions)
    }

    func formattedRemaining(in category: String, year: Int, month: Int, transactions: [Transaction]) -> String {
        let cents = remaining(in: category, year: year, month: month, transactions: transactions)
        let value = NSNumber(value: Double(cents) / 100)
        return AppEnvironment.shared.currencyFormatter.string(from: value) ?? "\(cents)"
    }
}
