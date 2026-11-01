import Foundation
import Testing

@testable import LedgerApp

@MainActor
@Test func remainingSubtractsSpendingInTheMonth() {
    let calculator = BudgetCalculator(budgets: ["Groceries": 10_000])
    let october = Date(timeIntervalSince1970: 1_791_000_000)
    let november = Date(timeIntervalSince1970: 1_793_700_000)
    let transactions = [
        Transaction(id: UUID(), date: october, amountCents: 2_500, category: "Groceries", memo: "Market"),
        Transaction(id: UUID(), date: november, amountCents: 9_000, category: "Groceries", memo: "Next month"),
        Transaction(id: UUID(), date: october, amountCents: 4_000, category: "Transit", memo: "Pass"),
    ]
    #expect(calculator.remaining(in: "Groceries", year: 2026, month: 10, transactions: transactions) == 7_500)
}

@MainActor
@Test func formattedRemainingUsesTheAppCurrency() {
    let calculator = BudgetCalculator(budgets: ["Dining": 1_999])
    #expect(calculator.formattedRemaining(in: "Dining", year: 2026, month: 10, transactions: []) == "$19.99")
}
